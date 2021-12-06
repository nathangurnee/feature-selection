from utils import *

with open('../data/small_data_97.txt') as file:
    data_file = file.read()

split_data = data_file.split('\n')

data = []
for item in split_data:
    data.append(item.split())
data.pop() # Removes the random empty list at the end

feature_search(data)