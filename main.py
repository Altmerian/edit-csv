import csv
import json

# open your csv file in read mode and load the data into memory
with open('data/Searchandiser_Liverpool_2023-09-14.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    data = list(reader)

# locate the column number that contains the json
json_col = headers.index('requestBody')

# iterate over the rows and update the json
for row in data:
    json_data = json.loads(row[json_col])  # parse the json string into a Python dict
    # json_data['clientKey'] = '3b5193f2-0019-44fb-a677-78de48a23af8'   # replace the 'clientKey' value
    # json_data['area'] = 'Production'        # replace the 'area' value

    # Check if 'customUrlParams' exists and is a list
    if 'customUrlParams' in json_data and isinstance(json_data['customUrlParams'], list):
        # Append the new parameter to the existing list
        json_data['customUrlParams'].append({"key": "loadTest", "value": "true"})
    else:
        # If 'customUrlParams' doesn't exist or isn't a list, create a new list with the custom parameter
        json_data['customUrlParams'] = [{"key": "loadTest", "value": "true"}]

    row[json_col] = json.dumps(json_data)  # convert the Python dict back into a json string

# write the updated data into a new csv file
with open('data/Searchandiser_Liverpool_2023-09-14_updated.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)
