from tester import make_test, get_tests
from nn_problems import *
from svm_problems import *
from lab6 import sigmoid, TEST_NN_GRID
from random import random, randint


def randnum(max_val=100):
    "Generates a random float 0 < n < max_val"
    return random() * randint(1, int(max_val))

def dict_contains(d, pairs):
    "Returns True if d contains all the specified pairs, otherwise False"
    items = d.items()
    return all([p in items for p in pairs])

def dict_approx_equal(dict1, dict2, epsilon=0.00000001):
    """Returns True if two dicts have the same keys and approximately equal
    values, otherwise False"""
    return (set(dict1.keys()) == set(dict2.keys())
            and all([approx_equal(dict1[key], dict2[key], epsilon)
                     for key in dict1.keys()]))


#### NEURAL NETS ###############################################################

## stairstep
#T=0, x>T -> 1
def stairstep_0_getargs() :  #TEST 1
    return [randnum()]
def stairstep_0_testanswer(val, original_val = None) :
    return val == 1
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = stairstep_0_getargs,
          testanswer = stairstep_0_testanswer,
          expected_val = "1",
          name = 'stairstep')

#T=0, x<T -> 0
def stairstep_1_getargs() :  #TEST 2
    return [-randnum(), 0]
def stairstep_1_testanswer(val, original_val = None) :
    return val == 0
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = stairstep_1_getargs,
          testanswer = stairstep_1_testanswer,
          expected_val = "0",
          name = 'stairstep')

#T>0, x=T -> 1
def stairstep_2_getargs() :  #TEST 3
    T = randnum()
    return [T, T]
def stairstep_2_testanswer(val, original_val = None) :
    return val == 1
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = stairstep_2_getargs,
          testanswer = stairstep_2_testanswer,
          expected_val = "1",
          name = 'stairstep')


## sigmoid
#S=1, M=0, x>>M -> ~1
def sigmoid_0_getargs() :  #TEST 4
    return [10, 1, 0]
def sigmoid_0_testanswer(val, original_val = None) :
    return approx_equal(val, 0.9999, 0.0001)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = sigmoid_0_getargs,
          testanswer = sigmoid_0_testanswer,
          expected_val = "~0.9999",
          name = 'sigmoid')

#S=any, M>>0, x=M -> 0.5
def sigmoid_1_getargs() :  #TEST 5
    M = randnum()+10
    return [M, randnum(), M]
def sigmoid_1_testanswer(val, original_val = None) :
    return val == 0.5
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = sigmoid_1_getargs,
          testanswer = sigmoid_1_testanswer,
          expected_val = "0.5",
          name = 'sigmoid')

#S=1, M>>0, x=0 -> ~0
def sigmoid_2_getargs() :  #TEST 6
    return [0, 1, 15]
def sigmoid_2_testanswer(val, original_val = None) :
    return approx_equal(val, 0, 0.00001)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = sigmoid_2_getargs,
          testanswer = sigmoid_2_testanswer,
          expected_val = "~0",
          name = 'sigmoid')

#S=0.5, M=0.5, x=0 -> ~0.4378 (arbitrary parameters)
def sigmoid_3_getargs() :  #TEST 7
    return [0, 0.5, 0.5]
def sigmoid_3_testanswer(val, original_val = None) :
    return approx_equal(val, 0.4378, 0.0001)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = sigmoid_3_getargs,
          testanswer = sigmoid_3_testanswer,
          expected_val = "~0.4378",
          name = 'sigmoid')


## accuracy
#d=a -> 0
def accuracy_0_getargs() :  #TEST 8
    d = randnum()-50
    return [d, d]
def accuracy_0_testanswer(val, original_val = None) :
    return val == 0
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = accuracy_0_getargs,
          testanswer = accuracy_0_testanswer,
          expected_val = "0",
          name = 'accuracy')

#d=1, a=0 -> -0.5
def accuracy_1_getargs() :  #TEST 9
    return [1, 0]
