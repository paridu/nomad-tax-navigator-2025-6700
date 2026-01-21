"""
Core Logic for determining Tax Residency based on the 183-day rule 
and Tie-breaker rules found in most DTAs.
"""

class ResidencyEngine:
    def __init__(self, user_travel_history, home_country, host_country):
        self.history = user_travel_history
        self.home = home_country
        self.host = host_country

    def calculate_days(self, year):
        return sum(stay['days'] for stay in self.history if stay['year'] == year and stay['country'] == self.host)

    def evaluate_status(self, year):
        days_in_host = self.calculate_days(year)
        
        # Standard OECD Model Threshold
        if days_in_host > 183:
            return {
                "status": "RESIDENT_BY_PRESENCE",
                "risk_level": "HIGH",
                "action": "Evaluate Tie-Breaker Rules (Permanent Home, Vital Interests)",
                "days": days_in_host
            }
        elif days_in_host > 90:
            return {
                "status": "NON_RESIDENT_POTENTIAL_NEXUS",
                "risk_level": "MEDIUM",
                "action": "Monitor stay; check local specific laws",
                "days": days_in_host
            }
        else:
            return {
                "status": "NON_RESIDENT",
                "risk_level": "LOW",
                "action": "Maintain travel logs",
                "days": days_in_host
            }

# Example Usage
nomad_history = [{"country": "Thailand", "days": 190, "year": 2024}]
engine = ResidencyEngine(nomad_history, "USA", "Thailand")
print(engine.evaluate_status(2024))