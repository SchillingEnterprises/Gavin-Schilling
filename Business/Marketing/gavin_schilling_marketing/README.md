# Marketing and Payroll Django Subproject

This is one of several preserved projects inside the Gavin-Schilling repository. It contains a Django marketing site and a legacy payroll/business-data prototype.

## Current state

- Django 4.1-era project and dependencies.
- Marketing website routes remain separate from the static Schilling Enterprises brand pages.
- Payroll models are prototype code and have not been cleared for production use.
- Public SSN intake is disabled. The legacy employee model still has an SSN field for compatibility; do not expose it or add collection routes.
- The old Google API key and Django signing key were removed from current source configuration and are now environment-backed.

## Local setup

Install requirements from this subproject directory, export the variables from `.env.example`, and run Django commands from this project's root. Do not place real credentials in the example file or Git.

## Security and privacy

See [SECURITY.md](SECURITY.md). Rotate the previously exposed Google API key and replace the historical Django signing key before any deployment. The current requirements pin Django 4.1, an end-of-life release, so this app is not production-ready until its framework and third-party packages are upgraded and validated.

Do not submit, store, or test with real Social Security numbers in this prototype.
