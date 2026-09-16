# Learning Report

## Task 01 — Physical Sensing

**Candidate:** Yash Navalkar
**Project:** Antarikshyaan
**Track:** 7-4-3

## 1\. Sensor-to-Measurement Chain

A sensor detects a physical quantity such as
temperature, pressure, distance, or light.

The general data chain is:

Physical quantity → Sensor → Electrical signal
→ Signal processing → Measurement → Timestamped data

### 1.1 Sensor

A sensor detects a physical quantity and produces
a signal related to that quantity.

Example:
A temperature sensor detects temperature and
produces a corresponding electrical signal.

### 1.2 Signal

A signal is a physical representation of information
that can be measured or processed.

Signals may be analog or digital.

### 1.3 Measurement

A measurement is the value obtained by observing
a physical quantity using a measurement system.

A measurement should include:

* Value
* Unit
* Timestamp
* Relevant measurement conditions

## 2\. Analog vs Digital Sensing

### Analog Sensing

An analog signal varies continuously over a range.

Example:
A temperature sensor producing a voltage that
changes with temperature.

### Digital Sensing

A digital sensor communicates measurements as
digital data, often through a protocol such as
I2C, SPI, or UART.

The measurement is represented using numerical
data that software can process.

## 3\. Sampling Rate

Sampling rate is the number of measurements
collected per second.

It is measured in hertz (Hz).

For example:

* 1 Hz means 1 sample per second.
* 10 Hz means 10 samples per second.
* 100 Hz means 100 samples per second.

A sampling rate that is too low may miss changes
in the physical quantity.

## 4\. Sensor Noise

Noise is unwanted variation in a measurement.

For example, a temperature sensor may report:

25.0°C
25.2°C
24.9°C
25.1°C

even when the actual temperature is nearly constant.

Noise can affect the reliability of measurements.

## 5\. Calibration and Bias

Calibration compares or adjusts a measurement
system against a known reference.

Bias is a systematic error that causes measurements
to be consistently shifted from the actual value.

Example:

Actual temperature: 25°C
Sensor readings: 27°C, 27°C, 27°C

The sensor may have a positive bias of approximately
2°C under those conditions.

## 6\. Accuracy, Precision, Resolution, Noise and Drift

### Accuracy

How close a measurement is to the true or
accepted reference value.

### Precision

How closely repeated measurements agree with
one another.

### Resolution

The smallest change in a quantity that the
measurement system can distinguish or represent.

### Noise

Random or unwanted variation in measurements.

### Drift

A gradual change in the measurement behaviour
over time or changing conditions.

## 7\. Timestamping

A timestamp records when an observation occurred.

Timestamps help determine:

* When a measurement was collected.
* The time between samples.
* Whether data is delayed or stale.
* Whether observations are in the correct order.

## 8\. Application to Antarikshyaan Testing

These concepts will help me determine whether
observed sensor or telemetry data is consistent,
complete, timely, and suitable for analysis.

No physical sensor measurements have been collected
yet. The actual test results will be recorded after
the permitted Antarikshyaan interface or device
has been identified.

\## Task 01 — Embedded and IoT Data



\### 9. ESP32 Fundamentals



The ESP32 is a microcontroller commonly used in embedded and IoT systems. It can read sensor inputs, process measurements, and communicate data to another device or host.



For black-box testing, understanding the ESP32 helps me reason about how physical sensor observations may become digital data before reaching the test harness.



\### 9.1 GPIO



GPIO stands for General Purpose Input/Output.



GPIO pins can be configured to read digital inputs or control digital outputs.



A sensor or external device may use GPIO for simple digital signals such as a switch, interrupt, or status indication.



\### 9.2 I2C



I2C is a digital communication protocol commonly used to connect sensors and other peripherals to a microcontroller.



It uses two main signal lines:



\- SDA — Serial Data

\- SCL — Serial Clock



Multiple devices can share the same I2C bus using device addresses.



