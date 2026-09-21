import os
import json
import pytest
from decision_support.triage_evaluator import EmergencyTriageEngine

def test_esi_level_1_resuscitation():
    vitals = {"heart_rate": 30, "respiratory_rate": 6, "systolic_bp": 50, "spo2": 70, "gcs": 3}
    res = EmergencyTriageEngine.evaluate_triage(vitals, is_life_saving_needed=True)
    assert res["esi_level"] == 1
    assert res["placement_target"] == "IMMEDIATE"

def test_esi_level_2_high_risk():
    vitals = {"heart_rate": 115, "respiratory_rate": 20, "systolic_bp": 110, "spo2": 95, "gcs": 15}
    res = EmergencyTriageEngine.evaluate_triage(vitals, is_high_risk=True, expected_resources=2)
    assert res["esi_level"] == 2
    assert res["placement_target"] == "UNDER_10_MINUTES"

def test_esi_level_4_single_resource():
    vitals = {"heart_rate": 72, "respiratory_rate": 14, "systolic_bp": 120, "spo2": 99, "gcs": 15}
    res = EmergencyTriageEngine.evaluate_triage(vitals, is_high_risk=False, expected_resources=1)
    assert res["esi_level"] == 4
    assert res["placement_target"] == "UNDER_60_MINUTES"

def test_clinical_vignettes_consistency():
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    with open(os.path.join(data_dir, "clinical_vignettes.json"), "r") as f:
        cases = json.load(f)
    for c in cases:
        res = EmergencyTriageEngine.evaluate_triage(
            vitals=c["vitals"],
            is_life_saving_needed=c["immediate_life_support"],
            is_high_risk=c["high_risk_flag"],
            expected_resources=c["expected_resources"]
        )
        assert res["esi_level"] == c["gold_standard_esi"]