def accuracy_1_testanswer(val, original_val = None) :
    return val == -0.5
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = accuracy_1_getargs,
          testanswer = accuracy_1_testanswer,
          expected_val = "-0.5",
          name = 'accuracy')

#d=0, a=0.3 -> -0.045 (arbitrary parameters)
def accuracy_2_getargs() :  #TEST 10
    return [0, 0.3]
def accuracy_2_testanswer(val, original_val = None) :
    return val == -0.045
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = accuracy_2_getargs,
          testanswer = accuracy_2_testanswer,
          expected_val = "-0.045",
          name = 'accuracy')


## forward_prop
#basic fwd prop, 1 neuron, constant and variable inputs
def forward_prop_0_getargs() :  #TEST 11
    return [nn_basic.copy(), nn_basic_inputs.copy()]
def forward_prop_0_testanswer(val, original_val = None) :
    out, d = val
    return out == 1 and dict_contains(d, [('neuron', 1)])
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = forward_prop_0_getargs,
          testanswer = forward_prop_0_testanswer,
          expected_val = ("(1, (dict containing key-value pair: "
                          + "('neuron', 1))"),
          name = 'forward_prop')

#1 neuron, edge case: ==T -> 1
def forward_prop_1_getargs() :  #TEST 12
    return [nn_AND.copy(), {'x':1.5, 'y':0}]
def forward_prop_1_testanswer(val, original_val = None) :
    out, d = val
    return out == 1 and dict_contains(d, [('N1', 1)])
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = forward_prop_1_getargs,
          testanswer = forward_prop_1_testanswer,
          expected_val = ("(1, (dict containing key-value pair: "
                          + "('N1', 1)))"),
          name = 'forward_prop')

#5 neurons, XOR of two lines
def forward_prop_2_getargs() :  #TEST 13
    return [nn_XOR_lines.copy(), {'x':0.5, 'y':4}]
forward_prop_2_expected_outputs = [('line1', 0), ('line2', 0),
                                   ('X1', 0), ('X2', 1), ('AND', 0)]
def forward_prop_2_testanswer(val, original_val = None) :
    out, d = val
    return out == 0 and dict_contains(d, forward_prop_2_expected_outputs)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = forward_prop_2_getargs,
          testanswer = forward_prop_2_testanswer,
          expected_val = ("(0, (dict containing key-value pairs: "
                          + str(forward_prop_2_expected_outputs) + "))"),
          name = 'forward_prop')

#5 neurons, XOR of two lines; shuffle to check for dependence on list ordering
def forward_prop_3_getargs() :  #TEST 14
    return [nn_XOR_lines.copy().shuffle_lists(), {'x':4, 'y':0.5}]
forward_prop_3_expected_outputs = [('line1', 1), ('line2', 0),
                                   ('X1', 1), ('X2', 1), ('AND', 1)]

def forward_prop_3_testanswer(val, original_val = None) :
    out, d = val
    return out == 1 and dict_contains(d, forward_prop_3_expected_outputs)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = forward_prop_3_getargs,
          testanswer = forward_prop_3_testanswer,
          expected_val = ("(1, (dict containing key-value pairs: "
                          + str(forward_prop_3_expected_outputs) + "))"),
          name = 'forward_prop')

#3 neurons, River problem with stairstep function
def forward_prop_4_getargs() :  #TEST 15
    return [get_nn_River(1, -2, 5, 1, -2, 1), nn_River_inputs.copy()]
forward_prop_4_expected_outputs = [('A', 1), ('B', 0), ('C', 0)]
def forward_prop_4_testanswer(val, original_val = None) :
    out, d = val
    return out == 0 and dict_contains(d, forward_prop_4_expected_outputs)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = forward_prop_4_getargs,
          testanswer = forward_prop_4_testanswer,
          expected_val = ("(0, (dict containing key-value pairs: "
                          + str(forward_prop_4_expected_outputs) + "))"),
          name = 'forward_prop')

#3 neurons, River problem with stairstep function
def forward_prop_5_getargs() :  #TEST 16
    """ original test code
    return [get_nn_River(1, -2, 5, 3, -2, 1), nn_River_inputs.copy()]
    """
    return [get_nn_River(1, -2, 3, 5, -2, 1), nn_River_inputs.copy()]
