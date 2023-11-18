import json
import numpy as np

# Load json
with open('<FILEPATH>\\10score.json') as file:
    data = json.load(file)

# Get data list
data_list = data["aaa"]

# Get scores
scores = [float(item['score']) for item in data_list if 'score' in item and item['score'] is not None]

average = np.mean(scores)

print(scores)
print(average)
