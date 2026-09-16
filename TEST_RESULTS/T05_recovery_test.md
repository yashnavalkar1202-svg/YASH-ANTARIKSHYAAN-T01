# T05 — Recovery Test

## Objective

Verify that the test harness records missing sensor data followed by the return of valid measurements.

## Test Data

Input file: `recovery_test_data.csv`

Data type: Controlled synthetic test data

Note: This dataset is test-generated and is not Antarikshyaan telemetry.

## Expected Result

- Missing sensor values should be detected.
- Valid measurements following the missing period should be captured.
- No malformed or duplicate records should be present.
- The returning measurements should remain within the defined range.

## Observed Result

- Total records: 7
- Missing values: 2
- Malformed values: 0
- Duplicate sequences: 0
- Valid sample count: 5
- Minimum value: 25.2
- Maximum value: 25.4
- Mean value: 25.28
- Out-of-range values: 0
- Average timestamp interval: 1.00 second
- Observed timestamp frequency: 1.00 Hz

Missing sensor values occurred at sequences 3 and 4. Valid measurements were present again at sequences 5, 6, and 7.

## Conclusion

The test harness successfully detected the missing measurements and recorded valid measurements after the missing period.

This demonstrates detection of a temporary data gap and observation of subsequent valid data using controlled synthetic data. A physical communication or sensor recovery cannot be confirmed without testing an actual Antarikshyaan interface.