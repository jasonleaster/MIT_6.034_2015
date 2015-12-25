from tester import make_test, get_tests
from nets import *

def get_descendants_0_getargs() :
    return [net_basic, 'A']
get_descendants_0_expected = set('C')
def get_descendants_0_testanswer(val, original_val = None) :
    return val == get_descendants_0_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = get_descendants_0_getargs,
          testanswer = get_descendants_0_testanswer,
          expected_val = str(get_descendants_0_expected),
          name = 'get_descendants')

def get_descendants_1_getargs() :
    return [net_dsep, 'D']
get_descendants_1_expected = set('FG')
def get_descendants_1_testanswer(val, original_val = None) :
    return val == get_descendants_1_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = get_descendants_1_getargs,
          testanswer = get_descendants_1_testanswer,
          expected_val = str(get_descendants_1_expected),
          name = 'get_descendants')

def get_descendants_2_getargs() :
    return [net_dsep, 'B']
get_descendants_2_expected = set('CDEFG')
def get_descendants_2_testanswer(val, original_val = None) :
    return val == get_descendants_2_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = get_descendants_2_getargs,
          testanswer = get_descendants_2_testanswer,
          expected_val = str(get_descendants_2_expected),
          name = 'get_descendants')

def get_descendants_3_getargs() :
    return [net_dsep, 'E']
get_descendants_3_expected = set()
def get_descendants_3_testanswer(val, original_val = None) :
    return val == get_descendants_3_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = get_descendants_3_getargs,
          testanswer = get_descendants_3_testanswer,
          expected_val = str(get_descendants_3_expected),
          name = 'get_descendants')

def get_descendants_4_getargs() :
    return [net_disjoint, 'A']
get_descendants_4_expected = set()
def get_descendants_4_testanswer(val, original_val = None) :
    return val == get_descendants_4_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = get_descendants_4_getargs,
          testanswer = get_descendants_4_testanswer,
          expected_val = str(get_descendants_4_expected),
          name = 'get_descendants')


def get_nondescendants_0_getargs() :
    return [net_basic, 'A']
get_nondescendants_0_expected = set('B')
def get_nondescendants_0_testanswer(val, original_val = None) :
    return val == get_nondescendants_0_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = get_nondescendants_0_getargs,
          testanswer = get_nondescendants_0_testanswer,
          expected_val = str(get_nondescendants_0_expected),
          name = 'get_nondescendants')

def get_nondescendants_1_getargs() :
    return [net_basic, 'C']
get_nondescendants_1_expected = set('AB')
def get_nondescendants_1_testanswer(val, original_val = None) :
    return val == get_nondescendants_1_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = get_nondescendants_1_getargs,
          testanswer = get_nondescendants_1_testanswer,
          expected_val = str(get_nondescendants_1_expected),
          name = 'get_nondescendants')

def get_nondescendants_2_getargs() :
    return [net_dsep, 'F']
get_nondescendants_2_expected = set('ABCDE')
def get_nondescendants_2_testanswer(val, original_val = None) :
    return val == get_nondescendants_2_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = get_nondescendants_2_getargs,
          testanswer = get_nondescendants_2_testanswer,
          expected_val = str(get_nondescendants_2_expected),
          name = 'get_nondescendants')

def get_nondescendants_3_getargs() :
    return [net_dsep, 'E']
get_nondescendants_3_expected = set('ABCDFG')
def get_nondescendants_3_testanswer(val, original_val = None) :
    return val == get_nondescendants_3_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = get_nondescendants_3_getargs,
          testanswer = get_nondescendants_3_testanswer,
          expected_val = str(get_nondescendants_3_expected),
          name = 'get_nondescendants')

def get_nondescendants_4_getargs() :
    return [net_dsep, 'D']
get_nondescendants_4_expected = set('ABCE')
def get_nondescendants_4_testanswer(val, original_val = None) :
    return val == get_nondescendants_4_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = get_nondescendants_4_getargs,
          testanswer = get_nondescendants_4_testanswer,
          expected_val = str(get_nondescendants_4_expected),
          name = 'get_nondescendants')

