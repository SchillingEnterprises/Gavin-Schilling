# Gavin Schilling | Schilling Enterprises

Static responsive brand website for GitHub Pages.

## Brand

AI. Technology. Business Innovation.

Connect strategy. Build what matters.

## Root website

- Home, Services, Work, About, Insights, Contact
- Six service pages under `services/`
- Shared stylesheet at `assets/css/site.css`
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
- The nested payroll/SSN intake is disabled in the security maintenance branch until a secure data-processing design is completed.
- Review brand/logo permissions and personal-data exposure before publishing nested operations or client assets.
- Marketing is integrated-selective, not a general-purpose agency offer.
