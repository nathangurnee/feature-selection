from math import sqrt
import copy

def euclidean_distance(list1, list2):
    sum = 0
    for i in range(len(list1)):
        sum += ((list2[i] - list1[i]) ** 2)
    return sqrt(sum)

def cross_validation(data, current_set, feature_to_add):
    zero_data = copy.deepcopy(data)
    for i in range(len(zero_data)):
        for j in range(1, len(zero_data[i])):
            if j not in current_set and j != feature_to_add:
                zero_data[i][j] = 0

    number_correctly_classified = 0

    for i in range(len(zero_data)):
        object_to_classify = list(map(float, (zero_data[i])[1:len(zero_data[i])]))
        label_object_to_classify = int(float(zero_data[i][0]))

        nearest_neighbor_distance = float('inf')
        nearest_neighbor_location = float('inf')
        nearest_neighbor_label = None

        for j in range(len(zero_data)):
            if j != i:
                object_to_compare = list(map(float, (zero_data[j])[1:len(zero_data[j])]))
                distance = euclidean_distance(object_to_classify, object_to_compare)
                
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = j
                    nearest_neighbor_label = int(float(zero_data[nearest_neighbor_location][0]))

        if label_object_to_classify == nearest_neighbor_label:
            number_correctly_classified += 1

    return number_correctly_classified / len(zero_data)


def forward_selection(data):
    current_set_of_features = set()
    best_accuracy_overall = 0
    best_set_overall = set()

    for i in range(len(data[0]) - 1):
        feature_to_add_at_this_level = None
        best_so_far_accuracy = 0
    
        for j in range(1, len(data[0])):
            if j not in current_set_of_features:
                accuracy = cross_validation(data, current_set_of_features, j)
                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add_at_this_level = j;

        current_set_of_features.add(feature_to_add_at_this_level)

        if best_so_far_accuracy > best_accuracy_overall:
            best_accuracy_overall = best_so_far_accuracy
            best_set_overall = copy.copy(current_set_of_features)

    format_accuracy = "{:.2f}".format(best_accuracy_overall)
    print('The best feature subset is ' + str(best_set_overall) + ', which has an accuracy of ' + str(best_accuracy_overall * 100) + '%')


