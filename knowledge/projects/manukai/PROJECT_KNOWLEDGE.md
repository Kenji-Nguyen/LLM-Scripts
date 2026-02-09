---
doc_id: proj-manukai-main
project_id: manukai
title: Manukai Project Knowledge
language_mode: EN
status: active
last_updated: 2026-02-08
owners: Maji Team
---

# Manukai Project Knowledge

## Project Snapshot
- Name: Manukai
- Goal: AI-powered CNC programming automation platform that accelerates NC code generation by analyzing production history to find geometrically similar features and adapt proven machining operations to new parts
- Stage: Active development (Beta/MVP)
- Stakeholders: Manukai (product company), Maji (design & engineering partner)
- Core value: Up to 80% reduction in programming time, 15% reduction in cycle times
- Deployment: 100% on-premise (no internet required, full data privacy)
- Tagline: "Write Better CNC Programs Faster"
- App type: Standalone desktop application (Electron + React frontend, Python/FastAPI backend)
- AI/ML: Separate backend/ML team handles feature detection and similarity algorithms

### Supported CAM Systems
- Mastercam
- TopSolid
- GibbsCAM
- Siemens NX
- Fusion 360
- Additional systems upon request

### Current Clients

| Client | Location | CAM System | Notes |
|--------|----------|------------|-------|
| PSI | Switzerland | TopSolid, Hypermill | Multiple interviewees, 12-person team |
| Bosch | Schwieberdingen, Germany | Siemens NX | 5-axis CNC, focus on precision |
| Straumann | ? | ? | Medical devices |

## Linked Pages
- GitHub issues: #192-#216 (feature design, research, design system)
- Figma: (link TBD)

## Sources
- `SRC-001` | type: legacy-migration | date: 2026-02-08 | link/file: `manukai/MANUKAI_KNOWLEDGE.md`
- `SRC-002` | type: interviews | date: 2025-10 to 2025-12 | link/file: User interviews (PSI, Bosch participants)
- `SRC-003` | type: web-research | date: 2026-01 | link/file: CAM domain research, competitor analysis

## Personas

### CAM Programmer (Primary User)
- Segment: CNC programmers responsible for creating NC programs
- Core job to be done: Create reliable, efficient NC programs for new and existing parts
- Behaviors: 4-20+ years experience, 70%+ time in CAM software, mix of new parts (90%) and optimizations (10%), often sole/limited programmers for multiple machines
- Needs: Process reliability over speed (especially low-volume), tool life/Standzeit visibility, quality (surface finish, tolerance adherence), clear visualization of proposals, ability to fine-tune and maintain control
- Pains: Repetitive programming of similar features, no easy way to reuse proven strategies, knowledge loss when colleagues leave, bottleneck for production
- Evidence refs: `SRC-002`

### CNC Operator (Secondary User)
- Segment: Machine operators who work directly at the CNC machine
- Core job to be done: Run programs reliably, handle setups and monitoring
- Behaviors: Works directly at machine, may do simple programming on machine control, often older and less comfortable with new software, handles setups/tool changes/monitoring
- Needs: Reliable programs that run without issues, simple adjustments when needed
- Pains: Small adjustments at machine not always fed back to CAM, disconnect between programming and execution
- Evidence refs: `SRC-002`

## Product Requirements

### PRD-001: Similar Feature Search
- Problem: CAM programmers repeatedly program similar features from scratch, with no systematic way to reuse proven strategies from production history
- Outcome: Programmers can find geometrically similar features from past projects and apply proven operations to new parts
- Scope: Search within same Feature Group, filter by material/tool/machine/similarity/roughness/time/programmer/date
- Non-goals: Cross-Feature-Group search, automatic parameter adjustment
- Success metrics: Reduction in programming time per feature, adoption rate of suggested operations
- Evidence refs: `SRC-002`, `SRC-003`

### PRD-002: Operation Management
- Problem: Managing, grouping, and sequencing operations across features is complex and error-prone
- Outcome: Users can add, edit, group, sequence, and assign operations to features with clear multi-feature support
- Scope: Operation CRUD, grouping by setup (Spannung/SP1, SP2), drag-and-drop sequencing, multi-feature operation assignment
- Non-goals: Automatic operation generation without user input
- Success metrics: Time to complete operation assignment, user satisfaction with operation overview
- Evidence refs: `SRC-002`

### PRD-003: Feature Detection & Assignment
- Problem: Manual identification and classification of geometric features is time-consuming
- Outcome: AI automatically detects Feature Groups and individual Features from 3D geometry, with user ability to correct
- Scope: Auto-detection, manual reassignment, face merging, multi-select for operation assignment
- Non-goals: User-created custom Feature Group types (list is fixed)
- Success metrics: Detection accuracy, correction rate
- Evidence refs: `SRC-002`

### PRD-004: CAM System Integration
- Problem: Operations and tools created in Manukai need to flow back into CAM software
- Outcome: Seamless export of operations, tools, and sequences to supported CAM systems
- Scope: Export to TopSolid, MasterCAM, NX; bidirectional import of existing programs
- Non-goals: Replacing CAM system functionality
- Success metrics: Export success rate, parameter fidelity
- Evidence refs: `SRC-002`

## Feature Requirements

