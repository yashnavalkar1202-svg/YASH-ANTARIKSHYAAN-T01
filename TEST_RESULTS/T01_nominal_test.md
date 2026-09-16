# T01 — Nominal Data Validation

## Objective

Verify that normally formatted sensor data can be loaded and validated without missing, malformed, duplicate, or out-of-range values.

## Test Data

Input file: `sample_sensor_data.csv`

Data type: Synthetic test data

Note: This dataset is test-generated and is not Antarikshyaan telemetry.

## Expected Result

- All records should contain the required fields.
- No missing values should be present.
- No malformed values should be present.
- No duplicate sequence numbers should be present.
- All numerical values should remain within the defined test range of 0–50.
- The observed update frequency should be approximately 1 Hz.

## Observed Result

- Total records: 10
- Missing values: 0
- Malformed values: 0
- Duplicate sequences: 0
- Sequence gaps: 0
- Out-of-range values: 0
- Minimum value: 25.1
- Maximum value: 25.4
- Mean value: 25.27
- Average update interval: 1.00 second
- Observed update frequency: 1.00 Hz

## Conclusion

The synthetic nominal dataset passed the implemented validation checks. No data-integrity issues were detected in this test.

This result demonstrates validation of the test harness using controlled synthetic data. It does not constitute validation of the physical Antarikshyaan system.