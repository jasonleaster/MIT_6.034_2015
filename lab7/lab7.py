# 6.034 Lab 7 2015: Boosting (Adaboost)

from math import log as ln
INF = float('inf')

# Helper function for pick_best_classifier and adaboost
def fix_roundoff_error(inp, n=15):
    """inp can be a number, a list of numbers, or a dict whose values are numbers.
    * If inp is a number: Rounds the number to the nth decimal digit to reduce
        previous Python roundoff error.  Returns a float.
    * If inp is a list of numbers: Rounds each number as above.  Does not modify
        the original list.
    * If inp is a dictionary whose values are numbers: Rounds each value as
        above.  Does not modify the original dictionary."""
    fix_val = lambda val: round(abs(val),n)*[-1,1][val>=0]
    if isinstance(inp, list): return map(fix_val, inp)
    if isinstance(inp, dict): return {key: fix_val(inp[key]) for key in inp}
    return fix_val(inp)


#### BOOSTING (ADABOOST) #######################################################

def initialize_weights(training_points):
    """Assigns every training point a weight equal to 1/N, where N is the number
    of training points.  Returns a dictionary mapping points to weights."""
    dic = {}

    weight = 1.0/len(training_points)
    for p in training_points: 
        dic[p] = weight

    return dic

def calculate_error_rates(point_to_weight, classifier_to_misclassified):
    """Given a dictionary mapping training points to their weights, and another
    dictionary mapping classifiers to the training points they misclassify,
    returns a dictionary mapping classifiers to their error rates."""
    errRate = {}

    for classifier, points in classifier_to_misclassified.items():
        summer = 0
        for p in points:
            summer += point_to_weight[p]

        errRate[classifier] = summer

    return errRate

def pick_best_classifier(classifier_to_error_rate, use_smallest_error=True):
    """Given a dictionary mapping classifiers to their error rates, returns the
    best* classifier.  Best* means 'smallest error rate' if use_smallest_error
    is True, otherwise 'error rate furthest from 1/2'."""
    best = None
    
    if use_smallest_error == True:
        for classifier, err in classifier_to_error_rate.items():
            if best == None:
                best = classifier
            else:
                if classifier_to_error_rate[best] == classifier_to_error_rate[classifier]:
                    ans = [best, classifier]
                    ans.sort()
                    best = ans[0]

                if classifier_to_error_rate[best] > classifier_to_error_rate[classifier]:
                    best = classifier
    else:
        errRate = 0.5
        for classifier, err in classifier_to_error_rate.items():
            if best == None:
                best = classifier
            else:

                if abs(fix_roundoff_error(abs(classifier_to_error_rate[classifier] - 0.5)) - \
                       fix_roundoff_error(abs(classifier_to_error_rate[best]       - 0.5))) < 1e-14:
                    ans = [best, classifier]
                    ans.sort()
                    best = ans[0]
                    continue

                if fix_roundoff_error(abs(classifier_to_error_rate[classifier] - 0.5)) > \
                   fix_roundoff_error(abs(classifier_to_error_rate[best]       - 0.5)):
                    best = classifier
                        
    return best

def calculate_voting_power(error_rate):
    """Given a classifier's error rate (a number), returns the voting power
    (aka alpha, or coefficient) for that classifier."""
    import numpy
    if error_rate == 0:
        return INF
    elif error_rate == 1:
        return -INF
    else:
        return 0.5*( ln((1- error_rate)/error_rate) )

def is_good_enough(H, training_points, classifier_to_misclassified,
                   mistake_tolerance=0):
    """Given an overall classifier H, a list of all training points, a
    dictionary mapping classifiers to the training points they misclassify, and
    a mistake tolerance (the maximum number of allowed misclassifications),
    returns False if H misclassifies more points than the tolerance allows,
    otherwise True.  H is represented as a list of (classifier, voting_power)
    tuples."""
    import numpy

    counter = 0
    for p in training_points:
        summer = 0
        tie = False
        for (classifier, voting_power) in H:
            points = classifier_to_misclassified[classifier]
            if p in points:
                summer += (-voting_power)
            else:
                summer += (voting_power)

        for i in range(1, len(H)):
            if H[i-1][1] == H[i][1]:
                tie = True
                counter += 1
                break

        if tie == True:
            continue

        if numpy.sign(summer) == -1:
            counter += 1

    if counter > mistake_tolerance:
        return False
    else:
        return True

def update_weights(point_to_weight, misclassified_points, error_rate):
    """Given a dictionary mapping training points to their old weights, a list
    of training points misclassified by the current weak classifier, and the
    error rate of the current weak classifier, returns a dictionary mapping
    training points to their new weights.  This function is allowed (but not
    required) to modify the input dictionary point_to_weight."""
    new_weight = {}
    for point, old_weight in point_to_weight.items():
        if point in misclassified_points:
            new_weight[point] = fix_roundoff_error(0.5*(1.0/error_rate)*old_weight)
        else:
            new_weight[point] = fix_roundoff_error(0.5*(1.0/(1-error_rate)) * old_weight)

    return new_weight

def adaboost(training_points, classifier_to_misclassified,
             use_smallest_error=True, mistake_tolerance=0, max_num_rounds=INF):
    """Performs the Adaboost algorithm for up to max_num_rounds rounds.
    Returns the resulting overall classifier H, represented as a list of
    (classifier, voting_power) tuples."""

    H = []

    point_to_weight = initialize_weights(training_points)

    rounds = 0

    while rounds < max_num_rounds:

        classifier_to_error_rate = calculate_error_rates(point_to_weight, classifier_to_misclassified)

        best_classifier = pick_best_classifier(classifier_to_error_rate, use_smallest_error)

        error_rate = classifier_to_error_rate[best_classifier]

        voting_power = calculate_voting_power( error_rate )

        if fix_roundoff_error(error_rate) == 0.5:
            return H

        H.append( (best_classifier, voting_power) )

        misclassified_points = classifier_to_misclassified[best_classifier]

        point_to_weight = update_weights(point_to_weight, misclassified_points, error_rate)

        if is_good_enough(H, training_points, classifier_to_misclassified, mistake_tolerance):
            return H


        rounds += 1


    return H





#### SURVEY ####################################################################

NAME = "EOF"
COLLABORATORS = "None"
HOW_MANY_HOURS_THIS_LAB_TOOK = 3
WHAT_I_FOUND_INTERESTING = "Everything in 6.034"
WHAT_I_FOUND_BORING = "Nothing"
SUGGESTIONS = "Move interesting lab"
