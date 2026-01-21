import openai
from src.models.compliance_models import LegalClauseInterpretation

class LegalInterpreterAgent:
    """
    AI Agent responsible for translating complex DTA (Double Tax Agreement) 
    legalese into actionable logic for the scoring engine.
    """

    def __init__(self, api_key: str):
        self.client = openai.OpenAI(api_key=api_key)
        self.system_prompt = """
        You are a Global Tax Compliance Expert specializing in OECD Model Tax Conventions.
        Your task is to parse Tax Treaty clauses and extract:
        1. The 'Tie-breaker' rule priority.
        2. Specific day-count thresholds for residency.
        3. Definitions of 'Permanent Establishment' for remote workers.
        
        Output must be structured as JSON matching the LegalClauseInterpretation schema.
        """

    def interpret_clause(self, country_a: str, country_b: str, clause_text: str) -> LegalClauseInterpretation:
        prompt = f"Interpret the following treaty clause between {country_a} and {country_b}: \n\n {clause_text}"
        
        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ],
            response_format={ "type": "json_object" }
        )
        
        return LegalClauseInterpretation.model_validate_json(response.choices[0].message.content)

    def assess_permanent_establishment(self, activity_description: str):
        # Specific logic for PE risk (e.g., is a home office a fixed place of business?)
        pass