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



\## Test Families



\- T01 — Nominal operation

\- T02 — Repeatability

\- T03 — Boundary/Stress

\- T04 — Communication/Data Fault

\- T05 — Recovery



\## Validation Capabilities



The current test harness can validate:



\- Required fields

\- Missing values

\- Malformed sensor values

\- Duplicate sequence numbers

\- Sequence-number gaps

\- Timestamp format

\- Numerical statistics

\- Observed update interval

\- Observed update frequency

\- Configured numerical range



\## Evidence and Data Integrity



Raw datasets are preserved in `RAW\_DATA/` and are not overwritten by processing.



Processed validation results are stored separately in `PROCESSED\_DATA/`.



Test results, observations, and failure records are documented separately to maintain traceability between input data, validation results, and engineering interpretation.



\## Important Limitation



The current test datasets are controlled synthetic datasets created to validate the testing methodology and test harness.



They are \*\*not actual Antarikshyaan telemetry\*\*.



Physical validation of the Antarikshyaan system requires an observable device, simulator, API, telemetry stream, or other system interface to be provided.



Therefore, the current results demonstrate the validation methodology and implemented test-harness capabilities rather than physical Antarikshyaan system performance.



\## Reproducibility



From the repository root, the validation harness can be executed using:



```text

python .\\TEST\_HARNESS\\validator.py <input\_file.csv>

