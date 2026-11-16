# Marketing and Payroll Django Subproject

This is one of several preserved projects inside the Gavin-Schilling repository. It contains a Django marketing site and a legacy payroll/business-data prototype.

## Current state

- Django 4.1-era project and dependencies.
- Marketing website routes remain separate from the static Schilling Enterprises brand pages.
- The legacy payroll app is deliberately disabled in `INSTALLED_APPS`; its prototype models and forms are preserved but not loaded by Django.
- Public SSN intake is disabled. The legacy Employee SSN field remains in the existing schema for compatibility but is now non-editable and not registered in admin. No SSN data is deleted or exposed through a view.
- The old Google API key and Django signing key were removed from current source configuration and are now environment-backed.

## Local setup

Install requirements from this subproject directory, export the variables from `.env.example`, and run Django commands from this project's root. Do not place real credentials in the example file or Git.

## Security and privacy

See [SECURITY.md](SECURITY.md). Rotate the previously exposed Google API key and replace the historical Django signing key before any deployment. The current requirements pin Django 4.1, an end-of-life release, so this app is not production-ready until its framework and third-party packages are upgraded and validated.

Do not submit, store, or test with real Social Security numbers in this prototype.
