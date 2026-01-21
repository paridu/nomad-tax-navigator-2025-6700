COMPLIANCE_ADVICE_PROMPT = """
Context:
User is a digital nomad from {home_country} currently in {host_country}.
Current Days Spent: {days_spent}
Treaty Status: {treaty_status}
Risk Score: {risk_score}

Task:
Based on the Compliance Score of {risk_score}, generate a priority list of actions 
to minimize tax liability and legal risk. 

Rules:
1. If score < 50, prioritize "Immediate Departure" or "Tax Registration".
2. If score 50-80, prioritize "Documenting Vital Interests".
3. Use professional yet accessible language.
4. Cite specific DTA articles if available.
"""

TIE_BREAKER_ANALYSIS_PROMPT = """
Analyze the 'Tie-Breaker Rule' for residency between {country_a} and {country_b}.
Determine the hierarchy of:
1. Permanent Home
2. Center of Vital Interests
3. Habitual Abode
4. Nationality

Compare this against the user's provided profile: {user_profile}.
Who has the primary taxing right?
"""