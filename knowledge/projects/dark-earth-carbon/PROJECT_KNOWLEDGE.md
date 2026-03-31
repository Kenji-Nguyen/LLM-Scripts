---
doc_id: proj-dark-earth-carbon-main
project_id: dark-earth-carbon
title: Dark Earth Carbon — Project Knowledge
language_mode: EN
status: active
last_updated: 2026-03-31
owners: Maji Team
---

# Dark Earth Carbon — Project Knowledge

## Project Snapshot
- Name: Dark Earth Carbon (DEC)
- Goal: Scale biochar carbon removal in Tanzania through optimized production, open-source dMRV, and biochar compound fertilizer (BCF) development
- Stage: Active Development (prototype complete, P0 compliance phase)
- Country: Tanzania (Mafinga + Kigoma facilities)
- Stakeholders: Maji GmbH, DEC Tanzania Ltd, FiBL (Jacques Fuchs), Isometric (certifier), Atmosfair, TARI, NCMC, TFRA, TaHA
- Revenue streams: (1) Biochar / BCF sales to farmers, (2) Carbon removal credit trading
- dMRV platform: **Noma** — open-source digital Monitoring, Reporting & Verification
- Repo: github.com/Maji-Studio/noma-dmrv
- Tech stack: Next.js 16, React 19, TypeScript 5.9, PostgreSQL, Drizzle ORM, Better Auth, TailwindCSS 4, Playwright, Vitest
- Auth model: Admin-invite only; roles: admin, user (app-level); owner, admin, member, viewer (project-level)
- Database: 45+ tables across 14 entity domains (see Research Notes)
- CI/CD: GitHub Actions (E2E on PR, schema migration, Claude code review)
- Project timeframe: Feb 2025 – Feb 2027
- Funding: REPIC grant (CHF 500k of CHF 1.76M total)

## Linked Pages
- Offering context: REPIC Rollout — Scaling Biochar Carbon Removal
- Design tracker: —
- Engineering tracker: GitHub Issues (Maji-Studio/noma-dmrv)
- GitHub Project: Maji-Studio Project #9 (Prio 1/2/3 lanes, Size XS-XL)
- Isometric protocols: Biochar v1.2, Biomass Feedstock Accounting v1.3, Soil Storage v1.2, Energy Use v1.2, Transportation v1.1, GHG Accounting v1.0
- Other references: REPIC Proposal (2024-12-03)

## Sources
- `SRC-001` | type: proposal | date: 2024-12-03 | file: 2024-12-03_Proposal_Maji_Tanzania_export.pdf
- `SRC-002` | type: codebase | date: 2026-03-31 | file: noma-dmrv/docs/schema-overview.md
- `SRC-003` | type: codebase | date: 2026-03-31 | file: noma-dmrv/docs/architecture.md
- `SRC-004` | type: compliance | date: 2026-03-31 | file: noma-dmrv/docs/isometric/p0-compliance-checklist.md
- `SRC-005` | type: compliance | date: 2026-03-31 | file: noma-dmrv/docs/isometric/requirements-shortlist.md
- `SRC-006` | type: compliance | date: 2026-03-31 | file: noma-dmrv/docs/isometric/schema-mapping.md
- `SRC-007` | type: codebase | date: 2026-03-31 | file: noma-dmrv/docs/auth.md
- `SRC-008` | type: plan | date: 2026-02-01 | file: noma-dmrv/docs/archive/improvement-plan-2026.md
- `SRC-009` | type: plan | date: 2026-03-02 | file: noma-dmrv/docs/archive/260302-iteration-plan-prototype.md

## Personas

### Site Operator
- Segment: Facility-level staff at Mafinga/Kigoma who run daily production operations
- Core job to be done: Record production runs, feedstock intake, deliveries, and field applications accurately so the chain of custody is complete
- Behaviors: Uses Production and Distribution sidebar sections daily; creates feedstock deliveries, production runs, biochar products, orders, deliveries, applications; works on desktop or tablet
- Needs: Fast data entry via slide-over forms, clear entity relationships, auto-generated codes, offline resilience for field work
- Pains: Manual Excel tracking, missing required fields causing form errors, complex feedstock-to-run allocation logic
- Evidence refs: `SRC-001`, `SRC-003`, `SRC-009`

