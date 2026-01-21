import hashlib

def anonymize_ip(ip_address: str) -> str:
    """Masks the last octet of an IP address for privacy."""
    parts = ip_address.split('.')
    if len(parts) == 4:
        return f"{parts[0]}.{parts[1]}.{parts[2]}.0"
    return "0.0.0.0"

def pseudonymize_user_id(user_id: str, salt: str) -> str:
    """Creates a pseudonym for analytics without exposing real user IDs."""
    return hashlib.sha256((user_id + salt).encode()).hexdigest()

def obfuscate_location(lat: float, lon: float, precision: float = 0.01) -> tuple:
    """
    Rounds coordinates to decrease precision.
    0.01 is approx 1.1km - sufficient for tax country determination 
    while protecting exact home address.
    """
    return (round(lat / precision) * precision, round(lon / precision) * precision)