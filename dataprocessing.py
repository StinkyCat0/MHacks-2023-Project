import json
import os

def findavg(data):
    scores = [item['score'] for item in data['aaa']]
    return sum(scores) / len(scores)

# Get list of all files in the directory
files = os.listdir('sample_json_scores')

# Initialize a list to store averages
averages = []

# Process each file
for file in files:
    # Ensure we're only processing .json files
    if file.endswith('.json'):
        with open(f'sample_json_scores/{file}', 'r') as f:
            data = json.load(f)
        # Use the data with findavg function
        average = findavg(data)
        averages.append(average)

# Print all averages
for i, average in enumerate(averages):
    print(f"Average for file {files[i]}: {average}")


def findavg(data):
    sum = 0
    for i in data:
        sum += i
    return sum / len(data)