\### 9.3 UART



UART is a serial communication method used for transferring data between devices.



It commonly uses:



\- TX — Transmit

\- RX — Receive



UART is useful for understanding how an embedded device may send telemetry or diagnostic data to a host.



\### 9.4 SPI



SPI is a synchronous digital communication protocol commonly used for high-speed communication with peripherals.



It typically uses:



\- SCLK — Clock

\- MOSI — Master Out, Slave In

\- MISO — Master In, Slave Out

\- CS — Chip Select



For this task, I only need a conceptual understanding of SPI rather than firmware-level implementation.



\### 9.5 Polling vs Event-Driven Acquisition



In polling, the microcontroller repeatedly checks whether new sensor data is available.



In event-driven acquisition, an event such as an interrupt can notify the system that new data requires attention.



Polling can be simpler but may consume processing time continuously. Event-driven acquisition can respond efficiently to events but requires appropriate event handling.



\### 9.6 Device-to-Host Communication



A device-to-host data path transfers observations from an embedded device to another system that can record or analyse them.



For testing, I need to understand that the value received by the host may be affected by communication timing, missing packets, malformed data, duplication, or delays.



This is why receiving a numerical value alone does not automatically prove that the underlying measurement is trustworthy.

## Task 01 — Data Integrity and Telemetry

### 10. Timestamps
A timestamp records when an observation was generated or recorded. Timestamps are important for analysing the order and timing of sensor observations.

For black-box validation, I need to distinguish between the time associated with the observation and the time at which the test harness receives the data. A difference between these times can help identify communication delay or latency.

### 10.1 Sequence Numbers
A sequence number identifies the order of observations or packets.

Sequence numbers can help detect missing or lost observations. For example, if the received sequence changes from 5 to 7, sequence 6 may be missing.

They can also help identify duplicate observations when the same sequence number appears more than once.

### 10.2 Missing Data
Missing data occurs when an expected observation or field is absent.

The test harness should detect missing values rather than silently treating them as valid measurements. Missing data can affect statistics and conclusions about system behaviour.

### 10.3 Duplicate Data
Duplicate data occurs when the same observation or sequence number is received more than once.

Duplicates should be identified and reported because they can make the apparent sample count different from the actual number of unique observations.

### 10.4 Malformed Data
Malformed data is data that does not follow the expected format.

Examples include a non-numeric sensor value where a numerical measurement is expected, an invalid timestamp, or an invalid sequence number.

The validation harness should detect malformed fields and preserve the original data as evidence.

### 10.5 Stale Data
Stale data is data that is valid in format but is no longer sufficiently recent.

For example, if a system is expected to produce measurements regularly but continues reporting an old observation, the value may appear valid while not representing the current system state.

Detecting stale data requires a defined freshness or timing requirement.

### 10.6 Communication Disconnection and Packet Loss
A communication interruption can prevent observations from reaching the host.

Packet loss may appear as missing sequence numbers or gaps in received observations. However, a sequence gap alone does not prove the physical cause of the gap. It could also result from data-generation or logging issues.

Therefore, the cause should be treated as a hypothesis unless additional evidence is available.

### 10.7 Latency
Latency is the delay between an observation being generated and the corresponding data being received or recorded by the host.

To measure communication latency reliably, the system should provide suitable source and arrival timestamps or another synchronized timing reference.

### 10.8 Logging and Reproducibility
A validation test should preserve enough information to reproduce and investigate its result.

Important evidence includes the test ID, input condition, timestamp, observed output, validation result, raw data, processed results, and test environment.

Raw data should not be overwritten during processing. Processed datasets and analysis should remain traceable to the original evidence.

## Task 01 — Python Data Validation and Analysis

### 11. Python for Test Instrumentation
Python can be used as an external test and analysis tool without modifying the system being tested.

For this task, Python is used to read observable data, validate its structure and values, calculate statistics, and produce reproducible validation results.

