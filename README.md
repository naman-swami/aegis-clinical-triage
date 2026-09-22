# Aegis Clinical Decision Support System (CDSS)

> **Emergency Severity Index (ESI v4) & Hemodynamic Sepsis Triage Engine**  
> Operationalizing Shock Index, qSOFA Criteria, and Acuity Stratification for Emergency Departments.

---

> [!CAUTION]
> **Clinical Software as a Medical Device (SaMD) Notice**: Aegis is an algorithmic clinical decision support prototype designed for triage education and protocol verification. It does not replace independent physician diagnosis. Review [CLINICAL_NOTICE.md](CLINICAL_NOTICE.md) before deployment.

---

### Emergency Severity Index (ESI v4) Acuity Algorithm

```
                 Patient Arrival (Vitals & Chief Complaint)
                                   │
                    Does patient require immediate
                   life-saving intervention? (Airway/SpO2/Arrest)
                                  / \
                            YES  /   \  NO
                                /     \
                         LEVEL 1       Is this a high-risk situation?
                       (Resuscitation) Confused/Lethargic? Severe Pain?
                                              / \
                                        YES  /   \  NO
                                            /     \
                                     LEVEL 2       How many diagnostic/treatment
                                    (Emergent)     resources are required?
                                                          /   |   \
                                                        None One  Two+
                                                         /    |     \
                                                    LEVEL 5 LEVEL 4 LEVEL 3
```

---

### Hemodynamic Risk Formulations

1. **Shock Index (SI)**:
   $$SI = \frac{\text{Heart Rate (BPM)}}{\text{Systolic Blood Pressure (mmHg)}} \quad (\text{Normal: } 0.5 - 0.7; \text{ Critical Shock: } > 0.9)$$
2. **qSOFA Sepsis Screening** ($\ge 2$ triggers sepsis alert):
   - Respiratory Rate $\ge 22$ breaths/min (+1)
   - Altered Mental Status ($	ext{GCS} < 15$) (+1)
   - Systolic Blood Pressure $\le 100$ mmHg (+1)

---

### Triage Case Study Evaluation

```bash
# Evaluate real clinical vignettes from data/clinical_vignettes.json
python triage.py --demo

# Run clinical protocol validation tests
pytest tests/ -v
```

Standard triage schemas and vital sign ranges are strictly validated using `schemas/vitals_record.schema.json`. See [EXPLAINABILITY.md](EXPLAINABILITY.md) for full clinical reasoning pathways.
