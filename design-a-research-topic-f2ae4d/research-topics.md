# Three LLM Research Topics for a Strong Middle School Student

**Student profile:** doing well in USACO (strong algorithms + implementation), has
built a web app before. Comfortable writing real code, thinking rigorously about
correctness, and shipping a front end.

**Design principles used for these topics**

1. **Feasible for a middle schooler** — no GPU training, no huge datasets. Everything
   runs on a laptop using a hosted LLM API (Claude, GPT, Gemini, or a free/local model
   via Ollama) plus a few hundred API calls. Total cost: a few dollars.
2. **Real research, not a demo** — each topic asks a *measurable question* and produces
   a number, a chart, and a conclusion someone could disagree with. That is what makes
   it "research" rather than "I built a chatbot."
3. **Plays to the student's strengths** — the USACO background makes them unusually good
   at (a) writing an automated grader/evaluation harness and (b) reasoning about
   algorithmic problems; the web-app background lets them ship an interactive result
   dashboard, which makes any project look far more finished.

Each topic below is written so the student can start this week and have a real result
in 4–8 weekends.

---

## Topic 1 — Can LLMs Solve USACO? A Benchmark and Failure-Mode Study

**One-line pitch:** Measure exactly how good today's LLMs are at competitive programming,
and *categorize why they fail* — the part almost nobody does carefully.

**Why it's a great fit:** The student already knows USACO deeply. That domain expertise
is the whole edge here — most researchers benchmarking LLMs on code can't tell a "greedy
vs. DP" mistake from a "wrong data structure" mistake. This student can.

**Research questions**
- What fraction of USACO Bronze / Silver / Gold problems can an LLM solve correctly?
- *Where does it break?* (misreads the problem, wrong algorithm choice, right algorithm
  but off-by-one / edge cases, TLE from bad complexity, etc.)
- Does complexity of the intended solution predict failure better than problem length?

**What to build**
- A dataset of ~40–60 USACO problems (public, from the USACO site) with the official test
  data.
- An **automated judge harness** (this is the USACO-flavored part): send the problem to
  the LLM, extract the code, compile it, run it against the official test cases, record
  pass/fail + which tests failed. USACO students already know how to run code against
  test files.
- A hand-built **failure taxonomy**: for each failure, the student labels the *type* of
  mistake. This human-labeled analysis is the scientific contribution.
- A web dashboard (their strength) showing accuracy by division, a heatmap of
  error-type-vs-difficulty, and clickable examples.

**Experiments to run**
- Baseline accuracy per division.
- Does "chain-of-thought" prompting ("first explain your algorithm, then code it") help?
- Does giving the LLM the *intended algorithm tag* (e.g., "this is a DP problem") close
  the gap? That isolates "can't pick the algorithm" from "can't implement it."

**Expected result / deliverable:** a short paper + dashboard: "LLMs solve X% of Bronze,
Y% of Silver, Z% of Gold; failures are dominated by [algorithm selection] on harder
problems and [edge cases] on easier ones."

**Stretch goals:** compare two different models; test whether the LLM can *fix* its own
solution when shown the failing test case (leads directly into Topic 2).

**Feasibility notes:** Fully doable. Main effort is the harness (a weekend for a USACO
kid) and the manual labeling (the valuable, tedious part). No training required.

---

## Topic 2 — Does "Self-Correction" Actually Help? A Controlled Study

**One-line pitch:** LLMs are often told to "check your work." Does that *actually* make
them more correct, or just more confident? Measure it.

**Why it's a great fit:** This is a clean, controlled experiment — exactly the kind of
rigorous thinking a USACO student is good at. It requires carefully defining conditions
and not fooling yourself, which is a real research skill.

**Research questions**
- On a task with a *checkable* answer (arithmetic word problems, small algorithmic
  puzzles, or logic grid puzzles), does asking the model to review and revise its answer
  improve accuracy?
- Does self-correction ever make a *right* answer *wrong* (harmful revisions)? What's the
  net effect?
- Does the model actually *know* when it's wrong? (Compare its self-reported confidence
  to real correctness.)

**What to build**
- Pick one dataset with automatically-checkable answers (e.g., GSM8K grade-school math,
  or a set of generated logic puzzles the student writes a checker for — very USACO).
- Three experimental conditions:
  1. **Direct** — answer once.
  2. **Self-critique** — answer, then "review your answer for mistakes and revise."
  3. **Self-consistency** — sample the answer 5 times, take the majority vote.
