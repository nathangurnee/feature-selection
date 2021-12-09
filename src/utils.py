from math import sqrt
import copy

# Performs leave-one-out cross-validation on a data set
def cross_validation(data, current_set, feature, algorithm):
    zero_data = copy.deepcopy(data) # Deep copy of the data set

    # If 1: set all features not in the current set or not the feature to
    # be added to zero
    # If 2': set all features not in the current set and the feature to
    # be removed to zero
    if algorithm == 1:
        for i in range(len(zero_data)):
            for j in range(1, len(zero_data[i])):
                if j not in current_set and j != feature:
                    zero_data[i][j] = 0
    else:
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

# Iterates over the features of the data using two algorithms:
# -- Forward selection: starts with empty set of features and adds the feature
#    with the highest accuracy at each level
# -- Backward elimination: starts with a set of all the features and removes the
#    feature that creates the worst accuracy at each level
def feature_selection(data, algorithm):
    current_set_of_features = set() if algorithm == 1 else set(range(1, len(data[0])))
    best_accuracy_overall = 0
    best_set_overall = set()

    for i in range(len(data[0]) - 1):
        feature_at_this_level = None
        best_so_far_accuracy = 0

        for j in range(1, len(data[0])):
            if algorithm == 1:
                if j not in current_set_of_features:
                    accuracy = cross_validation(data, current_set_of_features, j, algorithm)
                    if accuracy > best_so_far_accuracy:
                        best_so_far_accuracy = accuracy
                        feature_at_this_level = j
            else:
                if j in current_set_of_features:
                    accuracy = cross_validation(data, current_set_of_features, j, algorithm)
                    if accuracy > best_so_far_accuracy:
                        best_so_far_accuracy = accuracy
                        feature_at_this_level = j

        # Chooses the feature that yields the best accuracy
        if algorithm == 1:
            current_set_of_features.add(feature_at_this_level)
        else:
            current_set_of_features.remove(feature_at_this_level)

        print('Current features: ', current_set_of_features)
        print('Accuracy: ', best_so_far_accuracy)

        if best_so_far_accuracy > best_accuracy_overall:
            best_accuracy_overall = best_so_far_accuracy
            best_set_overall = copy.copy(current_set_of_features)

    print('The best feature subset is ' + str(best_set_overall) + ', which has an accuracy of ' + str(best_accuracy_overall * 100) + '%')