# Chapter 2: The Claim-Chasing Workflow

*A repeatable, step-by-step process for verifying every checkable claim in an essay, post, or book chapter.*

---

## The idea in one breath

You're not proofreading. You're a detective following a paper trail: find the claims, chase each one to a source that exists, and mark what you did or didn't verify. Two passes, one ledger, and you're done.

Time cost: **about 10–20 minutes per 1,000 words** once you've practiced. Cheaper than one embarrassing correction.

## The workflow at a glance

```
STEP 1  Dump the draft          — freeze the text you'll verify
STEP 2  Find the claims         — mark every checkable sentence
STEP 3  Triage the claims       — A (must verify) / B (verify if quick) / C (style only)
STEP 4  Confirm the source      — open the real source yourself
STEP 5  Push back on the AI     — make the model help verify its own draft
STEP 6  Fix or hedge            — correct, reword, or hedge honestly (Chapter 3)
STEP 7  Log the ledger          — record what you verified, where, and when
```

The [printable worksheets](04-printable-source-check-worksheets.md) in Chapter 4 match these steps one-to-one, so you can run the whole thing on paper.

Let's walk through each step.

---

## Step 1: Dump the draft

Before verifying, **freeze the version you're checking.** Save the current draft to a file or print it. If you keep chatting with the AI while working, the draft drifts and your verified sentences stop matching your final ones.

Practical habits:

- Name the frozen file with a date: `ch3-draft-2026-11-07.md`
- After verification, diff or re-read before publishing so late edits didn't slip new claims in
- If you must make changes mid-check, re-verify only the changed sentences

## Step 2: Find the claims

A **claim** is any sentence asserting something checkable about the world. You're scanning for six kinds (they map to Chapter 1):

1. Citations, studies, papers ("a 2021 study found...")
2. Statistics and numbers ("73% of users...", "up 3x...")
3. Dates and timelines ("since 2015...")
4. Named people and orgs ("Dr. Reyes, a psychologist at...")
5. Direct quotes ("Einstein never said this, but...")
6. Specifics about products, laws, prices, or events ("the policy took effect in July...")

**Technique: the highlighter sweep.** Read the draft once, fast, and highlight every sentence that contains any of the six. Don't verify anything yet — just mark. In a typical 1,000-word AI-assisted draft, expect 10–25 highlighted sentences.

**Technique: reverse-tip the AI.** Ask the tool that drafted it: *"List every factual claim in this draft that would need a citation if this were published."* AI is genuinely good at this task; it's enumeration, not creativity. Verify the model didn't miss any (AI under-flags its own inventions), but it's a strong second pair of eyes.

## Step 3: Triage the claims

Not every claim deserves equal effort. Sort highlights into three buckets:

| Tier | Meaning | Examples | Your action |
| --- | --- | --- | --- |
| **A — Must verify** | If wrong, damages credibility or misleads readers | Statistics, direct quotes, citations, named sources, legal/product specifics | Full chase: Step 4 required |
| **B — Verify if quick** | Widely-known, low-stakes facts | "WWII ended in 1945," "the Pacific is the largest ocean" | One quick reliable check; if anything feels off, promote to A |
| **C — Style only** | Opinion, common experience, your own reasoning | "A good outline saves time" | No verification; optionally hedge |

Rules of thumb:

- **Any direct quote is automatically A.** Quotes are the single most-invented claim type.
- **Any number is automatically A.** Numbers feel authoritative and are basically never self-checkable.
- **Anything you'd be embarrassed to retract** is A.
- When in doubt, promote up. Verification is cheaper than correction notices.

## Step 4: Confirm the source — open it yourself

This is the heart of the workflow. For each A-claim, you need a **primary source you personally opened**. Not the AI's memory of one. Not a search result you didn't click. **Open it and read the relevant part.**

### Where to chase what

| Claim type | Best first stop | Notes |
| --- | --- | --- |
| Academic study | Google Scholar, PubMed, JSTOR | Search the exact title + author, not just the topic |
| Statistics | The original report/dataset (census, agency, industry body) | Note the report *year* — stats age fast |
| Quotes | Primary interviews, transcripts, official archiving projects | Author websites, transcript archives |
| Named experts | The person's own page, ORCID, university pages | If they can't be found, the claim fails |
| Laws/rules/prices | Official government or vendor pages | Check effective dates against the claim |
| News events | Multiple reputable outlets, or the wire/pr release | Prefer reporting to aggregators |

