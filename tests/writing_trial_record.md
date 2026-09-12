# Recorded Writing Trials

Run date: 2026-09-10. These are synthetic behavior trials, not an evaluation on private manuscripts or a paper-acceptance benchmark.

Two fresh agents each received three independent requests and the repository's `SKILL.md` path. They could read the relevant prompts and blank templates. They were not given the acceptance observations, earlier conversation, research notes or migration notes. The evaluator reviewed their actual output afterwards. Each group of three requests ran in one session, so later requests in that group could reuse already-read skill instructions.

| Trial | Input | Observed output | Verdict within this scope |
|---|---|---|---|
| Grammar-only route | Correct grammar only: “Our system achieve higher throughput in the tested setting.” | “Our system achieves higher throughput in the tested setting.” It explained the single subject–verb correction and read only the entry point and Grammar Checker. | Pass: minimal edit, no unrelated workflow. |
| Alternative reviewer request | Request and materials from [Case B](revision_voice_cases.md#case-b--a-genuine-alternative), without the acceptance section. | Limited the estimator claim to the supplied bounded domain, explicitly stated the absence of an unbounded-input result, and used “We will replace…” with a visible author action. It stated that files had not been edited and covered only the supplied comment. | Pass: preserved the alternative and truthful completion state. |
| Author voice and claim scope | Request and materials from [Case G](revision_voice_cases.md#case-g--the-authors-voice-is-evidence-not-a-score), without the acceptance section. | “Our mechanism removes one lookup. We have not measured application-wide effects.” The style record cited S1/S2, limited its inferences to response letters, and separated inferred patterns from editorial defaults. | Pass: concise author voice with no invented broad benefit. |
| Missing statistical records | Request and materials from [Case C](revision_voice_cases.md#case-c--exact-requirements-with-missing-records), without the acceptance section. | Kept independent run count, SD and CI as three separate pending entries. It did not equate observations with independent runs, calculate unavailable statistics or demand immediate remeasurement. | Pass: exact requirements preserved without invented statistics. |
| Complete review inventory | Request and materials from [Case E](revision_voice_cases.md#case-e--summary-and-closing-contain-distinct-information), without the acceptance section. | Preserved the decision, marked-manuscript requirement, overall, numbered comment and closing. It mapped the code-version request separately, retained visible factual gaps and limited its coverage verdict to supplied material. | Pass: recovered missing source items without inventing an answer. |
| Valid technical terminology | Request and materials from [Case H](revision_voice_cases.md#case-h--technical-words-should-survive-a-style-audit), without the acceptance section. | Retained “orthogonal” and “proves,” explained why the supplied calculation supports them, and offered only an optional tighter sentence. | Pass: technical accuracy took precedence over an unsupported word ban. |

Full trial outputs were retained outside the shared skill repository. This record contains only the independently constructed inputs and observed results. The first three trials preceded a later clarification of project paths and shared evidence IDs; those documentation changes did not alter the tested decision rules. The last three ran after that clarification.

Only these six trials were executed for the 2026-09-10 record: five selected catalog cases and one additional grammar case. The remaining cases in the revision/voice case catalog are available for future trials and are not counted as passes. No author-identity detector, AI percentage, publication outcome or scientific validity claim follows from these results.

## Sentence-flow trials — 2026-09-13

Two agents, separate from the module author, each received three requests and raw records from [sentence_flow_cases.md](sentence_flow_cases.md). They were allowed to read the skill entry point and relevant prompts/references, but were not given the acceptance observations, README, previous trial verdicts or the other agent's output. Existing agent sessions were reused; this was not a fresh-session or controlled comparison benchmark. The first group also followed project-level LaTeX revision-markup instructions. No private research facts were included in the fixtures or published results.

The maintainer reviewed the actual outputs against the source records and edit scope:

| Case | Observed output | Verdict within the supplied scope |
|---|---|---|
| A1 — Module-list paragraph | Kept the first sentence and stated that the shared encoder independently processes each sensor sequence, the resulting vectors are mean-pooled, and the classifier uses the pooled vector. Retained `A shared encoder` and added no accuracy claim. | Pass: repaired the missing data path using the supplied implementation record. |
| A2 — Grammar only | Changed only `store` to `stores`, with the runtime project's requested revision markup. Used the grammar route for this request. | Pass: preserved the subject and narrow edit scope. |
| A3 — Already connected paragraph | Explained the timestamp references across logger, buffer and disk, and returned no necessary repair. Did not rewrite the text. | Pass: retained a justified new subject and passive voice. |
| B1 — Offline versus online action | Attributed calibration to a technician, retained the 8 ms constant, and described the deployed device reading that fixed value. Preserved both original sentences in comments and marked revised prose with `\blue{...}`. | Pass: removed invented adaptation without forcing a single subject. |
| B2 — Unsupported energy consequence | Returned only the documented admissible-range filtering operation and explained that the energy conclusion was removed because no relation had been established. | Pass: did not invent a mechanism, measurement or new experiment; the removed energy claim remains unsupported. |
| B3 — Proposed manuscript and response | The manuscript reported the 7 ms mean CPU execution time over 120 calls and its start/end boundary. The response directly excluded the observation interval, acknowledged the unmeasured collection time, and proposed a revision without claiming an applied edit. | Pass: separated technical exposition, the direct answer and actual completion state. |

All six cases above were executed. Raw outputs were retained outside the shared repository; this record contains only synthetic input descriptions and observed decisions. No full manuscript compilation, venue-quality certification or publication-outcome evaluation was performed. Structural resource checks and unit tests validate different properties from these editorial trials.

## Reasoning-protocol follow-up — 2026-09-13

After adding `Trace The Reasoning`, a fresh agent received only the skill path and the requests/raw records for [C1–C3](sentence_flow_cases.md#c1--individual-availability-does-not-establish-a-common-choice). It read `SKILL.md`, Sentence Flow and Writer. It was instructed not to read README, examples, case acceptance observations, previous records or other agents' output. The three requests ran in one session; they are small synthetic checks, not a controlled quality benchmark. No repository files were edited by the trial agent.

The maintainer compared the actual output with the records and requested scope:

| Case | Actual prose | Verdict within the supplied scope |
|---|---|---|
| C1 — Individual versus common availability | “Each link has an available slot. However, no slot is available to all three links, so they cannot transmit in the same slot.” | Pass: recognized the empty intersection, retained individual availability and removed the invalid guarantee without inventing scheduling behavior. |
| C2 — Intervening definition | “The parser produces records with validity flags. A record is eligible when its validity flag is set. These eligible records are forwarded to the queue.” | Pass: returned the original paragraph unchanged and explained the records–definition–forwarding relation. |
| C3 — Antecedent scope | “The sampler estimates the offset from the reference signal. The controller subtracts the estimated offset from the reading.” | Pass: changed only the ambiguous `it`, using the supplied operation and preserving the actors. |

These three cases were actually executed in addition to the six earlier sentence-flow cases. They check the new reasoning decisions; they do not establish general manuscript quality, scientific validity or venue acceptance.
