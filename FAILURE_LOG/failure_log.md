\# Failure Log



\## Purpose



Record observed validation failures and distinguish detected data issues from confirmed system failures.



| Failure ID | Condition | Observation | Reproduction | Severity | Evidence | Suspected Cause |

|---|---|---|---|---|---|---|

| F001 | T04 - Duplicate sequence | Sequence number 2 occurred more than once | Run `fault\_test\_data.csv` through the validation harness | Data integrity | `RAW\_DATA/fault\_test\_data.csv`; T04 validation output | Hypothesis: duplicate packet, retransmission, or data-generation issue |

| F002 | T04 - Missing value | Sensor value was missing at sequence 4 | Run `fault\_test\_data.csv` through the validation harness | Data integrity | `RAW\_DATA/fault\_test\_data.csv`; T04 validation output | Hypothesis: missing observation, packet-content issue, or data-generation issue |

| F003 | T04 - Malformed value | Sensor value `not\_a\_number` could not be parsed numerically | Run `fault\_test\_data.csv` through the validation harness | Data format | `RAW\_DATA/fault\_test\_data.csv`; T04 validation output | Hypothesis: malformed packet or invalid data-generation input |

| F004 | T03 - Boundary condition | Value 50.1 exceeded the configured test range of 0.0-50.0 | Run `boundary\_stress\_test\_data.csv` through the validation harness | Boundary violation | `RAW\_DATA/boundary\_stress\_test\_data.csv`; T03 validation output | Hypothesis: input exceeded the configured validation boundary |

| F005 | T05 - Temporary data gap | Sensor values were missing at sequences 3 and 4, followed by valid values at sequences 5-7 | Run `recovery\_test\_data.csv` through the validation harness | Data availability | `RAW\_DATA/recovery\_test\_data.csv`; T05 validation output | Hypothesis: temporary data interruption or data-generation gap |

| F006 | T04 - Sequence gap | Sequence 3 was expected but sequence 4 was received | Run `fault\_test\_data.csv` through the validation harness | Data integrity | `RAW\_DATA/fault\_test\_data.csv`; T04 validation output | Hypothesis: missing packet, packet loss, or data-generation issue |

| F007 | T06 - Stale/delayed data | An observation interval of 4 seconds exceeded the configured 2-second freshness threshold | Run `stale_data_test.csv` through the validation harness | Timing/data freshness | `RAW_DATA/stale_data_test.csv`; `TEST_RESULTS/T06_stale_delayed_data_test.md`; `PROCESSED_DATA/stale_data_test_measurement_plot.png` | Hypothesis: delayed observation, communication delay, or data-generation timing condition |

| F008 | T07 - Timestamp discontinuity | Two consecutive observations had the same timestamp, producing a non-increasing timestamp interval | Run `timestamp_discontinuity_test.csv` through the validation harness | Data integrity | `RAW_DATA/timestamp_discontinuity_test.csv`; `TEST_RESULTS/T07_timestamp_discontinuity_test.md` | Hypothesis: timestamp-generation, logging, or data-ordering condition |



\## Engineering Note



The detected issues are based on controlled synthetic test data. They should not be interpreted as confirmed failures of the Antarikshyaan hardware, sensor, firmware, or communication system.



All entries under `Suspected Cause` are explicitly hypotheses because the current evidence does not establish a physical or system-level root cause.



Additional evidence from an actual observable interface would be required before assigning a confirmed root cause.

