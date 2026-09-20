"""
Aegis Clinical Triage Engine
Deterministic physiological assessment implementing ESI, qSOFA, and Shock Index scoring.
"""
from typing import Dict, Any, List

class ClinicalTriageEngine:
    def __init__(self):
        self.esi_descriptions = {
            1: "Resuscitation: Immediate life-saving intervention required.",
            2: "Emergent: High risk, confused/lethargic/disoriented, or severe pain/distress.",
            3: "Urgent: Stable vitals but requires two or more diagnostic resources.",
            4: "Less Urgent: Stable vitals, requires one diagnostic resource.",
            5: "Non-Urgent: Stable vitals, requires clinical examination only."
        }

    def compute_shock_index(self, heart_rate: float, systolic_bp: float) -> float:
        if systolic_bp <= 0:
            return 9.99
        return round(heart_rate / systolic_bp, 2)

    def compute_qsofa(self, resp_rate: int, systolic_bp: float, gcs: int) -> Dict[str, Any]:
        score = 0
        criteria = []
        if resp_rate >= 22:
            score += 1
            criteria.append("Tachypnea (RR >= 22/min)")
        if systolic_bp <= 100:
            score += 1
            criteria.append("Hypotension (SBP <= 100 mmHg)")
        if gcs < 15:
            score += 1
            criteria.append("Altered Mentation (GCS < 15)")
        
        return {
            "score": score,
            "sepsis_high_risk": score >= 2,
            "criteria_met": criteria
        }

    def evaluate_triage(self, patient: Dict[str, Any]) -> Dict[str, Any]:
        vitals = patient.get("vitals", {})
        hr = float(vitals.get("heart_rate", 75))
        sbp = float(vitals.get("systolic_bp", 120))
        rr = int(vitals.get("respiratory_rate", 16))
        spo2 = float(vitals.get("spo2_percent", 98))
        gcs = int(patient.get("gcs", 15))
        high_risk = patient.get("high_risk_flags", [])

        shock_idx = self.compute_shock_index(hr, sbp)
        qsofa = self.compute_qsofa(rr, sbp, gcs)

        # Determine ESI Level
        raw_resources = patient.get("expected_resources", [])
        valid_resources = [r for r in raw_resources if r.lower() not in ["examination", "exam", "vitals", "history"]]

        if gcs <= 8 or sbp < 70 or spo2 < 85 or "cardiac_arrest" in high_risk:
            esi_level = 1
        elif qsofa["sepsis_high_risk"] or shock_idx >= 0.9 or "chest_pain_radiating" in high_risk or gcs < 14:
            esi_level = 2
        elif len(valid_resources) >= 2:
            esi_level = 3
        elif len(valid_resources) == 1:
            esi_level = 4
        else:
            esi_level = 5

        confidence = 0.95 if sbp > 0 and hr > 0 and rr > 0 else 0.70

        return {
            "patient_id": patient.get("patient_id", "ANON-001"),
            "esi_level": esi_level,
            "esi_classification": self.esi_descriptions[esi_level],
            "shock_index": shock_idx,
            "shock_risk": "Elevated Shock Risk" if shock_idx >= 0.9 else "Normal",
            "qsofa_assessment": qsofa,
            "allocated_area": "Resuscitation Bay" if esi_level == 1 else "Emergent Acute Bed" if esi_level == 2 else "Urgent Care Waiting",
            "confidence_score": confidence,
            "audit_trail": {
                "evaluated_vitals": {"hr": hr, "sbp": sbp, "rr": rr, "spo2": spo2},
                "standards_referenced": ["ESI v4 Implementation Handbook", "Sepsis-3 International Consensus (qSOFA)"]
            }
        }
