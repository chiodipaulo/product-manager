---
name: ship-decisions
description: Guides "ship or iterate?" decisions using Shreyas Doshi's frameworks, Marty Cagan's shipping philosophy, and Tobi Lutke's reversible decision-making. Use when deciding if feature is ready, preventing perfectionism paralysis, applying one-way vs two-way door thinking, or balancing technical debt vs shipping speed.
---

# The Shipping Decision Matrix

## When This Skill Activates

Claude uses this skill when:
- User asks "is this ready to ship?"
- Deciding between shipping now vs iterating more
- Evaluating if "good enough" is good enough
- Balancing technical debt vs shipping speed
- Preventing perfectionism paralysis

## Core Frameworks

### 1. Reversible vs Irreversible Decisions (Source: Jeff Bezos, applied by Shreyas Doshi)

**One-Way vs Two-Way Doors:**
> "Some decisions are like one-way doors - hard to reverse. Most decisions are like two-way doors - easy to reverse. Don't treat all decisions the same."

**The Framework:**

**🚪 Two-Way Doors (Reversible)**
- Can be undone or changed easily
- Low cost to reverse
- Learning > being right
- **Decision speed:** FAST (hours/days)
- **Process:** Ship and iterate

**🚪 One-Way Doors (Irreversible)**
- Hard or impossible to reverse
- High cost to undo
- Need to get it right
- **Decision speed:** SLOW (weeks/months)
- **Process:** Research, debate, decide carefully

**How to Apply:**
```
Before shipping, ask:
1. "Can we reverse this decision?"
   - YES → Two-way door → Ship fast, iterate
   - NO → One-way door → Go slow, get it right

2. "What's the cost of being wrong?"
   - LOW → Ship and learn
   - HIGH → Research more

3. "Can we learn more by shipping?"
   - YES → Ship to learn
   - NO → Prototype/test first
```

**Examples:**
```
TWO-WAY DOORS (Ship Fast):
✅ Button color
✅ Copy/messaging
✅ UI layout
✅ Feature flag experiments
✅ Pricing (for small customers)

ONE-WAY DOORS (Go Slow):
⚠️ Database schema (migrations expensive)
⚠️ API contracts (breaking changes hurt users)
⚠️ Brand decisions (hard to rebrand)
⚠️ Pricing (for enterprise customers)
⚠️ Architecture (refactoring expensive)
```

---

### 2. The Shipping Scorecard (Source: Shreyas Doshi)

**Is It Ready?**
> "Don't ship broken products. But also don't wait for perfect. Ship when it's good enough for real users to get value."

**The 5-Check System:**

**✅ 1. Core Functionality Works**
- Happy path functions end-to-end
- User can complete main job
- No critical bugs

**✅ 2. Edge Cases Acceptable**
- Not perfect, but handled gracefully
- Errors don't break experience
- User can recover

**✅ 3. Reversible Decision**
- Can we undo or iterate?
- Is this a two-way door?
- What's the rollback plan?

**✅ 4. Learning Value > Polish Value**
- Will shipping teach us more than building more?
- Do we need real user feedback to improve?
- Is hypothetical polish valuable without data?

**✅ 5. Risk Mitigated**
- Critical failure modes addressed
- Monitoring in place
- Gradual rollout plan

**Scoring:**
```
5/5 checks → SHIP NOW
4/5 checks → SHIP TO SMALL GROUP
3/5 checks → ITERATE ONE MORE CYCLE
<3/5 checks → NOT READY
```

---

### 3. Technical Debt vs Shipping Speed (Source: Marty Cagan, Tobi Lutke)

**The Tradeoff:**
> "Technical debt isn't inherently bad. It's bad when it slows you down. Ship fast, pay down debt strategically."

**When to Ship with Tech Debt:**
- **Learning debt:** Need user feedback to validate approach
- **Temporary:** Planning to refactor soon anyway
- **Isolated:** Debt doesn't affect other systems
- **Value >> Debt cost:** User value gained > refactor cost

**When to Pay Down Debt First:**
- **Compounding debt:** Will make future changes harder
- **Security/Privacy:** User trust at risk
- **Platform/API:** Breaking changes expensive
- **Team velocity:** Slowing everyone down

**Framework:**
```
Assess Tech Debt:
1. What's the carrying cost?
   - Slows future features?
   - Blocks other teams?
   - Creates bugs?

2. What's the payoff of fixing?
   - Unblocks work?
   - Reduces bugs?
   - Improves velocity?

3. What's the user value of shipping now?
   - Solves immediate problem?
   - Competitive advantage?
   - Revenue impact?

Decision:
IF (user value > debt cost) → SHIP
IF (debt blocks future) → REFACTOR
IF (uncertain) → SHIP TO SMALL GROUP
```

---