### Carbon Manager
- Segment: DEC carbon team member responsible for credit issuance and Isometric compliance
- Core job to be done: Assemble reporting-period credit batches, verify all compliance evidence is complete, and submit to Isometric registry
- Behaviors: Uses Verification section (credit batches, samples); reviews chain-of-custody DAG; checks P0 compliance items; manages GHG materiality assessments
- Needs: Automated compliance guardrails (P0-01 through P0-15), complete chain-of-custody traceability, Isometric API integration, audit-ready data exports
- Pains: 15 open P0 compliance gaps blocking credit issuance, manual evidence assembly, no issuance-time guardrails
- Evidence refs: `SRC-001`, `SRC-004`, `SRC-005`, `SRC-006`

### Admin
- Segment: Maji engineering team and DEC management with admin-level access
- Core job to be done: Manage system configuration, user access, facilities, reactors, emission factors, and platform health
- Behaviors: Uses Infrastructure section and admin routes; invites users; configures facilities and reactors; manages emission factor tables; monitors CI/CD
- Needs: Secure admin-invite auth, rate limiting, environment audit, connection pooling, error monitoring
- Pains: No monitoring/alerting in production, incomplete admin UI, manual environment variable management
- Evidence refs: `SRC-003`, `SRC-007`, `SRC-008`

### Auditor / Verifier
- Segment: Isometric-appointed verifiers conducting periodic audits of dMRV data
- Core job to be done: Review the completeness and integrity of all reported data for a crediting period
- Behaviors: Read-only access (viewer role); reviews chain-of-custody visualization, credit batch details, sample records, incident reports, certification submissions
- Needs: Complete audit trail, immutable submission history, monitoring-parameter inventory, embodied-emissions documentation, document/evidence attachments
- Pains: Polymorphic CoC references hard to validate, no structured monitoring-parameter register, embodied-emissions evidence scattered
- Evidence refs: `SRC-001`, `SRC-005`, `SRC-006`

## Product Requirements

### PRD-001
- Problem: Biochar production facilities rely on spreadsheets for operations, making carbon credit reporting error-prone and unscalable
- Outcome: Full-chain digital MRV from feedstock intake through credit issuance, deployed across 2+ facilities
- Scope: 14 entity domains with CRUD UI, chain-of-custody visualization, facility-scoped data, role-based access
- Non-goals: Mobile offline app (deferred), PLC real-time integration, farmer-facing tools
- Success metrics: All 14 entity domains have working CRUD UI; full-chain E2E test passes; deployed to production
- Evidence refs: `SRC-001`, `SRC-002`, `SRC-003`, `SRC-009`

### PRD-002
- Problem: 15 P0 compliance gaps in the Isometric biochar protocol prevent credit issuance
- Outcome: All P0 items resolved with DB-level guardrails, structured evidence models, and issuance-time validation
- Scope: P0-01 through P0-15 covering biomass cap, counterfactual lifecycle, Method B enforcement, calibration tracking, loss accounting, durability evidence, stockpiling, mixing attestations, CoC hardening, facility classification, EC1-EC5 evidence, BCU retirement, materiality gate, reversal risk, embodied emissions
- Non-goals: P1 items (deferred), direct Isometric API submission automation
- Success metrics: Zero open P0 items; credit batch cannot reach verified/issued with incomplete evidence
- Evidence refs: `SRC-004`, `SRC-005`, `SRC-006`

### PRD-003
- Problem: The platform lacks testing coverage, monitoring, security hardening, and CI/CD maturity for production deployment
- Outcome: Production-grade infrastructure with automated testing, monitoring, and security controls
- Scope: Vitest unit coverage, Playwright E2E expansion, Sentry integration, rate limiting, connection pooling, pre-commit hooks
- Non-goals: Redis caching, Storybook, DevContainer (Tier 4 items)
- Success metrics: 80%+ server-side test coverage; E2E suite stable in CI; error monitoring live in production
- Evidence refs: `SRC-008`, `SRC-009`