def get_nondescendants_5_getargs() :
    return [net_disjoint, 'A']
get_nondescendants_5_expected = set('B')
def get_nondescendants_5_testanswer(val, original_val = None) :
    return val == get_nondescendants_5_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = get_nondescendants_5_getargs,
          testanswer = get_nondescendants_5_testanswer,
          expected_val = str(get_nondescendants_5_expected),
          name = 'get_nondescendants')


def remove_nondescendants_0_getargs() :
    return [net_dsep, 'F', dict(D=True, E=False, G=True, C=True, A=False)]
remove_nondescendants_0_expected = dict(D=True, G=True)
def remove_nondescendants_0_testanswer(val, original_val = None) :
    return val == remove_nondescendants_0_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = remove_nondescendants_0_getargs,
          testanswer = remove_nondescendants_0_testanswer,
          expected_val = str(remove_nondescendants_0_expected),
          name = 'remove_nondescendants_given_parents')

def remove_nondescendants_1_getargs() :
    return [net_dsep, 'F', dict(E=False, G=True, C=True)]
remove_nondescendants_1_expected = False
def remove_nondescendants_1_testanswer(val, original_val = None) :
    return val == remove_nondescendants_1_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = remove_nondescendants_1_getargs,
          testanswer = remove_nondescendants_1_testanswer,
          expected_val = str(remove_nondescendants_1_expected),
          name = 'remove_nondescendants_given_parents')

def remove_nondescendants_2_getargs() :
    return [net_dsep, 'C', dict(A=True, E=False, G=True, D=True)]
remove_nondescendants_2_expected = False
def remove_nondescendants_2_testanswer(val, original_val = None) :
    return val == remove_nondescendants_2_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = remove_nondescendants_2_getargs,
          testanswer = remove_nondescendants_2_testanswer,
          expected_val = str(remove_nondescendants_2_expected),
          name = 'remove_nondescendants_given_parents')

def remove_nondescendants_3_getargs() :
    return [net_dsep, 'C', dict(A=True, E=False, G=True, B=False, D=True)]
remove_nondescendants_3_expected = dict(A=True, E=False, G=True, B=False, D=True)
def remove_nondescendants_3_testanswer(val, original_val = None) :
    return val == remove_nondescendants_3_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = remove_nondescendants_3_getargs,
          testanswer = remove_nondescendants_3_testanswer,
          expected_val = str(remove_nondescendants_3_expected),
          name = 'remove_nondescendants_given_parents')


def probability_lookup_0_getargs() :
    return [net_racoon, {'B':True}]
probability_lookup_0_expected = 0.1
def probability_lookup_0_testanswer(val, original_val = None) :
    return approx_equal(val, probability_lookup_0_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_lookup_0_getargs,
          testanswer = probability_lookup_0_testanswer,
          expected_val = str(probability_lookup_0_expected),
          name = 'probability_lookup')

def probability_lookup_1_getargs() :
    return [net_racoon, {'D':True}, {'B':True, 'R':False}]
probability_lookup_1_expected = 0.8
def probability_lookup_1_testanswer(val, original_val = None) :
    return approx_equal(val, probability_lookup_1_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_lookup_1_getargs,
          testanswer = probability_lookup_1_testanswer,
          expected_val = str(probability_lookup_1_expected),
          name = 'probability_lookup')

#implicitly uses infer_missing
def probability_lookup_2_getargs() :
    return [net_racoon, {'D':False}, {'B':True, 'R':False}]
probability_lookup_2_expected = 0.2
def probability_lookup_2_testanswer(val, original_val = None) :
    return approx_equal(val, probability_lookup_2_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_lookup_2_getargs,
          testanswer = probability_lookup_2_testanswer,
          expected_val = str(probability_lookup_2_expected),
          name = 'probability_lookup')

def probability_lookup_3_getargs() :
    return [net_racoon, {'D':True}, {'B':True}]
probability_lookup_3_expected = None
def probability_lookup_3_testanswer(val, original_val = None) :
    return val == probability_lookup_3_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_lookup_3_getargs,
          testanswer = probability_lookup_3_testanswer,
          expected_val = str(probability_lookup_3_expected),
          name = 'probability_lookup')