forward_prop_5_expected_outputs = [('A', 1), ('B', 0), ('C', 1)]
def forward_prop_5_testanswer(val, original_val = None) :
    out, d = val
    return out == 1 and dict_contains(d, forward_prop_5_expected_outputs)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = forward_prop_5_getargs,
          testanswer = forward_prop_5_testanswer,
          expected_val = ("(1, (dict containing key-value pairs: "
                          + str(forward_prop_5_expected_outputs) + "))"),
          name = 'forward_prop')

#1 neuron, sigmoid
def forward_prop_6_getargs() :  #TEST 17
    return [nn_AND.copy(), {'x':1, 'y':1}, sigmoid]
def forward_prop_6_testanswer(val, original_val = None) :
    out, d = val
    return approx_equal(out, 0.622459, 0.0001) and d['N1'] == out
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = forward_prop_6_getargs,
          testanswer = forward_prop_6_testanswer,
          expected_val = ("(~0.62246, (dict containing key-value pair: "
                          + "('N1', ~0.62246)))"),
          name = 'forward_prop')

#1 neuron, different threshold function
def forward_prop_7_getargs() :  #TEST 18
    return [nn_AND.copy(), {'x':20, 'y':23.5}, ReLU]
def forward_prop_7_testanswer(val, original_val = None) :
    out, d = val
    return out == 42 and d['N1'] == out
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = forward_prop_7_getargs,
          testanswer = forward_prop_7_testanswer,
          expected_val = ("(42, (dict containing key-value pair: "
                          + "('N1', 42)))"),
          name = 'forward_prop')


#### BACKWARD PROPAGATION

## calculate_deltas
#3 weights to update, final layer only
def calculate_deltas_0_getargs() :  #TEST 19
    return [nn_AND.copy(), {'x':3.5, 'y':-2}, 1]
def calculate_deltas_0_testanswer(val, original_val = None) :
    return val == {'N1': 0.125}
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = calculate_deltas_0_getargs,
          testanswer = calculate_deltas_0_testanswer,
          expected_val = "{'N1': 0.125}",
          name = 'calculate_deltas')

#6 weights to update (River nn); shuffled
def calculate_deltas_2_getargs() :  #TEST 20
    return [get_nn_River(1, -2, 5, 3, -2, 1).shuffle_lists(),
            nn_River_inputs.copy(), nn_River_desired]
calculate_deltas_2_expected_deltas = {'A': 0.04441976755198489,
                                      'B': -0.01186039570737828,
                                      'C': -0.1129630506644473}
def calculate_deltas_2_testanswer(val, original_val = None) :
    return dict_approx_equal(val, calculate_deltas_2_expected_deltas)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = calculate_deltas_2_getargs,
          testanswer = calculate_deltas_2_testanswer,
          expected_val = str(calculate_deltas_2_expected_deltas),
          name = 'calculate_deltas')

# Here's where all the numbers above came from:
#    A = sigmoid(1) = 0.7310585786300049
#    B = sigmoid(-2) = 0.11920292202211757
#    C = sigmoid(A*-2+B+3) = 0.839846413654423
#    delta_C = C*(1-C)*-C = -0.1129630506644473
#    delta_A = A*(1-A)*-2*delta_C = 0.04441976755198489
#    delta_B = B*(1-B)*delta_C = -0.011860395707378284

#requires summation over outgoing neurons C_i
def calculate_deltas_3_getargs() :  #TEST 21
    return [nn_branching.shuffle_lists(), {'in': 17}, 1]
calculate_deltas_3_expected_deltas = {'N1': 0.033042492944110255, \
    'N2': 0.027644450191861528, 'N3': -0.06291182225171182, \
    'Nin': -0.025101018356825537, 'Nout': 0.1406041318860752}
