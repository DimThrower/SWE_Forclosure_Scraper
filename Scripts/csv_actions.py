import csv


# Headers for the CSV file
headers = [
    "Address", "Yr Built", "Original Owner", "Tax Account ID Nbr",
    "Property Value", "Loan Orig Date", "Legal Description", "Key Map", "Current Owner",
    "Link to Deed of Trust", "Est Loan Balance", "Loan Type", "Mortgagee", "Bdrms",
    "Trustee Reference Nbr", "Est Bid/Previous Posts", "Title Report", "Loan Term",
    "Trustee / View Notice", "Sq Ftg", "Sale Hrs/Record Posted", "Original Loan Amount",
    "Estimated Equity", "Estimated Margin"
]

# Example data row as a dictionary
data_row = {
    "Address (Links to Google Map)": "123 Example Street",
    "Yr Built": "2000",
    # ... fill in other fields as necessary
}

def csv_writer(csv_path, headers, data_row):
    # Open a CSV file to write
    with open(csv_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)

        #Check to see if first row is empty
        if is_first_row_empty(csv_path):
            # Write the header
            writer.writeheader()

        # Write the data row
        writer.writerow(data_row)
        # print(data_row)

    # print("CSV file 'property_data.csv' created with headers and data.")


def is_first_row_empty(file_name):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            first_row = next(reader, None)  # Read the first row
            return not bool(first_row)  # Return True if first row is empty
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
        return True  # If file doesn't exist, treat as if first row is empty
    except Exception as e:
        print(f"An error occurred: {e}")
        return True  # In case of other errors, handle accordingly