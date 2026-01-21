export type RiskLevel = 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';

export interface ComplianceFactor {
  factor_name: string;
  weight: number;
  score: number;
  evidence: string;
  mitigation_advice?: string;
}

export interface ComplianceReport {
  user_id: string;
  country_code: string;
  country_name: string;
  overall_compliance_score: number;
  risk_level: RiskLevel;
  factors: ComplianceFactor[];
  dta_applied: boolean;
  interpretation_summary: string;
  next_steps: string[];
  days_spent: number;
  tax_threshold_days: number;
}