def calculate_deltas_3_testanswer(val, original_val = None) :
    return dict_approx_equal(val, calculate_deltas_3_expected_deltas)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = calculate_deltas_3_getargs,
          testanswer = calculate_deltas_3_testanswer,
          expected_val = str(calculate_deltas_3_expected_deltas),
          name = 'calculate_deltas')

# Here's where the numbers above came from:
# sigmoid(0) = 0.5
# delta_Nout = out*(1-out)*(1-out)
# delta_N1 = sigmoid(0.5)*(1-sigmoid(0.5))*1*delta_Nout
# delta_N2 = sigmoid(2*0.5)*(1-sigmoid(2*0.5))*1*delta_Nout
# delta_N3 = sigmoid(3*0.5)*(1-sigmoid(3*0.5))*-3*delta_Nout
# delta_Nin = 0.5*(1-0.5)*(delta_N1+2*delta_N2+3*delta_N3)


## update_weights
#3 weights to update, final layer only
def update_weights_0_getargs() :  #TEST 22
    return [nn_AND.copy(), {'x':3.5, 'y':-2}, 1]
def update_weights_0_testanswer(val, original_val = None) :
    return val == nn_AND_update_iter1
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = update_weights_0_getargs,
          testanswer = update_weights_0_testanswer,
          expected_val = str(nn_AND_update_iter1),
          name = 'update_weights')

#3 weights to update, final layer only, different r
def update_weights_1_getargs() :  #TEST 23
    return [nn_AND.copy(), {'x':3.5, 'y':-2}, 1, 10]
def update_weights_1_testanswer(val, original_val = None) :
    return val == nn_AND_update_iter1_r10
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = update_weights_1_getargs,
          testanswer = update_weights_1_testanswer,
          expected_val = str(nn_AND_update_iter1_r10),
          name = 'update_weights')

#6 weights to update (River nn); shuffled
def update_weights_2_getargs() :  #TEST 24
    return [get_nn_River(1, -2, 5, 3, -2, 1).shuffle_lists(),
            nn_River_inputs.copy(), nn_River_desired]
update_weights_2_expected_net = get_nn_River(1.0444197675519848, \
    -2.0118603957073784, 5, 2.8870369493355525, -2.08258260725646, \
    0.9865344742802654)
def update_weights_2_testanswer(val, original_val = None) :
    return val == update_weights_2_expected_net
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = update_weights_2_getargs,
          testanswer = update_weights_2_testanswer,
          expected_val = str(update_weights_2_expected_net),
          name = 'update_weights')

# Here's where all the numbers above came from:
#    A = sigmoid(1) = 0.7310585786300049
#    B = sigmoid(-2) = 0.11920292202211757
#    C = sigmoid(A*-2+B+3) = 0.839846413654423
#    delta_C = C*(1-C)*-C = -0.1129630506644473
#    delta_A = A*(1-A)*-2*delta_C = 0.04441976755198489
#    delta_B = B*(1-B)*delta_C = -0.011860395707378284
#    w1 = 1+delta_A = 1.0444197675519848
#    w2 = -2+delta_B = -2.0118603957073784
#    w3 = 5 + 0 = 5
#    w4 = 3+delta_C = 2.8870369493355525
#    w5 = -2+A*delta_C = -2.08258260725646
#    w6 = 1+B*delta_C = 0.9865344742802654

#requires summation over outgoing neurons C_i
def update_weights_3_getargs() :  #TEST 25
    return [nn_branching.shuffle_lists(), {'in': 17}, 1]
def update_weights_3_testanswer(val, original_val = None) :
    return val.__eq__(nn_branching_update_iter1, 0.00000001)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = update_weights_3_getargs,
          testanswer = update_weights_3_testanswer,
          expected_val = str(nn_branching_update_iter1),
          name = 'update_weights')

