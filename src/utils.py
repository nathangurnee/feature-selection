import random

def cross_validation(data, current_set, feature_to_add):
    return random.randint(1, 10)

def feature_search(data):
    features = set()

    for i in range(len(data)):
        feature_to_add = ""
        highest_accuracy = 0
        print('On the ' + str(i + 1) + 'th level of the search tree')
        for j in range(1, len(data[i])):
            if j not in features:
                print('--Considering adding the ' + str(j) + ' feature')
                accuracy = cross_validation(data, features, float(data[i][j]))

                if accuracy > highest_accuracy:
                    highest_accuracy = accuracy
                    feature_to_add = j
                    
        features.add(feature_to_add)
        print('On level ' + str(i + 1) + ', added feature ' + str(feature_to_add) + ' to current set')
        
    features.pop() # Removes the empty string from the set

    print(features)
