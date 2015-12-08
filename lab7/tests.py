from tester import make_test, get_tests

from math import log as ln
INF = float('inf')

def approx_equal(a, b, epsilon=0.00000001):
    return abs(a-b) <= epsilon

def dict_approx_equal(dict1, dict2, epsilon=0.00000001):
    """Returns True if two dicts have the same keys and approximately equal
    values, otherwise False"""
    return (set(dict1.keys()) == set(dict2.keys())
            and all([approx_equal(dict1[key], dict2[key], epsilon)
                     for key in dict1.keys()]))

def classifier_approx_equal(H1, H2, epsilon=0.00000001):
  return (len(H1) == len(H2) and \
    all([H1[i][0] == H2[i][0] and \
      approx_equal(H1[i][1], H2[i][1], epsilon) for i in range(len(H1))]))


def initialize_2_getargs() :  #TEST 1
    return [["PointA"]]
initialize_2_expected = {"PointA":1.0}
def initialize_2_testanswer(val, original_val = None) :
    return val == initialize_2_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = initialize_2_getargs,
          testanswer = initialize_2_testanswer,
          expected_val = str(initialize_2_expected),
          name = 'initialize_weights')

def initialize_3_getargs() :  #TEST 2
    return [["-6","-5","-4","-3","-2","-1","0","1","2","3","4","5"]]
initialize_3_expected = {"-6":1.0/12.0,"-5":1.0/12.0,"-4":1.0/12.0,"-3":1.0/12.0,"-2":1.0/12.0,"-1":1.0/12.0,"0":1.0/12.0,"1":1.0/12.0,"2":1.0/12.0,"3":1.0/12.0,"4":1.0/12.0,"5":1.0/12.0}
def initialize_3_testanswer(val, original_val = None) :
    return val == initialize_3_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = initialize_3_getargs,
          testanswer = initialize_3_testanswer,
          expected_val = str(initialize_3_expected),
          name = 'initialize_weights')


# TEST 0 FOR CALCULATE_ERROR_RATE - ALL POINTS CORRECTLY CLASSIFIED
# only one classifier
def calculate_error_rates_0_getargs() :  #TEST 3
    return [{"0" : 1.0/4, "1": 1.0/4, "2": 1.0/4, "3": 1.0/4}, {"classifier_0":[]}]
calculate_error_rates_0_expected = {"classifier_0" : 0}
def calculate_error_rates_0_testanswer(val, original_val = None) :
    return val == calculate_error_rates_0_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = calculate_error_rates_0_getargs,
          testanswer = calculate_error_rates_0_testanswer,
          expected_val = str(calculate_error_rates_0_expected),
          name = 'calculate_error_rates')

# TEST 2 FOR CALCULATE_ERROR_RATE - SOME POINTS MISCLASSIFIED
def calculate_error_rates_2_getargs() :  #TEST 4
    return [{"0" : 1.0/8, "1": 1.0/8, "2": 1.0/8, "3": 1.0/8, "4": 1.0/2}, {"classifier_0":["0", "1", "4"], "classifier_1":["0", "1", "2", "3"]}]
calculate_error_rates_2_expected = {"classifier_0" : 3.0/4, "classifier_1": 1.0/2}
def calculate_error_rates_2_testanswer(val, original_val = None) :
    return val == calculate_error_rates_2_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = calculate_error_rates_2_getargs,
          testanswer = calculate_error_rates_2_testanswer,
          expected_val = str(calculate_error_rates_2_expected),
          name = 'calculate_error_rates')


def pick_best_classifier_0_getargs() :  #TEST 5
    #have a perfect test!
    classifier_to_error_rate = {}
    classifier_to_error_rate["classifier_0"] = 0
    classifier_to_error_rate["classifier_0.1"] = 0.1
    classifier_to_error_rate["classifier_0.5"] = 0.5
    classifier_to_error_rate["classifier_0.9"] = 0.9
    return [classifier_to_error_rate]

pick_best_classifier_0_expected = "classifier_0"

