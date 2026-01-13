# Manukai - AI Context Knowledge File

> **Purpose**: AI context file for Claude to understand Manukai in future conversations.
> **Last Updated**: January 2026
> **Maintained by**: Maji (Design & Engineering Partner)

---

## 1. Product Overview

### What is Manukai?

Manukai is an **AI-powered CNC programming automation platform** that accelerates NC code generation by analyzing production history to find geometrically similar features and adapt proven machining operations to new parts.

**Core Value Proposition:**
- Up to **80% reduction** in programming time
- Up to **15% reduction** in cycle times
- **100% on-premise** deployment (no internet required, full data privacy)
- **Human-in-the-loop**: AI suggests, user decides (no black box)

**Tagline**: "Write Better CNC Programs Faster"

### How It Works

1. **Understanding**: AI extracts geometry, material information, and tolerances from 3D models and technical drawings
2. **Finding**: Searches production history to identify similar features across past projects
3. **Adjustment**: User selects optimal strategy; add-in creates operations tailored to new geometry in existing CAM environment
4. **Improvement**: Standardizes practices, aggregates team insights, highlights inconsistencies

### Supported CAM Systems

- Mastercam
- TopSolid
- GibbsCAM
- Siemens NX
- Fusion 360
- Additional systems upon request

---

## 2. Data Model

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│     Part ─────────────────┬──────────────── Technical Drawing       │
│       │                   │                    (1:*)                │
│       │ (1:*)             │ (1:*)                                   │
│       ▼                   ▼                                         │
│  Feature Groups       Projects                                      │
│       │                   │                                         │
│       │ (1:*)             │ (1:*)                                   │
│       ▼                   ▼                                         │
│   Features            Program                                       │
│       │                   │                                         │
│       │                   │ (1:*)                                   │
│       │                   ▼                                         │
│       └────────(*:*)─ Operations ─────(*:1)───── Tools              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Entity Definitions

| Entity | Description | Attributes |
|--------|-------------|------------|
| **Part** | The physical workpiece/component to be machined | 3D geometry, material |
| **Technical Drawing** | 2D PDF drawings with tolerances, annotations | Tolerances, dimensions, surface requirements |
| **Projects** | Container for machining a specific part | State, history |
| **Program** | A complete machining program (NC code output) | Sequence of operations |
| **Feature Groups** | Categories/types of geometric elements (e.g., "through holes") | Type classification |
| **Features** | Individual instances of a feature group on a part | Polygons/faces, geometric properties |
| **Operations** | Individual machining tasks | Type, sequences, time, parameters |
| **Tools** | Cutting tools used in operations | Geometry, cutting data |

### Feature Groups & Features

**Feature Groups** are purely classification/type categories, while **Features** are the individual instances on a part. Feature Groups do not store shared properties—they only group features by type.

**UI display**: Feature Groups show instance count, e.g., "Through Hole (3)" means 3 through hole features.

**Operations** are assigned at the individual Feature level, not the Feature Group level.

| Feature Group (EN) | Feature Group (DE) | Description |
|--------------------|-------------------|-------------|
| Through Hole | Bohrung | Hole that goes completely through the part |
| Blind Hole | Sackbohrung | Hole that doesn't go all the way through |
| Passage | Durchführung | Opening/channel through the part |
| Pocket | Tasche | Enclosed recessed area |
| Chamfer | Kante | Angled edge/bevel |
| Fillet | Rundung | Rounded edge/corner |
| Open Pocket | Offene Tasche | Pocket open on one or more sides |
| Surface | Oberfläche | Flat or curved surfaces to be machined |
| Contour | Kontur | Profile/outline shapes |

**Feature Group detection**: AI automatically detects Feature Groups from 3D geometry. The list of Feature Groups is fixed—users cannot create custom types.

**Reassignment workflow**: If the AI misclassifies a feature, users can manually select specific faces and trigger a recompute, which reassigns the feature to a different Feature Group.

**Similar search**: When searching for similar features in production history, the search only looks within the same Feature Group (e.g., searching from a through hole only finds other through holes). Similarity is primarily based on geometry, but material and tolerances can be additional factors depending on available data.

**Similar search results display**:
- Preview image of the feature
- Similarity percentage (WIP)
- Machining time
- Number of operations

**Applying similar results**: Users can select and configure individual operations from a similar feature—not forced to take the entire operation sequence. Operations are currently copied as-is without automatic adjustment to the new geometry (e.g., different dimensions). Parameter editing happens in the CAM system, not in Manukai.