# Here's where the numbers above came from:
# sigmoid(0) = 0.5
# delta_Nout = out*(1-out)*(1-out)
# delta_N1 = sigmoid(0.5)*(1-sigmoid(0.5))*1*delta_Nout
# delta_N2 = sigmoid(2*0.5)*(1-sigmoid(2*0.5))*1*delta_Nout
# delta_N3 = sigmoid(3*0.5)*(1-sigmoid(3*0.5))*-3*delta_Nout
# delta_Nin = 0.5*(1-0.5)*(delta_N1+2*delta_N2+3*delta_N3)
# w_in_to_Nin = 0 + 17*delta_Nin
# w_Nin_to_N1 = 1 + 0.5*delta_N1
# w_Nin_to_N2 = 2 + 0.5*delta_N2
# w_Nin_to_N3 = 3 + 0.5*delta_N3
# w_N1_to_Nout = 0 + sigmoid(0.5) * delta_Nout
# w_N2_to_Nout = 0 + sigmoid(2*0.5) * delta_Nout
# w_N3_to_Nout = 0 + sigmoid(3*0.5) * delta_Nout


## back_prop
#stops after 1 iter, better than default min_acc
def back_prop_0_getargs() :  #TEST 26
    return [nn_AND.copy(), {'x':3.5, 'y':-2}, 1, 10, -0.000001]
def back_prop_0_testanswer(val, original_val = None) :
    net, count = val
    return net == nn_AND_update_iter1_r10 and count == 1
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = back_prop_0_getargs,
          testanswer = back_prop_0_testanswer,
          expected_val = "(" + str(nn_AND_update_iter1_r10) + ", 1)",
          name = 'back_prop')

#stops after 1 iter, not as good as default min_acc
def back_prop_1_getargs() :  #TEST 27
    return [nn_AND.copy(), {'x':3.5, 'y':-2}, 1, 1, -0.01]
def back_prop_1_testanswer(val, original_val = None) :
    net, count = val
    return net == nn_AND_update_iter1 and count == 1
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = back_prop_1_getargs,
          testanswer = back_prop_1_testanswer,
          expected_val = "(" + str(nn_AND_update_iter1) + ", 1)",
          name = 'back_prop')

#already high enough accuracy; stops after 0 iter
def back_prop_2_getargs() :  #TEST 28
    return [nn_AND.copy(), {'x':-10, 'y':-10}, 0]
def back_prop_2_testanswer(val, original_val = None) :
    net, count = val
    return net == nn_AND and count == 0
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = back_prop_2_getargs,
          testanswer = back_prop_2_testanswer,
          expected_val = "((original neural net, unchanged), 0)",
          name = 'back_prop')


#three iterations
def back_prop_4_getargs() :  #TEST 29
    return [nn_AND.copy(), {'x':3.5, 'y':-2}, 1, 1, -0.0035]
def back_prop_4_testanswer(val, original_val = None) :
    net, count = val
    return nn_AND_update_iter3.__eq__(net, 0.000000000001) and count == 3
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = back_prop_4_getargs,
          testanswer = back_prop_4_testanswer,
          expected_val = "(" + str(nn_AND_update_iter3) + ", 3)",
          name = 'back_prop')


#### SUPPORT VECTOR MACHINES ###################################################

## dot_product
def dot_product_0_getargs() :  #TEST 30
    return [(3, -7), [2.5, 10]]
def dot_product_0_testanswer(val, original_val = None) :
    return val == -62.5
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = dot_product_0_getargs,
          testanswer = dot_product_0_testanswer,
          expected_val = "-62.5",
          name = 'dot_product')

def dot_product_1_getargs() :  #TEST 31
    return [[4], (5,)]
def dot_product_1_testanswer(val, original_val = None) :
    return val == 20
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = dot_product_1_getargs,
          testanswer = dot_product_1_testanswer,
          expected_val = "20",
          name = 'dot_product')

def dot_product_2_getargs() :  #TEST 32
    return [(1,2,3,4,2), (1, 10, 1000, 100, 10000)]
def dot_product_2_testanswer(val, original_val = None) :
    return val == 23421
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = dot_product_2_getargs,
          testanswer = dot_product_2_testanswer,
          expected_val = "23421",
          name = 'dot_product')


## norm
def norm_0_getargs() :  #TEST 33
    return [(-3, 4)]