#requires remove_nondescendants
def probability_lookup_4_getargs() :
    return [net_racoon, {'D':False}, {'B':True, 'R':False, 'T':True}]
probability_lookup_4_expected = 0.2
def probability_lookup_4_testanswer(val, original_val = None) :
    return approx_equal(val, probability_lookup_4_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_lookup_4_getargs,
          testanswer = probability_lookup_4_testanswer,
          expected_val = str(probability_lookup_4_expected),
          name = 'probability_lookup')


def probability_joint_0_getargs() :
    return [net_racoon, {v:True for v in 'BRDTC'}]
probability_joint_0_expected = 0.0288
def probability_joint_0_testanswer(val, original_val = None) :
    return approx_equal(val, probability_joint_0_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_joint_0_getargs,
          testanswer = probability_joint_0_testanswer,
          expected_val = str(probability_joint_0_expected),
          name = 'probability_joint')

def probability_joint_1_getargs() :
    return [net_racoon, {v:False for v in 'BRDTC'}]
probability_joint_1_expected = 0.43663455
def probability_joint_1_testanswer(val, original_val = None) :
    return approx_equal(val, probability_joint_1_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_joint_1_getargs,
          testanswer = probability_joint_1_testanswer,
          expected_val = str(probability_joint_1_expected),
          name = 'probability_joint')

def probability_joint_2_getargs() :
    return [net_racoon, dict(B=False, R=False, D=True, T=False, C=True)]
probability_joint_2_expected = 0.003564
def probability_joint_2_testanswer(val, original_val = None) :
    return approx_equal(val, probability_joint_2_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_joint_2_getargs,
          testanswer = probability_joint_2_testanswer,
          expected_val = str(probability_joint_2_expected),
          name = 'probability_joint')


def probability_marginal_0_getargs() :
    return [net_racoon, {'B':False}]
probability_marginal_0_expected = 0.9
def probability_marginal_0_testanswer(val, original_val = None) :
    return approx_equal(val, probability_marginal_0_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_marginal_0_getargs,
          testanswer = probability_marginal_0_testanswer,
          expected_val = str(probability_marginal_0_expected),
          name = 'probability_marginal')

def probability_marginal_1_getargs() :
    return [net_racoon, {'D':False}]
probability_marginal_1_expected = 0.6405
def probability_marginal_1_testanswer(val, original_val = None) :
    return approx_equal(val, probability_marginal_1_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_marginal_1_getargs,
          testanswer = probability_marginal_1_testanswer,
          expected_val = str(probability_marginal_1_expected),
          name = 'probability_marginal')

def probability_marginal_2_getargs() :
    return [net_racoon, {'T':True, 'C':False}]
probability_marginal_2_expected = 0.20151845
def probability_marginal_2_testanswer(val, original_val = None) :
    return approx_equal(val, probability_marginal_2_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_marginal_2_getargs,
          testanswer = probability_marginal_2_testanswer,
          expected_val = str(probability_marginal_2_expected),
          name = 'probability_marginal')

def probability_marginal_3_getargs() :
    return [net_racoon, dict(B=False, R=False, D=True, T=False, C=True)]
probability_marginal_3_expected = 0.003564
def probability_marginal_3_testanswer(val, original_val = None) :
    return approx_equal(val, probability_marginal_3_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_marginal_3_getargs,
          testanswer = probability_marginal_3_testanswer,
          expected_val = str(probability_marginal_3_expected),
          name = 'probability_marginal')


def probability_conditional_0_getargs() :
    return [net_racoon, {'D':True}, dict(B=True, R=False, T=False)]
probability_conditional_0_expected = 0.8
def probability_conditional_0_testanswer(val, original_val = None) :
    return approx_equal(val, probability_conditional_0_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_conditional_0_getargs,
          testanswer = probability_conditional_0_testanswer,
          expected_val = str(probability_conditional_0_expected),
          name = 'probability_conditional')

def probability_conditional_1_getargs() :
    return [net_racoon, {'B':True, 'R':True}, {'D':False, 'T':False}]