## Feature Requirements

### FRD-001
- Feature name: Feedstock Intake and Supply Chain
- User story: As a site operator, I want to record feedstock deliveries, manage suppliers, and track sustainability criteria so every biomass input is traceable and compliant
- Functional requirements:
  - Built: Feedstock deliveries CRUD with transport attributes; feedstock batch records with mass/quality; supplier master list with source region; feedstock type catalog; feedstock SC assessments table; auto-allocation from storage bins to production runs via production_run_feedstocks
  - Remaining: P0-01 (RP-level ineligible biomass >25% cap ledger with eligible vs ineligible mass and computed fraction); P0-02 (counterfactual validity lifecycle model with assessment date, evidence window, valid-to, reassessment trigger); market leakage evidence fields (ML4/ML5/ML6 tests)
- Acceptance criteria: Every feedstock batch links to a supplier, sustainability assessment, and counterfactual assessment; ineligible fraction computed per reporting period; RP blocks issuance when >25%
- Dependencies: PRD-002
- Evidence refs: `SRC-002`, `SRC-004`, `SRC-005`

### FRD-002
- Feature name: Production and Sampling
- User story: As a site operator, I want to record production runs with temperature/pressure readings, link samples, and log incidents so every batch has complete quality evidence
- Functional requirements:
  - Built: Production runs CRUD with energy inputs, output mass, reactor linkage; production run readings (time-series telemetry); production samples (in-process measurements); lab samples with full chemistry (H/Corg, O/Corg, contaminants); incident reports; reactor CRUD with sampling method (A/B); formulations with multi-ingredient recipes; biochar product CRUD
  - Remaining: P0-03 (DB trigger guardrails for Method B switch — 30-sample minimum and 1/10 cadence enforcement at DB layer); P0-04 (calibration/test event structure for pressure monitoring with standards and evidence refs); P0-05 (mass-loss adjustment ledger linking incidents to affected run/delivery/application with batch deduction); P0-08 (mixing attestation model for irreversibility and fuel-unsuitability on mixed products)
- Acceptance criteria: Method B transition blocked at DB layer without 30 samples; calibration events linked to reactor/run readings; loss adjustments deduct from credited mass; mixed-batch records require attestations before crediting
- Dependencies: FRD-001, PRD-002
- Evidence refs: `SRC-002`, `SRC-004`, `SRC-005`

### FRD-003
- Feature name: Distribution and Logistics
- User story: As a site operator, I want to manage customer orders, record deliveries with transport emissions, and track drivers/vehicles so product movement is fully documented
- Functional requirements:
  - Built: Orders CRUD linked to customers and biochar products; deliveries CRUD with dry/wet mass documentation; transport legs with energy/distance emission methods; vehicles and drivers master data; customer and customer location management
  - Remaining: P0-12 (BCU retirement model with registry transaction ID, anti-double-count attestation — required if Book-and-Claim transport is adopted); transport method hierarchy evidence flag (justify distance method fallback); round-trip/onward-leg evidence fields
- Acceptance criteria: Every delivery has transport legs with emissions calculated; BCU usage requires retirement proof; transport emission factors validated for recency
- Dependencies: FRD-002, PRD-002
- Evidence refs: `SRC-002`, `SRC-005`, `SRC-006`

### FRD-004
- Feature name: Soil Application and Durability
- User story: As a site operator, I want to record biochar application to soil with GPS-tagged evidence and soil temperature data so durability calculations are defensible
- Functional requirements:
  - Built: Applications CRUD with CO2e storage outputs; soil temperature measurements table (baseline and global database sources); credit batch to applications M:N linkage; document attachments for photo/video evidence
  - Remaining: P0-06 (cross-entity completeness guardrail — verified/issued transition fails when linked applications lack required temperature evidence for 200-year batches); P0-07 (stockpile entity with start/end, condition/risk controls, 12-month exception approval); structured GPS/geotag validation on visual evidence; soil temperature baseline quality check (>=10 measurements per site-month)
