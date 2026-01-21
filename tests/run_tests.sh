#!/bin/bash

# Exit on any error
set -e

echo "🚀 Starting Global Compliance Compass QA Suite..."

# Run Unit Tests
echo "Running Unit Tests..."
pytest tests/unit --cov=src

# Run Integration Tests
echo "Running Integration Tests..."
pytest tests/integration

# Run Scenario Checks
echo "Running Legal Scenario Validations..."
pytest tests/scenarios -v

echo "✅ All Automated Checks Passed."