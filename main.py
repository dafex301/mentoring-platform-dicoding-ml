from function.rank_similarity import *
import json

# Open the JSON file
with open('C:/Users/LENOVO/anaconda3/Data Science/Bangkit/Capstone1/mathmaking_api/matchmaking/data1.json', 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)

sim_per_mentee = rank_sim(data)
print(sim_per_mentee)