def norm_0_testanswer(val, original_val = None) :
    return val == 5
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = norm_0_getargs,
          testanswer = norm_0_testanswer,
          expected_val = "5",
          name = 'norm')

def norm_1_getargs() :  #TEST 34
    return [(17.2,)]
def norm_1_testanswer(val, original_val = None) :
    return val == 17.2
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = norm_1_getargs,
          testanswer = norm_1_testanswer,
          expected_val = "17.2",
          name = 'norm')

def norm_2_getargs() :  #TEST 35
    return [[6, 2, 11, -2, 2]]
def norm_2_testanswer(val, original_val = None) :
    return val == 13
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = norm_2_getargs,
          testanswer = norm_2_testanswer,
          expected_val = "13",
          name = 'norm')


## positiveness
def positiveness_0_getargs() :  #TEST 36
    return [svm_basic.copy(), Point('p', (0, 0))]
def positiveness_0_testanswer(val, original_val = None) :
    return val == 3
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = positiveness_0_getargs,
          testanswer = positiveness_0_testanswer,
          expected_val = "3",
          name = 'positiveness')

def positiveness_1_getargs() :  #TEST 37
    return [SVM(Boundary([2, 5, -1, 1, 0, -0.1], 0.01)),
            Point('v', [3, -2, -7, -10, 99, 8])]
def positiveness_1_testanswer(val, original_val = None) :
    return val == -7.79
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = positiveness_1_getargs,
          testanswer = positiveness_1_testanswer,
          expected_val = "-7.79",
          name = 'positiveness')

def positiveness_2_getargs() :  #TEST 38
    return [svm_untrained.copy(), ptD]
def positiveness_2_testanswer(val, original_val = None) :
    return val == 0
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = positiveness_2_getargs,
          testanswer = positiveness_2_testanswer,
          expected_val = "0",
          name = 'positiveness')


## classify
#point doesn't have classification
def classify_0_getargs() :  #TEST 39
    return [svm_basic.copy(), Point('test_point', (0, 0))]
def classify_0_testanswer(val, original_val = None) :
    return val == 1
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = classify_0_getargs,
          testanswer = classify_0_testanswer,
          expected_val = "+1",
          name = 'classify')

#point has classification; misclassified
def classify_1_getargs() :  #TEST 40
    return [svm_untrained.copy(), ptF]
def classify_1_testanswer(val, original_val = None) :
    return val == -1
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = classify_1_getargs,
          testanswer = classify_1_testanswer,
          expected_val = "-1",
          name = 'classify')

#point has classification; classified correctly
def classify_2_getargs() :  #TEST 41
    return [svm_basic.copy(), ptD]
def classify_2_testanswer(val, original_val = None) :
    return val == -1
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = classify_2_getargs,
          testanswer = classify_2_testanswer,
          expected_val = "-1",
          name = 'classify')

# point on boundary
def classify_3_getargs() :  #TEST 42
    return [svm_basic.copy(), Point('x', [1.5, randnum()])]
def classify_3_testanswer(val, original_val = None) :
    return val == 0
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = classify_3_getargs,
          testanswer = classify_3_testanswer,
          expected_val = "0",
          name = 'classify')

#point within margin, not on boundary
def classify_4_getargs() :  #TEST 43
    return [svm_basic.copy(), Point('x', [1.6, randnum()])]
def classify_4_testanswer(val, original_val = None) :
    return val == -1
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = classify_4_getargs,
          testanswer = classify_4_testanswer,
          expected_val = "-1",
          name = 'classify')


## margin_width
# w=[-3,4], so norm=5 -> 0.4
def margin_width_0_getargs() :  #TEST 44
    return [SVM(Boundary((-3, 4), -13.78))]
def margin_width_0_testanswer(val, original_val = None) :
    return val == 0.4
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = margin_width_0_getargs,
          testanswer = margin_width_0_testanswer,
          expected_val = "0.4",
          name = 'margin_width')

# w=[1,0], point on boundary, point misclassified -> 2 (ignore points)
def margin_width_1_getargs() :  #TEST 45
    return [svm_untrained.copy()]
