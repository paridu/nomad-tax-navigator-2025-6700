from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from enum import Enum

class RiskLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class ComplianceFactor(BaseModel):
    factor_name: str
    weight: float  # 0.0 to 1.0
    score: float   # 0.0 to 100.0
    evidence: str
    mitigation_advice: Optional[str]

class ComplianceReport(BaseModel):
    user_id: str
    country_code: str
    overall_compliance_score: float
    risk_level: RiskLevel
    factors: List[ComplianceFactor]
    dta_applied: bool
    interpretation_summary: str
    next_steps: List[str]

class LegalClauseInterpretation(BaseModel):
    clause_id: str
    original_text: str
    simplified_meaning: str
    applicability_threshold: str
    risk_indicators: List[str]