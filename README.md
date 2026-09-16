\# YASH-ANTARIKSHYAAN-T01



External black-box testing and validation of sensor, IoT, and data systems for Antarikshyaan.



\## Project Overview



This repository contains a black-box testing workflow developed to validate observable sensor-like data without modifying the internal system.



The project includes:



\- Sensor and embedded-system learning documentation

\- A structured test plan

\- A Python-based validation test harness

\- Raw and processed datasets

\- Nominal, repeatability, boundary/stress, fault, and recovery tests

\- Test results and validation summaries

\- Failure logging

\- Engineering observations and reflection

\- Handover documentation






## Test Families

- T01 — Nominal operation
- T02 — Repeatability
- T03 — Boundary/Stress
- T04 — Communication/Data Fault
- T05 — Recovery
- T06 — Stale/Delayed Data Detection
- T07 — Timestamp Discontinuity Detection






## Evidence and Data Integrity

## Validation Capabilities

The current test harness can validate:

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

Raw datasets are preserved in `RAW_DATA/` and are not overwritten by processing.



Processed validation results are stored separately in `PROCESSED_DATA/`.



Test results, observations, and failure records are documented separately to maintain traceability between input data, validation results, and engineering interpretation.



## Important Limitation



The current test datasets are controlled synthetic datasets created to validate the testing methodology and test harness.



They are \*\*not actual Antarikshyaan telemetry\*\*.



Physical validation of the Antarikshyaan system requires an observable device, simulator, API, telemetry stream, or other system interface to be provided.



Therefore, the current results demonstrate the validation methodology and implemented test-harness capabilities rather than physical Antarikshyaan system performance.



## Reproducibility

From the repository root, the validation harness can be executed using:

```text
python .\TEST_HARNESS\validator.py

## Environment and Dependencies

- Python 3.12
- matplotlib

Install the required Python dependency using:

```text
python -m pip install matplotlib