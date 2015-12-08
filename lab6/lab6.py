# 6.034 Lab 6 2015: Neural Nets & SVMs

from nn_problems import *
from svm_problems import *
from math import e

#### NEURAL NETS ###############################################################

# Wiring a neural net

nn_half = [1]

nn_angle = [2,1]

nn_cross = [2,2,1]

nn_stripe = [3,1]

nn_hexagon = [6,1]

# Optional problem; change TEST_NN_GRID to True to test locally
TEST_NN_GRID = True
nn_grid = [4,2,1]

# Helper functions
def stairstep(x, threshold=0):
    "Computes stairstep(x) using the given threshold (T)"
    if x >= threshold:
        return 1
    else:
        return 0

def sigmoid(x, steepness=1, midpoint=0):
    "Computes sigmoid(x) using the given steepness (S) and midpoint (M)"
    return 1/(1 + e**(-steepness * (x - midpoint)))

def accuracy(desired_output, actual_output):
    "Computes accuracy. If output is binary, accuracy ranges from -0.5 to 0."
    return (-0.5) * ((desired_output - actual_output)**2)


# Forward propagation
def forward_prop(net, input_values, threshold_fn=stairstep):
    """Given a neural net and dictionary of input values, performs forward
    propagation with the given threshold function to compute binary output.
    This function should not modify the input net.  Returns a tuple containing:
    (1) the final output of the neural net
    (2) a dictionary mapping neurons to their immediate outputs"""
    dic = {}
    wires = net.wires
    out = 0

    neurons = net.topological_sort()

    for neuron in neurons:
        summer = 0
        incoming_neighbors = net.get_incoming_neighbors(neuron)
        for i in incoming_neighbors:
            for w in wires:
                if w.startNode == i and w.endNode == neuron:
                    if i in input_values:
                        summer += input_values[i] * w.weight
                    else:
                        summer += i * w.weight

        out = threshold_fn(summer)
        dic[neuron] = out
        input_values[neuron] = out

    return (out, dic)

# Backward propagation
def calculate_deltas(net, input_values, desired_output):
    """Computes the update coefficient (delta_B) for each neuron in the
    neural net.  Uses sigmoid function to compute output.  Returns a dictionary
    mapping neuron names to update coefficient (delta_B values)."""
    neurons = net.topological_sort()
    wires = net.wires

    for neuron in neurons:
        summer = 0
        incoming_neighbors = net.get_incoming_neighbors(neuron)
        for i in incoming_neighbors:
            for w in wires:
                if w.startNode == i and w.endNode == neuron:
                    if i in input_values:
                        summer += input_values[i] * w.weight
                    else:
                        summer += i * w.weight

        input_values[neuron] = sigmoid(summer)

    OutNeural = net.get_output_neuron()
    out = input_values[OutNeural]
    deltas = {}
    neurons = neurons[::-1]

    for neuron in neurons:
        summer = 0
        tmp = input_values[neuron] * (1 - input_values[neuron])
        if neuron == OutNeural:
            deltas[neuron] = tmp * (desired_output - out)
        else:
            out_going = net.get_outgoing_neighbors(neuron)
            for i in out_going:
                for w in wires:
                    if w.startNode == neuron and w.endNode == i:
                        summer += w.weight * deltas[i]

            deltas[neuron] = tmp * summer

    return deltas

def update_weights(net, input_values, desired_output, r=1):
    """Performs a single step of back-propagation.  Computes delta_B values and
    weight updates for entire neural net, then updates all weights.  Uses
    sigmoid function to compute output.  Returns the modified neural net, with
    updated weights."""
    deltas = calculate_deltas(net, input_values, desired_output)
    neurons = net.topological_sort()
    wires = net.wires

    for neuron in neurons:
        summer = 0
        incoming_neighbors = net.get_incoming_neighbors(neuron)
        for i in incoming_neighbors:
            for w in wires:
                if w.startNode == i and w.endNode == neuron:
                    if i in input_values:
                        summer += input_values[i] * w.weight
                    else:
                        summer += i * w.weight

        input_values[neuron] = sigmoid(summer)
    
    for w in net.wires:
        if w.endNode in net.neurons:
            if w.startNode in input_values:
                w.weight += r * input_values[w.startNode] * deltas[w.endNode]
            else:
                w.weight += r * w.startNode * deltas[w.endNode]

    return net

