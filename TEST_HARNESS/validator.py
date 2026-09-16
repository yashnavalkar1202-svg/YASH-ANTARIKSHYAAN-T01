import csv
import sys
from pathlib import Path
from datetime import datetime


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "RAW_DATA"

if len(sys.argv) > 1:
    RAW_DATA_FILE = RAW_DATA_DIR / sys.argv[1]
else:
    RAW_DATA_FILE = RAW_DATA_DIR / "sample_sensor_data.csv"


MIN_ALLOWED_VALUE = 0.0
MAX_ALLOWED_VALUE = 50.0


def load_data(file_path):
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def validate_data(data):
    required_fields = ["test_id", "timestamp", "sequence", "value"]

    missing_count = 0
    malformed_count = 0
    duplicate_count = 0

    sequences = set()

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
                float(record["value"])
            except (ValueError, TypeError):
                print(f"Malformed sensor value: {record.get('value')}")
                malformed_count += 1

        # Check duplicate sequence numbers
        try:
            sequence = int(record["sequence"])

            if sequence in sequences:
                print(f"Duplicate sequence number: {sequence}")
                duplicate_count += 1

            sequences.add(sequence)

        except (ValueError, TypeError):
            print(f"Malformed sequence number: {record.get('sequence')}")
            malformed_count += 1

    return missing_count, malformed_count, duplicate_count


# Load data
data = load_data(RAW_DATA_FILE)

print(f"Loaded {len(data)} records.")


# Validate data
missing, malformed, duplicates = validate_data(data)

print("\nValidation Summary")
print("------------------")
print(f"Total records: {len(data)}")
print(f"Missing values: {missing}")
print(f"Malformed values: {malformed}")
print(f"Duplicate sequences: {duplicates}")


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


print("\nTiming Analysis")
print("---------------")

if time_differences:
    average_interval = sum(time_differences) / len(time_differences)
    update_frequency = 1 / average_interval

    print(f"Average update interval: {average_interval:.2f} seconds")
    print(f"Observed update frequency: {update_frequency:.2f} Hz")
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
# Save a validation summary
PROCESSED_DATA_DIR = PROJECT_ROOT / "PROCESSED_DATA"
PROCESSED_DATA_DIR.mkdir(exist_ok=True)

RESULT_FILE = PROCESSED_DATA_DIR / "validation_summary.csv"

with open(RESULT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "input_file",
        "total_records",
        "missing_values",
        "malformed_values",
        "duplicate_sequences",
        "out_of_range_values"
    ])

    writer.writerow([
        RAW_DATA_FILE.name,
        len(data),
        missing,
        malformed,
        duplicates,
        out_of_range_count
    ])

print(f"\nValidation summary saved to: {RESULT_FILE}")