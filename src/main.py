from utils import *

if __name__ == '__main__':
    with open('../data/small_data_86.txt') as file:
        data_file = file.read()

    split_data = data_file.split('\n')

    data = []
    for item in split_data:
        data.append(item.split())
    data.pop() # Removes the random empty list at the end

    forward_selection(data)