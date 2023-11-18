import json
import numpy as np

# Load json
with open('C:\\Users\\cshu\\Documents\\shool_work\\2023-2024\\sem1\\mhack\\dataset\\sample_json_scores\\10score.json') as file:
    data = json.load(file)

# Get data list
data_list = data["aaa"]

# Get scores
scores = [float(item['score']) for item in data_list if 'score' in item and item['score'] is not None]

average = np.mean(scores)

print(scores)
print(average)