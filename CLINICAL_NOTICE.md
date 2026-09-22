# Clinical Decision Support Notice & SaMD Regulatory Charter

## 1. Regulatory Status & Classification
**Aegis Clinical Decision Support System (CDSS)** is classified as an investigational and educational Clinical Decision Support tool in accordance with **FDA Guidance on Clinical Decision Support Software (21 CFR Part 860)** and **EU Medical Device Regulation (EU MDR 2017/745, Annex VIII Rule 11)**. 

> [!CAUTION]
> **Not a Substitute for Physician Clinical Judgment**: Aegis is NOT an autonomous diagnostic device. The outputs, acuity categorizations (ESI Levels 1–5), shock index calculations, and qSOFA sepsis flags produced by this software are intended exclusively to assist licensed healthcare practitioners (registered emergency nurses, triage officers, and emergency physicians) as an advisory cognitive aid. The ultimate duty of diagnostic evaluation, resuscitation, and clinical management rests solely with the treating clinician.

---

## 2. Intended Clinical Use & Target Population
- **Target Setting**: Hospital Emergency Departments (ED), Urgent Care Centers, and Field Triage units.
- **Target Population**: Adult patients ($\ge 18$ years of age) presenting with acute physical trauma, non-specific physiological complaints, or acute infection symptoms.
- **Contraindications**: 
  - Neonatal and pediatric triage ($< 18$ years), where age-adjusted Pediatric Early Warning Scores (PEWS) must be applied.
  - Obstetric triage during active labor or third-trimester emergencies, which must follow specialized ACOG/AWHONN Maternal Fetal Triage protocols.
  - Patients unable to provide physiological vital signs or presenting with catastrophic trauma requiring immediate trauma-bay team activation.

---

## 3. Algorithmic Decision Support Frameworks

### A. Emergency Severity Index (ESI Version 4)
The system executes a deterministic triage algorithm based on the Agency for Healthcare Research and Quality (AHRQ) ESI v4 handbook:
- **ESI Level 1 (Resuscitation)**: Patient requires immediate life-saving intervention (e.g., intubation, pulselessness, acute apnea, severe respiratory distress with SpO2 $< 85\%$, or unresponsiveness).
- **ESI Level 2 (Emergent)**: Patient should not wait; high-risk situation, confused/lethargic/disoriented, severe pain/distress, or deranged vital signs (HR $> 100$, RR $> 20$, SBP $< 90$).
- **ESI Level 3 (Urgent)**: Stable vitals; anticipated to require two or more diagnostic or therapeutic resource types (e.g., lab work + CT scan + IV fluids).
- **ESI Level 4 (Less Urgent)**: Stable vitals; anticipated to require exactly one diagnostic or therapeutic resource type (e.g., x-ray or simple laceration repair).
- **ESI Level 5 (Non-Urgent)**: Stable vitals; anticipated to require zero diagnostic or therapeutic resource types (e.g., suture removal, prescription refill).

### B. Hemodynamic Sepsis & Shock Indices
1. **Shock Index (SI)**:
   $$SI = \frac{\text{Heart Rate (BPM)}}{\text{Systolic Blood Pressure (mmHg)}}$$
   - *Normal Range*: $0.5 - 0.7$
   - *Mild Elevation*: $0.7 - 0.9$ (monitor closely for occult hypoperfusion)
   - *Critical Shock*: $> 0.9$ (strongly indicative of systemic hypoperfusion, sepsis, or occult hemorrhage)

2. **quick Sequential Organ Failure Assessment (qSOFA)**:
   - Respiratory Rate $\ge 22$ breaths/minute ($+1$ point)
   - Altered mental status (Glasgow Coma Scale $\text{GCS} < 15$) ($+1$ point)
   - Systolic Blood Pressure $\le 100$ mmHg ($+1$ point)
   - *Clinical Action*: Score $\ge 2$ triggers immediate bedside physician evaluation, lactate draw, and IV access.

---

## 4. Human-in-the-Loop & Clinician Override Protocol
1. **Mandatory Clinician Verification**: Every algorithmic recommendation must be explicitly acknowledged or amended by the attending triage officer before admission to the clinical tracking board.
2. **Clinician Override**: Any registered clinician may override an ESI recommendation based on clinical intuition or qualitative presentation ("patient appears critically toxic"), recording the clinical justification in the medical record.
3. **Audit Logging & Provenance**: All inputs, calculation timestamps, model inferences, and human overrides are permanently logged into immutable session transcripts for quality assurance and morbidity/mortality review.
