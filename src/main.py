from utils import *

if __name__ == '__main__':
    with open('../data/small_data_97.txt') as file:
        data_file = file.read()

    split_data = data_file.split('\n')

    data = []
    for item in split_data:
        data.append(item.split())
    data.pop() # Removes the random empty list at the end

    choice = input("Type the number of the algorithm you want to run.\n\t1) Forward Selection\n\t2) Backward Elimination\n")
    if choice == '1':
        forward_selection(data), range(10)
    elif choice == '2':
        backward_elimination(data)
    else:
        print('Incorrect choice.')