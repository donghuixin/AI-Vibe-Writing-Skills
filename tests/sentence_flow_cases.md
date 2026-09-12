# Sentence-flow behavior cases

All requests, prose, records and values below are independently constructed fixtures. They are not manuscript excerpts, real reviews or measurements. Give an evaluator the request and raw material only; withhold acceptance observations and prior trial results. Judge supported meaning and edit scope, not exact wording.

These complement [revision and author-voice cases](revision_voice_cases.md). The module examples explain decisions; these cases check its use on different material. Execution status belongs in [writing_trial_record.md](writing_trial_record.md), not in this catalog.

## A1 — An implementation record supplies the missing connection

**Request:** “This paragraph reads like a list of modules. Make the smallest changes justified by the implementation record. Return the English paragraph and a brief explanation; do not add experimental facts.”

**Original:** “Each sensor produces a temperature sequence. A shared encoder is available in the implementation. A classifier estimates the operating state.”

**Record:** Each sensor's sequence is independently processed by the same encoder. The feature vectors from the sensors are mean-pooled. The classifier receives the pooled vector and outputs the operating-state label. Only this paragraph and record are supplied.

**Acceptance observations:** The repair connects sequences, encoded features, pooling and classifier input using the record. It preserves correct original material and does not add an accuracy or efficiency claim. Keeping `A shared encoder` is valid once its role is clear. The verdict is limited to the supplied scope.

## A2 — Grammar remains a narrow task

**Request:** “Correct grammar only; preserve everything else.”

**Original:** “A buffer store the timestamps until the next flush.”

**Acceptance observations:** Correct `store` to `stores`. Do not replace the subject, remove the indefinite article or launch a wider argument audit. If the project requires revision markup, it may wrap the correction without expanding the edit.

## A3 — A new subject and passive voice can already be clear

**Request:** “Review only. Identify any sentence-connection problem that must be repaired; do not rewrite.”

**Original:** “The logger records packet arrival times. A buffer stores these timestamps until the next flush. The buffered timestamps are then written to disk.”

**Record:** The logger emits one timestamp per arrival; the buffer holds them until flushing; the flush operation writes that buffer's timestamps to disk.

**Acceptance observations:** Recognize the existing timestamp chain. No necessary revision is a valid result. Do not introduce a finding solely because the subjects change, the buffer uses `A`, or the last sentence is passive. Leave source files unchanged.

## B1 — Do not turn calibration into runtime adaptation

**Request:** “Minimally revise these two LaTeX sentences against the implementation record. Preserve replaced original text in `%` comments and mark changed prose with `\blue{...}`. Return the complete fragment and any necessary explanation.”

**Original:** “We selected a sampling interval of 8 ms during calibration. The device adapts this interval as the workload changes.”

**Record:** A technician compares sampling intervals offline during calibration, selects 8 ms and stores it as a constant. The deployed device always reads that constant; it has no workload estimator or interval-update operation.

**Acceptance observations:** Keep offline calibration distinct from the deployed device's fixed setting. Repair the unsupported adaptation without inventing another runtime decision. Maintain the requested comment and highlighting convention; a change from `we` to the device is not itself an error.

## B2 — A clear connective can assert an unsupported relation

**Request:** “Make the argument clearer using existing material only, with no new experiments. Give a minimal revision and necessary unresolved items.”

**Original:** “The filter removes outliers. Therefore, the device consumes less energy.”

**Record:** The implementation discards samples outside the specified admissible range. No energy measurements, comparison configuration or analysis linking this operation to energy consumption is provided.

**Acceptance observations:** Preserve the filtering behavior within the record and remove or explicitly leave unresolved the energy claim. Do not fabricate fewer transmissions, less computation or a quantitative saving as the missing mechanism. A shorter supported account does not resolve the absent energy evidence.

## B3 — A result sentence and a response have different jobs

**Request:** “Give proposed manuscript prose and an English answer to this reviewer question. Only suggested text is requested; no manuscript source file is provided. Do not claim files have already been revised.”

**Original:** “The system delivers an end-to-end latency of 7 ms. We note that this value does not establish all possible deployment delays. This limitation should prevent overinterpretation of our timing result.”

**Synthetic review:** “Does the 7 ms include the observation interval?”

**Record:** The 7 ms is the mean CPU execution time of the classification function over 120 evaluation calls. Timing starts after the input window is already assembled and stops when the label is returned. Observation-collection time was not measured. This manuscript paragraph reports inference timing only.

**Acceptance observations:** The proposed manuscript reports the supported execution metric and relevant conditions without retaining repetitive editorial disclaimers. The response directly distinguishes inference timing from observation collection and states the evidence limit. Do not claim a completed manuscript edit, discard the reviewer's timing question or invent the observation duration.

## C1 — Individual availability does not establish a common choice

**Request:** “Check the inference and minimally revise these two sentences. Preserve established facts; do not add experiments. Return plain English prose and a brief explanation.”

**Original:** “Each link has an available slot. This guarantees that all three links can transmit in the same slot.”

**Record:** Available slots are {1, 2} for L1, {2, 3} for L2 and {1, 3} for L3. The discussed scheme requires all three links to use the same slot for one joint transmission. No other scheduling mechanism is specified.

**Acceptance observations:** Distinguish each link having a slot from all links sharing one slot. The supplied intersection is empty, so the joint-transmission guarantee cannot stand. Retain individual availability, repair the conclusion, and do not invent retries, slot reassignment or an alternative mechanism.

## C2 — An intervening definition carries the paragraph forward

**Request:** “Minimally repair any actual reading discontinuity. If there is none, preserve the paragraph; do not rewrite for its own sake. Return plain English prose and a brief explanation.”

**Original:** “The parser produces records with validity flags. A record is eligible when its validity flag is set. These eligible records are forwarded to the queue.”

**Record:** The parser gives each record a validity flag. Eligible is defined in this paragraph as having that flag set. Only eligible records are forwarded to the queue.

**Acceptance observations:** Keep the definition and the reference to eligible records. The topic is traceable through records, their defined condition and forwarding. Do not require a causal connector, repeated parser subjects, a new conclusion in every sentence or a rewrite of the passive sentence.

## C3 — Resolve the antecedent without rewriting the mechanism

**Request:** “Repair only a reference that affects understanding; preserve other information. Return plain English prose and a brief explanation.”

**Original:** “The sampler estimates the offset from the reference signal. The controller subtracts it from the reading.”

**Record:** The sampler estimates the offset using the reference signal. The controller subtracts the estimated offset from the reading, not the reference signal.

**Acceptance observations:** Make the subtracted object explicit using the record, for example with `the estimated offset`. Retain the sampler/controller roles and original actions. Do not rewrite every pronoun or add a calibration stage, timing rule or quality claim.
