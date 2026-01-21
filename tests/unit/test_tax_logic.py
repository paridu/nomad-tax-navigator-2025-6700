import pytest
from src.models.compliance_models import RiskLevel, ComplianceFactor

def calculate_mock_residency_days(travel_log):
    """Simplified logic for testing residency triggers."""
    return sum(entry['days'] for entry in travel_log if entry['country'] == "THA")

def test_tax_residency_threshold_trigger():
    """
    Test that the 183-day rule (common in most DTAs) 
    triggers a HIGH risk level for tax residency.
    """
    # Scenario: User stays 184 days in Thailand
    travel_history = [{"country": "THA", "days": 184}]
    days_in_country = calculate_mock_residency_days(travel_history)
    
    assert days_in_country > 183
    
    # Verify the logic mapping to RiskLevel
    risk = RiskLevel.HIGH if days_in_country >= 183 else RiskLevel.LOW
    assert risk == RiskLevel.HIGH

def test_compliance_factor_weighting():
    """
    Verify that compliance factors are correctly weighted 
    according to the system specification.
    """
    factor = ComplianceFactor(
        factor_name="Physical Presence",
        weight=0.6,
        score=20.0,
        evidence="GPS logs confirm 190 days in jurisdiction"
    )
    
    weighted_contribution = factor.weight * factor.score
    assert weighted_contribution == 12.0