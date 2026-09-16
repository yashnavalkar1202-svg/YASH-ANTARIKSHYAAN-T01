# T02 — Repeatability Test

## Objective

Evaluate whether repeated measurements under controlled conditions remain consistent.

## Test Data

Input file: `repeatability_test_data.csv`

Data type: Controlled synthetic test data

Note: This dataset is test-generated and is not Antarikshyaan telemetry.

## Expected Result

Repeated measurements should remain within a narrow range, with no missing, malformed, duplicate, or out-of-range data.

## Observed Result

- Total records: 10
- Missing values: 0
- Malformed values: 0
- Duplicate sequences: 0
- Minimum value: 25.2
- Maximum value: 25.3
- Mean value: 25.25
- Average update interval: 1.00 second
- Observed update frequency: 1.00 Hz
- Out-of-range values: 0

The observed measurement range was 0.1 units.

## Conclusion

The controlled synthetic dataset showed consistent repeated measurements with a narrow observed variation of 0.1 units.

This demonstrates repeatability analysis using the test harness. It does not establish the repeatability of a physical Antarikshyaan sensor.