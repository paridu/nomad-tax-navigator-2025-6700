-- Extensions for Compliance Scoring and Interpretation Logs

CREATE TABLE compliance_scores (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    country_code VARCHAR(3) NOT NULL,
    overall_score DECIMAL(5,2) NOT NULL,
    risk_level VARCHAR(20) NOT NULL,
    assessment_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    metadata JSONB -- Stores the breakdown of factors
);

CREATE TABLE legal_interpretations_cache (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    treaty_id VARCHAR(100),
    clause_reference VARCHAR(50),
    hash_key TEXT UNIQUE, -- Hash of original text to avoid redundant LLM calls
    interpreted_json JSONB,
    last_updated TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_user_compliance ON compliance_scores(user_id, country_code);
CREATE INDEX idx_treaty_lookup ON legal_interpretations_cache(treaty_id, clause_reference);

-- Audit log for legal changes
CREATE TABLE compliance_audit_log (
    id SERIAL PRIMARY KEY,
    entity_type VARCHAR(50), -- 'USER' or 'TREATY'
    entity_id UUID,
    change_type VARCHAR(20),
    previous_value JSONB,
    new_value JSONB,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);