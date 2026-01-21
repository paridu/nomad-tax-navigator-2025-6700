from datetime import date, timedelta
from typing import List
from src.database.models import TravelEntry

class ResidencyLogicService:
    @staticmethod
    def calculate_days_in_country(travel_history: List[TravelEntry], country_code: str, year: int) -> int:
        """
        Calculates the number of days spent in a specific country within a calendar year.
        Standard for the 183-day rule.
        """
        total_days = 0
        year_start = date(year, 1, 1)
        year_end = date(year, 12, 31)

        for entry in travel_history:
            if entry.country_code != country_code:
                continue
            
            # Determine overlapping period
            start = max(entry.entry_date, year_start)
            end = min(entry.exit_date or date.today(), year_end)
            
            if start <= end:
                total_days += (end - start).days + 1
                
        return total_days

    @staticmethod
    def check_residency_trigger(days_spent: int, threshold: int = 183) -> bool:
        """Determines if the day count triggers tax residency."""
        return days_spent >= threshold