def pick_best_classifier_0_testanswer(val, original_val = None) :
    return val == pick_best_classifier_0_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = pick_best_classifier_0_getargs,
          testanswer = pick_best_classifier_0_testanswer,
          expected_val = str(pick_best_classifier_0_expected),
          name = 'pick_best_classifier')

def pick_best_classifier_1_getargs() :  #TEST 6
    #have a pretty good test
    classifier_to_error_rate = {}
    classifier_to_error_rate["classifier_0.1"] = 0.1
    classifier_to_error_rate["classifier_0.5"] = 0.5
    classifier_to_error_rate["classifier_0.9"] = 0.9
    return [classifier_to_error_rate]

pick_best_classifier_1_expected = "classifier_0.1"

def pick_best_classifier_1_testanswer(val, original_val = None) :
    return val == pick_best_classifier_1_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = pick_best_classifier_1_getargs,
          testanswer = pick_best_classifier_1_testanswer,
          expected_val = str(pick_best_classifier_1_expected),
          name = 'pick_best_classifier')

def pick_best_classifier_2_getargs() :  #TEST 7
    #have no good tests
    classifier_to_error_rate = {}
    classifier_to_error_rate["classifier_0.5"] = 0.5
    classifier_to_error_rate["classifier_0.6"] = 0.6
    classifier_to_error_rate["classifier_0.9"] = 0.9
    return [classifier_to_error_rate]

pick_best_classifier_2_expected = "classifier_0.5"

def pick_best_classifier_2_testanswer(val, original_val = None) :
    return val == pick_best_classifier_2_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = pick_best_classifier_2_getargs,
          testanswer = pick_best_classifier_2_testanswer,
          expected_val = str(pick_best_classifier_2_expected),
          name = 'pick_best_classifier')


def pick_best_classifier_4_getargs() :  #TEST 8
    #have perfectly wrong test
    classifier_to_error_rate = {}
    classifier_to_error_rate["classifier_0.1"] = 0.1
    classifier_to_error_rate["classifier_0.6"] = 0.6
    classifier_to_error_rate["classifier_0.9"] = 0.9
    classifier_to_error_rate["classifier_1"] = 1
    return [classifier_to_error_rate, False]

pick_best_classifier_4_expected = "classifier_1"

def pick_best_classifier_4_testanswer(val, original_val = None) :
    return val == pick_best_classifier_4_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = pick_best_classifier_4_getargs,
          testanswer = pick_best_classifier_4_testanswer,
          expected_val = str(pick_best_classifier_4_expected),
          name = 'pick_best_classifier')

#check tie-breaking
def pick_best_classifier_5_getargs() :  #TEST 9
    return [dict(B=0.3, A=0.4, C=0.3)]
pick_best_classifier_5_expected = "B"
def pick_best_classifier_5_testanswer(val, original_val = None) :
    return val == pick_best_classifier_5_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = pick_best_classifier_5_getargs,
          testanswer = pick_best_classifier_5_testanswer,
          expected_val = str(pick_best_classifier_5_expected) \
              +' (Hint: This test checks tie-breaking.)',
          name = 'pick_best_classifier')

#check roundoff error
def pick_best_classifier_6_getargs() :  #TEST 10
    return [dict(cl_1=2./3, cl_2=1./3), False]
pick_best_classifier_6_expected = "cl_1"
def pick_best_classifier_6_testanswer(val, original_val = None) :
    return val == pick_best_classifier_6_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = pick_best_classifier_6_getargs,
          testanswer = pick_best_classifier_6_testanswer,
          expected_val = str(pick_best_classifier_6_expected) \
              +' (Hint: This test checks roundoff error. See wiki for details.)',
          name = 'pick_best_classifier')


def calculate_voting_power_0_getargs() :  #TEST 11
    return [.001]
calculate_voting_power_0_expected = 3.453377389324277
def calculate_voting_power_0_testanswer(val, original_val = None) :
    return approx_equal(val, calculate_voting_power_0_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = calculate_voting_power_0_getargs,
          testanswer = calculate_voting_power_0_testanswer,
          expected_val = str(calculate_voting_power_0_expected),
          name = 'calculate_voting_power')


