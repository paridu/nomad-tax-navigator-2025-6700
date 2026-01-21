from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.session import get_db
from src.api.services.residency_logic import ResidencyLogicService
from src.models.compliance_models import ComplianceReport, RiskLevel, ComplianceFactor # Imported from previous AI spec

router = APIRouter()

@app.post("/evaluate/{user_id}/{country_code}", response_model=ComplianceReport)
def evaluate_compliance(user_id: int, country_code: str, db: Session = Depends(get_db)):
    """
    Evaluates tax compliance risk for a specific country based on user travel history
    and Double Tax Agreements (DTA).
    """
    # 1. Fetch Travel History
    travels = db.query(TravelEntry).filter(TravelEntry.user_id == user_id).all()
    
    # 2. Calculate Physical Presence
    current_year = date.today().year
    days_spent = ResidencyLogicService.calculate_days_in_country(travels, country_code, current_year)
    residency_triggered = ResidencyLogicService.check_residency_trigger(days_spent)

    # 3. Simulate Logic for DTA and PE Risk (To be connected to AI Agent Service)
     risk_level = RiskLevel.LOW
     if days_spent > 90:
         risk_level = RiskLevel.MEDIUM
     if residency_triggered:
         risk_level = RiskLevel.HIGH

    # 4. Construct Report (Simplified for API Core Service)
    return ComplianceReport(
        user_id=str(user_id),
        country_code=country_code,
        overall_compliance_score=max(0, 100 - (days_spent * 0.5)),
        risk_level=risk_level,
        factors=[
            ComplianceFactor(
                factor_name="Physical Presence Test",
                weight=0.6,
                score=100 if not residency_triggered else 20,
                evidence=f"Spent {days_spent} days in {country_code} in {current_year}.",
                mitigation_advice="Consider leaving before 183 days to avoid automatic tax residency."
            )
        ],
        dta_applied=True,
        interpretation_summary="Evaluation based on Article 4 (Resident) of the Model Tax Convention.",
        next_steps=["Document all business expenses", "Keep boarding passes as evidence of exit"]
    )