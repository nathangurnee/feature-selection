with open('../data/small_data_97.txt') as file:
    data_file = file.read()

split_data = data_file.split('\n')

data = []
for item in split_data:
    data.append(item.split())
data.pop() # Removes the random empty list at the end

for i in range(len(data)):
    print('On the ' + str(i + 1) + 'th level of the search tree')
    for j in range(1, len(data[i])):
        print('--Considering adding the ' + str(j) + ' feature')