def calculate_voting_power_3_getargs() :  #TEST 12
    return [.3]
calculate_voting_power_3_expected = 0.42364893019360184
def calculate_voting_power_3_testanswer(val, original_val = None) :
    return approx_equal(val, calculate_voting_power_3_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = calculate_voting_power_3_getargs,
          testanswer = calculate_voting_power_3_testanswer,
          expected_val = str(calculate_voting_power_3_expected),
          name = 'calculate_voting_power')

def calculate_voting_power_4_getargs() :  #TEST 13
    return [.7]
calculate_voting_power_4_expected = -0.4236489301936017
def calculate_voting_power_4_testanswer(val, original_val = None) :
    return approx_equal(val, calculate_voting_power_4_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = calculate_voting_power_4_getargs,
          testanswer = calculate_voting_power_4_testanswer,
          expected_val = str(calculate_voting_power_4_expected),
          name = 'calculate_voting_power')

#perfect classifier -> INF
def calculate_voting_power_5_getargs() :  #TEST 14
    return [0]
calculate_voting_power_5_expected = INF
def calculate_voting_power_5_testanswer(val, original_val = None) :
    return val == calculate_voting_power_5_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = calculate_voting_power_5_getargs,
          testanswer = calculate_voting_power_5_testanswer,
          expected_val = str(calculate_voting_power_5_expected),
          name = 'calculate_voting_power')

#perfectly wrong classifier -> -INF
def calculate_voting_power_6_getargs() :  #TEST 15
    return [1]
calculate_voting_power_6_expected = -INF
def calculate_voting_power_6_testanswer(val, original_val = None) :
    return val == calculate_voting_power_6_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = calculate_voting_power_6_getargs,
          testanswer = calculate_voting_power_6_testanswer,
          expected_val = str(calculate_voting_power_6_expected),
          name = 'calculate_voting_power')


def is_good_enough_0_getargs() :  #TEST 16
    return [[("h1", 1)], ['A','B'], {'h1':['A','B'],'h2':['A']}, 1]
is_good_enough_0_expected = False
def is_good_enough_0_testanswer(val, original_val = None) :
    return val == is_good_enough_0_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = is_good_enough_0_getargs,
          testanswer = is_good_enough_0_testanswer,
          expected_val = str(is_good_enough_0_expected),
          name = 'is_good_enough')

#All classifiers included in H
#h with voting power of 0
#H misclassifies A = mistake_tolerance
def is_good_enough_1_getargs() :  #TEST 17
    return [[("h1", 1),("h2", 0)], ['A','B'], {'h1': ['A'], 'h2': ['B']}, 1]
is_good_enough_1_expected = True
def is_good_enough_1_testanswer(val, original_val = None) :
    return val == is_good_enough_1_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = is_good_enough_1_getargs,
          testanswer = is_good_enough_1_testanswer,
          expected_val = str(is_good_enough_1_expected),
          name = 'is_good_enough')

# Not all points misclassified by any classifier
# H misclassifies A & B > mistake tolerance
def is_good_enough_2_getargs() :  #TEST 18
    return [[("h1", .5),("h2", .3),("h3", .76)], ['A','B','C','D'],
             {'h1': ['A'], 'h2': ['A','B'], 'h3': ['B','C']}, 1]
is_good_enough_2_expected = False
def is_good_enough_2_testanswer(val, original_val = None) :
    return val == is_good_enough_2_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = is_good_enough_2_getargs,
          testanswer = is_good_enough_2_testanswer,
          expected_val = str(is_good_enough_2_expected),
          name = 'is_good_enough')

#No points misclassified by h3
#H misclassifies C = mistake_tolerance
def is_good_enough_3_getargs() :  #TEST 19
    return [[("h1", .5),("h2", -.3),("h3", .76)], ['A','B','C'],
             {'h1': ['A','C'], 'h2': ['A','B'], 'h3': []}, 1]
is_good_enough_3_expected = True
def is_good_enough_3_testanswer(val, original_val = None) :
    return val == is_good_enough_3_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = is_good_enough_3_getargs,
          testanswer = is_good_enough_3_testanswer,
          expected_val = str(is_good_enough_3_expected),
          name = 'is_good_enough')

