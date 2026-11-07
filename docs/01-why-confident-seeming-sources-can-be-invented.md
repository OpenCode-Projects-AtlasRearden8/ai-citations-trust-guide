# Chapter 1: Why Confident-Sounding Sources Can Be Invented

*The most dangerous AI sentences are the ones that sound exactly right.*

---

## The scene you probably know

You ask your AI tool for help with a paragraph, and it hands you this:

> "A 2019 study by researchers at Stanford found that 68% of readers never check sources in online articles."

It sounds plausible. It has a year, an institution, a percentage. It *reads* like something that happened. And if you paste it into your draft with a quick mental "that sounds right," you've just published an invented fact under your own byline.

This chapter explains why that happens, so the next part — the actual verification workflow in [Chapter 2](02-the-claim-chasing-workflow.md) — makes sense instead of feeling like paranoid box-ticking.

## The three things AI text generators actually do

Modern AI tools are extraordinary at one core job: **predicting what words should come next** so that a sentence feels fluent, natural, and complete. Three consequences follow directly from that:

### 1. Fluency is not truth

The model is rewarded for making text that *reads correctly*, not text that *is correct*. A sentence can be beautifully written and 100% invented. The polish is not evidence. It's just polish.

### 2. The model writes the shape of a citation, not the citation itself

Because "a 2019 study from Stanford found..." is the *style* of sentence people commonly write, the model can produce that shape perfectly. But the specific study, year, and percentage are filled in the way a novelist fills in dialogue: plausibility first, reality not required.

### 3. Training data has gaps, and the model fills them quietly

AI models learn from enormous amounts of text with a snapshot date — like a photo of the internet at one moment. Anything after that date is often simply unknown to the model, and anything obscure, paywalled, or niche may be barely captured at all. Instead of saying "I don't know that," the model tends to produce the most statistically reasonable-sounding answer. That output is called a **hallucination** — a term of art, not a moral judgment. The model isn't lying; it's generating the likely-looking thing.

## The anatomy of an invented citation

Invented (or "hallucinated") citations usually contain some real ingredients and some fake ones, which is exactly why they fool people. Here's the typical recipe:

| Ingredient | What it looks like | What's real |
| --- | --- | --- |
| **Real author name** | A famous researcher you've heard of | Usually real |
| **Wrong paper** | Attached to work they didn't write, or wrote years earlier/later | Often invented |
| **Wrong year** | Plausible, adjacent to reality | Frequently off |
| **Wrong journal/venue** | Sounds right, doesn't exist or doesn't match | Mixed |
| **Genuine-sounding stat** | "68% of readers...", "3x more likely..." | The most invented part |
| **Reasonable DOI or link** | A string that looks like a real web address | Frequently dead, mismatched, or fabricated |

The trap: because *some* ingredients are real, your brain pattern-matches to "this checks out." Verification means checking every link in that chain, not sampling.

## Six claims AI tools most often invent

From watching writers work and being a writer myself, these are the recurring offenders:

1. **Citations, papers, and quotes by famous people** *(the classic — fake Einstein quotes have floated around the internet for decades on human feeding, and AI inherited the habit)*
2. **Statistics and percentages** — specific numbers feel authoritative and are basically never verifiable inside the model
3. **Dates and timelines** — "in 2015, the industry shifted..." can be smooth nonsense
4. **Named sources** — "according to Dr. A———, chief economist at..." (a person who cannot be found)
5. **Recent events and product details** — anything near or after the model's training snapshot; prices, versions, "the latest research"
6. **Local, niche, or paywalled knowledge** — small-town data, journal articles behind paywalls, internals of companies

If your draft touches any of those six, that's your priority list for Chapter 2.

## Why this isn't just an AI problem (but AI makes it worse)

People invent facts too — that's why fact-checkers have jobs. What's different with AI:

- **Speed and scale.** A person can insert ten dubious facts an hour. An AI draft can arrive with fifty.
- **Confidence without cost.** Humans hesitate when unsure; the model writes the same brisk tone whether it knows or doesn't.
- **No consequence loop.** A human source fears being caught out. The model has no worries — so *you* are the entire quality department.
- **Perfect form.** Citations come pre-formatted, quotes come pre-punctuated, numbers come pre-rounded. The wrapped package screams "finished," which trains you to skim instead of check.

## The mindset shift

Here's the reframing that makes everything in this manual easier:

> **The AI draft is a claim *generator*, not a fact *supplier*.**

A draft from AI is like a rough sketch from a freelance artist you've never worked with: the overall shape may be genuinely useful, and every individual detail might be wrong. You wouldn't print the sketch on the cover of a book without looking at it. Same energy here.

And to be fair in the other direction: AI is *good at finding its own mistakes once you press it*. That's a huge part of the workflow in the next chapter — making the model help you chase the very claims it generated.

## What this doesn't mean

Before we get tactical, two fair warnings about the opposite error:

- **Don't become a verification fundamentalist.** Not every sentence is a checkable claim. "Morning sunlight feels good" is fine. "A 2019 study found morning sunlight reduces cortisol by 25%" is a claim. Chapter 2 shows you how to triage quickly.
- **Don't give up on AI writing.** Used with the workflow, AI cuts drafting time dramatically while keeping accuracy yours. That combination is the whole game.

## Chapter 1 in three lines

1. AI predicts plausible text; it does not verify facts.
2. Citations arrive as plausible *shapes*, with a fake-ingredient mix that pattern-matches as real.
3. Your polished draft is a hypothesis, not a publication-ready document — until it's verified.

**Next:** [Chapter 2 — The Claim-Chasing Workflow](02-the-claim-chasing-workflow.md)

---

*© 2026 Asdale Dynamics, LLC · MIT license · Educational content only.*
