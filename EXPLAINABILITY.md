# Explainability — aegis-clinical-triage

## Decision Reasoning
Aegis decides triage urgency by identifying chief complaints, cross-referencing physiological vitals against abnormal clinical thresholds, and calculating ESI scores (Tiers 1-5). It constructs differential diagnostic priority lists using evidence-based pathophysiology.

## Data Sources and Inputs Used
Clinical practice guidelines (AHA, ESC, CDC), peer-reviewed triage scales (Emergency Severity Index ESI, Manchester Triage System MTS), and patient intake parameters (vital signs, reported symptoms, timeline).

## Confidence Scoring Methodology
Before returning a final recommendation or analysis, aegis-clinical-triage assigns an internal confidence score (0–100%) based on:
1. **Source Grounding**: High (90–100%) when corroborated by primary authoritative standards and deterministic checks.
2. **Structural Completeness**: Moderate (75–89%) when operating on partial context or heuristic inferences.
3. If confidence falls below 85%, aegis-clinical-triage will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named standards, statutory codes, or operational benchmarks, aegis-clinical-triage explicitly cites the governing framework or canonical specification rather than presenting deductions as ungrounded truths.

## Bias Awareness
aegis-clinical-triage actively accounts for domain-specific operational biases:
- **Baseline Skew**: Avoids over-indexing on standard common scenarios at the expense of rare edge cases.
- **Reporting Disparity**: Recognizes that historical telemetry and training data may underrepresent frontier or non-standard architectures.
- **Jurisdictional & Demographic Neutrality**: Strives to maintain universal, objective evaluation standards across varying environments.

## Limitation Taxonomy per Domain
- Emergency Care: Cannot perform direct physical examinations, palpation, or auscultation.
- Diagnostic Tests: Cannot independently run laboratory blood panels, ECGs, or CT imaging.
- Pharmacology: Cannot prescribe medications; all drug recommendations require physician sign-off.
- Telemedicine: Recommendations are supportive triage advice, not definitive medical diagnoses.

## Uncertainty Quantification Approach
When symptoms present atypical or overlapping presentations (e.g., silent MI in diabetic patients, atypical appendicitis), Aegis flags high diagnostic uncertainty, defaults to the higher acuity safety tier, and mandates immediate bedside physician evaluation.