#All negative voting powers
#H misclassifies A,B,D> mistake_tolerance
def is_good_enough_4_getargs() :  #TEST 20
    return [[("h1", -.5),("h2", -.3),("h3", -.45)], ['A','B','C','D'],
             {'h1': ['A','C'], 'h2': ['B','C'], 'h3': ['D']}, 2]
is_good_enough_4_expected = False
def is_good_enough_4_testanswer(val, original_val = None) :
    return val == is_good_enough_4_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = is_good_enough_4_getargs,
          testanswer = is_good_enough_4_testanswer,
          expected_val = str(is_good_enough_4_expected),
          name = 'is_good_enough')

#misclassified training point is not listed in misclassifications
#same classifier used multiple times
def is_good_enough_5_getargs() :  #TEST 21
    return [[("h1", -0.549),("h2", 0.347),("h1", -0.255)], list('ABCD'),
             dict(h1=list('ABC'), h2=list('AC'), h3=list('BC')), 0]
is_good_enough_5_expected = False
def is_good_enough_5_testanswer(val, original_val = None) :
    return val == is_good_enough_5_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = is_good_enough_5_getargs,
          testanswer = is_good_enough_5_testanswer,
          expected_val = str(is_good_enough_5_expected) \
              +' (Hint: What happens if a training point is misclassified by ' \
              +'H, but not misclassified by any weak classifier?)',
          name = 'is_good_enough')

#one point misclassified, vote is a tie
# (No, this particular situation would not happen in Adaboost.)
def is_good_enough_6_getargs() :  #TEST 22
    return [[("h1", 0.5), ("h2", 0.5)], ['A','B'],
             {'h1': ['A'], 'h2': []}, 0]
is_good_enough_6_expected = False
def is_good_enough_6_testanswer(val, original_val = None) :
    return val == is_good_enough_6_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = is_good_enough_6_getargs,
          testanswer = is_good_enough_6_testanswer,
          expected_val = str(is_good_enough_6_expected) \
              +' (Hint: This test checks what happens when the vote is a tie.)',
          name = 'is_good_enough')

#violates triangle sum property
def is_good_enough_7_getargs() :  #TEST 23
    return [[("h1", 0.5), ("h2", 0.2), ("h3", 0.2)], list('ABCD'),
             {'h1': ['A'], 'h2': ['B'], 'h3': ['C']}, 0]
is_good_enough_7_expected = False
def is_good_enough_7_testanswer(val, original_val = None) :
    return val == is_good_enough_7_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = is_good_enough_7_getargs,
          testanswer = is_good_enough_7_testanswer,
          expected_val = str(is_good_enough_7_expected) \
              +" (Hint: Make sure you're summing voting powers, not just "
              +'counting classifiers.)',
          name = 'is_good_enough')


def update_weights_0_getargs() :  #TEST 24
    return [{'A':1/6., 'B':1/6., 'C':1/6., 'D':1/6., 'E':1/6., 'F': 1/6.}, ['A', 'B'], 2/6.]
update_weights_0_expected = {'A':1/4., 'B':1/4., 'C':1/8., 'D':1/8., 'E':1/8., 'F':1/8.}
def update_weights_0_testanswer(val, original_val = None) :
    return dict_approx_equal(val, update_weights_0_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = update_weights_0_getargs,
          testanswer = update_weights_0_testanswer,
          expected_val = str(update_weights_0_expected),
          name = 'update_weights')

def update_weights_2_getargs() :  #TEST 25
    return [{'A':1/2., 'B':1/2.}, [], 0]
update_weights_2_expected = {'A':1/4., 'B':1/4.}
def update_weights_2_testanswer(val, original_val = None) :
    return dict_approx_equal(val, update_weights_2_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = update_weights_2_getargs,
          testanswer = update_weights_2_testanswer,
          expected_val = str(update_weights_2_expected),
          name = 'update_weights')

def update_weights_3_getargs() :  #TEST 26
    return [{'A':1/2., 'B':1/2.}, ['A', 'B'], 1]
