---
doc_id: proj-dark-earth-carbon-main
project_id: dark-earth-carbon
title: Dark Earth Carbon — Project Knowledge
language_mode: EN
status: active
last_updated: 2026-02-13
owners: Maji Team
---

# Dark Earth Carbon — Project Knowledge

## Project Snapshot
- Name: Dark Earth Carbon (DEC)
- Goal: Scale biochar carbon removal in Tanzania through optimized production, open-source dMRV, and biochar compound fertilizer (BCF) development
- Stage: Development
- Country: Tanzania (Mafinga + Kigoma facilities)
- Stakeholders: Maji GmbH, DEC Tanzania Ltd, FiBL (Jacques Fuchs), Isometric (certifier), Atmosfair, TARI, NCMC, TFRA, TaHA
- Revenue streams: (1) Biochar / BCF sales to farmers, (2) Carbon removal credit trading
- dMRV system: Varuna Carbon — open-source digital Monitoring, Reporting & Verification
- Project timeframe: Feb 2025 – Feb 2027
- Funding: REPIC grant (CHF 500k of CHF 1.76M total)

## Linked Pages
- Offering context: REPIC Rollout — Scaling Biochar Carbon Removal
- Design tracker: —
- Engineering tracker: —
- Other references: REPIC Proposal (2024-12-03)

## Sources
- `SRC-001` | type: proposal | date: 2024-12-03 | file: 2024-12-03_Proposal_Maji_Tanzania_export.pdf

## Personas

### Smallholder Farmer
- Segment: Small-scale farmers in Mafinga and Kigoma regions
- Core job to be done: Improve soil fertility and crop yields affordably
- Behaviors: Uses basic tools; limited access to chemical fertilizers; burns agricultural waste
- Needs: Affordable soil amendments, practical training on biochar application
- Pains: Degraded acidic soils, expensive chemical fertilizers, low crop yields
- Evidence refs: `SRC-001`

### Commercial Farmer
- Segment: Larger agricultural operations in Tanzania
- Core job to be done: Maximize crop output while maintaining soil health
- Behaviors: Purchases soil amendments at scale; open to data-backed products
- Needs: Consistent supply of quality BCF, evidence of ROI vs. NPK fertilizers
- Pains: Declining soil quality over time, rising fertilizer costs
- Evidence refs: `SRC-001`

### DEC Site Operator
- Segment: Facility managers and production staff at Mafinga / Kigoma plants
- Core job to be done: Run biochar production efficiently and generate verifiable carbon credits
- Behaviors: Currently uses Excel for operations; manages rotary kiln production
- Needs: User-friendly dMRV tools, real-time production monitoring, automated carbon credit reporting
- Pains: Manual data collection, limited visibility into production metrics, complex certification workflows
- Evidence refs: `SRC-001`

### Carbon Credit Buyer
- Segment: Organizations purchasing verified carbon removal credits (e.g., Atmosfair)
- Core job to be done: Source high-integrity, traceable carbon removal credits
- Behaviors: Evaluates credits on traceability, certification standard, and price
- Needs: Transparent verification, competitive pricing, reliable supply
- Pains: Market flooded with low-quality offsets, difficulty verifying permanence
- Evidence refs: `SRC-001`

## Product Requirements

### PRD-001
- Problem: Biochar production facilities lack digital tools — relying on spreadsheets limits operational optimization, carbon credit reporting, and scalability
- Outcome: A fully integrated dMRV platform (Varuna Carbon) that automates monitoring, reporting, and verification across multiple facilities
- Scope: Backend database, web + mobile front-ends, PLC integration, carbon credit API (Isometric), user training
- Non-goals: Hardware/kiln design, fertilizer formulation R&D
- Success metrics: System deployed across 2 facilities; automated carbon credit reporting; user adoption by site staff
- Evidence refs: `SRC-001`

### PRD-002
- Problem: Smallholder farmers are unaware of biochar benefits and lack access to quality BCF
- Outcome: Validated BCF formulations with demonstrated yield improvements, supported by farmer training programs
- Scope: Field trials (10+), BCF formulation optimization, training for 500 farmers
- Non-goals: Direct farmer-facing software
- Success metrics: 25% crop yield increase vs. baseline; 500 farmers trained; cost-benefit analysis vs. NPK
- Evidence refs: `SRC-001`

