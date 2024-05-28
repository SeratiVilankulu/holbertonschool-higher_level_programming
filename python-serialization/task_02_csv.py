import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON and save it to data.json file.
    Returns True if conversion is successful, otherwise False.
    """
    try:
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        return False

# Test the function with a sample CSV file
if __name__ == "__main__":
    csv_file = "data.csv"
    success = convert_csv_to_json(csv_file)
    if success:
        print(f"Data from {csv_file} has been converted to data.json")
    else:
        print(f"Failed to convert {csv_file} to JSON")
