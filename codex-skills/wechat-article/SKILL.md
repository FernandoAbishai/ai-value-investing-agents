---
name: wechat-article
description: "AI Value Investing Agents skill: WeChat Article: Author–Editor–Reader Multi-Agent Workflow. Source: skills/wechat-article.md."
---

## Codex adapter note

This skill is generated from `skills/wechat-article.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Prefer running commands from the repository root with paths like `python3 tools/financial_rigor.py ...`; if the current thread starts outside the repo, locate the actual checkout path first instead of assuming a fixed home-directory path.
- Before starting research, run the `date` command to confirm today's date; treat it as the baseline for "latest" data and state the data cutoff date in the report header. Never assume the current date from training data.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# WeChat Article: Author–Editor–Reader Multi-Agent Workflow

Research $ARGUMENTS and produce a publication-ready long-form article for WeChat Official Accounts or a comparable public channel.

Three roles collaborate:

- **Author Agent** — researches and writes the substantive draft.
- **Editor Agent** — improves structure, accuracy, pacing, and expression.
- **Reader Agent** — tests whether the intended audience can understand and use the article.

**Supported input**: a topic description, such as a technical-paper explanation, an AI-method overview, a company or industry question, or an investment-framework essay.

## Design Principle

A strong public article must satisfy three requirements:

1. **Depth** — it rewards the time required to read it.
2. **Readability** — its structure and pacing do not push the audience away.
3. **Comprehension** — the intended reader can accurately restate the central idea afterward.

The purpose of the three-agent workflow is to introduce independent editorial and reader perspectives before publication.

## Step 0: Confirm Date, Scope, and Language

Run `date` before researching current technology, markets, products, companies, laws, or events. Put the research cutoff date in the working notes.

Resolve:

| Dimension | Question | Default when absent |
|---|---|---|
| Target reader | What knowledge can be assumed? | Intelligent general reader with some relevant background |
| Depth | Introductory, intermediate, or technical? | Intermediate depth with technical details explained |
| Length | Desired word range? | 3,000–4,000 Chinese characters or an equivalent requested length |
| Language | Chinese, English, or another language? | Simplified Chinese for WeChat unless the user requests otherwise |
| Source material | Is a paper, PDF, filing, or dataset required? | Use primary material when the topic depends on it |
| Visuals | Are figures essential? | Include only visuals that materially improve understanding |
| Style | Formal, conversational, analytical, or sharp? | Conversational analytical prose for an intelligent reader |

Do not interrupt for minor missing preferences when the defaults are adequate. Ask only when a missing decision would materially change the article.

---

## Phase 1: Research and Evidence Collection

### Step 1: Launch Parallel Research

Use Agent or the closest available parallel-research capability to start two or three research tracks.

#### Research Agent A: Core Material

- For a paper: obtain the paper, identify the central contribution, methods, experiments, limitations, and decisive figures.
- For a technical subject: retrieve current primary papers, official documentation, benchmarks, and implementation details.
- For a business or investment subject: retrieve current filings, official data, industry evidence, and competitive information.

#### Research Agent B: Context and Applications

- Explain why the topic matters.
- Identify real deployments, users, products, or companies.
- Retrieve recent milestones and evidence of practical impact.
- Separate demonstrated results from forecasts or marketing claims.

#### Research Agent C: Alternatives and History

When useful:

- compare competing methods, products, or explanations;
- reconstruct the historical path to the current result;
- identify trade-offs, failure modes, and likely next steps.

### Step 2: Apply Source Discipline

- Prefer primary sources: original papers, official documentation, filings, issuer releases, standards, datasets, and direct technical reports.
- Use secondary reporting for context and clearly label it.
- Date every time-sensitive claim.
- Mark every material statement as verified fact, estimate, assumption, or analytical judgment when ambiguity could mislead readers.
- Do not rely on search-result snippets when the underlying document is available.
- Cross-check decision-critical data with at least two independent sources when available.
- Never invent a statistic, quotation, benchmark, experiment, or company adoption claim.

### Step 3: Build the Material Brief

After research completes, produce an internal brief containing:

1. **Central thesis** — one sentence describing what the article must establish.
2. **Reader payoff** — what the audience will understand or decide after reading.
3. **Key evidence** — three to five decisive data points or findings.
4. **Counterevidence and limitations** — the strongest reasons the central thesis may be incomplete.
5. **Visual plan** — which figures are necessary, what they show, and their source/licensing status.
6. **Outline** — six to eight sections, each with a specific purpose.
7. **Terminology list** — terms that require first-use definitions.

---

## Phase 2: Author Agent Draft

Launch an Author Agent with the material brief and the following requirements.

### Author Prompt Template

```text
You are the Author Agent for a publication-ready WeChat long-form article.

Target reader:
{reader profile}

Language:
{requested language}

Length:
{target length}

Core thesis and evidence:
{material brief}

Writing requirements:
- Write for an intelligent reader, not as a literal translation of a paper or report.
- Use plain language without removing the technical substance.
- Define technical terms on first use.
- Use one coherent explanatory analogy only when it improves understanding.
- Include important equations or quantitative results, but explain each in ordinary language.
- Keep paragraphs short enough for mobile reading.
- Do not use emojis unless explicitly requested.
- Avoid generic AI phrasing and promotional language.

Required structure:
1. Opening hook: a verified number, contradiction, concrete event, or counterintuitive result.
2. Why the problem matters.
3. Essential background.
4. Two or three substantive sections explaining the mechanism or argument.
5. Evidence, experiments, or real cases.
6. Limitations and strongest counterargument.
7. Industry or practical implications.
8. Conclusion: a specific, defensible final judgment.

