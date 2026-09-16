\# Antarikshyaan T01 - Test Matrix



| Test ID | Condition | Input | Expected | Observed | Pass/Fail | Evidence |

|---|---|---|---|---|---|---|

| T01 | Nominal operation | `sample\_sensor\_data.csv` | Valid records with no integrity faults and consistent updates | 10 records; 0 missing; 0 malformed; 0 duplicates; 0 sequence gaps; 0 out-of-range; 1.00 Hz | Pass - harness validation | `RAW\_DATA/sample\_sensor\_data.csv`; `TEST\_RESULTS/T01\_nominal\_test.md` |

| T02 | Repeatability | `repeatability\_test\_data.csv` | Repeated measurements should remain consistent with no data-integrity faults | 10 records; values 25.2-25.3; range 0.1; 0 integrity faults; 1.00 Hz | Pass - harness validation | `RAW\_DATA/repeatability\_test\_data.csv`; `TEST\_RESULTS/T02\_repeatability\_test.md` |

| T03 | Boundary/Stress | `boundary\_stress\_test\_data.csv` | Boundary values 0.0 and 50.0 accepted; value beyond configured range detected | 0.0 and 50.0 accepted; 50.1 detected as out-of-range | Pass - harness validation | `RAW\_DATA/boundary\_stress\_test\_data.csv`; `TEST\_RESULTS/T03\_boundary\_stress\_test.md` |

| T04 | Communication/Data Fault | `fault\_test\_data.csv` | Controlled missing, malformed, duplicate, sequence-gap, and out-of-range conditions should be detected | All 5 injected faults detected | Pass - harness validation | `RAW\_DATA/fault\_test\_data.csv`; `TEST\_RESULTS/T04\_communication\_fault\_test.md` |

| T05 | Recovery | `recovery\_test\_data.csv` | Temporary missing data should be detected and subsequent valid observations should remain processable | Missing values detected at sequences 3 and 4; valid observations resumed at sequences 5-7 | Pass - harness validation | `RAW\_DATA/recovery\_test\_data.csv`; `TEST\_RESULTS/T05\_recovery\_test.md` |
| T06 | Stale/Delayed Data | `stale_data_test.csv` | Individual update intervals greater than 2 seconds should be detected as potential stale/delayed data | 1 potential stale/delayed interval detected; average interval 2.00 seconds; 0 other integrity faults | Pass - harness validation | `RAW_DATA/stale_data_test.csv`; `TEST_RESULTS/T06_stale_delayed_data_test.md`; `PROCESSED_DATA/stale_data_test_measurement_plot.png`
| T07 | Timestamp Discontinuity | `timestamp_discontinuity_test.csv` | Non-increasing timestamps should be detected | 1 timestamp discontinuity detected; 0 other integrity faults | Pass - harness validation | `RAW_DATA/timestamp_discontinuity_test.csv`; `TEST_RESULTS/T07_timestamp_discontinuity_test.md`


\## Evidence Status



All results above are based on controlled synthetic datasets.



The Pass/Fail status indicates whether the \*\*test harness detected the expected condition in the controlled dataset\*\*. It does not indicate that the physical Antarikshyaan system passed or failed.



No result should be interpreted as physical validation of the Antarikshyaan system until an actual observable interface, device, simulator, or telemetry source is provided.



## Validation Coverage

The current test harness demonstrates detection of:

- Missing values
- Malformed sensor values
- Duplicate sequence numbers
- Sequence-number gaps
- Out-of-range values
- Basic numerical statistics
- Timestamp parsing
- Timestamp discontinuities
- Observed update interval
- Observed update frequency
- Potential stale/delayed intervals
- Measurement-over-time visualization