**Operation provenance**: No explicit tracking of which similar feature an operation was copied from. However, operations exist in a "knowledge database" so it's possible to look up where a specific operation has been used across projects.

**Knowledge database**: Company-specific (not shared across companies). Initial population: users load folders of existing data, and an analyzer (backend/ML team) processes it to create the database. The database grows over time as new projects are completed.

**Export to CAM**: Operations, tools, and their order/sequence are exported back to the CAM system.

**Operation details displayed in Manukai**:
- Time (Bearbeitungszeit)
- Distance
- Feed rate (Vorschub)
- Spindle speed (Drehzahl)

**UI display structure**:
```
▼ Through Hole (3)
    Through Hole  ⌀12mm, 25mm deep
    Through Hole  ⌀12mm, 25mm deep
    Through Hole  ⌀8mm, 15mm deep
▼ Pocket (2)
    Pocket  40x30mm, 10mm deep
    Pocket  20x20mm, 5mm deep
```
Features show their type name plus key geometric attributes (e.g., diameter, depth). Individual features are not uniquely named—they all use the Feature Group name. Different Feature Groups display different relevant attributes (e.g., holes show diameter/depth, pockets show dimensions/depth).

**Selection behavior**: Clicking a feature in the sidebar highlights it in the 3D viewer, and clicking geometry in the 3D viewer selects the corresponding feature in the list. Multi-select is supported for assigning operations to multiple features at once.

**Feature/Operation states**: Features and operations have states (e.g., unprocessed, assigned, complete) — currently WIP.

**Merging**: Users can merge faces or features together permanently—typically to correct detection errors where faces were wrongly detected or wrongly attached to a feature. No ad-hoc custom groupings for features—organizational grouping is only available for operations.

**Feature visibility**: No hide/show functionality for features in the 3D view yet.

**Technical drawing linkage**: Technical drawings can be connected to show correspondence—hovering over a feature in the 3D viewport highlights it in the drawing, and vice versa.

**Manual detail assignment**: Some details (e.g., "this hole is a thread") must be manually assigned by the programmer, regardless of whether that info appears in the technical drawing.

### Feature Types

Features in Manukai can be:
- **Predicted Features**: Auto-detected by AI from geometry
- **User Features**: Manually defined/refined by user (including fine-tuning)
- **Features from Operations**: Derived from imported operation data

Common feature types:
- Bohrungen (Drillings/Holes)
- Taschen (Pockets)
- Gewinde (Threads)
- Nuten (Slots)
- Oberflächen (Surfaces)
- Konturen (Contours)
- Fasen (Chamfers)
- Freiformflächen (Freeform surfaces)

### Relationships

- A **Part** can have multiple **Technical Drawings**
- A **Part** can have multiple **Feature Groups**
- A **Feature Group** can contain multiple **Features** (e.g., a "Through Hole" group with 3 individual through holes)
- A **Part** can have multiple **Projects** (different machining approaches)
- A **Project** contains one or more **Programs**
- A **Program** contains ordered **Operations**
- **Features** and **Operations** have a many-to-many relationship (one operation can machine multiple features; one feature may require multiple operations)
- Each **Operation** uses one **Tool**

---

## 3. CAM Domain Terminology

### German-English Glossary

| German | English | Definition |
|--------|---------|------------|
| Schruppen | Roughing | Rapid material removal, leaves stock for finishing |
| Schlichten | Finishing | Final passes for surface quality and dimensions |
| Bohren | Drilling | Creating holes |
| Gewindebohren | Tapping/Threading | Creating internal threads |
| Fräsen | Milling | Material removal with rotating cutter |
| Drehen | Turning | Material removal on rotating workpiece |
| Planfräsen | Face milling | Creating flat surfaces |
| Umfangfräsen | Peripheral milling | Cutting with side of tool |
| Taschenfräsen | Pocket milling | Machining enclosed pockets |
| Spannung / Aufspannung | Setup/Clamping | How part is held (SP1, SP2 = Setup 1, Setup 2) |
| Aufmass | Stock allowance | Material left for subsequent operations |
| Schnittdaten | Cutting data | Feeds, speeds, depths |
| Vorschub | Feed rate | Tool movement speed |
| Drehzahl | Spindle speed (RPM) | Rotation speed |
| Schnittgeschwindigkeit | Cutting speed | Surface speed at tool edge |
| Schnitttiefe | Depth of cut | How deep tool engages |
| Eingriffsbreite | Stepover/Width of cut | Radial engagement |
| Werkzeug | Tool | Cutting tool |
| Werkzeugwechsel | Tool change | Switching tools |
| Standzeit | Tool life | How long tool lasts before replacement |
| Kühlmittel | Coolant | Cooling/lubrication fluid |
| Rohteil | Raw part/Stock | Unfinished material block |
| Toleranz | Tolerance | Allowable dimensional variation |
| Oberflächenrauheit (Ra) | Surface roughness | Surface quality measure |
| Simulation | Simulation | Virtual verification before machining |
| Kollision | Collision | Tool/part/machine interference |
| Postprozessor | Post-processor | Converts toolpaths to machine-specific G-code |

