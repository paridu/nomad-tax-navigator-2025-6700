-- Schema for storing structured tax data and treaty metadata
CREATE SCHEMA IF NOT EXISTS taxonomy;

CREATE TABLE IF NOT EXISTS taxonomy.countries (
    iso_code CHAR(2) PRIMARY KEY,
    country_name VARCHAR(100) NOT NULL,
    tax_year_start DATE,
    tax_year_end DATE,
    residency_rule_days INTEGER DEFAULT 183
);

CREATE TABLE IF NOT EXISTS taxonomy.tax_treaties (
    id SERIAL PRIMARY KEY,
    country_a_iso CHAR(2) REFERENCES taxonomy.countries(iso_code),
    country_b_iso CHAR(2) REFERENCES taxonomy.countries(iso_code),
    treaty_type VARCHAR(50), -- DTA, TIEA, etc.
    effective_date DATE,
    document_url TEXT,
    raw_content_path TEXT, -- Link to S3/Storage
    vector_collection_id VARCHAR(100) -- Reference to ChromaDB/Pinecone
);

CREATE TABLE IF NOT EXISTS taxonomy.tax_rules (
    rule_id SERIAL PRIMARY KEY,
    iso_code CHAR(2) REFERENCES taxonomy.countries(iso_code),
    category VARCHAR(50), -- 'Income', 'Capital Gains', 'Digital Nomad Visa'
    rule_description TEXT,
    logic_expression JSONB, -- For the Rules Engine (TRE)
    source_citation TEXT
);