import csv
import json

# open your csv file in read mode and load the data into memory
with open('data/Searchandiser_Liverpool_2023-09-14.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    data = list(reader)

# locate the column number that contains the json
json_col = headers.index('requestBody')

# initialize a new list to hold rows without the "originalQuery"
new_data = []

# iterate over the rows
for row in data:
    # parse the json string into a Python dict
    if row[json_col].strip():
        json_data = json.loads(row[json_col])
        # check if the row starts with specific string
        if not list(json_data.keys())[0] == "navigationName":
            new_data.append(row)
    else:
        print("Empty JSON string in row:", row)

# write the updated data into a new csv file
with open('data/Searchandiser_Liverpool_2023-09-14_updated.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(new_data)
