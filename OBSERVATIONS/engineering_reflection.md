# Engineering Reflection

## What I Learned

This task helped me understand how a sensor system can be evaluated from its observable outputs without modifying the internal system.

I learned the importance of:

* Sensor-to-signal-to-measurement flow
* Analog and digital data
* Sampling and timestamps
* Noise, calibration, bias, accuracy, precision, resolution, and drift
* Sequence numbers and data integrity
* Missing, duplicate, malformed, and out-of-range data
* Basic Python-based validation
* Preserving raw evidence separately from processed results
* Reproducible testing and documentation

## Testing Approach

The testing approach was based on controlled datasets representing nominal operation, repeatability, boundary conditions, data faults, and recovery.

The test harness was used to produce repeatable validation results rather than relying only on manual inspection.

## Engineering Discipline

An important lesson was to distinguish an observation from an interpretation.

For example, detecting a missing value is an observation. It does not by itself prove that a sensor or communication system has failed. Additional evidence is required to determine the cause.

## Current Limitations

The current validation environment uses synthetic data because an actual Antarikshyaan observable interface, physical device, simulator, or telemetry source has not yet been provided or identified.

Therefore, the current results demonstrate the test harness and validation methodology rather than physical system performance.

## Future Improvements

When an actual observable interface is available, the test harness should be adapted to capture real data while preserving the same raw-data and evidence workflow.

Additional validation should include:

* Stale data detection
* Timestamp discontinuities
* Packet loss
* Communication latency
* Recovery timing
* More detailed statistical analysis
* Automated test reports

