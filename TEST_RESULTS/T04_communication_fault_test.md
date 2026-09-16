# T04 — Communication/Data Fault Validation

## Objective

Verify that the test harness detects common data-integrity faults in an incoming sensor data stream.

## Test Data

Input file: `fault_test_data.csv`

Data type: Controlled synthetic fault-injection data

Note: This dataset is test-generated and is not Antarikshyaan telemetry.

## Injected Faults

The dataset contains:
- A duplicate sequence number.
- A missing sensor value.
- A malformed sensor value.
- A sequence-number gap.
- An out-of-range sensor value.

## Expected Result

The test harness should detect each injected data-integrity fault without modifying the raw input data.

## Observed Result

- Total records: 6
- Missing values detected: 1
- Malformed values detected: 1
- Duplicate sequences detected: 1
- Sequence gaps detected: 1
- Out-of-range values detected: 1

## Basic Statistics

- Valid in-range samples: 3
- Minimum valid value: 25.1
- Maximum valid value: 25.3
- Mean valid value: 25.20
- Observed update frequency: 1.00 Hz

## Conclusion

The test harness successfully detected all five intentionally injected data-integrity faults in the synthetic dataset.

The raw dataset was preserved unchanged.

This demonstrates the fault-detection capability of the test harness for the controlled synthetic dataset. It does not represent a confirmed communication failure in the physical Antarikshyaan system.