## Feature Requirements

### FRD-001
- Feature name: Production Monitoring Dashboard
- User story: As a site operator, I want to see real-time production data so I can optimize kiln performance and catch issues early
- Functional requirements: Real-time data from PLC systems; production KPIs (throughput, temperature, uptime); alerts for anomalies
- Acceptance criteria: Dashboard loads in <3s; data refreshes in real-time; accessible on desktop web
- Dependencies: PLC integration, backend API
- Evidence refs: `SRC-001`

### FRD-002
- Feature name: Carbon Credit Reporting & Verification
- User story: As a carbon manager, I want automated carbon credit calculations and registry submissions so I can reduce manual work and ensure compliance
- Functional requirements: Calculate permanent fixed carbon; account for permanence factor, production emissions, delivery emissions; submit to Isometric API
- Acceptance criteria: Automated report generation; audit-ready data trail; Isometric registry integration
- Dependencies: Backend database, Isometric API
- Evidence refs: `SRC-001`

### FRD-003
- Feature name: Mobile Field Data Collection
- User story: As a field worker, I want to capture biomass intake and delivery data on my phone so records are accurate and centralized
- Functional requirements: Offline-capable mobile web app; barcode/QR scanning; photo capture; sync when connected
- Acceptance criteria: Works offline; syncs within 30s of connectivity; simple 3-tap workflow
- Dependencies: Backend API
- Evidence refs: `SRC-001`

### FRD-004
- Feature name: Sales & Inventory Tracking (Basic ERP)
- User story: As a site manager, I want to track biochar inventory, sales, and customer orders so I can manage operations without spreadsheets
- Functional requirements: Inventory levels, sales orders, customer records, basic CRM
- Acceptance criteria: Replaces current Excel-based workflow; real-time inventory accuracy
- Dependencies: Backend database
- Evidence refs: `SRC-001`

### FRD-005
- Feature name: Customer-Facing Carbon Traceability
- User story: As a carbon credit buyer, I want to trace the origin and verification of my credits so I can trust their integrity
- Functional requirements: Credit provenance dashboard; sustainability metrics; detailed production + verification reports
- Acceptance criteria: Each credit traceable to production batch; publicly accessible reports
- Dependencies: Carbon credit reporting (FRD-002), backend API
- Evidence refs: `SRC-001`

## Ideation
### Idea Backlog
- `IDEA-001`: Open-source the dMRV under MIT License for industry-wide adoption
- `IDEA-002`: Franchise model / Special Purpose Vehicles for scaling to new sites
- `IDEA-003`: Integration with additional carbon registries (Verra, Gold Standard) beyond Isometric
- `IDEA-004`: Farmer-facing mobile app for BCF application guidance and soil monitoring

## Research Notes
- Mafinga facility: operational, 1,800 t/yr biochar capacity, ~4,000 tCO2e/yr carbon removal credits. 200 tons sold to date at ~$250/ton.
- Kigoma facility: under construction, expected 4,500 t/yr biochar, ~10,000 tCO2e/yr. Commissioning target Q1 2025.
- Certification: Originally CSI (Carbon Standards International); now using Isometric as certifier.
- Atmosfair: guaranteed offtake for carbon credits during first 2 years of production.
- Tanzania biomass availability: Mafinga >500,000 t/yr wood waste; Kigoma >80,000 t/yr agricultural waste within 20 km.
- Financial: Revenue to date $50k; projected next 2 years $1.5M; gross margin 20%.
- Key work packages: (1) Facility Development, (2) BCF Dev & Field Trials, (3) Digital Systems / dMRV, (4) Commercial Viability, (5) Multiplication & Expansion.
- Maji role: Project lead, UX design, software engineering for dMRV platform.
- Key Maji staff: Martin von Siebenthal (UX Strategy), Kenji Nguyen (Software Engineering), Nadine Antenen (Project Management).
- Key DEC staff: Arno Rohwedder (MD), Alexander Chetkovich (Carbon), Natasha Davies (Partnerships), Nico Rovekamp (Engineering), Steve Mwandango (Mafinga), Giuseppe Carminati (Kigoma).

## Notes & Decisions
- 2026-02-13 | Created project page from REPIC proposal (2024-12-03). Certifier updated from CSI to Isometric per current status.
