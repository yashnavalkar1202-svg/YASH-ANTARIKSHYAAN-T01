# YASH-ANTARIKSHYAAN-T01 — Handover

## Project

External black-box testing and validation of sensor, IoT, and data systems for Antarikshyaan.

## Current Status

The repository contains a documented learning report, test plan, Python validation harness, synthetic test datasets, processed validation results, test results, observations, failure records, and engineering reflection.

## Test Coverage

The implemented test workflow covers:

- T01 — Nominal operation
- T02 — Repeatability
- T03 — Boundary/Stress
- T04 — Communication/Data Fault
- T05 — Recovery
- T06 — Stale/Delayed Data Detection
- T07 — Timestamp Discontinuity Detection

## Validation Capabilities

The current test harness validates:

- Required fields
- Missing values
- Malformed sensor values
- Duplicate sequence numbers
- Sequence-number gaps
- Timestamp format
- Timestamp discontinuities
- Numerical statistics
- Observed update interval
- Observed update frequency
- Potential stale/delayed intervals
- Configured numerical range
- Measurement-over-time visualization

## Evidence Policy

Raw datasets are preserved in `RAW_DATA/`.

Processed validation results are stored separately in `PROCESSED_DATA/`.

Test results and interpretations are documented in `TEST_RESULTS/` and `OBSERVATIONS/`.

The test matrix links each test case to its corresponding raw dataset and supporting evidence where applicable.

## Important Limitation

The current datasets are controlled synthetic datasets created to validate the testing methodology and harness.

They are not actual Antarikshyaan telemetry.

Physical validation of the Antarikshyaan system requires an observable device, simulator, API, telemetry stream, or other interface to be provided.

## Reproducibility

From the repository root, the validation harness can be executed using:

```text
python .\TEST_HARNESS\validator.py

The harness uses the default dataset:

RAW_DATA\sample_sensor_data.csv

A specific dataset can also be selected by providing its filename:

python .\TEST_HARNESS\validator.py <dataset_filename>.csv

The required Python dependency is matplotlib.