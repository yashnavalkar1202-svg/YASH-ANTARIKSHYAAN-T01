# Antarikshyaan T01 — Test Matrix

| Test ID | Test Family | Input Dataset | Purpose | Result |
|---|---|---|---|---|
| T01 | Nominal | sample_sensor_data.csv | Validate normal sensor data | Executed — synthetic |
| T02 | Repeatability | repeatability_test_data.csv | Evaluate consistency of repeated measurements | Executed — synthetic |
| T03 | Boundary/Stress | boundary_stress_test_data.csv | Test values at and beyond defined limits | Executed — synthetic |
| T04 | Communication/Data Fault | fault_test_data.csv | Detect missing, malformed, duplicate, sequence-gap and out-of-range data | Executed — synthetic |
| T05 | Recovery | recovery_test_data.csv | Detect temporary missing data and subsequent valid data | Executed — synthetic |

## Evidence Status

All results above are based on controlled synthetic datasets.

No result should be interpreted as physical validation of the Antarikshyaan system until an actual observable interface, device, simulator, or telemetry source is provided.

## Validation Coverage

The current test harness demonstrates detection of:

- Missing values
- Malformed sensor values
- Duplicate sequence numbers
- Sequence-number gaps
- Out-of-range values
- Basic numerical statistics
- Timestamp parsing
- Observed update interval
- Observed update frequency