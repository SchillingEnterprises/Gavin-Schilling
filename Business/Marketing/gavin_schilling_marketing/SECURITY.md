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

Report vulnerabilities privately through GitHub's private vulnerability reporting feature when available.