### 4. Gradual Rollout Strategy (Source: Modern tech best practices)

**Don't Ship to Everyone at Once:**
> "The safest way to ship is gradually. Start small, monitor, expand."

**The Rollout Ladder:**

**Stage 1: Internal (1-10 users)**
- Team uses it daily
- Find obvious bugs
- Duration: 1-3 days

**Stage 2: Early Adopters (1-5% users)**
- Select forgiving users
- Eager for new features
- Provide feedback actively
- Duration: 3-7 days

**Stage 3: Broader Beta (10-25%)**
- Larger sample size
- Monitor metrics closely
- Duration: 1-2 weeks

**Stage 4: General Availability (100%)**
- All users
- Stable metrics
- Duration: Ongoing

**Rollback Plan:**
```javascript
// Feature flag implementation
if (isFeatureEnabled(user, 'new-feature')) {
  return newExperience();
} else {
  return oldExperience();
}

// Quick rollback = change flag, no deploy
```

---

## Decision Tree: Ship or Wait?

```
FEATURE: Ready to evaluate
│
├─ Core functionality works? ───────NO──→ FIX CRITICAL BUGS
│  YES ↓
│
├─ Is this reversible decision? ────────┐
│  YES (two-way door) ──────────────────┤
│  NO (one-way door) → RESEARCH MORE    │
│                                        ↓
├─ Edge cases acceptable? ──────────────┤
│  YES ─────────────────────────────────┤
│  NO → FIX OR GRACEFUL DEGRADATION     │
│                                        ↓
├─ Can we learn from shipping? ─────────┤
│  YES ─────────────────────────────────┤
│  NO → TEST/PROTOTYPE MORE             │
│                                        ↓
├─ Risk mitigated? ─────────────────────┤
│  YES → SHIP GRADUALLY                 │
│  NO → ADD MONITORING/ROLLBACK         │
│                                        ↓
└─ SHIP ←───────────────────────────────┘
   Start: Internal → 5% → 25% → 100%
```

## Action Templates

### Template 1: Shipping Readiness Assessment

```markdown
# Feature: [Name]

## Shipping Scorecard

### 1. Core Functionality Works
- [ ] Happy path works end-to-end
- [ ] User can complete main job
- [ ] No critical bugs blocking core use
**Status:** [Ready / Needs work]

### 2. Edge Cases Acceptable
- [ ] Error states handled gracefully
- [ ] User can recover from failures
- [ ] Edge cases don't break experience
**Status:** [Acceptable / Needs improvement]

### 3. Reversible Decision
- Is this reversible? [Yes / No]
- Rollback plan: [describe]
- Two-way door? [Yes / No]
**Status:** [Safe to ship / Risky]

### 4. Learning Value
- Will shipping teach us more? [Yes / No]
- Do we need real user feedback? [Yes / No]
- Is polish speculative without data? [Yes / No]
**Status:** [Ship to learn / Build more first]

### 5. Risk Mitigated
- [ ] Monitoring in place
- [ ] Gradual rollout plan
- [ ] Critical failure modes addressed
**Status:** [Risks managed / Needs work]

## Score: [X / 5]

**Decision:**
- 5/5 → Ship to 5% immediately
- 4/5 → Ship to internal first
- 3/5 → One more iteration
- <3 → Not ready

## Rollout Plan
- [ ] Internal (team): [date]
- [ ] Early adopters (5%): [date]
- [ ] Broader beta (25%): [date]
- [ ] General availability (100%): [date]
```

### Template 2: Tech Debt Decision

```markdown
# Feature: [Name]

## Technical Debt Assessment

### Current Debt
[Describe shortcuts taken, code quality issues]

### Carrying Cost
- Slows future features? [Yes / No / How much]
- Blocks other teams? [Yes / No]
- Creates bugs? [Yes / No / Frequency]
- Security/privacy risk? [Yes / No]

**Debt Impact:** [High / Medium / Low]

### Payoff of Fixing Now
- Time to refactor: [X days]
- Would unblock: [list]
- Would improve: [list]

**Refactor Value:** [High / Medium / Low]

### User Value of Shipping Now
- User problem solved: [describe]
- Revenue/metric impact: [estimate]
- Competitive advantage: [Yes / No]
- User waiting for this: [Yes / No]

**Shipping Value:** [High / Medium / Low]

## Decision

IF Shipping Value > Debt Impact:
→ **SHIP NOW, refactor later**
   Plan: [when to address debt]

IF Debt Impact > Shipping Value:
→ **REFACTOR FIRST, then ship**
   Plan: [how to refactor]

IF Uncertain:
→ **SHIP TO SMALL GROUP (5%)**
   Monitor: [specific metrics]
```

### Template 3: One-Way vs Two-Way Door