probability_conditional_1_expected = 0.001/0.487945
def probability_conditional_1_testanswer(val, original_val = None) :
    return approx_equal(val, probability_conditional_1_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_conditional_1_getargs,
          testanswer = probability_conditional_1_testanswer,
          expected_val = str(probability_conditional_1_expected),
          name = 'probability_conditional')

#just calls probability_lookup
def probability_conditional_2_getargs() :
    return [net_racoon, {'D':False}, {'B':True, 'R':False}]
probability_conditional_2_expected = 0.2
def probability_conditional_2_testanswer(val, original_val = None) :
    return approx_equal(val, probability_conditional_2_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_conditional_2_getargs,
          testanswer = probability_conditional_2_testanswer,
          expected_val = str(probability_conditional_2_expected),
          name = 'probability_conditional')

#no givens; just calls probability_marginal
def probability_conditional_3_getargs() :
    return [net_racoon, dict(B=False, R=False, D=True, T=False, C=True)]
probability_conditional_3_expected = 0.003564
def probability_conditional_3_testanswer(val, original_val = None) :
    return approx_equal(val, probability_conditional_3_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_conditional_3_getargs,
          testanswer = probability_conditional_3_testanswer,
          expected_val = str(probability_conditional_3_expected),
          name = 'probability_conditional')


def probability_0_getargs() :
    return [net_racoon, {'B':False}]
probability_0_expected = 0.9
def probability_0_testanswer(val, original_val = None) :
    return approx_equal(val, probability_0_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_0_getargs,
          testanswer = probability_0_testanswer,
          expected_val = str(probability_0_expected),
          name = 'probability')

def probability_1_getargs() :
    return [net_racoon, {'D':True}, dict(B=True, R=False, T=False)]
probability_1_expected = 0.8
def probability_1_testanswer(val, original_val = None) :
    return approx_equal(val, probability_1_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_1_getargs,
          testanswer = probability_1_testanswer,
          expected_val = str(probability_1_expected),
          name = 'probability')

def probability_2_getargs() :
    return [net_racoon, {'D':False}]
probability_2_expected = 0.6405
def probability_2_testanswer(val, original_val = None) :
    return approx_equal(val, probability_2_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_2_getargs,
          testanswer = probability_2_testanswer,
          expected_val = str(probability_2_expected),
          name = 'probability')

def probability_3_getargs() :
    return [net_racoon, {'T':True, 'C':False}]
probability_3_expected = 0.20151845
def probability_3_testanswer(val, original_val = None) :
    return approx_equal(val, probability_3_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_3_getargs,
          testanswer = probability_3_testanswer,
          expected_val = str(probability_3_expected),
          name = 'probability')

def probability_4_getargs() :
    return [net_racoon, {'B':True, 'R':True}, {'D':False, 'T':False}]
probability_4_expected = 0.001/0.487945
def probability_4_testanswer(val, original_val = None) :
    return approx_equal(val, probability_4_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_4_getargs,
          testanswer = probability_4_testanswer,
          expected_val = str(probability_4_expected),
          name = 'probability')

def probability_5_getargs() :
    return [net_racoon, {v:False for v in 'BRDTC'}]
probability_5_expected = 0.43663455
def probability_5_testanswer(val, original_val = None) :
    return approx_equal(val, probability_5_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_5_getargs,
          testanswer = probability_5_testanswer,
          expected_val = str(probability_5_expected),
          name = 'probability')

def probability_6_getargs() :
    return [net_racoon, dict(B=False, R=False, D=True, T=False, C=True)]
probability_6_expected = 0.003564
def probability_6_testanswer(val, original_val = None) :
    return approx_equal(val, probability_6_expected)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = probability_6_getargs,
          testanswer = probability_6_testanswer,
          expected_val = str(probability_6_expected),
          name = 'probability')


def number_of_parameters_0_getargs() :
    return [net_basic]
number_of_parameters_0_expected = 6
def number_of_parameters_0_testanswer(val, original_val = None) :
    return val == number_of_parameters_0_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = number_of_parameters_0_getargs,
          testanswer = number_of_parameters_0_testanswer,
          expected_val = str(number_of_parameters_0_expected),
          name = 'number_of_parameters')