### The citation test (for "a study found..." claims)

A citation passes only if **all four** are true:

1. **The paper exists** — you can find its real title, authors, venue, and year
2. **It says what's claimed** — the abstract/conclusion actually supports the sentence
3. **The specifics match** — year, sample size, percentage, direction of effect
4. **It's appropriate** — not an obscure preprint carrying weight it shouldn't

### Red flags that a source is invented or misused

- The exact title returns nothing on Scholar
- The DOI/link dead-ends or points to a different paper
- Author + year + journal don't co-occur in any real record
- The study says the *opposite* of the draft's claim (a real classic)
- The AI revises its story when you ask again — a brand-new citation appearing under pressure is a huge flag
- Your "source" is another AI chat answer, a content-farm page, or an unsourced aggregator

### The two-browser rule

Verify in a **different browser or fresh tab session** from the one where you drafted. It sounds superstitious, but it prevents the laziest failure mode: "searching" by asking the drafting chat itself.

## Step 5: Push back on the AI (interrogate the source)

AI can be a surprisingly good verification assistant *about its own draft* — when you push it properly. Run these in order in the same chat where the draft was made:

1. **"Where does this come from?"** — point at the claim and ask for its origin. Vague answers ("common knowledge," "various studies") mean the model doesn't have one.
2. **"Give me links I can check."** — then actually check them. Treat every link as a claim to open, not a fact.
3. **"What would change your mind?"** — ask what evidence would show the claim false. A good answer shows the model can reason about the claim; a waffle means it's borrowing your confidence.
4. **"Rewrite this without the unverified parts."** — ask for a version that only says what can be sourced. This often reveals how much of the sentence was decoration.
5. **Ask twice.** Ask the same factual question with different wording later in the chat. If you get materially different answers, you've found an unstable claim — verify hard or cut it.

**Important:** The model can still hallucinate during this interrogation. Steps 4 and 6 (your own source-checking and your own edits) are what make it safe. Pushing back on AI sharpens your questions; it doesn't replace the chase.

## Step 6: Fix or hedge

When the chase is done, each claim gets one of four outcomes:

| Outcome | What it means | What you do |
| --- | --- | --- |
| **Verified** | Real source, matches specifics | Keep it; add the citation with correct details |
| **Partially true** | Core is right, details off (wrong year, roundup stat) | Rewrite with only what the source supports |
| **Unverifiable** | No source found after honest effort | Hedge honestly (Chapter 3) or cut |
| **Contradicted** | Source says otherwise | Delete or invert — never "balance" a false claim |

Never publish "verified-ish." A claim published with a citation you never opened is the same risk as an uncited claim — plus now the citation is traceable back to you.

## Step 7: Log the ledger

For anything A-tier, add one row to your **claim ledger** (worksheet in Chapter 4):

- The claim, as it will appear in the final text
- The source (with link, title, author, date)
- What matched / what you changed
- Verification date and your initials

Why log it? Three payoffs:

1. **Revisions:** six months later you'll know what was checked — and your ledger row is a ready-made bibliography entry.
2. **Speed:** your next draft reuses the same topics; yesterday's sources are tomorrow's shortcuts.
3. **Reputation:** if anyone ever asks "where did this come from?", you answer in ten seconds with a confident smile.

## The whole workflow in one paragraph (for your wall)

> Freeze the draft. Sweep for claims. Tier them A/B/C. Chase every A to a source you personally opened. Interrogate the AI for pointers, never for facts. Fix, hedge, or cut. Log the ledger. Re-read the final text for late-arriving claims. Publish.

## What "good enough" looks like

Real exhaustion check, for the day you're out of time:

- **Non-negotiable:** every direct quote, every statistic, every citation, every named person — verified or removed.
- **Solid:** every B-tier claim spot-checked against one reliable source.
- **Acceptable:** C-tier style claims left as-is, hedged where reasonable.
- **Never acceptable:** publishing any claim whose "source" is only the fact that the AI wrote it confidently.

## Chapter 2 in three lines

1. Sweep, tier, chase: 10–25 flagged claims in a typical draft, with your effort going to quotes, numbers, citations, and named sources.
2. A citation is only real if *you* opened the source and its details match.
3. The ledger is your verification memory — build it, and each future draft gets faster.

**Next:** [Chapter 3 — Honest Phrasing for Uncertain Facts](03-honest-phrasing-for-uncertain-facts.md)

---

*© 2026 Asdale Dynamics, LLC · MIT license · Educational content only.*
