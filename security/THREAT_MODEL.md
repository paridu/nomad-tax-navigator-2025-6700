# Threat Model & Security Controls

## 1. Identified Threats
*   **T1: Location Spoofing:** Users falsifying GPS to avoid tax residency triggers.
    *   *Mitigation:* Cross-reference IP geolocation with GPS data. Use device-level attestation (Apple DeviceCheck / Google Play Integrity).
*   **T2: Data Breach of PII:** Exposure of financial records and movement history.
    *   *Mitigation:* Field-level encryption for `tax_id` and `exact_gps_coords`. Automated data deletion for users who close accounts (GDPR Right to Erasure).
*   **T3: Unauthorized API Access:**
    *   *Mitigation:* JWT-based auth with short-lived tokens and rotation.

## 2. Encryption Standards
*   **In-Transit:** TLS 1.3 only.
*   **At-Rest:** AES-256 for databases and S3 buckets.
*   **Secrets Management:** HashiCorp Vault or AWS Secrets Manager.

## 3. Compliance Framework
*   **Privacy by Design:** Location data is obfuscated (stored at city-level unless precision is legally required for "Days Present" proof).