import json
import argparse
from src.triage_engine import ClinicalTriageEngine

def main():
    parser = argparse.ArgumentParser(description="Aegis Clinical Triage Assessment CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated acute clinical triage evaluation")
    args = parser.parse_args()

    engine = ClinicalTriageEngine()
    sample_patient = {
        "patient_id": "PT-94821",
        "chief_complaint": "Acute severe shortness of breath, diaphoretic",
        "gcs": 14,
        "vitals": {
            "heart_rate": 118,
            "systolic_bp": 92,
            "respiratory_rate": 26,
            "spo2_percent": 89
        },
        "high_risk_flags": ["tachypnea_hypoxia"],
        "expected_resources": ["labs", "chest_xray", "iv_antibiotics"]
    }

    report = engine.evaluate_triage(sample_patient)
    print("="*60)
    print(" AEGIS CLINICAL TRIAGE DECISION AUDIT REPORT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