def number_of_parameters_1_getargs() :
    return [net_racoon_no_probs]
number_of_parameters_1_expected = 10
def number_of_parameters_1_testanswer(val, original_val = None) :
    return val == number_of_parameters_1_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = number_of_parameters_1_getargs,
          testanswer = number_of_parameters_1_testanswer,
          expected_val = str(number_of_parameters_1_expected),
          name = 'number_of_parameters')

def number_of_parameters_2_getargs() :
    return [net_dsep]
number_of_parameters_2_expected = 14
def number_of_parameters_2_testanswer(val, original_val = None) :
    return val == number_of_parameters_2_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = number_of_parameters_2_getargs,
          testanswer = number_of_parameters_2_testanswer,
          expected_val = str(number_of_parameters_2_expected),
          name = 'number_of_parameters')

# 2 params for A, 1 for B, 3*2*(5-1)=24 for C
def number_of_parameters_3_getargs() :
    return [net_basic_nonboolean]
number_of_parameters_3_expected = 27
def number_of_parameters_3_testanswer(val, original_val = None) :
    return val == number_of_parameters_3_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = number_of_parameters_3_getargs,
          testanswer = number_of_parameters_3_testanswer,
          expected_val = str(number_of_parameters_3_expected),
          name = 'number_of_parameters')


def independent_0_getargs() :
    return [net_racoon, 'B', 'R']
independent_0_expected = True
def independent_0_testanswer(val, original_val = None) :
    return val == independent_0_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = independent_0_getargs,
          testanswer = independent_0_testanswer,
          expected_val = str(independent_0_expected),
          name = 'is_independent')

def independent_1_getargs() :
    return [net_racoon, 'B', 'R', {'D':True}]
independent_1_expected = False
def independent_1_testanswer(val, original_val = None) :
    return val == independent_1_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = independent_1_getargs,
          testanswer = independent_1_testanswer,
          expected_val = str(independent_1_expected),
          name = 'is_independent')

def independent_2_getargs() :
    return [net_racoon, 'D', 'T', {'B':True, 'R':False}]
independent_2_expected = True
def independent_2_testanswer(val, original_val = None) :
    return val == independent_2_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = independent_2_getargs,
          testanswer = independent_2_testanswer,
          expected_val = str(independent_2_expected),
          name = 'is_independent')

def independent_3_getargs() :
    return [net_basic_probs, 'A', 'B', {}]
independent_3_expected = True
def independent_3_testanswer(val, original_val = None) :
    return val == independent_3_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = independent_3_getargs,
          testanswer = independent_3_testanswer,
          expected_val = str(independent_3_expected),
          name = 'is_independent')

def independent_4_getargs() :
    return [net_basic_probs, 'B', 'C', {'A':False}]
independent_4_expected = True
def independent_4_testanswer(val, original_val = None) :
    return val == independent_4_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = independent_4_getargs,
          testanswer = independent_4_testanswer,
          expected_val = str(independent_4_expected),
          name = 'is_independent')

def independent_5_getargs() :
    return [net_basic_probs, 'C', 'B', {'A':False}]
independent_5_expected = True
def independent_5_testanswer(val, original_val = None) :
    return val == independent_5_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = independent_5_getargs,
          testanswer = independent_5_testanswer,
          expected_val = str(independent_5_expected),
          name = 'is_independent')

def independent_6_getargs() :
    return [net_basic_probs, 'B', 'C', {'A':True}]
independent_6_expected = False
def independent_6_testanswer(val, original_val = None) :
    return val == independent_6_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = independent_6_getargs,
          testanswer = independent_6_testanswer,
          expected_val = str(independent_6_expected),
          name = 'is_independent')

def independent_7_getargs() :
    return [net_basic_probs, 'B', 'C']
independent_7_expected = False
def independent_7_testanswer(val, original_val = None) :
    return val == independent_7_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = independent_7_getargs,
          testanswer = independent_7_testanswer,
          expected_val = str(independent_7_expected),
          name = 'is_independent')
