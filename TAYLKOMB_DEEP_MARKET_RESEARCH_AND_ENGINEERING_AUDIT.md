# TAYLKOMB MODULAR PROFESSIONAL COMB SYSTEM
## Deep Market Research & Engineering Audit

**Date:** April 12, 2026  
**Scope:** Research-backed engineering and market audit for patent-pending modular professional comb system  
**Purpose:** Finalize realistic product sizes, length ranges, weight ranges, ergonomic proportions, and production-credible geometry before the next CAD revision

---

## TABLE OF CONTENTS

1. [Executive Verdict](#section-1--executive-verdict)
2. [Part-by-Part Audit](#section-2--part-by-part-audit)
3. [Master Sizing Table](#section-3--master-sizing-table)
4. [Weight & Ergonomics Table](#section-4--weight--ergonomics-table)
5. [Connector Recommendation](#section-5--connector-recommendation)
6. [Materials Recommendation](#section-6--materials-recommendation)
7. [CAD Revision Plan](#section-7--cad-revision-plan)
8. [Prototype Validation Plan](#section-8--prototype-validation-plan)
9. [Parametric Appendix](#section-9--parametric-appendix)
10. [Sources & Evidence](#sources-and-evidence)

---

## SECTION 1 — EXECUTIVE VERDICT

### Current Draft System Assessment

#### Biggest Size Issues

- The **Round Comb Handle** at 242.65 mm overall is at the upper extreme of professional rat-tail/parting-tool length (Y.S. Park 111 = 221 mm; Y.S. Park 132 Extra Long = 239 mm). When combined with the Main Comb via the modular connector, the assembled comb+handle combination reaches ~450+ mm — substantially longer than any single-piece professional comb on the market. Connector overlap (engagement length) must be maximized to keep assembled tools manageable.
- The **Main Comb** body length at 208 mm with a 50.8 mm body height is within the professional cutting-comb envelope (Y.S. Park 332/334 = 185 mm; Sam Villa Long = 222 mm; Hercules Sägemann = 215–230 mm). The body height at ~51 mm is reasonable for a wide-tooth variant but may feel tall for fine cutting work.
- The **3.11 mm tip** on the Round Comb Handle is approximately 2× the diameter of elite metal rat-tail tips (~1.5 mm) and notably larger than typical plastic tips (~2.0–2.5 mm). This will feel blunt for precision parting on fine/straight hair but may be intentional for textured-hair safety.

#### Biggest Ergonomic Issues

- The **Double Handle at 27.2 mm outer grip width** is extremely narrow for a two-prong grip tool. Ergonomic research recommends 32–51 mm for power grip and 6–13 mm for precision pinch. At 27.2 mm, it sits in a dead zone — too wide for a precision pinch and too narrow for a comfortable wrap grip. **This is the single most urgent ergonomic revision.**
- **Assembled weights** must stay under ~45–55 g total for all-day fatigue-free use (benchmark: Y.S. Park cutting combs = 7–17 g; Hercules Sägemann handle combs = ~30 g; Sam Villa Long = ~23 g). The modular connector adds dead weight that single-piece combs don't carry.

#### Biggest Structural Issues

- The **modular connector interface** is the single biggest structural risk. Any connector that wobbles, creaks, or develops play will immediately undermine professional trust. This must be engineered to feel monolithic.
- **Tooth root thickness** and the transition from the tooth into the spine are the most common failure points in professional combs. Without confirmed tooth root dimensions, this requires immediate CAD attention.

#### Biggest Opportunities

- **No premium modular comb system exists on the market.** Y.S. Park, Sam Villa, and Hercules all sell single-piece tools. A system that lets a stylist carry fewer tools and swap configurations is genuinely novel.
- The **multi-handle concept** (round, flat, double) maps directly to distinct use cases (parting, smoothing, twisting) that stylists currently solve by switching between 3–5 separate combs.

#### What Is Closest to Working Now

- Main Comb body length (208 mm) is well-placed within the professional envelope.
- Wide and Narrow Comb overall lengths (~223 mm) are competitive.
- Round Handle working section (187.2 mm) is a credible rat-tail/parting length.

#### What Most Urgently Needs Redesign

1. **Double Handle grip width** (27.2 mm → revise to 32–38 mm)
2. **Round Handle tip diameter** (3.11 mm → revise to 1.8–2.5 mm)
3. **Connector engagement/interface definition** (not yet specified — must be defined before next CAD round)
4. **Assembled-length management** (connector overlap must be maximized to keep assembled tools under ~260 mm for handle combos)

---

## SECTION 2 — PART-BY-PART AUDIT

### 2.1 Main Comb

| Parameter | Current Draft | Assessment |
|-----------|--------------|------------|
| Body length | 208.01 mm | **Keep** — falls between Y.S. Park 332 (185 mm) and Sam Villa Long (222 mm). Sweet spot for multi-purpose professional comb. |
| Overall length | 228.81 mm | **Acceptable pending prototype** — the ~21 mm beyond body suggests a connector tail/block. Must validate that connector block doesn't feel awkward when used solo. |
| Body height | 50.8 mm | **Revise slightly** — good for detangling/wide-tooth but tall for fine cutting. Consider 42–48 mm for the main comb; reserve 50+ mm for the Wide Comb variant. |
| Tooth pitch | Not specified | **Must define** — target 1.5–2.0 mm for fine side, 3.0–4.0 mm for wide side (dual-pitch standard). Y.S. Park uses GDP (Gradually Decreasing Pitch) at ~10 µm/tooth. |
| Tooth length | Not specified | **Must define** — target 28–38 mm (benchmarks: cutting combs ~25–35 mm typical). |
| Connector block | ~21 mm implied | **Acceptable pending prototype** — must have at minimum 12–15 mm engagement depth for wobble-free lock. |

**What Works:** Body length is market-calibrated. The overall envelope is credible.

**What Doesn't Work:** Body height at 50.8 mm may be overbuilt for a "main" cutting/general comb — this dimension is more appropriate for a wide-tooth detangler.

**Ergonomic Concerns:** If the connector block adds significant visual bulk at the spine, it may feel top-heavy or clumsy.

**Structural Concerns:** Tooth root-to-spine transition must have fillets ≥ 0.5 mm radius to prevent stress cracking.

**Confidence Level:** Medium-High — dimensions are in the right ballpark but tooth geometry and connector interface need definition.

---

### 2.2 Round Comb Handle (Rat-Tail/Parting Handle)

| Parameter | Current Draft | Assessment |
|-----------|--------------|------------|
| Overall length | 242.65 mm | **Revise (slightly long)** — Y.S. Park 111 = 221 mm, Y.S. Park 132 Extra Long = 239 mm. At 243 mm, this is at the upper extreme. Target 220–235 mm. |
| Working section | 187.2 mm | **Acceptable but long** — most rat-tail working sections are 120–160 mm. This extra length is only justified if it doubles as a full sectioning/weaving tool. Consider 150–175 mm. |
| Tip diameter | 3.11 mm | **Too thick** — metal tips ≈ 1.5 mm; plastic tips ≈ 2.0–2.5 mm. At 3.11 mm, parting precision is lost. **Revise to 1.8–2.5 mm** (2.0 mm ideal for plastic). |
| Taper logic | Not fully specified | **Must define** — a professional tail taper is typically linear or slightly concave from ~8–10 mm at the base down to the tip over 120–160 mm. |
| Connector block | Implied from length delta | **Must define** — engagement block should be ≥ 12 mm engagement depth. |

**What Works:** The concept of a long tapered working section for weaving/sectioning is sound.

**What Doesn't Work:** Tip is too blunt for precision partwork. Overall length is at the extreme.

**Ergonomic Concerns:** With the working section at 187 mm, the balance point shifts far from the grip when connected to the comb, potentially creating a lever-arm fatigue issue.

**Structural Concerns:** Tips under 2 mm in injection-molded plastic become fragile. Recommend 2.0 mm minimum for production robustness.

**Confidence Level:** Medium — length needs trimming, tip needs thinning, but the concept is valid.

---

### 2.3 Flat Handle

| Parameter | Current Draft | Assessment |
|-----------|--------------|------------|
| Overall length | ~255 mm (dimension chain estimate) | **Too long** — this would be the longest piece in the system. Even if it includes the connector block, the functional handle portion should not exceed ~200 mm. **Revise to 220–240 mm total.** |
| Grip section | Not specified | **Must define** — target 100–130 mm usable grip length (ergonomic standard: 100–152 mm handle length for full-hand grip). |
| Width/thickness | Not specified | **Must define** — target 18–24 mm width × 8–12 mm thickness for a comfortable flat grip. |

**What Works:** The flat handle concept is sound for smoothing, pressing, and controlled detangling.

**What Doesn't Work:** At ~255 mm overall, it's likely overbuilt.

**Ergonomic Concerns:** Flat handles must have radiused edges (R ≥ 1.5 mm on all grip edges) to prevent pressure lines on fingers during long use.

**Structural Concerns:** A long thin flat handle may flex excessively if wall thickness is < 6 mm.

**Confidence Level:** Low-Medium — insufficient dimension detail; needs revision before next CAD pass.

---

### 2.4 Double Handle

| Parameter | Current Draft | Assessment |
|-----------|--------------|------------|
| Overall length | 242.8 mm | **Acceptable pending prototype** — if this is a two-prong fork handle for twist/curl work, this length is credible for reaching through hair sections. |
| Outer grip width | 27.2 mm | **Ergonomically weak — revise immediately** — too narrow for a comfortable two-finger grip. Ergonomic research suggests ≥ 32 mm for any wrap/power grip. Target 32–38 mm outer width. |
| Prong cross-section | Not specified | **Must define** — each prong should be ~8–12 mm diameter/width for comfortable single-prong contact. |
| Fork gap | Implied ~10–14 mm | **Acceptable pending prototype** — the gap between prongs must accommodate hair wrapping without snagging. Minimum 8 mm clear gap. |

**What Works:** The double-prong concept for twisting/curl manipulation.

**What Doesn't Work:** 27.2 mm outer width is the single worst ergonomic dimension in the current draft.

**Ergonomic Concerns:** At 27.2 mm, gripping this handle between thumb and forefinger will cause rapid fatigue and pressure-point discomfort. This is the most urgent fix in the system.

**Structural Concerns:** The fork junction (where two prongs meet the connector block) is a high-stress area. Fillet radius must be ≥ 2.0 mm at the fork root.

**Confidence Level:** Low — width must be revised before any prototype is made.

---

### 2.5 Wide Comb

| Parameter | Current Draft | Assessment |
|-----------|--------------|------------|
| Overall length | 223.23 mm | **Keep** — within the professional wide-tooth comb envelope (190–240 mm typical). Comparable to Hercules Sägemann handle combs (227 mm). |
| Body length | 208.01 mm | **Keep** — matches Main Comb body length, maintaining system consistency. |
| Tooth spacing | Not specified | **Must define** — for wide-tooth detangling on thick/curly hair, target 4.0–6.0 mm pitch (benchmark: professional wide-tooth combs = 6–10 mm for extreme wide, 3.5–5.0 mm for salon wide). |
| Tooth length | Not specified | **Must define** — target 35–45 mm for effective penetration into dense hair. |
| Tooth thickness | Not specified | **Must define** — target 1.8–2.5 mm for teeth, with 2.5–3.5 mm at the root. |
| Body height | Not specified | Target 55–65 mm (tooth length + spine). |

**What Works:** Overall and body lengths are well-calibrated.

**What Doesn't Work:** Cannot assess tooth geometry without dimensions.

**Ergonomic Concerns:** Wide-tooth combs must have absolutely smooth, fully radiused tooth tips (R ≥ 0.3 mm) to prevent snagging on curly/textured hair.

**Structural Concerns:** Wider tooth pitch means longer unsupported tooth spans — root thickness must be increased vs. the narrow comb.

**Confidence Level:** Medium — envelope is good but tooth details are critical and unspecified.

---

### 2.6 Narrow Comb

| Parameter | Current Draft | Assessment |
|-----------|--------------|------------|
| Overall length | 223.67 mm | **Keep** — consistent with system sizing. |
| Body length | 208.01 mm | **Keep** — standardized with Main and Wide, which is correct for the modular system. |
| Tooth spacing | Not specified | **Must define** — for fine-cutting/sectioning, target 1.2–2.0 mm pitch. Y.S. Park fine combs use GDP starting at ~2 mm and decreasing by 10 µm/tooth. |
| Tooth length | Not specified | **Must define** — target 25–32 mm for fine cutting/sectioning work. |
| Tooth thickness | Not specified | **Must define** — target 1.0–1.5 mm for teeth, 1.8–2.5 mm at root. |
| Body height | Not specified | Target 38–45 mm (shorter teeth than wide variant). |

**What Works:** Length and family consistency.

**What Doesn't Work:** Fine teeth under 1.0 mm thickness become fragile in injection molding. Must validate that the tooth count and pitch result in teeth thick enough for production.

**Ergonomic Concerns:** Fine-tooth combs generate more resistance through hair — the spine must be stiff enough to prevent flex during use.

**Structural Concerns:** Fine teeth are the most breakage-prone component. Tooth root fillet radii must be ≥ 0.4 mm.

**Confidence Level:** Medium — envelope is correct, teeth need full parameterization.

---

## SECTION 3 — MASTER SIZING TABLE

| Part | Dimension | Current Draft | Recommended Target | Acceptable Range | Too Small | Too Large | CAD Notes |
|------|-----------|--------------|-------------------|-----------------|-----------|-----------|-----------|
| **Main Comb** | Body length | 208.01 mm | 205 mm | 195–215 mm | <185 mm | >225 mm | Standardize at 205 mm across family |
| | Overall length | 228.81 mm | 220 mm | 215–230 mm | <210 mm | >240 mm | Connector block ≤ 18 mm protrusion |
| | Body height | 50.8 mm | 44 mm | 40–48 mm | <35 mm | >52 mm | Reserve >50 mm for Wide Comb only |
| | Tooth pitch (fine side) | TBD | 1.8 mm | 1.5–2.2 mm | <1.2 mm | >2.5 mm | Consider GDP (Y.S. Park style) |
| | Tooth pitch (wide side) | TBD | 3.5 mm | 3.0–4.5 mm | <2.5 mm | >5.0 mm | — |
| | Tooth length | TBD | 30 mm | 25–35 mm | <22 mm | >40 mm | — |
| | Spine thickness | TBD | 4.5 mm | 3.5–5.5 mm | <3.0 mm | >6.5 mm | Must resist flex under combing load |
| **Round Handle** | Overall length | 242.65 mm | 228 mm | 220–238 mm | <210 mm | >245 mm | Trim tail to reduce assembled length |
| | Working section | 187.2 mm | 160 mm | 145–175 mm | <130 mm | >185 mm | Professional rat-tails top out ~160 mm working |
| | Tip diameter | 3.11 mm | 2.0 mm | 1.8–2.5 mm | <1.5 mm (fragile) | >3.0 mm (blunt) | 2.0 mm ideal for plastic |
| | Base diameter | TBD | 9.0 mm | 8–11 mm | <7 mm | >13 mm | Taper from base to tip |
| | Connector engagement | TBD | 15 mm | 12–18 mm | <10 mm | >22 mm | Standardize across all handles |
| **Flat Handle** | Overall length | ~255 mm | 232 mm | 220–242 mm | <210 mm | >255 mm | Reduce to match system envelope |
| | Grip length | TBD | 115 mm | 100–130 mm | <90 mm | >145 mm | Full-hand wrap zone |
| | Grip width | TBD | 22 mm | 18–26 mm | <15 mm | >30 mm | — |
| | Grip thickness | TBD | 10 mm | 8–13 mm | <6 mm | >15 mm | Edge radius ≥ 1.5 mm |
| **Double Handle** | Overall length | 242.8 mm | 235 mm | 225–245 mm | <215 mm | >255 mm | — |
| | Outer grip width | 27.2 mm | 35 mm | 32–38 mm | <30 mm | >42 mm | **URGENT REVISION** |
| | Prong diameter | TBD | 10 mm | 8–12 mm | <7 mm | >14 mm | Each prong individually |
| | Fork gap (inner) | TBD | 12 mm | 8–16 mm | <6 mm | >20 mm | Hair passage clearance |
| | Fork root fillet | TBD | R 2.5 mm | R 2.0–3.5 mm | <R 1.5 mm | N/A | Critical stress concentration |
| **Wide Comb** | Overall length | 223.23 mm | 222 mm | 215–230 mm | <205 mm | >240 mm | — |
| | Body length | 208.01 mm | 205 mm | 195–215 mm | <185 mm | >225 mm | Match Main Comb |
| | Tooth pitch | TBD | 5.0 mm | 4.0–6.5 mm | <3.5 mm | >8.0 mm | Wide enough for 3C–4C curls |
| | Tooth length | TBD | 40 mm | 35–48 mm | <30 mm | >55 mm | Longer teeth for thick hair |
| | Tooth thickness | TBD | 2.2 mm | 1.8–2.8 mm | <1.5 mm | >3.5 mm | — |
| | Root thickness | TBD | 3.0 mm | 2.5–3.8 mm | <2.0 mm | >4.5 mm | — |
| **Narrow Comb** | Overall length | 223.67 mm | 222 mm | 215–230 mm | <205 mm | >240 mm | — |
| | Body length | 208.01 mm | 205 mm | 195–215 mm | <185 mm | >225 mm | Match Main Comb |
| | Tooth pitch | TBD | 1.6 mm | 1.2–2.0 mm | <1.0 mm | >2.5 mm | GDP optional |
| | Tooth length | TBD | 28 mm | 25–33 mm | <20 mm | >38 mm | Shorter than wide variant |
| | Tooth thickness | TBD | 1.2 mm | 1.0–1.5 mm | <0.8 mm (fragile) | >2.0 mm | — |
| | Root thickness | TBD | 2.0 mm | 1.8–2.5 mm | <1.5 mm | >3.0 mm | Fillet R ≥ 0.4 mm |

---

## SECTION 4 — WEIGHT & ERGONOMICS TABLE

### 4.1 Individual Part Weights

| Part | Target Weight | Max Suggested Weight | Balance Notes | Grip Type | Fatigue Risk |
|------|--------------|---------------------|---------------|-----------|-------------|
| **Main Comb (solo)** | 12–18 g | 22 g | Center of mass at mid-spine. No connector weight penalty when used solo. | Spine pinch between thumb and index | Low if weight is within range |
| **Round Handle (solo)** | 8–14 g | 18 g | Balance at ~60% from connector end toward tip for natural "pencil hold" feel | Precision pencil grip | Low |
| **Flat Handle (solo)** | 10–16 g | 20 g | Balance at mid-grip zone | Full-hand wrap or three-finger hold | Low-Medium (edge comfort critical) |
| **Double Handle (solo)** | 10–16 g | 20 g | Balance at fork junction | Two-finger straddle grip | **Medium-High** (current width = high fatigue) |
| **Wide Comb** | 14–20 g | 25 g | Slightly tooth-heavy acceptable for detangling pull-through | Spine pinch | Low-Medium |
| **Narrow Comb** | 10–16 g | 20 g | Center-balanced | Spine pinch | Low |

### 4.2 Assembled Weights

| Assembly | Target Weight | Max Suggested Weight | Balance Notes | Primary Grip |
|----------|--------------|---------------------|---------------|-------------|
| **Main Comb + Round Handle** | 22–30 g | 38 g | Balance point within ±15 mm of connector junction for neutral feel | Transitions between grip types |
| **Main Comb + Flat Handle** | 24–32 g | 40 g | Balance at or near handle grip center | Wrap grip on flat handle |
| **Main Comb + Double Handle** | 24–32 g | 40 g | Balance at fork junction | Fork straddle |
| **Wide/Narrow + any Handle** | 24–34 g | 42 g | Similar logic | Varies |

**Maximum All-Assembly Weight Before Fatigue Concern:** 45 g

> *Benchmark: Hercules Sägemann handle combs at ~30 g are considered comfortable for all-day use.*

### 4.3 Balance-Point Recommendations by Task

| Task | Recommended Mass Ratio (Comb:Handle) | Rationale |
|------|--------------------------------------|-----------|
| **Detangling** | 55:45 (comb-heavy) | Helps teeth pull through hair with less wrist force |
| **Parting** | 45:55 (handle-heavy) | Keeps the parting tip responsive and controlled |
| **Smoothing** | 50:50 (neutral) | Even control for surface work |
| **Twisting** | 40:60 (handle-heavy) | The handle does the work; comb needs to stay light and responsive |

### 4.4 Grip Recommendations

| Grip Mode | Application | Handle Diameter/Width | Surface Treatment |
|-----------|-------------|----------------------|-------------------|
| **Precision grip** (pencil hold) | Parting, sectioning | 8–13 mm | Smooth surface, no sharp edges |
| **Power grip** (full wrap) | Detangling through thick hair | 32–40 mm | Textured or soft-touch surface |
| **Modified precision** | Smoothing, pressing | 18–26 mm (flat) | Radiused edges, slight texture |

### 4.5 Ergonomic Risks in Current Draft

| Risk | Severity | Part Affected |
|------|----------|--------------|
| Double Handle 27.2 mm width | **CRITICAL** | Double Handle |
| Assembled tool length exceeding ~260 mm | **HIGH** | All handle combos |
| Round Handle tip at 3.11 mm (poor parting precision) | **HIGH** | Round Handle |
| No soft-touch or grip texture indicated | **MEDIUM** | All handles |
| Main Comb body height at 50.8 mm (overbuilt for cutting) | **MEDIUM** | Main Comb |

---

## SECTION 5 — CONNECTOR RECOMMENDATION

### Recommended Interface: Hybrid Rail-and-Slide with Positive Detent Lock

#### Why Not Pure Snap-Fit

Standard cantilever snap-fits fatigue after 100–1,000 cycles in most injection-molded plastics. For a professional tool that may be swapped 5–20× per day (1,500–6,000 swaps/year), a pure snap-fit will develop play within 6–12 months.

> *Source: Fictiv Snap-Fit Design Guide; BOYI Injection Molding Design Guide; Xometry Snap-Fit Joints reference.*

#### Why Not Pure Twist-Lock

Twist-lock (bayonet) systems are excellent for cycle life (10,000+) but add rotational alignment complexity that may feel unnatural for a comb — stylists want fast, linear attachment, not a two-step twist.

#### Recommended Architecture

1. **Linear rail engagement** — the handle connector slides onto the comb spine connector block along a dovetail or T-slot rail (12–18 mm engagement length).
2. **Positive detent click** — at the end of travel, a spring-loaded or cantilevered detent ball/nub clicks into a mating pocket, providing audible/tactile confirmation of lock.
3. **Release via button or thumb depression** — a small thumb-activated release lifts the detent to allow slide-off.

#### Why This Is Best for TAYLKOMB

- **Linear motion** feels fast and intuitive (push-on, click, done)
- **Dovetail rail** eliminates wobble in 2 axes
- **Detent click** provides positive lock and premium "click" feedback
- **Small release button** prevents accidental detachment while styling
- **Cycle life:** Dovetail surfaces wear slowly; the detent ball/nub is the only fatigue element and can be designed with a small separate spring or living-hinge element in fatigue-resistant material (POM or PA66-GF)

#### Tolerance Logic

| Parameter | Value | Notes |
|-----------|-------|-------|
| Rail width | Nominal ± 0.05 mm | Tight slip fit |
| Rail depth | Nominal ± 0.08 mm | — |
| Detent engagement | 0.3–0.5 mm click depth | Enough for secure lock, shallow enough for easy release |
| Overall rail clearance | 0.05–0.10 mm per side | Prevents rattle while allowing smooth slide |
| Seam step | ≤ 0.15 mm | Flush junction to prevent snagging |

#### Seam Strategy

- The connector junction should have a **flush seam** with ≤ 0.15 mm step between comb body and handle at the parting line.
- All edges at the seam should be **chamfered 0.3–0.5 mm × 45°** to eliminate any hair-snagging lip.
- A subtle **decorative groove or ridge** at the seam can visually mask any mismatch while serving as a physical hair-deflection feature.

#### Wear Risks

| Wear Point | Risk Level | Mitigation |
|-----------|-----------|-----------|
| Detent nub/pocket | Primary | Design as replaceable insert or oversize contact area |
| Rail surfaces | Secondary | 0.2–0.5 mm draft on rail walls; smooth finish |
| Long-term clearance increase | Expected ~0.05 mm over 5,000 cycles | Acceptable if initial fit is tight |

#### Standardization Requirements

**ALL 5 interchangeable pieces** (Main Comb, Wide Comb, Narrow Comb, and the connector-receiving end of all 3 handles) must use the **identical connector block geometry:**

- Same rail profile
- Same engagement length (target 15 mm)
- Same detent pocket location
- Same seam-line position

> **This is a non-negotiable system constraint. Define the connector as a master datum and derive all parts from it.**

---

## SECTION 6 — MATERIALS RECOMMENDATION

### 6.1 Primary Recommendation

**POM (Acetal/Delrin) for comb bodies + PA66-GF30 for handles/connector**

| Component | Recommended Material | Rationale |
|-----------|---------------------|-----------|
| **Comb bodies** (Main, Wide, Narrow) | **POM (Acetal)** | Excellent chemical resistance (bleach, Barbicide, salon solvents), low moisture absorption, low friction (teeth glide), dimensional stability, stiff in thin sections (teeth). Proven in precision consumer tools. |
| **Handles** (Round, Flat, Double) | **PA66-GF30** (30% glass-filled nylon) | Superior fatigue resistance at the connector flex zones, excellent strength, good heat resistance (260°C+ HDT), tough enough for drop impacts. Glass fill provides stiffness for connector rail. |
| **Connector detent element** | **POM** or spring-tempered stainless steel wire | POM detent nubs have excellent wear/fatigue for snap-in cycles. Alternatively, a 0.5 mm stainless spring wire detent adds near-infinite cycle life. |
| **Teeth** | **POM** (same as body) | Low friction, smooth surface finish, good chemical resistance. Tooth tips can be tumble-polished or vapor-smoothed. |

### 6.2 Alternative Material Options

| Option | When to Consider |
|--------|-----------------|
| **Ultem (PEI)** | If budget allows — superior heat resistance (220°C Tg), sterilization-safe, used by Y.S. Park. ~3–5× cost of POM. Best for premium-tier product positioning. |
| **Carbon-fiber-filled PA66** | If maximum stiffness is needed at the spine or connector. Adds cost and may feel less "premium" at tooth tips. |
| **Polycarbonate (PC)** | **AVOID** — poor chemical resistance to salon solvents and stress-cracking risk with Barbicide/alcohol. |
| **Hard rubber (ebonite)** | Only if pursuing Hercules Sägemann-level heritage positioning. Not practical for modular connectors. |

### 6.3 Hybrid Material Strategy: RECOMMENDED

Using POM for comb bodies and PA66-GF30 for handles is a **smarter strategy** than single-material because:

1. **POM** excels where chemical contact is highest (teeth, spine, body surfaces in direct contact with hair chemicals)
2. **PA66-GF30** excels where mechanical fatigue is highest (connector rail, detent flex zone, handle grip under repeated hand stress)
3. Both are injection-moldable in the same facility
4. Color matching between POM and PA66-GF is achievable with standard masterbatch

### 6.4 Critical Material Properties by Component

| Component | Most Critical Property | Secondary Property |
|-----------|----------------------|-------------------|
| **Teeth** | Low friction + chemical resistance | Stiffness in thin sections |
| **Connector rail** | Fatigue life + dimensional stability | Wear resistance |
| **Round Handle tip** | Toughness at small cross-section | Chemical resistance |
| **Spine** | Bending stiffness | Chemical resistance |
| **Detent nub** | Fatigue life over 10,000+ cycles | Dimensional stability |

### 6.5 Chemical Resistance Comparison

| Chemical/Class | PA66-GF | PC | POM (Acetal) |
|----------------|---------|-----|-------------|
| Alcohols | Good | Poor | Good |
| Acids (mild/moderate) | Fair | Fair | Good (mild) |
| Strong Alkalis | Poor | Poor | Fair |
| Oily solvents | Good | Good | Excellent |
| Peroxide/disinfectants | Fair | Poor | Good |
| Bleach/Ammonia | Poor | Poor | Fair |
| Water/steam | Fair | Excellent | Excellent |
| Moisture stability | Improved if glass-filled | Excellent | Excellent |

> *Sources: Professional Plastics Chemical Resistance Chart; Curbell Plastics Nylon vs. Acetal comparison; CyLex Plastics POM vs. Nylon guide.*

### 6.6 What Still Needs Material Validation

- POM tooth tips at 1.0–1.2 mm thickness: **mold-flow simulation needed** to confirm fill and ejection
- POM-to-PA66-GF color match: **sample shots needed**
- Chemical immersion test: both materials in Barbicide, salon bleach, and color developer for **30-day accelerated exposure**

---

## SECTION 7 — CAD REVISION PLAN

### 7.1 CHANGE NOW (Before Next CAD Pass)

| Priority | Revision | Part | Urgency |
|----------|----------|------|---------|
| 1 | Widen Double Handle to 35 mm outer | Double Handle | **Immediate** |
| 2 | Define connector master datum (rail, detent, engagement) | ALL PARTS | **Immediate** |
| 3 | Reduce Round Handle tip to 2.0 mm | Round Handle | **Immediate** |
| 4 | Reduce Main Comb body height to 44 mm | Main Comb | **Immediate** |
| 5 | Define all tooth dimensions (pitch, length, thickness, root) | Main/Wide/Narrow | **Immediate** |
| 6 | Trim Round Handle to 228 mm overall | Round Handle | **Next pass** |
| 7 | Trim Flat Handle to 232 mm overall | Flat Handle | **Next pass** |
| 8 | Add seam chamfers and fork fillets | All connectors, Double Handle | **Next pass** |
| 9 | Define spine thickness at 4.5 mm | All combs | **Next pass** |
| 10 | Add grip texture zones on all handles | All handles | **Pre-prototype** |

### 7.2 KEEP FOR NOW (Dimensions That Work)

- Main Comb body length: 208 mm (standardize at 205 mm across family)
- Wide Comb overall length: 223 mm
- Narrow Comb overall length: 224 mm
- Wide/Narrow body length: 208 mm (standardize at 205 mm)
- Double Handle overall length: 243 mm (acceptable after width revision)

### 7.3 PROTOTYPE BEFORE LOCKING

- Connector engagement feel: must validate click force, slide smoothness, wobble
- Round Handle balance point when assembled
- Tooth flex and breakage under load (especially Narrow Comb fine teeth)
- Flat Handle edge comfort during 30-minute continuous use
- Wide Comb tooth pitch effectiveness on 3C–4C curl patterns
- All assembled-weight combinations

### 7.4 DO-NOT-LOCK-YET LIST

| Dimension/Feature | Reason |
|-------------------|--------|
| Connector detent force | Must be tuned by prototype feel testing |
| Tooth pitch distribution (uniform vs GDP) | Must validate on hair |
| Wide Comb tooth pitch final value | Must test on 3B–4C hair |
| Flat Handle cross-section proportions | Must validate hand comfort |
| Round Handle taper curve (linear vs concave) | Must test parting feel |
| Surface texture type and location | Must validate grip and aesthetics in hand |
| Final material selection (POM vs Ultem) | Must validate cost at volume and chemical exposure |

### 7.5 HIGH-RISK LIST

| Risk | Severity | Mitigation |
|------|----------|------------|
| Connector develops wobble after 2,000+ swaps | **High** | Dovetail rail + positive detent; test to 15,000 cycles |
| Narrow Comb teeth break during detangling | **High** | Minimum 1.0 mm tooth thickness, R 0.4 mm root fillet |
| Assembled tool feels toy-like (too light/cheap) | **Medium** | Target 25–35 g assembled, premium surface finish |
| Connector seam snags hair | **High** | Chamfer + flush seam ≤ 0.15 mm step |
| Round Handle tip snaps off in use | **Medium** | Min 2.0 mm tip, PA66-GF material |
| Double Handle fork junction cracks | **Medium** | R 2.5 mm fillet, PA66-GF material, thickness ≥ 4 mm at junction |

---

## SECTION 8 — PROTOTYPE VALIDATION PLAN

| Test | Method | Pass Criteria | Parts Tested |
|------|--------|--------------|-------------|
| **Comfort Test** | 10 professional stylists use each assembled combo for 30-minute sessions; rate comfort 1–10 and identify pressure points | Average score ≥ 7/10; no pressure-point complaints from >2 testers | All assemblies |
| **Fatigue Test** | 4-hour continuous professional use (salon simulation): cutting, detangling, parting, twisting | No hand cramping, numbness, or discomfort reported; weight/balance acceptable | All assemblies |
| **Repeated Swap Test** | Automated or manual cycling: connect/disconnect 15,000 times | Wobble < 0.1 mm lateral play after 10,000 cycles; detent click force within ±20% of initial | Connector interface |
| **Detangling Performance Test** | Compare TAYLKOMB Wide Comb to Y.S. Park 452 and Hercules Sägemann wide-tooth on 3B–4C textured wigs | Equivalent or better glide, less snagging, comparable detangling time | Wide Comb + handles |
| **Snag Test** | Pull assembled tool through 100 passes of loose synthetic hair at seam zone; inspect for caught/broken fibers | Zero snags at connector seam across 100 passes | All assembled combos |
| **Heat/Chemical Exposure Test** | Immerse in 40°C Barbicide for 72 hours; immerse in salon bleach (vol 30) for 24 hours; expose to 220°C heat gun for 30 seconds | No warping, discoloration, surface degradation, or mechanical property loss >10% | All parts |
| **Drop/Breakage Test** | Drop assembled tool from 1.5 m onto concrete, tooth-first and handle-first, 5 times each orientation | No broken teeth, no connector separation, no handle fracture | All assemblies |
| **Stylist Field-Use Test** | 5 professional stylists use the system for 2 weeks in real salon conditions; collect daily journal + exit interview | Positive professional endorsement; no tool failure; connector remains tight; identifies any geometry tweaks needed | Full system |

---

## SECTION 9 — PARAMETRIC APPENDIX

### 9.1 Coordinate Reference System

- **Origin:** Center of connector block mating face (the face where comb meets handle)
- **X-axis:** Along tooth direction (perpendicular to spine, pointing toward tooth tips)
- **Y-axis:** Along spine/comb body length (pointing from connector end toward comb free end)
- **Z-axis:** Along spine thickness (perpendicular to flat face of comb body)

### 9.2 Connector Master Datum

```
Connector Rail Profile: Dovetail
  - Base width: 6.0 mm
  - Top width: 4.0 mm
  - Depth: 3.0 mm
  - Engagement length: 15.0 mm along Y-axis
  - Detent pocket center: 12.0 mm from leading edge of rail
  - Detent pocket diameter: 2.0 mm hemisphere
  - Detent nub diameter: 2.1 mm (0.1 mm interference for click)
  - All mating surfaces: ±0.05 mm tolerance
```

### 9.3 Taper Equations — Round Handle

```
D(y) = D_base - (D_base - D_tip) × (y / L_taper)^n

Where:
  D_base = 9.0 mm (diameter at connector junction)
  D_tip  = 2.0 mm (tip diameter)
  L_taper = 160 mm (working section length)
  y      = distance from base (0 to L_taper)
  n      = 1.0 for linear taper
           0.85 for slightly concave (RECOMMENDED)
```

> A concave taper (n < 1.0) keeps more material near the base for stiffness while reaching a fine tip.

### 9.4 Tooth-Array Spacing Logic

#### Uniform Pitch (Wide Comb)

```
x_i = i × P
Where:
  P = tooth pitch (e.g., 5.0 mm)
  i = tooth index from 0 to N-1
  N = floor(L_body / P) + 1
```

#### Gradually Decreasing Pitch (GDP) — Fine/Narrow Comb (Y.S. Park style)

```
P_i = P_0 - (i × δ)
Where:
  P_0 = starting pitch (e.g., 2.0 mm)
  δ   = pitch decrement per tooth (e.g., 0.010 mm per tooth)
  x_i = Σ(P_j) for j = 0 to i-1
```

> This creates progressively tighter teeth from one end to the other, providing graduated tension control.

### 9.5 Centerline Logic

- All comb bodies share the same spine centerline at Z = spine_thickness/2
- Tooth centerline perpendicular to spine at each tooth position x_i
- Handle centerline aligns with connector rail centerline (coaxial)
- Round Handle: single centerline; circular cross-sections along taper
- Double Handle: two parallel centerlines offset ±(outer_width/2 - prong_radius) from central axis

### 9.6 Section Transition Rules

| Transition | Minimum Fillet Radius | Notes |
|-----------|----------------------|-------|
| Any cross-section change >20% over <5 mm | R ≥ 1.0 mm | General rule |
| Spine-to-connector transition | R ≥ 1.5 mm | Structural |
| Fork junction (Double Handle) | R ≥ 2.5 mm | High stress |
| Tooth root (fine teeth) | R ≥ 0.4 mm | Breakage prevention |
| Tooth root (wide teeth) | R ≥ 0.6 mm | Breakage prevention |
| All handle grip edges | R ≥ 1.5 mm | Comfort |

### 9.7 Connector Block Proportions

```
Block length (Y):  18 mm (15 mm engagement + 3 mm end wall)
Block width:       Match spine width + 1 mm per side for rail walls
Block height (Z):  Match spine thickness
Rail pocket:       Centered in block width
```

### 9.8 Parametric Relationships (System-Level)

```
Body_length_all_combs = 205 mm (standardized)
Overall_comb_length = Body_length + Connector_block_protrusion
Connector_block_protrusion = 15 mm (engagement) + 3 mm (end wall) = 18 mm
Overall_comb_length_target = 205 + 18 = 223 mm

Assembled_length = Overall_comb_length + Handle_overall_length - 2 × Engagement_length
Example: Main Comb + Round Handle = 223 + 228 - 2(15) = 421 mm

CRITICAL INSIGHT:
Assembled comb+handle will be ~420 mm for the Round Handle combo.
This exceeds single-tool comfort length and must be validated for wrist comfort.
Consider offering a "short handle" option at ~120 mm for compact assemblies.
```

---

## SOURCES AND EVIDENCE

### Market Benchmark Sources

1. **Y.S. Park official specifications** — yspark.co.jp — models 101, 102, 103, 111, 332, 334, 337, 339, 402
2. **Sam Villa Signature Series specifications** — saloncentric.com, samvilla.com
3. **Hercules Sägemann specifications** — hercules-saegemann.de, amazon.com listings
4. **Tangle Teezer Wide Tooth Comb** — us.tangleteezer.com

### Ergonomic Research Sources

5. **CCOHS Hand Tool Ergonomics** — ccohs.ca/oshanswers/ergonomics/handtools/tooldesign.html
6. **California DOSH Hand Tool Ergonomics** — dir.ca.gov/dosh/dosh_publications/handtools5.html
7. **CDC grip optimization study** — stacks.cdc.gov/view/cdc/196025
8. **VelocityEHS Ergonomic Handle Design** — ehs.com/blogs/ergonomic-handle-design-considerations/

### Materials Sources

9. **SABIC Ultem PEI datasheet** — sabic.com — Tg 217°C, tensile ~110 MPa
10. **Curbell Plastics PEI properties** — curbellplastics.com/materials/plastics/ultem/
11. **Professional Plastics Chemical Resistance Chart** — professionalplastics.com
12. **Nylon vs. Acetal comparison** — curbellplastics.com, cylexplastics.com

### Connector Design Sources

13. **Fictiv Snap-Fit Design Guide** — fictiv.com/articles/how-to-design-snap-fit-components
14. **BOYI Snap-Fit Design** — boyiprototyping.com
15. **Xometry Snap-Fit Joints** — xometry.pro
16. **ESINOUSA High-Performance Snap-Fit** — esinousa.com

### Engineering Inferences (Labeled)

- **Assembled tool balance-point ratios:** Engineering inference based on center-of-mass principles — no direct published data for modular comb systems.
- **Connector engagement length of 15 mm:** Engineering inference — derived from dovetail/rail connector best practices in similar-scale consumer products.
- **GDP tooth spacing parameters:** Engineering inference extrapolated from Y.S. Park's published "10 micron per tooth" description.
- **Weight targets:** Engineering inference — derived by scaling from known benchmark weights and adding estimated connector overhead (3–6 g per connector block).

---

## MARKET BENCHMARK REFERENCE DATA

### Professional Comb Benchmark Summary

| Brand / Model | Type | Overall Length | Weight | Material | Heat Resistance | Key Feature |
|---------------|------|---------------|--------|----------|----------------|-------------|
| Y.S. Park 332 | Cutting | 185 mm | 10 g | Ultem/PEI | 220°C | GDP pitch, parting head |
| Y.S. Park 334 | Cutting | 185 mm | ~10–17 g | Ultem/PEI | 220°C | GDP pitch |
| Y.S. Park 337 | Mid-length cutting | 190 mm | ~9 g | Ultem/PEI | 220°C | GDP pitch |
| Y.S. Park 339 | Fine cutting | 178 mm | 10–12 g | Ultem/PEI | 220°C | GDP pitch, most popular model |
| Y.S. Park 402 | Cutting | 190 mm | 17 g | Ultem/PEI + Carbon | 220°C | Nano Carbon Black |
| Y.S. Park 111 | Rat-tail | 221 mm | 7 g | Ultem/PEI | 220°C | GDP, precision tail |
| Y.S. Park 101 | Tail | 216 mm | 7 g | Super plastic | 220°C | Standard tail |
| Y.S. Park 102 | Tail | 220 mm | 9 g | Super plastic | 150–220°C | Metal tail option |
| Sam Villa Short | Cutting | 203 mm | 17 g | Carbon/graphite/silicone | 232°C (450°F) | Graphite composite |
| Sam Villa Long | Cutting | 222 mm | 23 g | Carbon/graphite/silicone | 232°C (450°F) | Graphite composite |
| Hercules Sägemann Multi | Multi-purpose | 230 mm | ~30 g | 100% ebonite (hard rubber) | Heat resistant | Hand-crafted, 35+ steps |
| Hercules Sägemann Handle | Detangling | 227 mm | ~30 g | 100% ebonite | Heat resistant | Anti-static, flexible |

### Key Benchmark Insights for TAYLKOMB

1. **Length envelope:** Professional cutting combs cluster at 178–222 mm. Handle/tail combs extend to 221–239 mm. TAYLKOMB's comb body lengths (205–208 mm) are perfectly positioned.
2. **Weight:** Elite combs weigh 7–30 g. TAYLKOMB assembled weights should target 22–35 g to feel premium but not fatiguing.
3. **Material:** The market leader (Y.S. Park) uses Ultem/PEI. POM is a strong cost-effective alternative with comparable chemical resistance.
4. **Tooth technology:** GDP (Gradually Decreasing Pitch) is the gold standard. TAYLKOMB should offer GDP on the Narrow Comb at minimum.
5. **No modular competitor exists.** This is TAYLKOMB's unique value proposition.

---

*Document generated as part of TAYLKOMB product development — April 2026*
*This document is confidential and intended for internal engineering and design use.*