def back_prop(net, input_values, desired_output, r=1, accuracy_threshold=-.001):
    """Updates weights until accuracy surpasses minimum_accuracy.  Uses sigmoid
    function to compute output.  Returns a tuple containing:
    (1) the modified neural net, with trained weights
    (2) the number of iterations (that is, the number of weight updates)"""

    (out, dic) = forward_prop(net, input_values, sigmoid)
    counter = 0
    while (abs(accuracy(desired_output, out)) > abs(accuracy_threshold)):
        update_weights(net, input_values, desired_output, r)
        counter += 1
        (out, dic) = forward_prop(net, input_values, sigmoid)

    return (net, counter)


#### SUPPORT VECTOR MACHINES ###################################################

# Vector math
def dot_product(u, v):
    """Computes dot product of two vectors u and v, each represented as a tuple
    or list of coordinates.  Assume the two vectors are the same length."""
    # you could also call numpy.dot() directly :)
    ans = 0.0
    for i in range(len(u)):
        ans += u[i]*v[i]*1.0
    return ans
    
def norm(v):
    "Computes length of a vector v, represented as a tuple or list of coords."
    import numpy
    ans = 0
    for i in v: ans += i**2
    return numpy.sqrt(ans)

# Equation 1
def positiveness(svm, point):
    "Computes the expression (w dot x + b) for the given point"
    w = svm.boundary.w
    b = svm.boundary.b
    return dot_product(w, point.coords) + b

def classify(svm, point):
    """Uses given SVM to classify a Point.  Assumes that point's classification
    is unknown.  Returns +1 or -1, or 0 if point is on boundary"""
    if positiveness(svm, point) == 0:
        return 0
    elif positiveness(svm, point) > 0:
        return +1
    else:
        return -1

# Equation 2
def margin_width(svm):
    "Calculate margin width based on current boundary."
    import numpy
    w = svm.boundary.w
    return 2/(numpy.sqrt(dot_product(w, w)))


# Equation 3
def check_gutter_constraint(svm):
    """Returns the set of training points that violate one or both conditions:
        * gutter constraint (positiveness == classification for support vectors)
        * training points must not be between the gutters
    Assumes that the SVM has support vectors assigned."""
    x = svm.training_points
    w = svm.boundary.w
    b = svm.boundary.b
    supported_vec = svm.support_vectors #unused !!

    ans = set()

    for i in x:
        """
        * training points must not be between the gutters
        """
        if abs(dot_product(w, i.coords) + b) < 1:
            ans.add(i)
        """
        * gutter constraint (positiveness == classification for support vectors)
        """
        if classify(svm, i) !=  i.classification:
            ans.add(i)
    return ans

# Equations 4, 5
def check_alpha_signs(svm):
    """Returns the set of training points that violate either condition:
        * all non-support-vector training points have alpha = 0
        * all support vectors have alpha > 0
    Assumes that the SVM has support vectors assigned, and that all training
    points have alpha values assigned."""
    ans = set()
    x = svm.training_points

    for i in x:
        if (not (i in svm.support_vectors)) and i.alpha != 0:
            ans.add(i)
        elif i in svm.support_vectors and i.alpha <= 0:
            ans.add(i)

    return ans

def check_alpha_equations(svm):
    """Returns True if both Lagrange-multiplier equations are satisfied,
    otherwise False.  Assumes that the SVM has support vectors assigned, and
    that all training points have alpha values assigned."""
    summer = 0
    for i in svm.training_points:
        summer += i.alpha * i.classification

    if summer != 0:
        return False

    vec = []
    for i in range(len(svm.boundary.w)): vec.append(0)

    for p in svm.training_points:
        mat = list(p.coords)

        for i in range(len(mat)):
            mat[i] *= (p.alpha * p.classification)

        for i in range(len(vec)):
            vec[i] += mat[i]

    if vec != svm.boundary.w:
        return False

    return True


# Classification accuracy
def misclassified_training_points(svm):
    """Returns the set of training points that are classified incorrectly
    using the current decision boundary."""
    ans = set()
    for p in svm.training_points:
        if classify(svm, p) != p.classification:
            ans.add(p)
    return ans


#### SURVEY ####################################################################

NAME = None
COLLABORATORS = None
HOW_MANY_HOURS_THIS_LAB_TOOK = None
WHAT_I_FOUND_INTERESTING = None
WHAT_I_FOUND_BORING = None
SUGGESTIONS = None