def margin_width_1_testanswer(val, original_val = None) :
    return val == 2
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = margin_width_1_getargs,
          testanswer = margin_width_1_testanswer,
          expected_val = "2",
          name = 'margin_width')

# 1D
def margin_width_2_getargs() :  #TEST 46
    return [SVM(Boundary([0.25], 0))]
def margin_width_2_testanswer(val, original_val = None) :
    return val == 8
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = margin_width_2_getargs,
          testanswer = margin_width_2_testanswer,
          expected_val = "8",
          name = 'margin_width')

# higher number of dimensions
def margin_width_3_getargs() :  #TEST 47
    return [SVM(Boundary([0, -5, 0, 12], 1))]
def margin_width_3_testanswer(val, original_val = None) :
    return approx_equal(val, 2./13, 0.000001)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = margin_width_3_getargs,
          testanswer = margin_width_3_testanswer,
          expected_val = "~" + str(2./13),
          name = 'margin_width')


## check_gutter_constraint
# pass -> empty set
def check_gutter_constraint_0_getargs() :  #TEST 48
    return [svm_basic.copy()]
def check_gutter_constraint_0_testanswer(val, original_val = None) :
    return val == set()
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = check_gutter_constraint_0_getargs,
          testanswer = check_gutter_constraint_0_testanswer,
          expected_val = set(),
          name = 'check_gutter_constraint')

# fail gutter constraint equation
def check_gutter_constraint_1_getargs() :  #TEST 49
    return [svm_basic.copy().set_boundary(Boundary([1, 0], -1.5))]
check_gutter_constraint_1_expected = set([ptA, ptB, ptD])
def check_gutter_constraint_1_testanswer(val, original_val = None) :
    return equality_by_string(val, check_gutter_constraint_1_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = check_gutter_constraint_1_getargs,
          testanswer = check_gutter_constraint_1_testanswer,
          expected_val = check_gutter_constraint_1_expected,
          name = 'check_gutter_constraint')

# fail with point in gutter
def check_gutter_constraint_2_getargs() :  #TEST 50
    svm = svm_basic.copy()
    svm.training_points.append(ptL)
    return [svm]
check_gutter_constraint_2_expected = set([ptL])
def check_gutter_constraint_2_testanswer(val, original_val = None) :
    return equality_by_string(val, check_gutter_constraint_2_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = check_gutter_constraint_2_getargs,
          testanswer = check_gutter_constraint_2_testanswer,
          expected_val = check_gutter_constraint_2_expected,
          name = 'check_gutter_constraint')


## check_alpha_signs
# set should include: sv w alpha=0, sv w alpha<0, pt w alpha < 0, pt w alpha > 0
# set should not include: sv w alpha > 0, pt w alpha = 0
def check_alpha_signs_0_getargs() :  #TEST 51
    return [svm_alphas.copy()]
check_alpha_signs_0_expected = set([ptF, ptG, ptJ, ptH, ptD])
def check_alpha_signs_0_testanswer(val, original_val = None) :
    return equality_by_string(val, check_alpha_signs_0_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = check_alpha_signs_0_getargs,
          testanswer = check_alpha_signs_0_testanswer,
          expected_val = str(check_alpha_signs_0_expected),
          name = 'check_alpha_signs')

# return empty set
def check_alpha_signs_1_getargs() :  #TEST 52
    return [svm_basic.copy()]
def check_alpha_signs_1_testanswer(val, original_val = None) :
    return val == set()
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = check_alpha_signs_1_getargs,
          testanswer = check_alpha_signs_1_testanswer,
          expected_val = set(),
          name = 'check_alpha_signs')


## check_alpha_equations
# both equations hold -> True
def check_alpha_equations_0_getargs() :  #TEST 53
    return [svm_basic.copy()]
def check_alpha_equations_0_testanswer(val, original_val = None) :
    return val == True
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = check_alpha_equations_0_getargs,
          testanswer = check_alpha_equations_0_testanswer,
          expected_val = "True",
          name = 'check_alpha_equations')