- Acceptance criteria: 200-year credit batches cannot reach verified without complete temperature evidence on all linked applications; stockpile records enforce 12-month cap; application photos validated for GPS metadata
- Dependencies: FRD-003, PRD-002
- Evidence refs: `SRC-002`, `SRC-004`, `SRC-005`

### FRD-005
- Feature name: Credit Issuance and Compliance Guardrails
- User story: As a carbon manager, I want credit batches that automatically enforce all Isometric compliance requirements so no batch can be issued with incomplete evidence
- Functional requirements:
  - Built: Credit batches CRUD with reporting period, durability pathway, net removal components (CO2e stored, emissions, counterfactual); GHG materiality assessments table; buffer pool percentage; certification submissions with immutable versioned payloads; certifier projects/sources linkage
  - Remaining: P0-10 (annual facility electricity rollup + intensive/non-intensive classification >200 GWh); P0-11 (structured EC1-EC5 low-carbon procurement evidence model — PPA/EAC retirement IDs, COD, grid region, temporal matching); P0-13 (computed materiality threshold gate — SSR/net removals <1% check at issuance); P0-14 (reversal risk questionnaire/score history and reassessment schedule); P0-15 (normalized embodied-emissions inventory — materials/equipment, EPD/LCA verification, allocation cycle); co-product allocation model; emissions amortization review schedule
- Acceptance criteria: Credit batch transition to verified/issued blocked when: materiality items unresolved, facility classification missing, EC1-EC5 evidence incomplete, reversal risk assessment expired, embodied inventory incomplete
- Dependencies: FRD-001 through FRD-004, PRD-002
- Evidence refs: `SRC-004`, `SRC-005`, `SRC-006`

### FRD-006
- Feature name: Chain of Custody and Audit Trail
- User story: As an auditor, I want to review end-to-end chain-of-custody from feedstock to credit with complete evidence attachments so I can verify compliance
- Functional requirements:
  - Built: Custody handoffs ledger (material type, sender/receiver, handoff timestamp, document linkage); chain-of-custody DAG visualization (React Flow, 14 entity nodes); documents table (entity-type polymorphic evidence store); certification sync events (operation log)
  - Remaining: P0-09 (stronger party/material integrity model — typed FKs or validated registry references instead of polymorphic strings; mandatory evidence rules per handoff type); third-party purchaser affidavit model (clause-level attestations); monitoring-parameter inventory register; audit-ready export functionality
- Acceptance criteria: Handoffs cannot be created without valid sender/receiver/material FK references; purchaser affidavit required for third-party sales; monitoring parameters traceable to protocol modules
- Dependencies: PRD-002
- Evidence refs: `SRC-002`, `SRC-004`, `SRC-006`

### FRD-007
- Feature name: Platform Infrastructure and Quality
- User story: As an admin, I want the platform to have comprehensive test coverage, error monitoring, and security controls so it is reliable and maintainable in production
- Functional requirements:
  - Built: E2E Playwright suite (69+ tests, 13 spec files); GitHub Actions CI (e2e.yml, migrate.yml, claude.yml, claude-code-review.yml); Vitest setup with unit tests; Better Auth with admin-invite; Docker Compose for local dev; ESLint flat config
  - Remaining: Tier 1 — security dependency patches (CVE-2025-29927), environment variable audit, complete projects CRUD; Tier 2 — Vitest unit coverage expansion (target 80%+ server-side), Sentry error monitoring, connection pool optimization; Tier 3 — pre-commit hooks (husky + lint-staged), Renovate for dependency updates, circular dependency detection
- Acceptance criteria: Server-side unit test coverage >80%; Sentry capturing production errors; CI passes on all PRs; pre-commit hooks enforce lint + type check
- Dependencies: PRD-003
- Evidence refs: `SRC-008`, `SRC-009`

