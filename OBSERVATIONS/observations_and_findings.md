# Observations and Findings

## Observation 1 — Nominal Data

The nominal synthetic dataset contained 10 records with no missing, malformed, duplicate, or out-of-range values. The observed update frequency was 1 Hz.

## Observation 2 — Repeatability

The repeatability dataset contained measurements between 25.2 and 25.3 units. The observed range was 0.1 units, with no detected data-integrity issues.

## Observation 3 — Boundary Behaviour

The boundary test included values at 0.0 and 50.0, which were accepted by the configured validation range. A value of 50.1 was detected as out-of-range.

## Observation 4 — Data Fault Detection

The fault-injection dataset demonstrated detection of a duplicate sequence number, a missing sensor value, a malformed sensor value, and an out-of-range value.

## Observation 5 — Data Gap and Subsequent Valid Data

The recovery dataset contained missing values at sequences 3 and 4, followed by valid measurements at sequences 5, 6, and 7.

## Interpretation

The test harness is currently capable of performing basic validation of structured sensor-like data, including field presence, numeric formatting, sequence duplication, range checking, timestamps, and basic timing statistics.

## Hypotheses

Potential causes of the detected data issues could include communication loss, packet loss, malformed packets, sensor/interface problems, or data-generation errors. These causes cannot be distinguished using the current synthetic datasets.

## Conclusions

The implemented test harness demonstrates basic black-box data validation using controlled synthetic inputs.

The evidence is sufficient to demonstrate the current validation logic, but it is not sufficient to claim physical validation of the Antarikshyaan system.

Actual system validation requires an observable Antarikshyaan interface, device, simulator, or telemetry source.