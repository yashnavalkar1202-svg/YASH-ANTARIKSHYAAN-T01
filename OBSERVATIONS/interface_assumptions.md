# Antarikshyaan Observable Interface — Assumptions

## 1. Interface Availability

The Task 01 specification requires testing a supplied Antarikshyaan observable interface. At the beginning of this testing phase, no physical device, simulator, API, live data stream, or sample telemetry file has been identified.

## 2. Current Assumptions

The following assumptions are provisional and have not been verified:

- The actual Antarikshyaan interface may be supplied at a later stage.
- The test harness must eventually consume externally observable data.
- The data format and available fields are currently unknown.
- The communication method is currently unknown.
- The sensor types and measurement ranges are currently unknown.

## 3. Testing Limitation

Actual Antarikshyaan integration and physical-system validation cannot be confirmed until an observable interface is provided.

## 4. Temporary Approach

A local synthetic data source may be used to develop and demonstrate the external validation logic. This data will be clearly labelled as test-generated data and will not be treated as genuine Antarikshyaan telemetry.

## 5. Unknowns

- Actual interface type.
- Available inputs and outputs.
- Data format.
- Sensor types and measurement ranges.
- Communication protocol.
- Permitted fault-injection methods.
- Expected system behaviour.

## 6. Verification Required

These assumptions must be revisited when the actual interface or additional instructions become available.