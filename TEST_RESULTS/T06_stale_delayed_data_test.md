# T06 — Stale/Delayed Data Detection Test

## Objective

Verify that the test harness detects an individual timestamp interval that exceeds the configured maximum update interval.

## Test Data

Input file: `stale_data_test.csv`

Data type: Controlled synthetic test data

Note: This dataset is test-generated and is not Antarikshyaan telemetry.

## Expected Result

- A timestamp interval greater than 2 seconds should be detected as a potential stale/delayed interval.
- Valid measurements should remain processable.
- No missing, malformed, duplicate, or sequence-gap faults should be present.
- Measurements should remain within the defined range.

## Observed Result

- Total records: 4
- Missing values: 0
- Malformed values: 0
- Duplicate sequences: 0
- Sequence gaps: 0
- Valid sample count: 4
- Minimum value: 25.2
- Maximum value: 25.4
- Mean value: 25.27
- Average timestamp interval: 2.00 seconds
- Observed timestamp frequency: 0.50 Hz
- Potential stale/delayed intervals: 1
- Timestamp discontinuities: 0
- Out-of-range values: 0

One timestamp interval exceeded the configured 2-second threshold and was detected as a potential stale/delayed interval.

## Evidence

- Raw dataset: `RAW_DATA/stale_data_test.csv`
- Measurement plot: `PROCESSED_DATA/stale_data_test_measurement_plot.png`
- Processed validation summary: `PROCESSED_DATA/validation_summary.csv`

## Conclusion

The test harness successfully detected one potential stale/delayed interval while continuing to process the valid measurements.

This demonstrates detection of a timing-related degraded-data condition using controlled synthetic data. It does not establish the presence of stale data in the actual Antarikshyaan system because no Antarikshyaan telemetry interface was available for this test.