## Ideation
- `IDEA-001`: Open-source the dMRV under MIT License for industry-wide adoption
- `IDEA-002`: Franchise model / Special Purpose Vehicles for scaling to new sites
- `IDEA-003`: Integration with additional carbon registries (Verra, Gold Standard) beyond Isometric
- `IDEA-004`: Mobile field data collection app with offline/sync capability
- `IDEA-005`: Real-time PLC integration for production monitoring (kiln temperature, pressure, flow rates)
- `IDEA-006`: Redis caching layer for dashboard performance at scale
- `IDEA-007`: Customer-facing carbon traceability portal for credit buyers

## Research Notes

### Database Entity Domains (14 core areas)
```
Suppliers -> Feedstock Deliveries -> Feedstock Batches -> Production Runs -> Biochar Products -> Orders -> Deliveries -> Applications -> Credit Batches
                                                              |                                                                            |
                                                   Reactors, Samples,                                                        Soil Temp, Durability,
                                                   Incident Reports                                                           CoC Handoffs, Materiality
```
Supporting entities: feedstock types, feedstock SC assessments, storage locations, production readings, production samples, formulations, formulation ingredients, vehicles, drivers, transport legs, customer locations, emission factors, documents, certification submissions, certifier projects/sources, sync events.

### App Navigation Structure
- **Production**: Facilities, Reactors, Feedstocks (types, deliveries, batches, storage), Production Runs, Samples
- **Infrastructure**: Suppliers, Customers, Emission Factors, Formulations
- **Distribution**: Biochar Products, Orders, Deliveries, Applications
- **Verification**: Credit Batches, Chain of Custody, Certification

### Isometric P0 Compliance Summary (15 open items)
- **Feedstock** (2): P0-01 ineligible biomass cap, P0-02 counterfactual lifecycle
- **Production** (4): P0-03 Method B enforcement, P0-04 calibration tracking, P0-05 loss accounting, P0-08 mixing attestations
- **Application/Storage** (2): P0-06 durability evidence gate, P0-07 stockpiling controls
- **Chain of Custody** (1): P0-09 party/material integrity hardening
- **Energy** (2): P0-10 facility electricity classification, P0-11 EC1-EC5 evidence
- **Credits** (4): P0-12 BCU retirement, P0-13 materiality threshold, P0-14 reversal risk, P0-15 embodied emissions

### Architecture
Layered: components -> hooks (React Query) -> fn (server actions + Zod) -> data-access (authz + queries) -> db (Drizzle). UI never talks to DB directly. Auth enforced at data-access layer. Proxy.ts (Node.js runtime) replaces Next.js middleware for Better Auth compatibility.

### Auth Roles
- App-level: admin (full system access), user (standard access)
- Project-level: owner, admin, member, viewer
- Admin-invite only (ALLOW_SELF_SIGNUP=false)

### Key Staff
- Maji: Martin von Siebenthal (UX Strategy), Kenji Nguyen (Software Engineering), Nadine Antenen (Project Management)
- DEC: Arno Rohwedder (MD), Alexander Chetkovich (Carbon), Natasha Davies (Partnerships), Nico Rovekamp (Engineering), Steve Mwandango (Mafinga), Giuseppe Carminati (Kigoma)

### Facility Metrics
- Mafinga: operational, 1,800 t/yr biochar capacity, ~4,000 tCO2e/yr credits. 200 tons sold to date at ~$250/ton.
- Kigoma: under construction, expected 4,500 t/yr biochar, ~10,000 tCO2e/yr.
- Certification: Isometric (switched from CSI). Atmosfair: guaranteed offtake for first 2 years.
- Financial: Revenue to date $50k; projected next 2 years $1.5M; gross margin 20%.

## Notes & Decisions
- 2026-02-13 | Created project page from REPIC proposal (2024-12-03). Certifier updated from CSI to Isometric per current status.
- 2026-03-31 | Major rewrite: updated from proposal-based stub to codebase-grounded knowledge page. Renamed dMRV from "Varuna Carbon" to "Noma". Replaced 4 stakeholder personas with 4 software user personas (Site Operator, Carbon Manager, Admin, Auditor). Restructured to 3 PRDs and 7 workflow-grouped FRDs covering built and remaining work. Added SRC-002 through SRC-009. Registered project in REGISTRY.md and INDEX.md.
