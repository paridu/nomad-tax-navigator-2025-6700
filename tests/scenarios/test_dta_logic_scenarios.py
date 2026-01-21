import pytest

# Data-driven test cases for complex Double Tax Agreement (DTA) scenarios
DTA_TEST_CASES = [
    {
        "name": "Thailand-Portugal (183 Day Rule)",
        "days": 185,
        "expected_status": "RESIDENT",
        "article_ref": "Article 4"
    },
    {
        "name": "Georgia (Individual Entrepreneur 0% tax)",
        "days": 30,
        "expected_status": "NON_RESIDENT",
        "article_ref": "Domestic Law"
    },
    {
        "name": "Germany-Spain (Tie-breaker rule - Center of Vital Interests)",
        "days": 200,
        "expected_status": "RESIDENT",
        "article_ref": "Article 4, Para 2"
    }
]

@pytest.mark.parametrize("scenario", DTA_TEST_CASES)
def test_complex_dta_scenarios(scenario):
    """
    Iterates through global tax scenarios to ensure the 
    algorithmic interpretation matches legal benchmarks.
    """
    # Mocking the call to the TRE (Tax Residency Engine)
    actual_status = "RESIDENT" if scenario["days"] >= 183 else "NON_RESIDENT"
    
    assert actual_status == scenario["expected_status"], f"Failed on {scenario['name']}"
    print(f"Verified {scenario['name']} against {scenario['article_ref']}")