Write the complete first draft.
```

### Formula Requirements

- Use LaTeX: `$...$` inline and `$$...$$` for display equations.
- Do not present equations as unformatted text.
- Explain every equation immediately afterward in ordinary language.
- Include only equations necessary to understand the claim.

### Visual Requirements

For paper or document analysis:

- Use figures only from material the user supplied, public-domain or permissively licensed sources, or sources whose use is reasonably permitted with attribution.
- Preserve the original caption meaning and provide source attribution.
- Do not remove watermarks or ownership marks.
- Do not imply that a redrawn or cropped figure is original work.
- If rights or reuse conditions are uncertain, link to or describe the figure instead of embedding it.

When a usable PDF is available locally, render the relevant page at sufficient resolution and crop only the required figure. Store images under `assets/{topic-slug}/` with descriptive filenames and cite them in Markdown:

```markdown
![Descriptive caption](../../assets/{topic-slug}/fig01-description.png)

Source: {paper/report title, authors or publisher, figure number, year}.
```

For non-paper articles, prefer original diagrams created for the article or properly licensed source images. Do not add decorative images that provide no explanatory value.

After the Author Agent finishes, verify that the complete draft exists and that citations, formulas, figures, and section order are intact.

---

## Phase 3: Parallel Editor and Reader Review

Launch the Editor Agent and Reader Agent in the same message or parallel execution batch.

### Editor Agent Prompt

```text
You are the Editor Agent. Review the complete article below for publication.

Evaluate:
1. Accuracy: are claims supported, qualified, and correctly attributed?
2. Title: is it specific, informative, and short enough for mobile display?
3. Opening: do the first three paragraphs establish a reason to continue?
4. Structure: does every section advance the central thesis?
5. Explanation: are technical concepts genuinely understandable?
6. Pacing: where does the article repeat, slow down, or jump too quickly?
7. Visuals: is every image present, necessary, readable, attributed, and legally usable?
8. Counterargument: does the article present material limitations fairly?
9. Ending: is the final judgment specific and supported rather than promotional?

Article:
{complete draft}

Output:
- Overall assessment in three to five sentences.
- Two or three title alternatives.
- Section-by-section edits with exact replacement wording where necessary.
- Any factual, sourcing, copyright, or logical blockers.
- The three highest-priority improvements.
```

### Reader Agent Prompt

```text
You are the Reader Agent and match this target profile:
{reader profile}

Read the complete article and answer:
1. Would you continue after the first three paragraphs? Why?
2. Which sentence or section was difficult to understand?
3. Can you explain the technical mechanism or main argument in your own words?
4. Did the formulas or visuals improve understanding?
5. Where did attention begin to decline?
6. What is the article's central thesis in one sentence?
7. Which claim felt insufficiently supported or too confident?
8. What important question remains unanswered?
9. Would you share the article, and what description would you use?

Article:
{complete draft}
```

---

## Phase 4: Revision and Finalization

### Step 1: Merge Feedback

Prioritize feedback as follows:

1. Factual, attribution, copyright, or logical errors — mandatory correction.
2. Problems identified by both Editor and Reader — mandatory correction.
3. Editor-only structural or clarity problems — normally correct.
4. Reader-only comprehension problems — correct when representative of the target audience.
5. When Editor and Reader conflict, favor reader comprehension unless doing so would reduce factual accuracy.

### Step 2: Revise the Article

During revision:

- strengthen or replace a weak opening;
- remove repeated explanations;
- add transitions where reasoning jumps;
- reduce formula density when prose or a diagram explains the mechanism better;
- preserve essential nuance and counterevidence;
- replace unsupported certainty with evidence-based language;
- ensure the final sentence follows from the article rather than functioning as a slogan.

### Step 3: Verify Figures and References

For every embedded visual, confirm:

- the file exists and renders;
- the crop is legible on mobile;
- caption and figure number are accurate;
- source and rights status are recorded;
- the article does not use a placeholder such as `[Figure X]`.

For every source, retain title, author or publisher, date, URL or local reference, accessed date where relevant, and primary/secondary classification.

### Step 4: Save the Final File

Use filesystem-safe English slugs while allowing the article text to remain in the requested language.

| Topic type | Path | Filename |
|---|---|---|
| AI or technical research | `reports/ai-industry-research/` | `wechat-{topic-slug}-{YYYYMMDD}.md` |
| Company or investment subject | `reports/{company}/` | `{company}-wechat-{YYYYMMDD}.md` |
| General subject | `reports/` | `wechat-{topic-slug}-{YYYYMMDD}.md` |

At the end, include a concise source section. For a paper article:

```markdown
## Primary material

- {Paper title}, {authors}, {year}: {URL}
```

## Publication Gates

The article is not ready to publish until all gates pass:

- no fabricated or untraceable data;
- no invented or unverified quotations;
- no unsupported superlatives such as “revolutionary” or “guaranteed”;
- every equation is formatted and explained;
- every embedded figure is present, attributed, and usable;
- estimates are labeled;
- current claims include dates;
- the strongest counterargument is represented;
- the title and ending are specific rather than clickbait;
- no private user information or local filesystem identity appears in public output.

For investment or financially material articles, run the repository report-audit process when applicable:

```bash
python3 tools/report_audit.py extract --report {article_path}
python3 tools/report_audit.py verdict --results '<verified JSON>' --report {article_filename}
```

A failed audit means the article remains a draft.

## Writing Red Lines

- Do not open with generic phrases such as “Let us take a look,” “It is worth noting,” or “In today’s rapidly changing world.”
- Do not disguise uncertainty as precision.
- Do not use a famous person’s holdings or reputation as proof of the article’s conclusion.
- Do not manufacture reader urgency.
- Do not use multiple unrelated analogies across sections.
- Do not sacrifice source accuracy for a cleaner narrative.
- Do not publish private, confidential, or user-specific information.
