# Learning Report

## Task 01 — Physical Sensing

**Candidate:** Yash Navalkar
**Project:** Antarikshyaan
**Track:** 7-4-3

## 1. Sensor-to-Measurement Chain

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

- Value
- Unit
- Timestamp
- Relevant measurement conditions

## 2. Analog vs Digital Sensing

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

## 3. Sampling Rate

Sampling rate is the number of measurements
collected per second.

It is measured in hertz (Hz).

For example:

- 1 Hz means 1 sample per second.
- 10 Hz means 10 samples per second.
- 100 Hz means 100 samples per second.

A sampling rate that is too low may miss changes
in the physical quantity.

## 4. Sensor Noise

Noise is unwanted variation in a measurement.

For example, a temperature sensor may report:

25.0°C
25.2°C
24.9°C
25.1°C

even when the actual temperature is nearly constant.

Noise can affect the reliability of measurements.

## 5. Calibration and Bias

Calibration compares or adjusts a measurement
system against a known reference.

Bias is a systematic error that causes measurements
to be consistently shifted from the actual value.

Example:

Actual temperature: 25°C
Sensor readings: 27°C, 27°C, 27°C

The sensor may have a positive bias of approximately
2°C under those conditions.

## 6. Accuracy, Precision, Resolution, Noise and Drift

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

## 7. Timestamping

A timestamp records when an observation occurred.

Timestamps help determine:

- When a measurement was collected.
- The time between samples.
- Whether data is delayed or stale.
- Whether observations are in the correct order.

## 8. Application to Antarikshyaan Testing

These concepts will help me determine whether
observed sensor or telemetry data is consistent,
complete, timely, and suitable for analysis.

No physical sensor measurements have been collected
yet. The actual test results will be recorded after
the permitted Antarikshyaan interface or device
has been identified.