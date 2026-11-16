"""Source-level guardrails for the legacy marketing/payroll Django project."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
APP = ROOT / "Business/Marketing/gavin_schilling_marketing"
SETTINGS = (APP / "gavin_schilling_marketing/settings.py").read_text(encoding="utf-8")
CREDENTIALS = (APP / "gavin_schilling_marketing/credentials.py").read_text(encoding="utf-8")
SSN_VIEW = (APP / "payroll/views.py").read_text(encoding="utf-8")


class MarketingSecurityTests(unittest.TestCase):
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

    def test_google_key_comes_from_environment(self):
        self.assertIn('os.environ.get("GOOGLE_API_KEY", "")', CREDENTIALS)
        self.assertNotRegex(CREDENTIALS, r"AIza[0-9A-Za-z_-]{20,}")

    def test_sensitive_intake_is_disabled_without_parsing_post_data(self):
        self.assertIn("HttpResponseGone", SSN_VIEW)
        self.assertNotIn("request.POST", SSN_VIEW)
        self.assertNotIn("SocialSecurityNumberForm", SSN_VIEW)

    def test_local_environment_template_contains_only_placeholders(self):
        template = (APP / ".env.example").read_text(encoding="utf-8")
        self.assertIn("DJANGO_SECRET_KEY=generate-a-long-random-secret", template)
        self.assertNotRegex(template, r"AIza[0-9A-Za-z_-]{20,}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
