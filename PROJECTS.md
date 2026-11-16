# Gavin-Schilling repository: preserved project catalogue

This repository contains multiple projects and historical work areas. This catalogue describes the current tree without moving, deleting, or reclassifying its contents. It is an inventory, not a claim that every nested project is complete or currently deployed.

## 1. Root Schilling Enterprises brand site

**Path:** repository root, `services/`, and `assets/`

**Type:** static HTML/CSS site for GitHub Pages.

**Contents:** Home, Services, Work, About, Insights, Contact, service pages, shared CSS and assets.

**Status:** root site has been refreshed and published through GitHub Pages. It is independent from the nested Django applications.

## 2. Marketing and payroll Django prototype

**Path:** `Business/Marketing/gavin_schilling_marketing/`

**Type:** Django 4.1-era application with a marketing website, website models, a payroll module, and a Dockerfile.

**Security boundary:** the legacy employee model contains a Social Security number field. The public SSN handler is disabled in the current security maintenance branch and returns HTTP 410 without reading submitted data. The current root URL configuration does not route to payroll intake, but the handler is disabled as an additional fail-closed measure. Do not reactivate SSN collection without encryption, least-privilege access, audit logging, retention/deletion, backups, incident response, and legal/privacy review.

**Credential boundary:** the historical Django signing key and Google API key were embedded in public source. The security branch moves them to environment configuration, but old values remain in Git history. Revoke/rotate any still-active Google key and generate a new Django signing key before deployment.

**Runtime status:** the pinned Django 4.1 release is end-of-life. This project is not ready for production until the framework, third-party dependencies, database setup, authentication, and hosting target are upgraded and tested.

## 3. Operations website and asset collection

**Path:** `Business/Operations/Website/`

**Type:** separate static website/assets collection, including styles and a large brand-logo image library.

**Status:** retained as an archival project area. Its images and logos are not automatically proof of client relationships, authorization, endorsement, or current affiliation. Confirm usage rights and client permissions before presenting these assets publicly or using them in marketing materials. No assets have been removed.

## 4. Networking and engineering client area

**Path:** `Business/Solutions Architecture/Networking/Engineering/Clients/`

**Type:** small static HTML area (currently a clients page plus a 404 page).

**Status:** preserved. It should be reviewed as a standalone project before linking it from the root site. Do not infer active client relationships solely from filenames or logos stored elsewhere.

## 5. Solutions Architecture / Software area

**Path:** `Business/Solutions Architecture/Software/`

**Type:** placeholder project area (the current tracked content is only a 404 page).

**Status:** no complete software application has been verified at this path. Keep the placeholder until the intended source project is identified.

## 6. File On Hold

**Path:** `File On Hold/`

**Type:** preserved standalone HTML area.

**Status:** intentionally not merged into the root site. Review purpose, ownership, data, and publication status before activating or deleting it.

## Preservation and deployment rules

- Keep each project area separate until ownership, technical boundaries, and data dependencies are documented.
- Do not commit credentials, populated databases, personal records, or payroll identifiers.
- Do not publish the nested Django applications with GitHub Pages; they require server-side hosting and private configuration.
- Keep the root static site deployment independent from nested projects.
- Any future extraction into separate repositories should retain Git history (for example, using a history-aware subtree/filter workflow) and be reviewed before changing links or deleting the original paths.
- Run security and rights reviews before exposing logo libraries, client names, tenant/employee fields, or other personal information.

## Current review branches

- [Marketing/payroll security hardening PR](https://github.com/SchillingEnterprises/Gavin-Schilling/pull/2) — environment-driven secrets, safer defaults, disabled SSN intake, and source checks.
- This catalogue is a documentation-only change and does not merge or deploy any nested application.
