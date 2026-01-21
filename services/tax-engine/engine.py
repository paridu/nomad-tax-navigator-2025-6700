"""
Core Logic for Residency Determination.
This script demonstrates the 183-day rule and DTA Tie-breaker logic.
"""

class TaxResidencyEngine:
    def __init__(self, user_data, movements):
        self.user = user_data
        self.movements = movements # List of (country_code, days)

    def calculate_residency(self, tax_year):
        results = {}
        for country, days in self.movements.items():
            # Rule 1: Physical Presence (The 183-Day Rule)
            is_resident = False
            if days >= 183:
                is_resident = True
            
            # Rule 2: Substantial Presence (e.g., USA 3-year weighted average)
            # This would be expanded per country config
            
            results[country] = {
                "is_resident": is_resident,
                "days_spent": days,
                "threshold": 183,
                "status": "Warning" if 150 < days < 183 else "Clear"
            }
        return results

    def check_dta_tiebreaker(self, country_a, country_b):
        """
        Implements OECD Model Convention Article 4 (Resident)
        1. Permanent Home
        2. Center of Vital Interests
        3. Habitual Abode
        4. Nationality
        """
        # Logic to be fetched from Rules DB
        tie_breaker_priority = ["permanent_home", "vital_interests", "habitual_abode", "nationality"]
        return tie_breaker_priority

# Example Usage
if __name__ == "__main__":
    engine = TaxResidencyEngine(
        user_data={"id": "nomad_001", "home_country": "TH"},
        movements={"TH": 100, "DE": 190}
    )
    print(engine.calculate_residency(2023))