# Eq 4 fails
def check_alpha_equations_1_getargs() :  #TEST 54
    return [svm_fail_eq4.copy()]
def check_alpha_equations_1_testanswer(val, original_val = None) :
    return val == False
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = check_alpha_equations_1_getargs,
          testanswer = check_alpha_equations_1_testanswer,
          expected_val = "False",
          name = 'check_alpha_equations')

# Eq 5 fails
def check_alpha_equations_2_getargs() :  #TEST 55
    return [svm_fail_eq5.copy()]
def check_alpha_equations_2_testanswer(val, original_val = None) :
    return val == False
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = check_alpha_equations_2_getargs,
          testanswer = check_alpha_equations_2_testanswer,
          expected_val = "False",
          name = 'check_alpha_equations')


## misclassified_training_points
def misclassified_training_points_0_getargs() :  #TEST 56
    return [svm_basic.copy()]
def misclassified_training_points_0_testanswer(val, original_val = None) :
    return val == set()
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = misclassified_training_points_0_getargs,
          testanswer = misclassified_training_points_0_testanswer,
          expected_val = set(),
          name = 'misclassified_training_points')

def misclassified_training_points_1_getargs() :  #TEST 57
    return [svm_untrained.copy()]
misclassified_training_points_1_expected = set([ptD, ptF])
def misclassified_training_points_1_testanswer(val, original_val = None) :
    return equality_by_string(val, misclassified_training_points_1_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = misclassified_training_points_1_getargs,
          testanswer = misclassified_training_points_1_testanswer,
          expected_val = str(misclassified_training_points_1_expected),
          name = 'misclassified_training_points')


#### WIRING A NEURAL NET #######################################################
# TESTS 58-62 (63 optional)

nn_half_getargs = 'nn_half'
def nn_half_testanswer(val, original_val = None):
    return val == [1]
make_test(type = 'VALUE',
          getargs = nn_half_getargs,
          testanswer = nn_half_testanswer,
          expected_val = ('(list indicating correct minimum number of neurons '
                          + 'per layer)'),
          name = nn_half_getargs)

nn_angle_getargs = 'nn_angle'
def nn_angle_testanswer(val, original_val = None):
    return val == [2, 1]
make_test(type = 'VALUE',
          getargs = nn_angle_getargs,
          testanswer = nn_angle_testanswer,
          expected_val = ('(list indicating correct minimum number of neurons '
                          + 'per layer)'),
          name = nn_angle_getargs)

nn_cross_getargs = 'nn_cross'
def nn_cross_testanswer(val, original_val = None):
    return val == [2, 2, 1]
make_test(type = 'VALUE',
          getargs = nn_cross_getargs,
          testanswer = nn_cross_testanswer,
          expected_val = ('(list indicating correct minimum number of neurons '
                          + 'per layer)'),
          name = nn_cross_getargs)

nn_stripe_getargs = 'nn_stripe'
def nn_stripe_testanswer(val, original_val = None):
    return val == [3, 1]
make_test(type = 'VALUE',
          getargs = nn_stripe_getargs,
          testanswer = nn_stripe_testanswer,
          expected_val = ('(list indicating correct minimum number of neurons '
                          + 'per layer)'),
          name = nn_stripe_getargs)

nn_hexagon_getargs = 'nn_hexagon'
def nn_hexagon_testanswer(val, original_val = None):
    return val == [6, 1]
make_test(type = 'VALUE',
          getargs = nn_hexagon_getargs,
          testanswer = nn_hexagon_testanswer,
          expected_val = ('(list indicating correct minimum number of neurons '
                          + 'per layer)'),
          name = nn_hexagon_getargs)

if TEST_NN_GRID:
    nn_grid_getargs = 'nn_grid'
    def nn_grid_testanswer(val, original_val = None):
        return val == [4, 2, 1]
    make_test(type = 'VALUE',
              getargs = nn_grid_getargs,
              testanswer = nn_grid_testanswer,
              expected_val = ('(list indicating correct minimum number of neurons '
                              + 'per layer)'),
              name = nn_grid_getargs)
