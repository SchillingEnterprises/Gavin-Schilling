# Marketing and Payroll Django Subproject

This is one of several preserved projects inside the Gavin-Schilling repository. It contains a Django marketing site and a legacy payroll/business-data prototype.

## Current state

- Django 6.1.3; the maintained CI/runtime baseline is Python 3.12, with direct dependencies pinned in the repository-root `requirements.txt`.
- Marketing website routes remain separate from the static Schilling Enterprises brand pages.
- The legacy payroll app is deliberately disabled in `INSTALLED_APPS`; its prototype models and forms are preserved but not loaded by Django.
- Public SSN intake is disabled. The legacy Employee SSN field remains in the existing schema for compatibility but is now non-editable and not registered in admin. No SSN data is deleted or exposed through a view.
- The old Google API key and Django signing key were removed from current source configuration and are now environment-backed.

## Local setup

From the repository root, install the pinned dependencies and then run commands from this project directory:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cd Business/Marketing/gavin_schilling_marketing
python manage.py check
python manage.py test
```

Export the required variables from `.env.example` in your shell or container environment. Django does not automatically load `.env` files. `DJANGO_SECRET_KEY` must contain at least 50 characters and at least 5 distinct characters; generate a fresh value with `python -c 'import secrets; print(secrets.token_urlsafe(64))'`. Never put real credentials in the example file or Git.

## Local-development container

Build from the repository root so the project retains its documented path layout:

```bash
docker build --file Business/Marketing/gavin_schilling_marketing/Dockerfile --tag gavin-marketing:dev .
```

The image runs as a non-root user, contains only this Django project and the pinned requirements, and exposes port 8000. It is a local-development image, not a production server. A smoke check is part of GitHub Actions; deployment, persistent database configuration, HTTPS, backups, monitoring, and operational ownership are not provided by this container.

## Security and privacy

See [SECURITY.md](SECURITY.md). Rotate the previously exposed Google API key and replace the historical Django signing key before any deployment. Django 6.1.3 and the Python 3.12 CI baseline are maintained, but this prototype is still not approved for production or real payroll/employee data.

Do not submit, store, or test with real Social Security numbers in this prototype.
