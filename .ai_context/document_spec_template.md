# Document Spec Template (Your Single Source of Truth)

**Topic**: [Enter the main topic of the document here]
**Goal**: [What is the primary objective of this writing?]
**Target Audience**: [Who are you writing for? E.g., technical experts, beginners]

## Core Argument (The "Why")
- [What is the central thesis or main takeaway?]
- [Key point 1]
- [Key point 2]

## Structural Constraints
- **Word Count Target**: [e.g., 1000-1500 words]
- **Required Sections**: [List the sections that must be present, e.g., Introduction, Methodology, Conclusion]
- **Format Requirements**: [e.g., Use bullet points for lists, keep paragraphs under 5 sentences]

## Defensive Writing Constraints (Reviewer Attack Surface)
- **Contribution Type**: [method / system / dataset / theory / benchmark / concept_feasibility]
- **Core Contribution Boundary**:
  - [What the paper truly claims as its central innovation]
  - [What evidence directly supports this claim]
- **Non-Core / Deployment Variables**:
  - [Variables that may affect deployment but should not be treated as core failure, e.g., distance, hardware packaging, power tuning]
- **Known Weaknesses To Disclose**:
  - [Weakness 1, e.g., short-range evaluation]
  - [Weakness 2, e.g., limited sample size]
- **Reviewer Attack Surfaces To Preempt**:
  - [e.g., baseline fairness, ablation completeness, generalizability, statistical significance, energy cost]
- **Preferred Defensive Strategy**:
  - **Upper Strategy Candidates (Feature Reframing)**: [Weaknesses that may be reframed as scenario-aligned features]
  - **Middle Strategy Candidates (Engineering Boundary Map)**: [Weaknesses that need cause/boundary/optimization analysis]
  - **Lower Strategy Candidates (Rebuttal Fallback)**: [Weaknesses that require rebuttal backup, claim narrowing, or extra evidence]
- **Claims That Must Be Narrowed**:
  - [Any claim that needs scope conditions because evidence is limited]

## Evidence Requirements (The "Proof")
- **Mandatory References**: 
  - [Reference ID or Title 1 from reference_library]
  - [Reference ID or Title 2]
- **Data/Facts to Include**:
  - [Fact 1]
  - [Data point 2]

## Vocabulary & Memory Constraints (The "Tone & Facts")
- **Hard Memory Terms (Must Use)**: 
  - [Term 1]
  - [Term 2]
- **Negative Constraints (Do NOT Use)**: 
  - [Check error_log.md for these, e.g., "delve", "in conclusion"]

> [!IMPORTANT]
> This Document Spec is the highest priority contract. The Outline Manager and Content Writer MUST strictly adhere to this spec. No writing should commence until this spec is approved by the user.
