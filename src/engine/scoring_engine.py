import math
from typing import List
from src.models.compliance_models import ComplianceFactor, ComplianceReport, RiskLevel

class ComplianceScoringEngine:
    """
    Calculates the Compliance Score based on weighted legal pillars:
    1. Physical Presence (183-day rule)
    2. Permanent Establishment (PE) Risk
    3. Center of Vital Interests (CVI)
    4. Documentation/Reporting Readiness
    """

    def __init__(self):
        self.weights = {
            "physical_presence": 0.40,
            "pe_risk": 0.30,
            "vital_interests": 0.20,
            "documentation": 0.10
        }

    def calculate_presence_score(self, days_spent: int, threshold: int = 183) -> float:
        if days_spent < threshold * 0.8:
            return 100.0
        elif days_spent < threshold:
            # Approaching threshold reduces score linearly
            return max(0, 100 - ((days_spent / threshold) * 100))
        else:
            return 0.0

    def evaluate_risk(self, factors: List[ComplianceFactor]) -> ComplianceReport:
        total_score = sum(f.score * f.weight for f in factors)
        
        if total_score >= 85:
            level = RiskLevel.LOW
        elif total_score >= 60:
            level = RiskLevel.MEDIUM
        elif total_score >= 40:
            level = RiskLevel.HIGH
        else:
            level = RiskLevel.CRITICAL

        return {
            "overall_score": round(total_score, 2),
            "risk_level": level,
            "factors": factors
        }

# Example Usage logic for the Agent logic
def run_assessment(user_data, country_rules):
    engine = ComplianceScoringEngine()
    
    # Logic to map user data to factors
    f1 = ComplianceFactor(
        factor_name="Physical Presence",
        weight=0.4,
        score=engine.calculate_presence_score(user_data['days']),
        evidence=f"User spent {user_data['days']} days in {user_data['country']}"
    )
    # ... more factors
    return engine.evaluate_risk([f1])