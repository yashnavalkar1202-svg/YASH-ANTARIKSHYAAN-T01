# T03 — Boundary/Stress Test

## Objective

Verify that the test harness correctly handles measurements at and beyond the defined sensor value boundaries.

## Test Data

Input file: `boundary_stress_test_data.csv`

Data type: Controlled synthetic test data

Note: This dataset is test-generated and is not Antarikshyaan telemetry.

## Expected Result

- Values at 0.0 and 50.0 should be accepted as within the defined range.
- A value above 50.0 should be detected as out-of-range.
- No missing, malformed, or duplicate records should be present.

## Observed Result

- Total records: 6
- Missing values: 0
- Malformed values: 0
- Duplicate sequences: 0
- Sequence gaps: 0
- Valid sample count: 5
- Minimum value: 0.0
- Maximum valid value: 50.0
- Mean of valid values: 25.00
- Out-of-range values: 1
- Detected out-of-range value: 50.1
- Average update interval: 1.00 second
- Observed update frequency: 1.00 Hz

## Conclusion

The test harness correctly accepted values at the defined boundaries and detected the value exceeding the upper boundary.

This demonstrates boundary validation using controlled synthetic data. It does not establish the actual operating range of an Antarikshyaan sensor.