### Operation Types in Manukai

| Operation Type | German | Description |
|----------------|--------|-------------|
| Roughing | Schruppen | Bulk material removal |
| Semi-Finishing | Vorschlichten | Intermediate passes |
| Finishing | Schlichten | Final surface quality |
| Drilling | Bohren | Hole creation |
| Tapping | Gewindebohren | Thread cutting |
| Boring | Aufbohren | Enlarging/finishing holes |
| Face Milling | Planfräsen | Flat surface creation |
| Contour Milling | Konturfräsen | Profile following |
| Pocket Milling | Taschenfräsen | Enclosed area machining |

### Machine Types

| Type | Axes | Common Use |
|------|------|------------|
| 3-Axis Mill | X, Y, Z | Simple prismatic parts |
| 3+2 Axis | X, Y, Z + indexed A/B | Angled features |
| 5-Axis Simultaneous | X, Y, Z, A, B continuous | Complex freeform surfaces |
| Mill-Turn | Milling + turning | Complete parts in one setup |

### Typical Programming Workflow (from Interviews)

**Traditional CAM workflow:**
1. Load CAD data (STEP, native format)
2. Clean/repair geometry if needed
3. Assign material
4. Define stock/raw part
5. Plan setups (Spannungen)
6. Program operations in sequence:
   - Typically: Roughing → Semi-Finishing → Finishing → Drilling → Threading
7. Run simulation
8. Post-process to G-code
9. Transfer to machine

**Manukai-assisted workflow (new part):**
1. Create/load part in CAD system
2. Export to Manukai
3. AI automatically detects Feature Groups and Features
4. For each feature (or group of features), search for similar features in knowledge database
5. Review results, select and apply relevant operations
6. Repeat until all features have operations assigned
7. Export operations back to CAM system
8. Fine-tune parameters in CAM if needed
9. Continue with simulation, post-process, transfer

**Manukai-assisted workflow (existing part):**
Users can also load existing parts from the knowledge database and edit existing programs—useful for optimizing old programs or updating when tools change.

**Standardization** (planned): Users will be able to define default tools or operations that should be used, helping standardize practices across the team. Not implemented yet.

---

## 4. Current Clients

| Client | Location | CAM System | Notes |
|--------|----------|------------|-------|
| PSI | Switzerland | TopSolid, Hypermill | Multiple interviewees, 12-person team |
| Bosch | Schwieberdingen, Germany | Siemens NX | 5-axis CNC, focus on precision |
| Straumann | ? | ? | Medical devices |
| *TODO: Add other clients* | | | |

---

## 5. User Personas (from Research)

### CAM Programmer (Primary User)

**Characteristics:**
- 4-20+ years experience
- Responsible for creating NC programs
- Often sole/limited programmers for multiple machines
- 70%+ of time in CAM software
- Mix of new parts (90%) and optimizations (10%)

**Key Pain Points:**
- Repetitive programming of similar features
- No easy way to reuse proven strategies
- Knowledge loss when colleagues leave
- Bottleneck for production

**What They Value:**
- **Process reliability** over speed (especially for low-volume)
- **Tool life/Standzeit** - want to know when tools need replacement
- **Quality** - surface finish, tolerance adherence
- Clear visualization of what's being proposed
- Ability to fine-tune and maintain control

### CNC Operator (Secondary User)

**Characteristics:**
- Works directly at the machine
- May do simple programming on machine control
- Often older, less comfortable with new software
- Handles setups, tool changes, monitoring

**Interaction with Manukai:**
- Receives programs from CAM programmers
- May make small adjustments at machine (not always fed back to CAM)

---

## 6. Key Design Patterns & Decisions

### Multi-Feature Operations

**Problem**: One operation can machine multiple features (e.g., roughing multiple pockets together).

