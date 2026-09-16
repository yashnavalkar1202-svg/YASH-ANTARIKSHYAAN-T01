import csv
import sys
from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "RAW_DATA"

if len(sys.argv) > 1:
    RAW_DATA_FILE = RAW_DATA_DIR / sys.argv[1]
else:
    RAW_DATA_FILE = RAW_DATA_DIR / "sample_sensor_data.csv"


MIN_ALLOWED_VALUE = 0.0
MAX_ALLOWED_VALUE = 50.0
MAX_ALLOWED_INTERVAL = 2.0


def load_data(file_path):
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def validate_data(data):
    required_fields = ["test_id", "timestamp", "sequence", "value"]

    missing_count = 0
    malformed_count = 0
    duplicate_count = 0
    sequence_gap_count = 0

    sequences = set()
    expected_sequence = None

    for record in data:

        # Check required fields and missing values
        for field in required_fields:
            if field not in record or record[field] == "":
                print(f"Missing value: {field} in record {record}")
                missing_count += 1

        # Check timestamp
        try:
            datetime.fromisoformat(record["timestamp"])
        except (ValueError, TypeError):
            print(f"Malformed timestamp: {record.get('timestamp')}")
            malformed_count += 1

        # Check sensor value
        if record.get("value") != "":
            try:
                value = float(record["value"])

                # Numeric values are valid format even if outside the allowed range.
                # Range checking is performed separately below.

            except (ValueError, TypeError):
                print(f"Malformed sensor value: {record.get('value')}")
                malformed_count += 1
        # Check sequence numbers for duplicates and gaps
        try:
            sequence = int(record["sequence"])

            if sequence in sequences:
                print(f"Duplicate sequence number: {sequence}")
                duplicate_count += 1

            if expected_sequence is not None and sequence > expected_sequence:
                gap = sequence - expected_sequence

                if gap > 0:
                    print(
                        f"Sequence gap detected: expected {expected_sequence}, "
                        f"received {sequence}"
                    )
                    sequence_gap_count += gap

            sequences.add(sequence)
            expected_sequence = sequence + 1

        except (ValueError, TypeError):
            print(f"Malformed sequence number: {record.get('sequence')}")
            malformed_count += 1

    return missing_count, malformed_count, duplicate_count, sequence_gap_count


# Load data
data = load_data(RAW_DATA_FILE)

print(f"Loaded {len(data)} records.")


# Validate data
missing, malformed, duplicates, sequence_gaps = validate_data(data)

print("\nValidation Summary")
print("------------------")
print(f"Total records: {len(data)}")
print(f"Missing values: {missing}")
print(f"Malformed values: {malformed}")
print(f"Duplicate sequences: {duplicates}")
print(f"Sequence gaps: {sequence_gaps}")


# Calculate basic statistics
values = []

for record in data:
    try:
        value = float(record["value"])

        if MIN_ALLOWED_VALUE <= value <= MAX_ALLOWED_VALUE:
            values.append(value)

    except (ValueError, TypeError):
        continue


print("\nBasic Statistics")
print("----------------")

if values:
    minimum = min(values)
    maximum = max(values)
    mean = sum(values) / len(values)
    sample_count = len(values)

    print(f"Sample count: {sample_count}")
    print(f"Minimum value: {minimum}")
    print(f"Maximum value: {maximum}")
    print(f"Mean value: {mean:.2f}")
    plot_timestamps = []
    plot_values = []

    for record in data:
        try:
            timestamp = datetime.fromisoformat(record["timestamp"])
            value = float(record["value"])

            if MIN_ALLOWED_VALUE <= value <= MAX_ALLOWED_VALUE:
                plot_timestamps.append(timestamp)
                plot_values.append(value)
        except (ValueError, TypeError):
            continue

    if plot_timestamps:
        plt.figure(figsize=(8, 4))
        plt.plot(plot_timestamps, plot_values, marker="o")
        plt.xlabel("Time")
        plt.ylabel("Measurement")
        plt.title(f"Measurement Over Time - {RAW_DATA_FILE.name}")
        plt.xticks(rotation=45)
        plt.tight_layout()

        plot_file = PROJECT_ROOT / "PROCESSED_DATA" / (
            RAW_DATA_FILE.stem + "_measurement_plot.png"
        )
        plt.savefig(plot_file)
        plt.close()

        print(f"Measurement plot saved to: {plot_file}")
else:
    print("No valid numerical values available.")


# Calculate observed update frequency
timestamps = []

for record in data:
    try:
        timestamp = datetime.fromisoformat(record["timestamp"])
        timestamps.append(timestamp)
    except (ValueError, TypeError):
        continue


time_differences = []

for i in range(1, len(timestamps)):
    difference = (timestamps[i] - timestamps[i - 1]).total_seconds()
    time_differences.append(difference)

    timestamp_discontinuities = [
    interval for interval in time_differences
    if interval <= 0
]


print("\nTiming Analysis")
print("---------------")
if time_differences:
    average_interval = sum(time_differences) / len(time_differences)

    if average_interval > 0:
        update_frequency = 1 / average_interval
        print(f"Average update interval: {average_interval:.2f} seconds")
        print(f"Observed update frequency: {update_frequency:.2f} Hz")

        stale_intervals = [
            interval for interval in time_differences
            if interval > MAX_ALLOWED_INTERVAL
        ]

        print(f"Potential stale/delayed intervals: {len(stale_intervals)}")
        print(f"Timestamp discontinuities: {len(timestamp_discontinuities)}")
    else:
        print("Average update interval is zero.")
else:
    print("Not enough valid timestamps to calculate update frequency.")

# Range validation
out_of_range_count = 0

for record in data:
    try:
        value = float(record["value"])
    except (ValueError, TypeError):
        continue

    if value < MIN_ALLOWED_VALUE or value > MAX_ALLOWED_VALUE:
        print(
            f"Out-of-range value: {value} "
            f"(allowed range: {MIN_ALLOWED_VALUE}–{MAX_ALLOWED_VALUE})"
        )
        out_of_range_count += 1


print("\nRange Validation")
print("----------------")
print(f"Allowed range: {MIN_ALLOWED_VALUE}–{MAX_ALLOWED_VALUE}")
print(f"Out-of-range values: {out_of_range_count}")


# Save or update the validation summary
PROCESSED_DATA_DIR = PROJECT_ROOT / "PROCESSED_DATA"
PROCESSED_DATA_DIR.mkdir(exist_ok=True)

RESULT_FILE = PROCESSED_DATA_DIR / "validation_summary.csv"

headers = [
    "input_file",
    "total_records",
    "missing_values",
    "malformed_values",
    "duplicate_sequences",
    "sequence_gaps",
    "out_of_range_values"
]

new_row = [
    RAW_DATA_FILE.name,
    len(data),
    missing,
    malformed,
    duplicates,
    sequence_gaps,
    out_of_range_count
]

existing_rows = []

if RESULT_FILE.exists():
    with open(RESULT_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        existing_rows = list(reader)

# Keep the header and preserve results from other test files.
rows_by_file = {}

if existing_rows:
    for row in existing_rows[1:]:
        if row:
            rows_by_file[row[0]] = row

rows_by_file[RAW_DATA_FILE.name] = new_row

with open(RESULT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    for row in rows_by_file.values():
        writer.writerow(row)

print(f"\nValidation summary saved to: {RESULT_FILE}")