### FRD-001: 3D Viewer
- Feature name: Interactive 3D geometry viewer
- User story: As a CAM programmer, I want to visualize the part geometry and see feature highlights so I can understand what the AI detected
- Functional requirements: Feature highlighting on selection, tolerance visualization, gizmo controls, linked highlighting with PDF viewer
- Acceptance criteria: Clicking feature in sidebar highlights in 3D; clicking geometry selects in sidebar list; multi-select supported
- Dependencies: Feature detection backend
- Evidence refs: `SRC-002` (Issues #198, #204)

### FRD-002: PDF/Technical Drawing Viewer
- Feature name: Technical drawing viewer with OCR
- User story: As a CAM programmer, I want to see the technical drawing linked to the 3D model so I can check tolerances and annotations
- Functional requirements: OCR extraction of tolerances, cross-highlighting with 3D viewer, dimension/surface requirement display
- Acceptance criteria: Hovering feature in 3D highlights in drawing and vice versa
- Dependencies: OCR backend
- Evidence refs: `SRC-002` (Issue #196)

## Ideation
- `IDEA-001`: Standardization — Users define default tools/operations for consistency across team (planned, not implemented)
- `IDEA-002`: Operation provenance tracking — Explicit tracking of which similar feature an operation was copied from
- `IDEA-003`: Feature visibility toggle — Hide/show features in 3D view for complex parts

## Research Notes

### Key User Research Insights (Oct-Dec 2025)

**Process Reliability > Speed**
> "Im Fräser nicht grosse Serien, Prozesssicherheit ist wichtiger als Zeit"
> (In milling, not big series, process reliability is more important than time)

**Trust Building is Critical**
> "Er bräuchte ein Vertrauen in die Software"
> (He would need trust in the software)

**Copilot Mental Model**
> "Er stellt sich Copilot wie Kit bei Knight Rider vor - er tut mir die Sachen vorlegen und ich kontrolliere ob ich einverstanden bin"
> (He imagines Copilot like Kit from Knight Rider - it presents things to me and I check if I agree)

**Minimize Operations**
> "Er versucht so wenig Operationen wie möglich zu programmieren"
> (He tries to program as few operations as possible)

### Sorting Preferences (from interviews)
- By Roughing/Finishing (Schruppen/Schlichten)
- By planes/levels (Ebenen)
- By tool (Fräser)
- Ability to exclude specific operations from sorting

### Important Information to Display
- Tool preview/illustration
- Material (critical for cutting data)
- Last edited date (recent = more trustworthy)
- Time estimate
- Stock allowance (Aufmass)
- Tool life/Standzeit
- Surface roughness requirements

### Competitive Landscape

| Competitor | Approach | Differentiation from Manukai |
|------------|----------|------------------------------|
| CloudNC CAM Assist | AI generates new toolpaths | Manukai reuses proven history |
| LimitlessCNC | AI copilot in Mastercam | ? |
| Traditional FBM | Template-based feature recognition | Manukai matches whole geometry, not just features |

### Open Questions
- What other clients beyond PSI, Bosch, Straumann?
- What's the current development phase? (Beta? MVP? Production?)
- What's the target market size / ideal customer profile?
- How does the geometry similarity algorithm work?
- What file formats are supported for import?
- How is on-premise deployment handled?
- Can a Feature belong to multiple Parts?
- What's the difference between Project and Program in practice?
- Where is the Figma file / design system?
- What's the current design maturity?

### Data Model

```
Part ──┬── Technical Drawing (1:*)
       │
       ├── Feature Groups (1:*)
       │       └── Features (1:*)
       │
       └── Projects (1:*)
               └── Program (1:*)
                       └── Operations (*:*) ── Tools (*:1)
                              └── Features (*:*)
```

**Key relationships:**
- Features and Operations have many-to-many relationship
- Each Operation uses one Tool
- Feature Groups are fixed types (auto-detected by AI)
- Knowledge database is company-specific, grows over time

### Feature Groups (EN/DE)

| Feature Group (EN) | Feature Group (DE) |
|--------------------|-------------------|
| Through Hole | Bohrung |
| Blind Hole | Sackbohrung |
| Passage | Durchführung |
| Pocket | Tasche |
| Chamfer | Kante |
| Fillet | Rundung |
| Open Pocket | Offene Tasche |
| Surface | Oberfläche |
| Contour | Kontur |

### CAM Domain Glossary (DE → EN)

| German | English |
|--------|---------|
| Schruppen | Roughing |
| Schlichten | Finishing |
| Bohren | Drilling |
| Gewindebohren | Tapping/Threading |
| Fräsen | Milling |
| Planfräsen | Face milling |
| Taschenfräsen | Pocket milling |
| Spannung/Aufspannung | Setup/Clamping |
| Aufmass | Stock allowance |
| Schnittdaten | Cutting data |
| Vorschub | Feed rate |
| Drehzahl | Spindle speed (RPM) |
| Werkzeug | Tool |
| Standzeit | Tool life |
| Rohteil | Raw part/Stock |
| Toleranz | Tolerance |
| Oberflächenrauheit (Ra) | Surface roughness |

### Design Patterns & Open Issues

**Multi-Feature Operations** (Issue #210): One operation can machine multiple features. Open questions around selection UX, timeline display, conflict handling, and feature removal.

**Operation Grouping** (Issue #197): Users group by Setup (SP1, SP2). Convention: `SP1_Teilname`. Open questions about visual display, drag-and-drop, nested vs. flat grouping.

**CAM Export Flow** (Issue #195): Design needed for export to different CAM systems, format handling, and conflict resolution.

### GitHub Issue Label System

| Label | Description |
|-------|-------------|
| `design` | Design issues |
| `feature-design` | New feature design |
| `research` | Research tasks |
| `visual` | Visual/UI issues |
| `improvement` | Enhancements |
| `design-system` | Design system components |
| `Prio 1/2/3` | Priority levels |

## Notes & Decisions
- 2026-02-08 | Created project page from legacy `manukai/MANUKAI_KNOWLEDGE.md` (SRC-001). Mapped 12 original sections into canonical 9-section format. Data model, glossary, and design patterns moved to Research Notes. Personas, feature areas, and requirements restructured into PRD/FRD format.
