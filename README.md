# Gavin Schilling | Schilling Enterprises

Static, responsive brand website for GitHub Pages. It uses native HTML, CSS, and
small dependency-free JavaScript enhancements; no build-time framework or
third-party client runtime is required.

## Brand

AI. Technology. Business Innovation.

Connect strategy. Build what matters.

## Root website

- Home, Services, Work, About, Insights, Contact
- Six service pages under `services/`
- Shared stylesheets at `assets/css/site.css` and `assets/css/enhancements.css`
- Accessible mobile navigation, saved light/dark theme preference, and a
  client-side service finder
- Honors the operating system's color preference and reduced-motion setting
- Static hosting via GitHub Pages; no server-side runtime is required for this root site

## Repository map

This repository preserves several distinct project areas. See [PROJECTS.md](PROJECTS.md) for the directory inventory, current technical status, privacy boundaries, and safe next steps.

The root Pages site is not the same application as the nested Django marketing/payroll prototype or the archived operations/client materials. Keep those concerns separate. Do not flatten, delete, or split folders without a reviewed migration plan that preserves commit history, data, and links.

## Deployment

The root website is published through the pinned GitHub Actions Pages workflow in `.github/workflows/pages.yml`. The workflow validates the public pages and stages an explicit allowlist of root HTML pages plus the `assets/` and `services/` directories. It does not publish the nested Django applications, operations archive, client/logo collection, or other business project folders. In repository Settings → Pages, select **GitHub Actions** as the build source.

The nested Django project requires a separate backend host and is not executed by GitHub Pages. Keep the root Pages artifact limited to the public brand website; do not replace the allowlist with a repository-wide copy.

## Content and privacy safeguards

- No unverified client-logo carousel is presented on the root site.
- No personal address or telephone metadata is included in the root site.
- No claims that prototypes are deployed products.
- The nested payroll/SSN intake is disabled on `master`; the security hardening was merged in [PR #2](https://github.com/SchillingEnterprises/Gavin-Schilling/pull/2). The endpoint returns HTTP 410 and does not process submitted identifiers.
- Historical signing-key and Google API-key values remain in Git history. Revoke any still-active historical Google key and use a newly generated Django signing key before any deployment; current source configuration alone cannot rotate credentials.
- The marketing/payroll Django prototype now uses Django 5.2.19 with Python 3.12 CI and a scoped development-container build. Payroll remains disabled, and the prototype is not production-ready.
- Review brand/logo permissions and personal-data exposure before publishing nested operations or client assets.
- Marketing is integrated-selective, not a general-purpose agency offer.

## Security

See [SECURITY.md](SECURITY.md) for this repository's security, privacy, and responsible-use guidance.
