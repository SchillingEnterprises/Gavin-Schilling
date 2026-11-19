# Security Policy — Marketing and Payroll Subproject

## Credential rotation

The legacy marketing Django project previously stored its signing key and Google API key in source files. Current code reads credentials from environment variables instead. Because the repository is public, assume historical values in Git history are exposed.

**Required owner action:** revoke and rotate the previously committed Google API key in Google Cloud Console, restrict any replacement to the exact APIs and approved domains, and generate a new DJANGO_SECRET_KEY. Store both only in the deployment provider's secret manager. Replacing the Django signing key invalidates existing sessions and signed reset links.

## Sensitive payroll data

The legacy Employee model includes a Social Security number field. The older intake view accepted an SSN form but did not store the submitted value. That intake view now returns HTTP 410 Gone and is not routed. The payroll app has been removed from `INSTALLED_APPS`, and the retained Employee SSN field is non-editable and not registered in admin. Existing data is preserved; do not reactivate collection or display.

Before any future SSN or payroll workflow is implemented, require a security and privacy design that covers a lawful collection purpose, encryption at rest and in transit, access controls and least privilege, audit trails, retention/deletion, backups, incident response, and appropriate legal/compliance review. Never write full SSNs to application logs, analytics, emails, or client-side storage.

## Runtime hardening

- DEBUG defaults to false.
- SECRET_KEY is required from DJANGO_SECRET_KEY.
- ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS are environment controlled.
- HTTPS redirects and secure cookies default on outside DEBUG.
- HSTS defaults off until deployment HTTPS and domain configuration are verified.
- No real credentials belong in .env.example or source history.

## Legacy framework

The subproject pins Django 4.1, which is an end-of-life release. Do not deploy it as a new public service. Upgrade the framework and third-party dependencies in a separately tested compatibility effort before production use.

### Dependency compatibility gate

Do not upgrade the Django version by changing only the `Django==4.1` line:

- The current dependency set includes `django-address==0.2.8`. Its published package requirements list Django 2.2/3.0 and Python 3.5–3.8, not the current runtime. The maintained project models use its `AddressField`, and historical migrations import its model field.
- The current `django-localflavor==3.1` release predates Django 4.x support. A maintained 5.1 release supports Django 4.2 through 6.0, but moving between major package generations requires checking the US state and postal-code fields used by the app and migrations.
- The pinned `django-money==3.0.0` and `django-phonenumber-field==6.3.0` also need a coordinated compatibility review rather than being assumed compatible with a newer Django release.

The preferred framework target is the Django 5.2 LTS series, currently at 5.2.19, with extended support through April 2028. Use a maintained Python runtime (3.12 or newer) for the upgraded app and CI.

### Required upgrade sequence

1. Inventory the app's active imports, model fields, forms, admin usage, and migration dependencies for `address`, localflavor, money, and phone-number packages.
2. Design a supported replacement or compatibility layer for the address package. Preserve the existing address table, primary keys, and foreign-key relationships; do not discard or recreate address records.
3. Upgrade Django and compatible third-party packages together, recording the chosen versions and constraints.
4. Run dependency checks, Django system/deployment checks, migration consistency, and application tests on Python 3.12–3.14 using only disposable CI databases.
5. Rehearse the full migration on an owner-approved, protected copy with representative address and employee/client relationships. Compare row counts and foreign-key integrity without exposing real payroll data.
6. Keep the app marked non-production until the migration rehearsal, secret rotation, hosting configuration, backup/restore, and privacy controls are complete.

Never use the tracked SQLite database for CI or upgrade rehearsals. Do not inspect, replace, migrate, or remove it as part of this compatibility work without a separate approved data-handling plan.

The subproject pins Django 4.1, which is an end-of-life release. Do not deploy it as a new public service. Upgrade the framework and third-party dependencies in a separately tested compatibility effort before production use.

Report vulnerabilities privately through GitHub's private vulnerability reporting feature when available.
