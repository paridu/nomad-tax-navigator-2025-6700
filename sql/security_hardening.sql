-- Enable Row Level Security (RLS)
ALTER TABLE user_profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE travel_logs ENABLE ROW LEVEL SECURITY;
ALTER TABLE compliance_reports ENABLE ROW LEVEL SECURITY;

-- Create Policies: Users can only see their own sensitive data
CREATE POLICY user_isolation_policy ON user_profiles
    FOR ALL
    USING (auth_user_id = current_setting('app.current_user_id'));

CREATE POLICY travel_isolation_policy ON travel_logs
    FOR ALL
    USING (user_id = current_setting('app.current_user_id'));

CREATE POLICY compliance_isolation_policy ON compliance_reports
    FOR ALL
    USING (user_id = current_setting('app.current_user_id'));

-- Audit Logging Function
CREATE TABLE IF NOT EXISTS security_audit_log (
    id SERIAL PRIMARY KEY,
    table_name TEXT,
    action TEXT,
    changed_by TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    old_value JSONB,
    new_value JSONB
);

CREATE OR REPLACE FUNCTION audit_trigger_func()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO security_audit_log (table_name, action, changed_by, old_value, new_value)
    VALUES (TG_TABLE_NAME, TG_OP, current_user, to_jsonb(OLD), to_jsonb(NEW));
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Attach Audit to Compliance Reports (Highly Sensitive)
CREATE TRIGGER audit_compliance_changes
AFTER UPDATE OR DELETE ON compliance_reports
FOR EACH ROW EXECUTE FUNCTION audit_trigger_func();