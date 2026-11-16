"""Environment-backed provider credentials. Never commit real API keys."""

import os


google_api_key = os.environ.get("GOOGLE_API_KEY", "")