- An automated checker for correctness (again, USACO-style grading).
- A results dashboard: accuracy per condition, and a "confusion" chart showing
  right→wrong vs. wrong→right transitions during self-correction.

**Expected result / deliverable:** a paper answering "self-correction helps by +N% on
task A but *hurts* on task B, and majority-voting beats self-critique." A clear, honest,
numerical conclusion — often self-correction helps less than people assume, which is a
genuinely interesting finding.

**Stretch goals:** test whether giving the model a *tool* (a calculator or a code
sandbox) beats pure self-correction. Test whether confidence is calibrated.

**Feasibility notes:** Very feasible; the trickiest part is designing fair conditions and
not letting the checker be buggy — good, character-building research practice.

---

## Topic 3 — Small-Scale RAG: How Much Does Retrieval Reduce Hallucination?

**One-line pitch:** Build a "closed-book vs. open-book" LLM over a chosen document set and
measure exactly how much giving it the source text reduces made-up answers.

**Why it's a great fit:** This one leans on the **web-app** skill. Retrieval-Augmented
Generation (RAG) is the backbone of most real LLM products, so building one is both
resume-worthy and genuinely educational, and the measurement part keeps it honest as
*research* rather than just a demo.

**Research questions**
- For questions about a specific corpus (e.g., a game's rules, a Wikipedia subset, a
  school handbook, or Pokédex data), how often does the LLM hallucinate *with* vs.
  *without* retrieval?
- How does the number of retrieved chunks (k = 1, 3, 5, 10) affect accuracy and wrong
  answers? Is there a point where more context *hurts*?
- Does chunk size matter (short vs. long passages)?

**What to build**
- Pick a self-contained corpus with clear factual answers.
- Write ~50 questions with known correct answers (the ground truth).
- A simple RAG pipeline: split docs into chunks → embed them (embedding API or a local
  model) → for each question, retrieve top-k chunks → ask the LLM using only those
  chunks.
- A web app (their strength) where you can type a question, see the retrieved passages,
  and see the answer — great for demos *and* for debugging.
- An evaluation script that scores answers against ground truth (exact-match or
  LLM-as-a-judge), run across all the k settings.

**Expected result / deliverable:** a paper + interactive demo: "Without retrieval the
model is right X% of the time and confidently wrong Y%; with k=3 retrieval it's right
Z%. Beyond k=5, accuracy plateaus and irrelevant chunks start causing errors."

**Stretch goals:** compare embedding-based retrieval vs. keyword search — does the fancy
method actually beat plain search on this corpus? (Often it barely does — a nice
myth-busting result.)

**Feasibility notes:** The web app makes this the most "shippable" of the three. The
research rigor comes from the fixed question set + ground truth, so it doesn't collapse
into "look, a chatbot."

---

## How to choose

| If the student most enjoys… | Pick |
|---|---|
| Algorithms and competitive programming | **Topic 1** (uses their USACO edge most directly) |
| Clean scientific experiments / "is this claim true?" | **Topic 2** (most rigorous, least building) |
| Building products people can click on | **Topic 3** (uses the web-app skill most) |

**Recommended pick: Topic 1.** It's the most *differentiated* — very few people can do a
careful failure analysis of LLMs on USACO problems, because it requires exactly this
student's rare combination of (competitive-programming expertise + coding a grader +
building a dashboard). It's the topic where this specific student has an unfair advantage.

## A realistic 6-weekend plan (using Topic 1 as the example)

1. **Weekend 1** — Collect 15–20 problems + test data; get one LLM call → code →
   compile → judge loop working end to end.
2. **Weekend 2** — Scale to 40–60 problems; automate the whole batch; store results in a
   JSON/CSV.
3. **Weekend 3** — Hand-label failure types on the first batch; refine the taxonomy.
4. **Weekend 4** — Run the prompting experiments (chain-of-thought, algorithm hints).
5. **Weekend 5** — Build the results dashboard (charts + clickable examples).
6. **Weekend 6** — Write the 4–6 page report; record findings; add one stretch goal.

## Tips for keeping it "research"
- Fix your dataset and questions **before** looking at results (no cherry-picking).
- Always report a **baseline** to compare against.
- Report when something **didn't** work — negative results are real results.
- Keep every prompt and script in a repo so the experiment is **reproducible**.
