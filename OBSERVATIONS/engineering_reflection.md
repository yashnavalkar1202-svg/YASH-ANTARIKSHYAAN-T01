\# Engineering Reflection



\## What I Learned



This task helped me understand how a sensor system can be evaluated from its observable outputs without modifying the internal system.



I learned the importance of:



\- Sensor-to-signal-to-measurement flow

\- Analog and digital data

\- Sampling and timestamps

\- Noise, calibration, bias, accuracy, precision, resolution, and drift

\- ESP32 fundamentals, GPIO, I2C, UART, and SPI concepts

\- Polling versus event-driven acquisition

\- Sequence numbers and data integrity

\- Missing, duplicate, malformed, stale, and out-of-range data

\- Basic Python-based validation

\- Preserving raw evidence separately from processed results

\- Reproducible testing and documentation



\## What Did I Initially Assume?



Initially, I assumed that the main challenge would be writing a Python utility to process sensor-like data.



During the task, I learned that the more important challenge is establishing whether an observation is trustworthy and separating measured evidence from interpretation.



I also initially expected that an Antarikshyaan device, simulator, or observable interface would be available for direct testing.



\## Which Assumption Was Wrong?



The assumption that a real Antarikshyaan observable interface would be available was not confirmed.



No physical device, simulator, API, or telemetry source was available or identified during this testing stage.



As a result, controlled synthetic datasets were used only to validate the external test harness and testing methodology.



\## What Did the Measurements Prove?



The controlled datasets demonstrated that the test harness can detect:



\- Missing values

\- Malformed sensor values

\- Duplicate sequence numbers

\- Sequence-number gaps

\- Values outside the configured numerical range

\- Timestamp formatting problems

\- Basic numerical statistics

\- Observed update interval and frequency

\- Potential stale/delayed intervals

\- Timestamp discontinuities

\- Measurement-over-time visualization



The T04 fault dataset demonstrated detection of five intentionally injected data-integrity conditions.



The T05 recovery dataset demonstrated detection of missing observations followed by subsequent valid observations.



These results demonstrate the behaviour of the test harness against controlled inputs.



\## What Could Not Be Determined?



The current evidence cannot determine:



\- Whether an actual Antarikshyaan sensor is functioning correctly

\- Whether a physical communication link is reliable

\- The root cause of a real missing or malformed observation

\- Actual packet loss or communication latency

\- Physical sensor accuracy, calibration, bias, noise, or drift

\- Whether the configured numerical range represents the real Antarikshyaan sensor limits

\- Whether the physical system recovers correctly after a real communication or sensor interruption



The synthetic results must therefore not be interpreted as physical validation of Antarikshyaan.



\## What Additional Instrumentation Would Be Required?



When an actual observable interface becomes available, additional instrumentation could include:



\- Direct access to the permitted telemetry or observation stream

\- Reliable source timestamps and sequence numbers

\- A method to identify packet arrival time

\- Communication latency measurements

\- Controlled interruption and restoration of the permitted interface

\- Sensor reference measurements where accuracy needs to be evaluated

\- Logging of connection/disconnection events

\- A defined sensor range and expected sampling/update rate



The instrumentation should remain at the external observation layer and should not require modification of Antarikshyaan internals.



\## What Would I Test Next?



With a real observable interface, I would next test:



1\. Nominal operation using real telemetry and repeated runs.

2\. Boundary behaviour using controlled external input variation.

3\. Temporary communication interruption or delayed data.

4\. Stale observations.

5\. Timestamp discontinuities.

6\. Packet loss and sequence gaps.

7\. Recovery after communication or sensor interruption.

8\. Communication latency and recovery timing.

9\. Sensor repeatability against a suitable reference where applicable.



\## Engineering Discipline



An important lesson was to distinguish an observation from an interpretation.



For example:



\*\*Observation:\*\* A value of 50.1 was present in the controlled T03 dataset while the configured test range was 0.0-50.0.



\*\*Interpretation:\*\* The value was outside the configured validation range.



\*\*Hypothesis:\*\* The input may represent an external boundary violation or data-generation condition.



The evidence does not prove that a physical sensor or communication system failed.



This distinction is important because reliable engineering conclusions must be based on measurable evidence rather than assumptions.



\## Current Limitations



The current validation environment uses controlled synthetic data because an actual Antarikshyaan observable interface, physical device, simulator, or telemetry source has not yet been provided or identified.



Therefore, the current results demonstrate the test harness and validation methodology rather than physical system performance.

