from math import sqrt
import copy

# Performs leave-on-out cross-validation on a data set
def cross_validation(data, current_set, feature, task):
    zero_data = copy.deepcopy(data) # Deep copy of the data set

    # If 'add': set all features not in the current set or not the feature to
    # be added to zero
    # If 'remove': set all freatures not in the current set and the feature to
    # be removed to zero
    if task == 'add':
        for i in range(len(zero_data)):
            for j in range(1, len(zero_data[i])):
                if j not in current_set and j != feature:
                    zero_data[i][j] = 0
    elif task == 'remove':
        for i in range(len(zero_data)):
            for j in range(1, len(zero_data[i])):
                if j not in current_set or j == feature:
                    zero_data[i][j] = 0

    number_correctly_classified = 0 # Correctly guessed objects

    for i in range(len(zero_data)):
        object_to_classify = list(map(float, (zero_data[i])[1:len(zero_data[i])]))
        label_object_to_classify = int(float(zero_data[i][0])) # Class

        nearest_neighbor_distance = float('inf')
        nearest_neighbor_location = float('inf')
        nearest_neighbor_label = None

        for j in range(len(zero_data)):
            if j != i:
                object_to_compare = list(map(float, (zero_data[j])[1:len(zero_data[j])]))

                # Euclidean distance
                distance = sqrt(sum((y - x) ** 2 for x, y in zip(object_to_classify, object_to_compare)))
                
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = j
                    nearest_neighbor_label = int(float(zero_data[nearest_neighbor_location][0]))

        if label_object_to_classify == nearest_neighbor_label:
            number_correctly_classified += 1

    # Overall accuracy of set
    return number_correctly_classified / len(zero_data)

# Iterates over the features of the data using the forward selection algorithm
def forward_selection(data):
    current_set_of_features = set()
    best_accuracy_overall = 0
    best_set_overall = set()

    for i in range(len(data[0]) - 1):
        feature_to_add_at_this_level = None
        best_so_far_accuracy = 0
    
        for j in range(1, len(data[0])):
            if j not in current_set_of_features:
                accuracy = cross_validation(data, current_set_of_features, j, 'add')
                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add_at_this_level = j;

        # Adds the feature that yields the best accuracy
        current_set_of_features.add(feature_to_add_at_this_level)

        print(current_set_of_features)
        print(best_so_far_accuracy)

        if best_so_far_accuracy > best_accuracy_overall:
            best_accuracy_overall = best_so_far_accuracy
            best_set_overall = copy.copy(current_set_of_features)

    
    print('The best feature subset is ' + str(best_set_overall) + ', which has an accuracy of ' + str(best_accuracy_overall * 100) + '%')

# Iterates over the features of the data using the backward elimination
# algorithm
def backward_elimination(data):
    current_set_of_features = set(range(1, len(data[0])))
    best_accuracy_overall = 0
    best_set_overall = set()

    for i in range(len(data[0]) - 1):
        feature_to_remove_at_this_level = None
        worst_so_far_accuracy = float('inf')
        best_so_far_accuracy = 0

        for j in range(1, len(data[0])):
            if j in current_set_of_features:
                accuracy = cross_validation(data, current_set_of_features, j, 'remove')
                if accuracy < worst_so_far_accuracy:
                    worst_so_far_accuracy = accuracy
                    feature_to_remove_at_this_level = j
                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy

        # Removes the feature that yields the worst accuracy
        current_set_of_features.remove(feature_to_remove_at_this_level)

        print(current_set_of_features)
        print(best_so_far_accuracy)

        if best_so_far_accuracy > best_accuracy_overall:
            best_accuracy_overall = best_so_far_accuracy
            best_set_overall = copy.copy(current_set_of_features)

    print('The best feature subset is ' + str(best_set_overall) + ', which has an accuracy of ' + str(best_accuracy_overall * 100) + '%')