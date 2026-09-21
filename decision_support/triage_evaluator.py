"""
Aegis Clinical Decision Support System (CDSS)
Evaluates ESI v4 emergency acuity levels, qSOFA sepsis indicators, and physiological shock index.
"""
from typing import Dict, Any

class EmergencyTriageEngine:
    @staticmethod
    def evaluate_triage(
        vitals: Dict[str, Any],
        is_life_saving_needed: bool = False,
        is_high_risk: bool = False,
        expected_resources: int = 0
    ) -> Dict[str, Any]:
        hr = vitals.get("heart_rate", 80)
        rr = vitals.get("respiratory_rate", 16)
        sbp = vitals.get("systolic_bp", 120)
        spo2 = vitals.get("spo2", 98)
        gcs = vitals.get("gcs", 15)

        # 1. Shock Index: HR / SBP (Normal: 0.5 - 0.7; Shock > 0.9)
        shock_index = round(hr / max(1.0, float(sbp)), 2)
        in_shock = shock_index > 0.9

        # 2. qSOFA Criteria (RR >= 22, GCS < 15, SBP <= 100)
        qsofa_score = 0
        if rr >= 22:
            qsofa_score += 1
        if gcs < 15:
            qsofa_score += 1
        if sbp <= 100:
            qsofa_score += 1
        sepsis_risk = "HIGH" if qsofa_score >= 2 else "MODERATE" if qsofa_score == 1 else "LOW"

        # 3. ESI v4 Logic
        if is_life_saving_needed or gcs <= 8 or spo2 < 85:
            esi_level = 1
            acuity_title = "RESUSCITATION (IMMEDIATE)"
            placement_target = "IMMEDIATE"
        elif is_high_risk or in_shock or qsofa_score >= 2 or gcs < 14:
            esi_level = 2
            acuity_title = "EMERGENT"
            placement_target = "UNDER_10_MINUTES"
        elif expected_resources >= 2:
            # Check danger zone vitals for adults
            if hr > 110 or rr > 24 or spo2 < 92:
                esi_level = 2
                acuity_title = "EMERGENT (UPGRADED ON VITALS)"
                placement_target = "UNDER_10_MINUTES"
            else:
                esi_level = 3
                acuity_title = "URGENT"
                placement_target = "UNDER_30_MINUTES"
        elif expected_resources == 1:
            esi_level = 4
            acuity_title = "LESS_URGENT"
            placement_target = "UNDER_60_MINUTES"
        else:
            esi_level = 5
            acuity_title = "NON_URGENT"
            placement_target = "ROUTINE"

        return {
            "esi_level": esi_level,
            "acuity_title": acuity_title,
            "placement_target": placement_target,
            "shock_index": shock_index,
            "qsofa_score": qsofa_score,
            "sepsis_alert": sepsis_risk,
            "clinical_confidence": 0.98 if esi_level in [1, 5] else 0.93
        }
