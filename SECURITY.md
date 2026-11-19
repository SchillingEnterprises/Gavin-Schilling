# Security Policy

## Scope and deployment boundaries

This repository contains a public static brand website at the root, a nested Django marketing/payroll prototype, and preserved business/operations materials. GitHub Pages publishes only the explicitly allowlisted root website assets; it does not execute the Django application. Files in a public Git repository and its history remain publicly accessible even when excluded from the Pages artifact.

## Sensitive data and credentials

- The payroll/SSN intake endpoint is disabled on the current default branch and must remain disabled unless a separately reviewed, compliant system is designed and approved.
- Never commit employee, payroll, Social Security, client, customer, or other personal records, populated databases, credentials, or production connection strings.
- Historical signing-key and Google API-key values were present in repository history. Treat them as exposed; revoke active provider keys and replace signing keys in deployment secrets. A source-code change does not rotate a provider credential or erase Git history.
- Review nested operations/client materials and brand assets before exposing them through the public Pages artifact.
- The nested Django application uses an end-of-life Django 4.1 release and is not production-ready. Do not deploy it with real personal data.

## Deployment

Keep the root Pages workflow's explicit publication allowlist. Do not replace it with a repository-wide artifact copy. Before any backend deployment, require a supported framework, managed secrets, verified authentication/authorization, privacy review, secure hosting, backups, and deployment tests.

## Reporting

Report vulnerabilities privately through GitHub's private vulnerability reporting feature when available. Do not include employee, payroll, SSN, client, or other sensitive data in public issues or pull requests.
