import argparse
import json
import os
from decision_support.triage_evaluator import EmergencyTriageEngine

def main():
    parser = argparse.ArgumentParser(description="Aegis Emergency Clinical Triage CDSS")
    parser.add_argument("--demo", action="store_true", help="Evaluate benchmark clinical vignettes")
    args = parser.parse_args()

    data_dir = os.path.join(os.path.dirname(__file__), "data")
    vignettes_file = os.path.join(data_dir, "clinical_vignettes.json")

    if args.demo:
        with open(vignettes_file, "r") as f:
            vignettes = json.load(f)
        print("=== AEGIS EMERGENCY TRIAGE CLINICAL EVALUATION ===\n")
        for c in vignettes:
            res = EmergencyTriageEngine.evaluate_triage(
                vitals=c["vitals"],
                is_life_saving_needed=c["immediate_life_support"],
                is_high_risk=c["high_risk_flag"],
                expected_resources=c["expected_resources"]
            )
            print(f"Case [{c['case_id']}] Age: {c['age']} | Chief Complaint: {c['presentation']}")
            print(f"  Assigned: ESI Level {res['esi_level']} ({res['acuity_title']}) | Target: {res['placement_target']}")
            print(f"  Shock Index: {res['shock_index']} | qSOFA Sepsis Risk: {res['sepsis_alert']}")
            print("-" * 50)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