**Current Design Questions** (from Issue #210):
- How do users select multiple features when assigning an operation?
- How is a multi-feature operation displayed in timeline?
- How handle conflicts/overlaps?
- What happens when removing one feature from multi-feature operation?

### Operation Grouping

**User Mental Model** (from interviews):
- Users group by **Spannung/Setup** (SP1, SP2)
- Convention: `SP1_Teilname` (Setup1_PartName)
- Within setup: typically ordered Rough → Finish → Drill

**Design Questions** (from Issue #197):
- How are groups visually displayed?
- Can operations be dragged in/out of groups?
- Nested groups or flat only?

### Similar Search

**Core Feature**: Find similar features from production history

**Filter Criteria** (from user research):
- Material (critical - aluminum vs. stainless steel = different approach)
- Werkzeug/Tool
- Machine
- Ähnlichkeit/Similarity percentage
- Oberflächenrauheit/Surface roughness
- Time/efficiency
- User/programmer who created it
- Date/recency

### CAM Export Flow

**Current State**: Design needed (Issue #195)

**Key Questions**:
- How does export to TopSolid/MasterCAM/NX work?
- What format is used?
- How are conflicts handled?

---

## 7. Feature Areas (from GitHub Issues)

| Area | Description | Key Issues |
|------|-------------|------------|
| **Similar Search** | Find matching features in history | #199, #200 |
| **Operation Management** | Add, edit, group, sequence operations | #197, #206, #207, #208, #210 |
| **3D Viewer** | Visualize geometry, tolerances, gizmo | #198, #204 |
| **PDF Viewer** | OCR technical drawings, extract tolerances | #196 |
| **Project Management** | History, states, lifecycle | #203 |
| **Feature Assignment** | Group features, manage assignments | #205 |
| **Design System** | Components, consistency | #192, #193 |
| **CAM Integration** | Export flows, keyboard controls | #195, #215 |

---

## 8. Technical Stack

- **App type**: Standalone desktop application (not a CAM add-in)
- **Frontend**: Electron + React
- **Backend**: Python with FastAPI
- **AI/ML**: Separate backend/ML team handles feature detection and similarity algorithms
- **Deployment**: On-premise (no internet required)

---

## 9. Open Questions (TODO)

### Product & Strategy
- [ ] What other clients beyond PSI, Bosch, Straumann?
- [ ] What's the current development phase? (Beta? MVP? Production?)
- [ ] What's the relationship between Manukai (company) and Maji (your team)?
- [ ] What's the target market size / ideal customer profile?

### Technical
- [ ] What is the technical stack (frontend, backend, AI)?
- [ ] How does the geometry similarity algorithm work?
- [ ] What file formats are supported for import?
- [ ] How is on-premise deployment handled?

### Data Model
- [ ] Can a Feature belong to multiple Parts? (diagram shows 1:*)
- [ ] What's the difference between Project and Program in practice?
- [ ] How are operation sequences stored/managed?
- [ ] What metadata is stored for Tools?

### CAM Integration
- [ ] How does the CAM add-in work technically?
- [ ] What gets exported back to CAM software?
- [ ] Is it bidirectional (can import existing CAM programs)?

### User Research
- [ ] Are there synthesized personas beyond what's in interviews?
- [ ] What are the top 3 user pain points prioritized?
- [ ] Any competitive products users mentioned?

### Design
- [ ] Where is the Figma file / design system?
- [ ] What's the current design maturity (wireframes, high-fi, implemented)?
- [ ] Are there established interaction patterns to follow?

---

## 10. Competitive Landscape

| Competitor | Approach | Differentiation from Manukai |
|------------|----------|------------------------------|
| CloudNC CAM Assist | AI generates new toolpaths | Manukai reuses proven history |
| LimitlessCNC | AI copilot in Mastercam | ? |
| Traditional FBM | Template-based feature recognition | Manukai matches whole geometry, not just features |

---

## 11. Key Insights from User Research

### From Interviews (Oct-Dec 2025)

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

**Sorting Preferences**
- By Roughing/Finishing (Schruppen/Schlichten)
- By planes/levels (Ebenen)
- By tool (Fräser)
- Ability to exclude specific operations from sorting

**Important Information to Display**
- Tool preview/illustration
- Material (critical for cutting data)
- Last edited date (recent = more trustworthy)
- Time estimate
- Stock allowance (Aufmass)
- Tool life/Standzeit
- Surface roughness requirements

---

## 12. Appendix: GitHub Issue Labels

| Label | Description |
|-------|-------------|
| `design` | Design issues |
| `feature-design` | New feature design |
| `research` | Research tasks |
| `visual` | Visual/UI issues |
| `improvement` | Enhancements |
| `clarification` | Needs clarification |
| `design-system` | Design system components |
| `Prio 1/2/3` | Priority levels |

---

## Changelog

- **2026-01-03**: Initial creation from GitHub issues #192-216, user interviews, website content, CAM domain research
