# Aegis Clinical Triage CDSS

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![Healthcare](https://img.shields.io/badge/Domain-Emergency_Medicine_CDSS-darkred.svg)](protocols/esi_v4_protocol.md)
[![Standard](https://img.shields.io/badge/Protocol-ESI_v4_Standard-orange.svg)](protocols/esi_v4_protocol.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

A clinical decision support system (CDSS) for emergency departments conforming to ACEP and ESI v4 standards, incorporating physiological shock index calculation and qSOFA sepsis screening.

```
                    ┌─────────────────────────┐
                    │ Patient Presentation    │
                    │   & Vitals Telemetry    │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   Physiological Shock   │
                    │   & qSOFA Sepsis Check  │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   ESI v4 Decision Tree  │
                    │   (Levels 1 through 5)  │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ Bedside Placement Alert │
                    │ (IMMEDIATE / <10m / etc)│
                    └─────────────────────────┘
```

## Features

- **ESI v4 Decision Logic**: Stratifies acute emergency arrivals across Level 1 (Resuscitation) to Level 5 (Non-urgent).
- **qSOFA Sepsis Screening**: Real-time evaluation of organ dysfunction criteria (respiratory rate $\ge 22$, mentation GCS $< 15$, SBP $\le 100$).
- **Shock Index Monitoring**: Early detection of occult hemodynamic collapse ($	ext{HR} / 	ext{SBP} > 0.9$).
- **Vitals Schema Validation**: Built-in JSON Schema enforcing clinical observational limits.

## Directory Structure

```
aegis-clinical-triage/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint medical decision provenance
├── decision_support/
│   └── triage_evaluator.py          # Clinical acuity & sepsis scoring engine
├── protocols/
│   └── esi_v4_protocol.md           # ACEP clinical decision standard
├── schemas/
│   └── vitals_record.schema.json    # JSON Schema for vital observations
├── data/
│   └── clinical_vignettes.json      # Gold-standard reference patient cases
├── tests/
│   └── test_agent.py                # Clinical triage accuracy test suite
├── triage.py                          # CDSS CLI
└── requirements.txt
```

## Quick Start

```bash
# Run triage test suite
pytest tests/ -v

# Evaluate benchmark clinical cases
python triage.py --demo
```

## Medical Device Notice

This software is an educational and investigational clinical decision support aid. It does not replace the independent medical judgment of a licensed emergency physician or triage nurse.
