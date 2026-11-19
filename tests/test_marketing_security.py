"""Source-level guardrails for the legacy marketing/payroll Django project."""
from pathlib import Path
import ast
import os
import re
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "Business/Marketing/gavin_schilling_marketing"
SETTINGS = (APP / "gavin_schilling_marketing/settings.py").read_text(encoding="utf-8")
CREDENTIALS = (APP / "gavin_schilling_marketing/credentials.py").read_text(encoding="utf-8")
SSN_VIEW = (APP / "payroll/views.py").read_text(encoding="utf-8")


class MarketingSecurityTests(unittest.TestCase):
    def load_boolean_parser(self):
        tree = ast.parse(SETTINGS)
        function = next(
            node for node in tree.body
            if isinstance(node, ast.FunctionDef) and node.name == "env_bool"
        )
        module = ast.Module(body=[function], type_ignores=[])
        namespace = {"os": os, "ImproperlyConfigured": ValueError}
        exec(compile(module, str(APP / "gavin_schilling_marketing/settings.py"), "exec"), namespace)
        return namespace["env_bool"]

    def test_invalid_boolean_environment_value_fails_closed(self):
        parser = self.load_boolean_parser()
        with patch.dict(os.environ, {"DJANGO_DEBUG": "tru"}):
            with self.assertRaisesRegex(ValueError, "DJANGO_DEBUG must be an explicit boolean value"):
                parser("DJANGO_DEBUG", False)

    def test_explicit_false_boolean_environment_values_are_supported(self):
        parser = self.load_boolean_parser()
        for value in ("0", "false", "no", "off"):
            with self.subTest(value=value), patch.dict(os.environ, {"DJANGO_DEBUG": value}):
                self.assertIs(parser("DJANGO_DEBUG", True), False)

    def test_secret_and_debug_are_environment_driven(self):
        self.assertIn('os.environ.get("DJANGO_SECRET_KEY")', SETTINGS)
        self.assertIn('DEBUG = env_bool("DJANGO_DEBUG", False)', SETTINGS)
        self.assertNotRegex(SETTINGS, r"(?m)^SECRET_KEY\s*=\s*['\"]")

    def test_hosts_and_https_security_are_configured(self):
        for item in (
            "DJANGO_ALLOWED_HOSTS",
            "DJANGO_CSRF_TRUSTED_ORIGINS",
            "SECURE_SSL_REDIRECT",
            "SESSION_COOKIE_SECURE",
            "CSRF_COOKIE_SECURE",
            "SECURE_CONTENT_TYPE_NOSNIFF",
            "X_FRAME_OPTIONS",
        ):
            with self.subTest(item=item):
                self.assertIn(item, SETTINGS)

    def test_database_path_is_environment_configurable_for_isolated_ci(self):
        self.assertIn('"DJANGO_DB_NAME"', SETTINGS)
        self.assertIn("Business/Marketing/gavin_schilling_marketing/db.sqlite3", SETTINGS)

    def test_google_key_comes_from_environment(self):
        self.assertIn('os.environ.get("GOOGLE_API_KEY", "")', CREDENTIALS)
        self.assertNotRegex(CREDENTIALS, r"AIza[0-9A-Za-z_-]{20,}")

    def test_sensitive_intake_is_disabled_without_parsing_post_data(self):
        self.assertIn("HttpResponseGone", SSN_VIEW)
        self.assertNotIn("request.POST", SSN_VIEW)
        self.assertNotIn("SocialSecurityNumberForm", SSN_VIEW)

    def test_legacy_payroll_app_is_not_loaded(self):
        self.assertNotIn("payroll.apps.PayrollConfig", SETTINGS)
        urls = (APP / "gavin_schilling_marketing/urls.py").read_text(encoding="utf-8")
        self.assertNotIn("payroll.urls", urls)

    def test_employee_ssn_field_is_non_editable_and_not_admin_registered(self):
        models = (APP / "website/models.py").read_text(encoding="utf-8")
        admin = (APP / "website/admin.py").read_text(encoding="utf-8")
        self.assertIn("USSocialSecurityNumberField(blank=True, null=True, editable=False)", models)
        self.assertNotIn("Employee", admin)

    def test_ssn_non_editable_migration_preserves_the_column(self):
        migration = (APP / "website/migrations/0002_employee_ssn_non_editable.py").read_text(encoding="utf-8")
        self.assertIn('name="social_security_number"', migration)
        self.assertIn("editable=False", migration)
        self.assertNotIn("RunPython", migration)
        self.assertNotIn("DeleteModel", migration)

    def test_local_environment_template_contains_only_placeholders(self):
        template = (APP / ".env.example").read_text(encoding="utf-8")
        self.assertIn("DJANGO_SECRET_KEY=generate-a-long-random-secret", template)
        self.assertNotRegex(template, r"AIza[0-9A-Za-z_-]{20,}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
