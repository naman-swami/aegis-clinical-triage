import pytest
from src.triage_engine import ClinicalTriageEngine

def test_nominal_stable_patient():
    engine = ClinicalTriageEngine()
    patient = {
        "patient_id": "STABLE-001",
        "vitals": {"heart_rate": 72, "systolic_bp": 120, "respiratory_rate": 14, "spo2_percent": 99},
        "gcs": 15,
        "expected_resources": ["examination"]
    }
    res = engine.evaluate_triage(patient)
    assert res["esi_level"] == 5
    assert res["shock_index"] == 0.60
    assert res["qsofa_assessment"]["score"] == 0
    assert res["confidence_score"] >= 0.90

def test_emergent_septic_shock_triage():
    engine = ClinicalTriageEngine()
    patient = {
        "patient_id": "EMERG-002",
        "vitals": {"heart_rate": 125, "systolic_bp": 85, "respiratory_rate": 24, "spo2_percent": 91},
        "gcs": 14,
        "expected_resources": ["blood_cultures", "iv_fluids"]
    }
    res = engine.evaluate_triage(patient)
    assert res["esi_level"] == 2
    assert res["shock_index"] > 1.0
    assert res["qsofa_assessment"]["sepsis_high_risk"] is True
    assert res["allocated_area"] == "Emergent Acute Bed"

def test_immediate_resuscitation_esi1():
    engine = ClinicalTriageEngine()
    patient = {
        "patient_id": "CRIT-003",
        "vitals": {"heart_rate": 150, "systolic_bp": 55, "respiratory_rate": 32, "spo2_percent": 75},
        "gcs": 6,
        "high_risk_flags": ["cardiac_arrest"]
    }
    res = engine.evaluate_triage(patient)
    assert res["esi_level"] == 1
    assert res["allocated_area"] == "Resuscitation Bay"
