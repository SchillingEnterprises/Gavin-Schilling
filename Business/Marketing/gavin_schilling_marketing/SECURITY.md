# Security Policy — Marketing and Payroll Subproject

## Current runtime and compatibility baseline

The current application baseline is Django 5.2.19 with Python 3.12 CI, using the repository-root `requirements.txt`. GitHub Actions installs the pinned dependencies and runs source checks, Django system and deployment checks, migration consistency checks, application tests, and a scoped local-development container smoke check.

The actively imported model fields and historical migrations use third-party field packages. The current direct pins include:

- `django-address==0.2.8`
- `django-localflavor==5.1`
- `django-money==3.6.2`
- `django-phonenumber-field==9.0.0`
- `phonenumbers==9.0.44`

Do not remove or upgrade these packages solely from a version-number assumption. Model definitions and historical migrations import their field classes. Review actual imports, model fields, migration dependencies, and database compatibility together before changing these pins. Run `pip-audit`, Django system/deployment checks, migration consistency, and the full test suite against disposable CI databases.

The app remains a prototype, not a production service. Passing CI does not establish hosting, operational, legal, privacy, or data-protection readiness.

## Credential rotation

The legacy marketing project previously stored a Django signing key and Google API key in source files. Current code reads those values from environment variables, but historical values remain visible in the public Git history. Treat them as exposed.

**Required owner action:** complete [the credential-rotation and privacy release issue](https://github.com/SchillingEnterprises/Gavin-Schilling/issues/21). Revoke any still-active historical Google API key in Google Cloud Console, restrict a replacement to the exact approved APIs and domains, generate a new unique `DJANGO_SECRET_KEY`, and store both only in the deployment provider's secret manager. Replacing the Django signing key invalidates existing sessions and signed reset links. Do not post credential values in issues, pull requests, chat, or logs.

## Sensitive payroll data

The legacy Employee model retains a Social Security number field in the existing schema for compatibility. The field is non-editable and is not registered in Django admin. The payroll app is removed from `INSTALLED_APPS`; the old public intake view returns HTTP 410 Gone without reading submitted data and is not routed by the current URL configuration.

Existing database content is preserved. Do not inspect, export, alter, migrate, replace, or delete the tracked SQLite database as part of ordinary optimization or CI. Never submit, store, or test with real Social Security numbers in this prototype.

Before any future payroll or SSN workflow is implemented, require a separate lawful-purpose and privacy design covering encryption at rest and in transit, authentication and authorization, least privilege, audit trails, retention/deletion, backups, incident response, and appropriate legal/compliance review. Never write full SSNs to logs, analytics, emails, or client-side storage.

## Runtime hardening

- `DEBUG` defaults to false and boolean environment values are validated explicitly.
- `DJANGO_SECRET_KEY` is required and must be at least 50 characters with at least 5 distinct characters. Generate a fresh value with `python -c 'import secrets; print(secrets.token_urlsafe(64))'`.
- `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` are environment controlled.
- HTTPS redirects and secure session/CSRF cookies default on outside DEBUG.
- HSTS defaults off until HTTPS and domain configuration are verified.
- The example environment file contains placeholders only; it is not loaded automatically by Django.
- GitHub Actions uses disposable CI database paths and does not need or inspect the tracked SQLite database.

## Deployment boundary

The Docker image is for local development only. No production deployment, managed persistent database, verified host configuration, backup/restore process, monitoring, or operational ownership is provided. Do not deploy the app with real payroll, employee, client, or other sensitive personal data. Keep the SSN intake disabled unless a separately reviewed and approved system replaces this prototype.

## Reporting

Report vulnerabilities privately through GitHub's private vulnerability reporting feature when available.