update_weights_3_expected = {'A':1/4., 'B':1/4.}
def update_weights_3_testanswer(val, original_val = None) :
    return dict_approx_equal(val, update_weights_3_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = update_weights_3_getargs,
          testanswer = update_weights_3_testanswer,
          expected_val = str(update_weights_3_expected),
          name = 'update_weights')


#recitation problem, from 2012 Quiz 4
boost_2012_tr_pts = ["A","B","C","D","E"]
boost_2012_cl_to_miscl = {"<2":["B","E"], "<4":["C","B","E"], "<6":["C"],
                          ">2":["A","C","D"], ">4":["A","D"],
                          ">6":["A","B","D","E"]}

#1 round
def adaboost_0_getargs() :  #TEST 27
    return [boost_2012_tr_pts, boost_2012_cl_to_miscl, True, 0, 1]
adaboost_0_expected = [("<6",.5*ln(4))]
def adaboost_0_testanswer(val, original_val = None) :
    return classifier_approx_equal(val, adaboost_0_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = adaboost_0_getargs,
          testanswer = adaboost_0_testanswer,
          expected_val = str(adaboost_0_expected),
          name = 'adaboost')

#2 rounds
def adaboost_1_getargs() :  #TEST 28
    return [boost_2012_tr_pts, boost_2012_cl_to_miscl, True, 0, 2]
adaboost_1_expected = [("<6",.5*ln(4)), ("<2", .5*ln(3))]
def adaboost_1_testanswer(val, original_val = None) :
    return classifier_approx_equal(val, adaboost_1_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = adaboost_1_getargs,
          testanswer = adaboost_1_testanswer,
          expected_val = str(adaboost_1_expected),
          name = 'adaboost')

#3 rounds
def adaboost_2_getargs() :  #TEST 29
    return [boost_2012_tr_pts, boost_2012_cl_to_miscl, True, 0, 3]
adaboost_2_expected = [("<6",.5*ln(4)), ("<2", .5*ln(3)), (">4",.5*ln(5))]
def adaboost_2_testanswer(val, original_val = None) :
    return classifier_approx_equal(val, adaboost_2_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = adaboost_2_getargs,
          testanswer = adaboost_2_testanswer,
          expected_val = str(adaboost_2_expected),
          name = 'adaboost')

#4 rounds (stops after 3)
def adaboost_3_getargs() :  #TEST 30
    return [boost_2012_tr_pts, boost_2012_cl_to_miscl, True, 0, 4]
adaboost_3_expected = [("<6",.5*ln(4)), ("<2", .5*ln(3)), (">4",.5*ln(5))]
def adaboost_3_testanswer(val, original_val = None) :
    return classifier_approx_equal(val, adaboost_3_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = adaboost_3_getargs,
          testanswer = adaboost_3_testanswer,
          expected_val = str(adaboost_3_expected),
          name = 'adaboost')

#INF rounds (stops after 3)
def adaboost_4_getargs() :  #TEST 31
    return [boost_2012_tr_pts, boost_2012_cl_to_miscl, True, 0, INF]
adaboost_4_expected = [("<6",.5*ln(4)), ("<2", .5*ln(3)), (">4",.5*ln(5))]
def adaboost_4_testanswer(val, original_val = None) :
    return classifier_approx_equal(val, adaboost_4_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = adaboost_4_getargs,
          testanswer = adaboost_4_testanswer,
          expected_val = str(adaboost_4_expected),
          name = 'adaboost')

#4 rounds (stops after 3); use error furthest from 1/2
def adaboost_5_getargs() :  #TEST 32
    return [boost_2012_tr_pts, boost_2012_cl_to_miscl, False, 0, 4]
adaboost_5_expected = [("<6",.5*ln(4)), ("<2", .5*ln(3)), ("<4",-.5*ln(5))]
def adaboost_5_testanswer(val, original_val = None) :
    return classifier_approx_equal(val, adaboost_5_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = adaboost_5_getargs,
          testanswer = adaboost_5_testanswer,
          expected_val = str(adaboost_5_expected),
          name = 'adaboost')