### 11.1 Reading Data
A Python test harness can read observations from a CSV file or another observable interface.

The input data should be preserved as raw evidence before any processing is performed.

### 11.2 Data Validation
The validation process can check whether required fields are present and whether values have the expected format.

For this project, validation includes missing values, malformed numerical values, duplicate sequence numbers, sequence-number gaps, timestamps, and configured measurement limits.

### 11.3 Statistical Analysis
Basic statistics can help describe the observed dataset.

Useful measurements include:
- Number of records
- Number of valid samples
- Minimum value
- Maximum value
- Mean value
- Missing-value count
- Duplicate count
- Sequence-gap count
- Out-of-range count
- Average update interval
- Observed update frequency

Statistics should be calculated from clearly defined observations so that invalid or missing values do not silently distort the results.

### 11.4 Measurement Over Time
Plotting a measurement against time can help identify changes, discontinuities, missing observations, unusual values, or possible drift.

For a real sensor system, a time-series plot could provide additional evidence when investigating stability or changes in behaviour.

The current validation work focuses primarily on numerical and timing analysis of controlled datasets. The validation harness now generates measurement-over-time plots for datasets with valid timestamped numerical measurements.

### 11.5 Raw Data and Processed Data
Raw data represents the observations as received by the test process and should remain unchanged.

Processed data contains calculated validation results or derived statistics.

Keeping raw and processed data separate makes the analysis traceable and allows the same raw evidence to be reprocessed later.

### 11.6 Reproducible Validation
A useful test harness should produce the same validation result when the same input and configuration are used.

The validation script in this project can be executed against each test dataset, allowing the checks and results to be reproduced without changing the original raw data.

## Task 01 — Evidence and Engineering Reasoning

### 12. Evidence-Based Validation
A validation result should be based on observable evidence rather than assumptions.

For each test, I should distinguish between:
- Observation — what was directly observed in the data
- Measurement — a numerical or countable result
- Interpretation — what the measurement indicates
- Hypothesis — a possible explanation that has not yet been proven
- Conclusion — what can reasonably be stated from the available evidence

### 12.1 Observation vs Inference
An observation is a directly recorded fact. For example, a sequence number may change from 2 to 4.

The missing sequence 3 is an observed data-integrity condition. Saying that a physical communication packet was definitely lost would be an inference unless additional evidence confirms that cause.

This distinction prevents unsupported conclusions.

### 12.2 Expected Behaviour Before Testing
Expected behaviour should be defined before running a test whenever possible.

Examples include:
- Required fields should be present.
- Numerical measurements should have the expected format.
- Sequence numbers should follow the expected order.
- Values should remain within the configured validation range.
- Measurements should be received at an expected update interval.

Defining expectations first makes the test result more objective and reproducible.

### 12.3 Evidence Preservation
Evidence should be preserved so that another person can inspect how a conclusion was reached.

Important evidence includes raw input, test conditions, timestamps, observed output, validation results, processed data, and failure records.

Raw evidence should not be changed to make the results appear cleaner.

### 12.4 Telemetry Is Evidence, Not Automatically Truth
A telemetry value received by a host is an observation produced by a data pipeline.

It may be affected by sensor characteristics, calibration, sampling, communication problems, timestamp issues, processing, or data corruption.

Therefore, receiving a value successfully does not by itself prove that the physical measurement is accurate or that the complete sensing pipeline is functioning correctly.

### 12.5 Engineering Conclusion
The purpose of black-box validation is not to prove that a system works simply because it produces data.

The purpose is to determine what can be demonstrated from observable evidence, identify deviations from expected behaviour, preserve reproducible evidence, and clearly state what remains unknown.

For this project, the controlled synthetic tests demonstrate that the external validation harness can detect several defined data-integrity and boundary conditions. They do not demonstrate the physical performance or communication reliability of the actual Antarikshyaan system because a real observable interface has not yet been provided.

