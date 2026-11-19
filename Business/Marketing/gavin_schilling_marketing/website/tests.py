"""Runtime tests for the marketing Django application security boundaries."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

from django.test import SimpleTestCase


APP_ROOT = Path(__file__).resolve().parents[1]


class SensitiveIntakeShutdownTests(SimpleTestCase):
    def test_ssn_intake_view_returns_gone_without_reading_request_data(self):
        """The retired endpoint must not require or inspect a request body."""
        view_path = APP_ROOT / "payroll" / "views.py"
        spec = spec_from_file_location("gavin_payroll_views_under_test", view_path)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)

        # The view must not need request.POST, request.body, a session, or a user.
        response = module.get_social_security_number(object())

        self.assertEqual(response.status_code, 410)
        self.assertIn(b"intake is disabled", response.content)
