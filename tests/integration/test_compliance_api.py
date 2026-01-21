import pytest
from fastapi import status

def test_generate_compliance_report_flow(client):
    """
    E2E Integration Test: Create a profile and request a compliance report 
    to ensure all micro-layers (Ingestion -> Engine -> API) communicate.
    """
    # 1. Setup Test Data
    user_payload = {
        "email": "nomad_tester@example.com",
        "base_country": "DEU",
        "current_location": "THA"
    }
    
    # 2. Mock movement history via API
    movement_payload = {
        "country_code": "THA",
        "entry_date": "2023-01-01",
        "exit_date": "2023-07-15", # Over 183 days
        "type": "WORK_REMOTELY"
    }

    # 3. Request Compliance Analysis
    response = client.post("/api/v1/compliance/analyze", json={
        "user_id": "test-uuid-123",
        "target_country": "THA",
        "movement_history": [movement_payload]
    })

    # 4. Assertions
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    
    assert "overall_compliance_score" in data
    assert data["risk_level"] in ["HIGH", "CRITICAL"]
    assert data["dta_applied"] is True
    assert "Thailand-Germany Tax Treaty" in data["interpretation_summary"]

def test_unauthorized_access(client):
    """Verify security middleware blocks unauthorized requests."""
    response = client.get("/api/v1/profiles/me") # Missing Bearer Token
    assert response.status_code == status.HTTP_401_UNAUTHORIZED