#allow 1 misclassification; stops after 1 round
def adaboost_6_getargs() :  #TEST 33
    return [boost_2012_tr_pts, boost_2012_cl_to_miscl, True, 1, 4]
adaboost_6_expected = [("<6",.5*ln(4))]
def adaboost_6_testanswer(val, original_val = None) :
    return classifier_approx_equal(val, adaboost_6_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = adaboost_6_getargs,
          testanswer = adaboost_6_testanswer,
          expected_val = str(adaboost_6_expected),
          name = 'adaboost')

#toy problem: exits after 1 round with all error rates = 1/2
def adaboost_7_getargs() :  #TEST 34
    return [list('XYZ'), {'cl_1':['Z'], 'cl_2':['X','Y']}, True, 0, 3]
adaboost_7_expected = [('cl_1', 0.5*ln(2))]
def adaboost_7_testanswer(val, original_val = None) :
    return classifier_approx_equal(val, adaboost_7_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = adaboost_7_getargs,
          testanswer = adaboost_7_testanswer,
          expected_val = str(adaboost_7_expected) \
              + ' (Hint: What should happen when the best error rate is 1/2?)',
          name = 'adaboost')

boost_toy1_tr_pts = list('ABCD')
boost_toy1_cl_to_miscl = {'h1':['A'], 'h2':list('BCD'), 'h3':list('ABC')}

#toy problem: exits after 1 round with smallest error rate = 1/2
def adaboost_8_getargs() :  #TEST 35
    return [boost_toy1_tr_pts, boost_toy1_cl_to_miscl, True, 0, 4]
adaboost_8_expected = [('h1', 0.5*ln(3))]
def adaboost_8_testanswer(val, original_val = None) :
    return classifier_approx_equal(val, adaboost_8_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = adaboost_8_getargs,
          testanswer = adaboost_8_testanswer,
          expected_val = str(adaboost_8_expected),
          name = 'adaboost')

#toy problem: has smallest error rate = 1/2 after 1 round, but continues
def adaboost_9_getargs() :  #TEST 36
    return [boost_toy1_tr_pts, boost_toy1_cl_to_miscl, False, 0, 2]
adaboost_9_expected = [('h1', 0.5*ln(3)), ('h3', -0.5*ln(5))]
def adaboost_9_testanswer(val, original_val = None) :
    return classifier_approx_equal(val, adaboost_9_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = adaboost_9_getargs,
          testanswer = adaboost_9_testanswer,
          expected_val = str(adaboost_9_expected),
          name = 'adaboost')

#picks same classifier multiple times
def adaboost_91_getargs() :  #TEST 37
    return [boost_toy1_tr_pts, boost_toy1_cl_to_miscl, False, 0, 4]
adaboost_91_expected = [('h1', 0.5*ln(3)), ('h3', -0.5*ln(5)),
                       ('h1', 0.5*ln(7./3)), ('h3', -0.5*ln(9./5))]
def adaboost_91_testanswer(val, original_val = None) :
    return classifier_approx_equal(val, adaboost_91_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = adaboost_91_getargs,
          testanswer = adaboost_91_testanswer,
          expected_val = str(adaboost_91_expected),
          name = 'adaboost')

#tolerance > 1 but continues multiple rounds; exits with error_rate=0.5
def adaboost_92_getargs() :  #TEST 38
    return [list('ABCDEFG'),
            dict(h1=list('ABC'), h2=list('ABD'), h3=list('ABE')),
            True, 2, 5]
adaboost_92_expected = [('h1', 0.1438410362258895), ('h2', 0.08352704233158378),
                        ('h3', 0.041982690058667164)]
def adaboost_92_testanswer(val, original_val = None) :
    return classifier_approx_equal(val, adaboost_92_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = adaboost_92_getargs,
          testanswer = adaboost_92_testanswer,
          expected_val = str(adaboost_92_expected) \
              + ' (Hint: If Adaboost does not exit when the best error rate '\
              + 'is 0.5, you may want to use fix_roundoff_error.)',
          name = 'adaboost')
