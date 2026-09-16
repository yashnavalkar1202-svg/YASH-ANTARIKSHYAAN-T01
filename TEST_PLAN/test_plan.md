
# Antarikshyaan Test Plan — Task 01

**Candidate:** Yash Navalkar  
**Project:** Antarikshyaan  
**Track:** 7-4-3

## 1. Objective

To evaluate the observable behaviour, data quality,
repeatability, and degraded-condition response of
the permitted Antarikshyaan test interface.

The testing will be performed externally without
modifying Antarikshyaan's internal implementation.

## 2. Test Environment

- Operating System: Windows
- Python version: 3.12.0
- Test harness: Python
- Interface under test: To be identified
- Sensors or simulator: To be identified
- Communication method: To be identified

## 3. Test Approach

The following steps will be followed:

1. Identify the permitted observable interface.
2. Document the available inputs and outputs.
3. Define expected behaviour before testing.
4. Capture raw observations without modification.
5. Add timestamps and test identifiers.
6. Validate the collected data.
7. Analyse the results.
8. Record evidence-backed findings.

## 4. Test Cases

### T01 — Nominal Operation

**Purpose:** Establish normal observable behaviour.

**Procedure:**
1. Set a defined input or operating condition.
2. Record the observed output.
3. Record timestamps and available metadata.
4. Repeat the test more than once.
5. Compare the results.

**Expected:** The system produces observations
consistent with the defined operating condition.

**Evidence:** Raw observation log and analysis.

### T02 — Repeatability

**Purpose:** Determine whether repeated tests
produce consistent behaviour.

**Procedure:**
1. Apply the same input or condition.
2. Repeat the observation several times.
3. Compare the outputs, timestamps, and anomalies.

**Expected:** Similar inputs produce comparable
observable behaviour within defined tolerances.

**Evidence:** Raw logs from repeated trials.

### T03 — Boundary or Stress Test

**Purpose:** Observe behaviour under a controlled
change in an external condition.

**Procedure:**
1. Define a safe variable to change.
2. Record the initial condition.
3. Change the variable in controlled steps.
4. Record the resulting observations.
5. Compare the observations with expectations.

**Expected:** The observed response is documented
and compared with the predefined expectation.

**Evidence:** Raw log and test measurements.

### T04 — Communication Fault

**Purpose:** Determine how the observable system
behaves during a controlled communication fault.

**Procedure:**
1. Establish normal communication.
2. Record the normal observations.
3. Introduce a permitted temporary interruption
   or simulated missing data.
4. Record the resulting behaviour.
5. Determine whether the fault is detectable.

**Expected:** Any missing or delayed observations
are identified and recorded.

**Evidence:** Raw log and failure record.

### T05 — Recovery

**Purpose:** Determine whether observable data
returns to normal after a degraded condition.

**Procedure:**
1. Establish a degraded condition safely.
2. Record the observations during degradation.
3. Restore the normal condition.
4. Record the recovery process.
5. Check whether observations return to the
   expected behaviour.

**Expected:** Recovery behaviour is documented
without assuming that recovery occurred.

**Evidence:** Raw log and recovery analysis.

## 5. Data Validation

The test harness will check for:

- Missing values
- Malformed values
- Duplicate records
- Unexpected ranges
- Stale observations
- Discontinuous measurements
- Missing timestamps
- Missing sequence numbers, where available

## 6. Evidence Policy

Raw data will be preserved without modification.

Derived measurements and cleaned datasets will be
stored separately from the original observations.

An observation will not be presented as a conclusion
without supporting evidence.

A suspected cause will be labelled as a hypothesis
unless it has been demonstrated by testing.

## 7. Current Limitations

The actual Antarikshyaan observable interface,
available sensors, communication protocol, and
permitted fault-injection methods have not yet
been identified.

Therefore, no real test results or pass/fail
decisions have been recorded at this stage.