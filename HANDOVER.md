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

## Validation Capabilities

The current test harness validates:

- Required fields
- Missing values
- Malformed sensor values
- Duplicate sequence numbers
- Sequence-number gaps
- Timestamp format
- Numerical statistics
- Observed update interval
- Observed update frequency
- Configured numerical range

## Evidence Policy

Raw datasets are preserved in `RAW_DATA/`.

Processed validation results are stored separately in `PROCESSED_DATA/`.

Test results and interpretations are documented in `TEST_RESULTS/` and `OBSERVATIONS/`.

## Important Limitation

The current datasets are controlled synthetic datasets created to validate the testing methodology and harness.

They are not actual Antarikshyaan telemetry.

Physical validation of the Antarikshyaan system requires an observable device, simulator, API, telemetry stream, or other interface to be provided.

## Reproducibility

The Python test harness can be executed from the repository root using:

```text
python .\TEST_HARNESS\validator.py <input_file.csv>