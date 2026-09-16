# Failure Log

## Purpose

Record observed validation failures and distinguish detected data issues from confirmed system failures.

| Failure ID | Test ID | Observed Issue | Detection Method | Status | Interpretation |
|---|---|---|---|---|---|
| F001 | T04 | Duplicate sequence number | Sequence validation | Detected | Data-integrity issue |
| F002 | T04 | Missing sensor value | Missing-value validation | Detected | Data-integrity issue |
| F003 | T04 | Malformed sensor value | Numeric validation | Detected | Data-format issue |
| F004 | T03 | Value above defined test range | Range validation | Detected | Boundary violation |
| F005 | T05 | Missing sensor values | Missing-value validation | Detected | Temporary data gap |

## Engineering Note

The detected issues are based on controlled synthetic test data. They should not be interpreted as confirmed failures of the Antarikshyaan hardware, sensor, firmware, or communication system.

Additional evidence from an actual observable interface would be required before assigning a root cause.