```markdown
# Decision: [Description]

## Reversibility Analysis

### Can we reverse this decision?
[Yes / No / Partially]

### Cost to reverse
- Time: [X days/weeks]
- Money: [$X]
- User impact: [High / Medium / Low]
- Team impact: [High / Medium / Low]

### Why hard to reverse?
[Technical, contractual, brand, user expectations, etc.]

## Door Type

**Two-Way Door (Reversible):**
→ Decide in: Hours/days
→ Process: Ship fast, iterate
→ Research: Minimal

**One-Way Door (Irreversible):**
→ Decide in: Weeks/months
→ Process: Research, debate, consensus
→ Research: Extensive

## Decision
Door type: [Two-way / One-way]
Decision timeline: [X time]
Process: [describe]
```

## Quick Reference Card

### 🚢 Shipping Decision Checklist

**Before Evaluating:**
- [ ] Core functionality tested
- [ ] Edge cases identified
- [ ] Rollback plan ready

**The 5 Questions:**
1. **Works?** Core functionality end-to-end ✓
2. **Acceptable?** Edge cases handled gracefully ✓
3. **Reversible?** Can we undo or iterate? ✓
4. **Learn?** Shipping teaches us more than building? ✓
5. **Safe?** Risks mitigated, monitoring ready ✓

**Decision Rules:**
- 5/5 → Ship to small group now
- 4/5 → Ship internal first
- 3/5 → One more iteration
- <3/5 → Not ready yet

**Rollout Ladder:**
1. Internal (team)
2. Early adopters (5%)
3. Broader beta (25%)
4. General availability (100%)

---

## Real-World Examples

### Example 1: Facebook's "Move Fast" Philosophy

**Approach:** Ship fast, break things (early days)
- Two-way doors: Ship immediately
- Feature flags: Easy rollback
- Gradual rollouts: 1% → 5% → 25% → 100%

**Evolution:** "Move fast with stable infrastructure"
- One-way doors: Go slow (API, platform)
- Two-way doors: Still fast (UI, features)

---

### Example 2: Stripe's API Versioning

**Challenge:** Changing API breaks customers

**Decision:** ONE-WAY DOOR
- Treat API as contract
- Never break backwards compatibility
- Version all changes
- Support old versions forever

**Result:** Trust through stability

---

### Example 3: Tech Debt at Airbnb

**Challenge:** Ship new features vs refactor

**Decision Framework:**
- Debt blocking growth → Refactor first
- Debt isolated → Ship, refactor later
- Uncertain → Ship to 5%, measure velocity

**Result:** Strategic debt paydown, maintained velocity

---

## Common Pitfalls

### ❌ Mistake 1: Treating All Decisions Like One-Way Doors
**Problem:** Slow decision-making, perfectionism
**Fix:** Identify two-way doors, ship fast on those

### ❌ Mistake 2: Shipping Broken Core Functionality
**Problem:** "Move fast and break things" gone wrong
**Fix:** Core must work, edge cases can be rough

### ❌ Mistake 3: No Rollback Plan
**Problem:** Ship breaks, no way to undo
**Fix:** Feature flags, gradual rollout

### ❌ Mistake 4: Ignoring Compounding Tech Debt
**Problem:** Short-term speed, long-term slowdown
**Fix:** Strategic debt paydown

---

## Related Skills

- **strategic-build** - For LNO framework (is this Leverage work?)
- **quality-speed** - For craft quality vs shipping speed
- **zero-to-launch** - For MVP scoping decisions
- **exp-driven-dev** - For A/B testing risky changes

---

## Key Quotes

**Jeff Bezos (Amazon):**
> "Some decisions are consequential and irreversible - one-way doors. Make those slowly. Most decisions are reversible - two-way doors. Make those fast."

**Shreyas Doshi:**
> "The best PMs know when 'good enough' is good enough. Ship to learn, not to be perfect."

**Marty Cagan:**
> "Technical debt isn't the enemy. The enemy is debt that compounds and slows you down."

**Tobi Lutke (Shopify):**
> "Trust is built on shipping what you promise. Ship early, ship often, ship small."

---

## Further Learning

- **references/reversible-decisions.md** - One-way vs two-way doors guide
- **references/shipping-checklist.md** - Comprehensive readiness assessment
- **references/gradual-rollout-guide.md** - Feature flag implementation
- **references/tech-debt-paydown.md** - Strategic refactoring frameworks

---

## Atribuição

Este arquivo integra a **PM Especialista**, criada e mantida pelo **Product Guru’s**. Os frameworks, conceitos e métodos citados permanecem atribuídos aos respectivos autores e fontes mencionados neste documento.

Ao transformar este conteúdo em template, canvas, matriz, checklist ou material distribuível, use a assinatura discreta: `Product Guru’s · PM Especialista`.
