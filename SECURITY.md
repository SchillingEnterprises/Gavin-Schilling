# Security Policy

## Scope and deployment boundaries

This public repository contains a static brand website at the root, a nested Django marketing/payroll prototype, and preserved business/operations materials. GitHub Pages publishes only the explicitly allowlisted root website assets. Excluding a path from the Pages artifact does not make that path or its Git history private: all committed files and historical revisions remain publicly accessible.

Keep the root Pages site separate from the nested Django application. The Django application is not hosted by GitHub Pages and is not approved for production use.

## Current application security baseline

The nested marketing application currently pins Django 5.2.19 and is tested by GitHub Actions on Python 3.12. Its CI checks source compilation, environment-driven security settings, Django system and deployment checks, migration consistency, application tests, and a scoped local-development container smoke check. Passing CI is not a production-readiness approval.

## Sensitive data and payroll

- The legacy employee model retains a Social Security number field for schema compatibility. The field is non-editable and is not registered in Django admin.
- The old public SSN intake view now returns HTTP 410 Gone without reading request data, and the root URL configuration does not route to it. Keep it disabled.
- Do not commit employee, payroll, Social Security, client, customer, or other personal records, populated databases, credentials, or production connection strings.
- Do not inspect, expose, migrate, replace, or remove the tracked SQLite database as part of routine CI or code optimization. Use disposable databases for automated tests and require a separately reviewed data-handling plan for any operation involving preserved records.
- Any future payroll or SSN workflow requires a separate lawful-purpose, privacy, encryption, least-privilege, audit, retention/deletion, backup, incident-response, and legal/compliance design.

## Historical credentials

A Django signing key and Google API key were previously committed to public source history. Treat historical values as exposed even though current source reads credentials from environment variables. Removing a value from the current tree does not revoke it or remove it from Git history.

**Required owner action:** complete credential rotation tracked in [issue #21](https://github.com/SchillingEnterprises/Gavin-Schilling/issues/21). Revoke any still-active historical Google API key, restrict any replacement to the exact approved APIs and domains, generate a new unique Django signing key, and store replacement credentials only in a secret manager. Never paste credential values into issues, pull requests, or logs.

## Deployment

Before any backend deployment, require a supported runtime, owner-controlled secret rotation, verified authentication/authorization, privacy review, secure hosting, backups and restore testing, monitoring, and explicit operational ownership. Keep payroll/SSN intake disabled. The local-development container and green CI checks do not provide production hosting or operational controls.

## Reporting

Report vulnerabilities privately through GitHub's private vulnerability reporting feature when available. Do not include employee, payroll, SSN, client, or other sensitive data in public issues or pull requests.
