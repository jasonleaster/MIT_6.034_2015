from tester import make_test, get_tests
from test_problems import *
from lab4 import TEST_MOOSE_PROBLEM
from random import randint, random


#### PART 1

## has_empty_domains
#all domains empty -> True  #TEST 1
def has_empty_domains_0_getargs() :
    return [CSP_all_domains_empty.copy()]
def has_empty_domains_0_testanswer(val, original_val = None) :
    return val == True
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = has_empty_domains_0_getargs,
          testanswer = has_empty_domains_0_testanswer,
          expected_val = "True",
          name = 'has_empty_domains')

#one domain empty -> True  #TEST 2
def has_empty_domains_1_getargs() :
    return [CSP_empty_domain_with_constraint.copy()]
def has_empty_domains_1_testanswer(val, original_val = None) :
    return val == True
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = has_empty_domains_1_getargs,
          testanswer = has_empty_domains_1_testanswer,
          expected_val = "True",
          name = 'has_empty_domains')

#no domains empty -> False  #TEST 3
def has_empty_domains_2_getargs() :
    return [CSP_no_soln.copy()]
def has_empty_domains_2_testanswer(val, original_val = None) :
    return val == False
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = has_empty_domains_2_getargs,
          testanswer = has_empty_domains_2_testanswer,
          expected_val = "False",
          name = 'has_empty_domains')

#all vars assigned (all domains singleton) -> False  #TEST 4
def has_empty_domains_3_getargs() :
    return [CSP_all_vars_assigned_inconsistent.copy()]
def has_empty_domains_3_testanswer(val, original_val = None) :
    return val == False
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = has_empty_domains_3_getargs,
          testanswer = has_empty_domains_3_testanswer,
          expected_val = "False",
          name = 'has_empty_domains')


## check_all_constraints
#no constraints -> True  #TEST 5
def check_all_constraints_0_getargs() :
    return [CSP_no_constraints.copy()]
def check_all_constraints_0_testanswer(val, original_val = None) :
    return val == True
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = check_all_constraints_0_getargs,
          testanswer = check_all_constraints_0_testanswer,
          expected_val = "True",
          name = 'check_all_constraints')

#constraints, no values assigned -> True  #TEST 6
def check_all_constraints_1_getargs() :
    return [CSP_no_vars_assigned.copy()]
def check_all_constraints_1_testanswer(val, original_val = None) :
    return val == True
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = check_all_constraints_1_getargs,
          testanswer = check_all_constraints_1_testanswer,
          expected_val = "True",
          name = 'check_all_constraints')

#constraint, one value assigned, other not -> True  #TEST 7
def check_all_constraints_2_getargs() :
    return [CSP_one_var_assigned.copy()]
def check_all_constraints_2_testanswer(val, original_val = None) :
    return val == True
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = check_all_constraints_2_getargs,
          testanswer = check_all_constraints_2_testanswer,
          expected_val = "True",
          name = 'check_all_constraints')

#constraints, some vals assigned, consistent -> True  #TEST 8
def check_all_constraints_3_getargs() :
    return [CSP_some_vars_assigned_consistent.copy()]
def check_all_constraints_3_testanswer(val, original_val = None) :
    return val == True
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = check_all_constraints_3_getargs,
          testanswer = check_all_constraints_3_testanswer,
          expected_val = "True",
          name = 'check_all_constraints')

#constraints, some vals assigned, one inconsistent -> False  #TEST 9
def check_all_constraints_4_getargs() :
    return [CSP_some_vars_assigned_inconsistent.copy()]
def check_all_constraints_4_testanswer(val, original_val = None) :
    return val == False
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = check_all_constraints_4_getargs,
          testanswer = check_all_constraints_4_testanswer,
          expected_val = "False",
          name = 'check_all_constraints')

#constraints, vals all assigned, consistent -> True
def check_all_constraints_5_getargs() :  #TEST 10
    return [CSP_all_vars_assigned_consistent.copy()]
def check_all_constraints_5_testanswer(val, original_val = None) :
    return val == True
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = check_all_constraints_5_getargs,
          testanswer = check_all_constraints_5_testanswer,
          expected_val = "True",
          name = 'check_all_constraints')

#constraints, vals all assigned, some inconsistent -> False
def check_all_constraints_6_getargs() :  #TEST 11
    return [CSP_all_vars_assigned_inconsistent.copy()]
def check_all_constraints_6_testanswer(val, original_val = None) :
    return val == False
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = check_all_constraints_6_getargs,
          testanswer = check_all_constraints_6_testanswer,
          expected_val = "False",
          name = 'check_all_constraints')

#A assigned, B unassigned, B has empty domain -> True
#This test checks that check_all_constraints does not special-case empty domains
def check_all_constraints_7_getargs() :  #TEST 12
    return [CSP_empty_domain_with_constraint.copy()]
def check_all_constraints_7_testanswer(val, original_val = None) :
    return val == True
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = check_all_constraints_7_getargs,
          testanswer = check_all_constraints_7_testanswer,
          expected_val = "True",
          name = 'check_all_constraints')


## solve_constraint_dfs
# triangle problem -> (assignments, extension_count)
solve_constraint_dfs_0_expected = (triangle_problem_soln.assigned_values, 15)
def solve_constraint_dfs_0_getargs() :  #TEST 13
    return [triangle_problem.copy()]
def solve_constraint_dfs_0_testanswer(val, original_val = None) :
    return val == solve_constraint_dfs_0_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_dfs_0_getargs,
          testanswer = solve_constraint_dfs_0_testanswer,
          expected_val = str(solve_constraint_dfs_0_expected),
          name = 'solve_constraint_dfs')

# trivial problem, no soln -> None
solve_constraint_dfs_1_expected = (None, 13)
def solve_constraint_dfs_1_getargs() :  #TEST 14
    return [CSP_impossible.copy()]
def solve_constraint_dfs_1_testanswer(val, original_val = None) :
    return val == solve_constraint_dfs_1_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_dfs_1_getargs,
          testanswer = solve_constraint_dfs_1_testanswer,
          expected_val = str(solve_constraint_dfs_1_expected),
          name = 'solve_constraint_dfs')

# longer (quiz) problem -> (assignments, extension_count)
solve_constraint_dfs_2_expected = ({'Q1':'B', 'Q3':'D', 'Q2':'B', 'Q5':'C',
                                    'Q4':'C'}, 20)
def solve_constraint_dfs_2_getargs() :  #TEST 15
    return [get_pokemon_problem()]
def solve_constraint_dfs_2_testanswer(val, original_val = None) :
    return val == solve_constraint_dfs_2_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_dfs_2_getargs,
          testanswer = solve_constraint_dfs_2_testanswer,
          expected_val = (str(solve_constraint_dfs_2_expected)
                          + " (Note: This is the Pokemon problem.)"),
          name = 'solve_constraint_dfs')

#one domain initially empty, return immediately -> (None, 1)
solve_constraint_dfs_3_expected = (None, 1)
def solve_constraint_dfs_3_getargs() :  #TEST 16
    return [CSP_empty_domain.copy()]
def solve_constraint_dfs_3_testanswer(val, original_val = None) :
    return val == solve_constraint_dfs_3_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_dfs_3_getargs,
          testanswer = solve_constraint_dfs_3_testanswer,
          expected_val = str(solve_constraint_dfs_3_expected),
          name = 'solve_constraint_dfs')


#### PART 2

## eliminate_from_neighbors
#no constraints on var -> []; csp unchanged
eliminate_0_input_csp = CSP_one_var_assigned_unconstrained.copy()
def eliminate_from_neighbors_0_getargs() :  #TEST 17
    return [eliminate_0_input_csp, 'B']
def eliminate_from_neighbors_0_testanswer(val, original_val = None) :
    return val == [] and eliminate_0_input_csp == CSP_one_var_assigned_unconstrained
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = eliminate_from_neighbors_0_getargs,
          testanswer = eliminate_from_neighbors_0_testanswer,
          expected_val = "[] (with original csp unchanged)",
          name = 'eliminate_from_neighbors')

#constraints on var, no neighbors reduced -> []; csp unchanged
eliminate_1_input_csp = CSP_one_var_assigned_unconstrained.copy()
def eliminate_from_neighbors_1_getargs() :  #TEST 18
    return [eliminate_1_input_csp, 'A']
def eliminate_from_neighbors_1_testanswer(val, original_val = None) :
    return val == [] and eliminate_1_input_csp == CSP_one_var_assigned_unconstrained
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = eliminate_from_neighbors_1_getargs,
          testanswer = eliminate_from_neighbors_1_testanswer,
          expected_val = "[] (with original csp unchanged)",
          name = 'eliminate_from_neighbors')

#domain reduced to size 0 -> None; check csp
eliminate_2_input_csp = CSP_B_nope.copy()
def eliminate_from_neighbors_2_getargs() :  #TEST 19
    return [eliminate_2_input_csp, 'A']
def eliminate_from_neighbors_2_testanswer(val, original_val = None) :
    return val == None and eliminate_2_input_csp == CSP_B_nope_after_eliminate
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = eliminate_from_neighbors_2_getargs,
          testanswer = eliminate_from_neighbors_2_testanswer,
          expected_val = "None (and B's domain becomes empty in original csp)",
          name = 'eliminate_from_neighbors')

#multiple constraints on var
#  -> [neighbors reduced, each once, alpha order]; csp with domains reduced
eliminate_4_input_csp = CSP_almost_stuck.copy()
def eliminate_from_neighbors_4_getargs() :  #TEST 20
    return [eliminate_4_input_csp,'A']
def eliminate_from_neighbors_4_testanswer(val, original_val = None) :
    return val == ['B','C'] and eliminate_4_input_csp == CSP_almost_stuck_after_eliminate
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = eliminate_from_neighbors_4_getargs,
          testanswer = eliminate_from_neighbors_4_testanswer,
          expected_val = "['B','C'] (and updated domains in original csp)",
          name = 'eliminate_from_neighbors')


## domain_reduction
#queue=[A], neighbor's domain gets reduced to 0 -> None; modify csp
domain_reduction_0_input_csp = CSP_almost_stuck.copy()
def domain_reduction_0_getargs() :  #TEST 21
    return [domain_reduction_0_input_csp, ['A']]
def domain_reduction_0_testanswer(val, original_val = None) :
    return val == None and domain_reduction_0_input_csp == CSP_now_stuck
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = domain_reduction_0_getargs,
          testanswer = domain_reduction_0_testanswer,
          expected_val = "None (with correctly reduced domains in original csp)",
          name = 'domain_reduction')

#queue=None, but no reduction -> add all vars to queue, pop all once; no change to csp
domain_reduction_1_input_csp = CSP_one_var_assigned_unconstrained.copy()
domain_reduction_1_expected = list('ABC')
def domain_reduction_1_getargs() :  #TEST 22
    return [domain_reduction_1_input_csp]
def domain_reduction_1_testanswer(val, original_val = None) :
    return (val == domain_reduction_1_expected
            and domain_reduction_1_input_csp == CSP_one_var_assigned_unconstrained)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = domain_reduction_1_getargs,
          testanswer = domain_reduction_1_testanswer,
          expected_val = (str(domain_reduction_1_expected)
                          + " (with original csp unchanged)"),
          name = 'domain_reduction')

#queue=[B,A], but no reduction -> [B,A]
domain_reduction_2_input_csp = CSP_no_vars_assigned.copy()
domain_reduction_2_expected = ['B','A']
def domain_reduction_2_getargs() :  #TEST 23
    return [domain_reduction_2_input_csp, ['B','A']]
def domain_reduction_2_testanswer(val, original_val = None) :
    return (val == domain_reduction_2_expected
            and domain_reduction_2_input_csp == CSP_no_vars_assigned)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = domain_reduction_2_getargs,
          testanswer = domain_reduction_2_testanswer,
          expected_val = (str(domain_reduction_2_expected)
                          + " (with original csp unchanged)"),
          name = 'domain_reduction')

#queue=[B,A], reduction and propagation -> [B, A, C, A, B]
domain_reduction_3_input_csp = triangle_problem_modified.copy()
domain_reduction_3_expected = list('BACAB')
def domain_reduction_3_getargs() :  #TEST 24
    return [domain_reduction_3_input_csp, ['B','A']]
def domain_reduction_3_testanswer(val, original_val = None) :
    return (val == domain_reduction_3_expected
            and domain_reduction_3_input_csp == triangle_problem_modified_reduced)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = domain_reduction_3_getargs,
          testanswer = domain_reduction_3_testanswer,
          expected_val = (str(domain_reduction_3_expected)
                          + " (with domains modified in original csp)"),
          name = 'domain_reduction')

#This test differentiates b/w full reduction/singletons
domain_reduction_4_input_csp = CSP_singleton_differentiate.copy()
domain_reduction_4_expected = list('ABC')
def domain_reduction_4_getargs() :  #TEST 25
    return [domain_reduction_4_input_csp, ['A']]
def domain_reduction_4_testanswer(val, original_val = None) :
    return (val == domain_reduction_4_expected
            and domain_reduction_4_input_csp == CSP_singleton_differentiate_reduced)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = domain_reduction_4_getargs,
          testanswer = domain_reduction_4_testanswer,
          expected_val = (str(domain_reduction_4_expected)
                          + " (with domains reduced in original csp)"),
          name = 'domain_reduction')

#queue=[] -> [] (don't propagate anything)
#This test checks that vars are being propagated only when specified
domain_reduction_5_input_csp = CSP_almost_stuck.copy()
def domain_reduction_5_getargs() :  #TEST 26
    return [domain_reduction_5_input_csp, []]
def domain_reduction_5_testanswer(val, original_val = None) :
    return val == [] and domain_reduction_5_input_csp == CSP_almost_stuck
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = domain_reduction_5_getargs,
          testanswer = domain_reduction_5_testanswer,
          expected_val = "[] (with original csp unchanged)",
          name = 'domain_reduction')


## ANSWER_1
ANSWER_1_getargs = 'ANSWER_1'  #TEST 27
def ANSWER_1_testanswer(val, original_val = None):
    return val == 20
make_test(type = 'VALUE',
          getargs = ANSWER_1_getargs,
          testanswer = ANSWER_1_testanswer,
          expected_val = ('(correct number of extensions for Pokemon problem, '
                          +'solved with DFS only)'),
          name = ANSWER_1_getargs)


## ANSWER_2
ANSWER_2_getargs = 'ANSWER_2'  #TEST 28
def ANSWER_2_testanswer(val, original_val = None):
    return val == 6
make_test(type = 'VALUE',
          getargs = ANSWER_2_getargs,
          testanswer = ANSWER_2_testanswer,
          expected_val = ('(correct number of extensions for Pokemon problem, '
                          +'solved with DFS after domain reduction)'),
          name = ANSWER_2_getargs)


#### PART 3
## solve_constraint_propagate_reduced_domains
#triangle problem
solve_constraint_propany_0_expected = (triangle_problem_soln.assigned_values, 5)
def solve_constraint_propany_0_getargs() :  #TEST 29
    return [triangle_problem.copy()]
def solve_constraint_propany_0_testanswer(val, original_val = None) :
    return val == solve_constraint_propany_0_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_propany_0_getargs,
          testanswer = solve_constraint_propany_0_testanswer,
          expected_val = str(solve_constraint_propany_0_expected),
          name = 'solve_constraint_propagate_reduced_domains')

#pokemon problem
solve_constraint_propany_2_expected = ({'Q1':'B', 'Q3':'D', 'Q2':'B', 'Q5':'C',
                                        'Q4':'C'}, 7)
def solve_constraint_propany_2_getargs() :  #TEST 30
    return [get_pokemon_problem()]
def solve_constraint_propany_2_testanswer(val, original_val = None) :
    return val == solve_constraint_propany_2_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_propany_2_getargs,
          testanswer = solve_constraint_propany_2_testanswer,
          expected_val = (str(solve_constraint_propany_2_expected)
                          + " (Note: This is the Pokemon problem.)"),
          name = 'solve_constraint_propagate_reduced_domains')

#This test checks that only newly reduced domains get propagated
# (ignore existing singletons, even if they've never been propagated)
solve_constraint_propany_7_expected = ({'A':2, 'B':2, 'C':2}, 5)
def solve_constraint_propany_7_getargs() :  #TEST 31
    return [CSP_no_prop.copy()]
def solve_constraint_propany_7_testanswer(val, original_val = None) :
    return val == solve_constraint_propany_7_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_propany_7_getargs,
          testanswer = solve_constraint_propany_7_testanswer,
          expected_val = str(solve_constraint_propany_7_expected),
          name = 'solve_constraint_propagate_reduced_domains')

#This test checks that singletons get propagated
solve_constraint_propany_8_expected = ({'A':2, 'B':2, 'C':2}, 4)
def solve_constraint_propany_8_getargs() :  #TEST 32
    return [CSP_propany_and_prop1.copy()]
def solve_constraint_propany_8_testanswer(val, original_val = None) :
    return val == solve_constraint_propany_8_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_propany_8_getargs,
          testanswer = solve_constraint_propany_8_testanswer,
          expected_val = str(solve_constraint_propany_8_expected),
          name = 'solve_constraint_propagate_reduced_domains')

#This test checks that newly reduced non-singletons DO get propagated
solve_constraint_propany_9_expected = ({'A':2, 'B':3, 'C':3}, 4)
def solve_constraint_propany_9_getargs() :  #TEST 33
    return [CSP_propany_not_prop1.copy()]
def solve_constraint_propany_9_testanswer(val, original_val = None) :
    return val == solve_constraint_propany_9_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_propany_9_getargs,
          testanswer = solve_constraint_propany_9_testanswer,
          expected_val = str(solve_constraint_propany_9_expected),
          name = 'solve_constraint_propagate_reduced_domains')


## ANSWER_3
ANSWER_3_getargs = 'ANSWER_3'  #TEST 34
def ANSWER_3_testanswer(val, original_val = None):
    return val == 7
make_test(type = 'VALUE',
          getargs = ANSWER_3_getargs,
          testanswer = ANSWER_3_testanswer,
          expected_val = ('(correct number of extensions for Pokemon problem, '
                          +'solved with DFS+FC+PROP-ANY)'),
          name = ANSWER_3_getargs)


#### PART 4
## domain_reduction_singleton_domains
#queue=[A], neighbor's domain gets reduced to 0 -> None; modify csp
domain_reduction_singleton_0_input_csp = CSP_almost_stuck.copy()
def domain_reduction_singleton_0_getargs() :  #TEST 35
    return [domain_reduction_singleton_0_input_csp, ['A']]
def domain_reduction_singleton_0_testanswer(val, original_val = None) :
    return val == None and domain_reduction_singleton_0_input_csp == CSP_now_stuck
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = domain_reduction_singleton_0_getargs,
          testanswer = domain_reduction_singleton_0_testanswer,
          expected_val = "None (with correctly reduced domains in original csp)",
          name = 'domain_reduction_singleton_domains')

#same as non-singleton
#queue=None, but no reduction -> add all vars to queue, pop each once; no change to csp
domain_reduction_singleton_1_input_csp = CSP_one_var_assigned_unconstrained.copy()
domain_reduction_singleton_1_expected = list('ABC')
def domain_reduction_singleton_1_getargs() :  #TEST 36
    return [domain_reduction_singleton_1_input_csp]
def domain_reduction_singleton_1_testanswer(val, original_val = None) :
    return (val == domain_reduction_singleton_1_expected
            and domain_reduction_singleton_1_input_csp == CSP_one_var_assigned_unconstrained)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = domain_reduction_singleton_1_getargs,
          testanswer = domain_reduction_singleton_1_testanswer,
          expected_val = (str(domain_reduction_singleton_1_expected)
                          + " (with original csp unchanged)"),
          name = 'domain_reduction_singleton_domains')

#This test differentiates b/w full reduction/singletons
domain_reduction_singleton_2_input_csp = CSP_singleton_differentiate.copy()
domain_reduction_singleton_2_expected = ['A','C']
def domain_reduction_singleton_2_getargs() :  #TEST 37
    return [domain_reduction_singleton_2_input_csp, ['A']]
def domain_reduction_singleton_2_testanswer(val, original_val = None) :
    return (val == domain_reduction_singleton_2_expected
            and domain_reduction_singleton_2_input_csp == CSP_singleton_differentiate_reduced)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = domain_reduction_singleton_2_getargs,
          testanswer = domain_reduction_singleton_2_testanswer,
          expected_val = (str(domain_reduction_singleton_2_expected)
                          + " (with domains reduced in original csp)"),
          name = 'domain_reduction_singleton_domains')

#queue=[B,A], reduction and propagation -> [B, A, C, A, B] #same as non-singleton
domain_reduction_singleton_3_input_csp = triangle_problem_modified.copy()
domain_reduction_singleton_3_expected = list('BACAB')
def domain_reduction_singleton_3_getargs() :  #TEST 38
    return [domain_reduction_singleton_3_input_csp, ['B','A']]
def domain_reduction_singleton_3_testanswer(val, original_val = None) :
    return (val == domain_reduction_singleton_3_expected
            and domain_reduction_singleton_3_input_csp == triangle_problem_modified_reduced)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = domain_reduction_singleton_3_getargs,
          testanswer = domain_reduction_singleton_3_testanswer,
          expected_val = (str(domain_reduction_singleton_3_expected)
                          + " (with domains modified in original csp)"),
          name = 'domain_reduction_singleton_domains')

#queue=[] -> [] (don't propagate anything) #same as non-singleton
#This test checks that vars are being propagated only when specified
domain_reduction_singleton_5_input_csp = CSP_almost_stuck_singletons.copy()
def domain_reduction_singleton_5_getargs() :  #TEST 39
    return [domain_reduction_singleton_5_input_csp, []]
def domain_reduction_singleton_5_testanswer(val, original_val = None) :
    return val == [] and domain_reduction_singleton_5_input_csp == CSP_almost_stuck_singletons
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = domain_reduction_singleton_5_getargs,
          testanswer = domain_reduction_singleton_5_testanswer,
          expected_val = "[] (with original csp unchanged)",
          name = 'domain_reduction_singleton_domains')


## solve_constraint_propagate_singleton_domains
#triangle problem DFS+FC+PROP-1
solve_constraint_prop1_0_expected = (triangle_problem_soln.assigned_values, 5)
def solve_constraint_prop1_0_getargs() :  #TEST 40
    return [triangle_problem.copy()]
def solve_constraint_prop1_0_testanswer(val, original_val = None) :
    return val == solve_constraint_prop1_0_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_prop1_0_getargs,
          testanswer = solve_constraint_prop1_0_testanswer,
          expected_val = str(solve_constraint_prop1_0_expected),
          name = 'solve_constraint_propagate_singleton_domains')

#pokemon problem DFS+FC+PROP-1
solve_constraint_prop1_2_expected = ({'Q1':'B', 'Q3':'D', 'Q2':'B', 'Q5':'C',
                                        'Q4':'C'}, 8)
def solve_constraint_prop1_2_getargs() :  #TEST 41
    return [get_pokemon_problem()]
def solve_constraint_prop1_2_testanswer(val, original_val = None) :
    return val == solve_constraint_prop1_2_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_prop1_2_getargs,
          testanswer = solve_constraint_prop1_2_testanswer,
          expected_val = (str(solve_constraint_prop1_2_expected)
                          + " (Note: This is the Pokemon problem.)"),
          name = 'solve_constraint_propagate_singleton_domains')

#This test checks that only new singletons get propagated
# (ignore existing singletons, even if they've never been propagated)
solve_constraint_prop1_7_expected = ({'A':2, 'B':2, 'C':2}, 5)
def solve_constraint_prop1_7_getargs() :  #TEST 42
    return [CSP_no_prop.copy()]
def solve_constraint_prop1_7_testanswer(val, original_val = None) :
    return val == solve_constraint_prop1_7_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_prop1_7_getargs,
          testanswer = solve_constraint_prop1_7_testanswer,
          expected_val = str(solve_constraint_prop1_7_expected),
          name = 'solve_constraint_propagate_singleton_domains')

#This test checks that singletons get propagated
solve_constraint_prop1_8_expected = ({'A':2, 'B':2, 'C':2}, 4)
def solve_constraint_prop1_8_getargs() :  #TEST 43
    return [CSP_propany_and_prop1.copy()]
def solve_constraint_prop1_8_testanswer(val, original_val = None) :
    return val == solve_constraint_prop1_8_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_prop1_8_getargs,
          testanswer = solve_constraint_prop1_8_testanswer,
          expected_val = str(solve_constraint_prop1_8_expected),
          name = 'solve_constraint_propagate_singleton_domains')

#This test checks that non-singletons do not get propagated
solve_constraint_prop1_9_expected = ({'A':2, 'B':3, 'C':3}, 5)
def solve_constraint_prop1_9_getargs() :  #TEST 44
    return [CSP_propany_not_prop1.copy()]
def solve_constraint_prop1_9_testanswer(val, original_val = None) :
    return val == solve_constraint_prop1_9_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_prop1_9_getargs,
          testanswer = solve_constraint_prop1_9_testanswer,
          expected_val = str(solve_constraint_prop1_9_expected),
          name = 'solve_constraint_propagate_singleton_domains')


## ANSWER_4
ANSWER_4_getargs = 'ANSWER_4'  #TEST 45
def ANSWER_4_testanswer(val, original_val = None):
    return val == 8
make_test(type = 'VALUE',
          getargs = ANSWER_4_getargs,
          testanswer = ANSWER_4_testanswer,
          expected_val = ('(correct number of extensions for Pokemon problem, '
                          +'solved with DFS+FC+PROP-1)'),
          name = ANSWER_4_getargs)


#### PART 5
## propagate

#test with lambda False
#This test differentiates b/w full reduction/singletons/FC
propagate_0_input_csp = CSP_singleton_differentiate.copy()
propagate_0_expected = ['A']
def propagate_0_getargs() :  #TEST 46
    return [lambda p,v: False, propagate_0_input_csp, ['A']]
def propagate_0_testanswer(val, original_val = None) :
    return (val == propagate_0_expected
            and propagate_0_input_csp == CSP_singleton_differentiate_reduced)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = propagate_0_getargs,
          testanswer = propagate_0_testanswer,
          expected_val = (str(propagate_0_expected)
                          + " (with domains reduced in original csp)"),
          name = 'propagate')

#test with lambda True
#This test differentiates b/w full reduction/singletons/FC
propagate_1_input_csp = CSP_singleton_differentiate.copy()
propagate_1_expected = list('AC')
def propagate_1_getargs() :  #TEST 47
    return [lambda p,v: len(p.get_domain(v))==1, propagate_1_input_csp, ['A']]
def propagate_1_testanswer(val, original_val = None) :
    return (val == propagate_1_expected
            and propagate_1_input_csp == CSP_singleton_differentiate_reduced)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = propagate_1_getargs,
          testanswer = propagate_1_testanswer,
          expected_val = (str(propagate_1_expected)
                          + " (with domains reduced in original csp)"),
          name = 'propagate')

#test with lambda len = 1
#This test differentiates b/w full reduction/singletons/FC
propagate_2_input_csp = CSP_singleton_differentiate.copy()
propagate_2_expected = list('ABC')
def propagate_2_getargs() :  #TEST 48
    return [lambda p,v: True, propagate_2_input_csp, ['A']]
def propagate_2_testanswer(val, original_val = None) :
    return (val == propagate_2_expected
            and propagate_2_input_csp == CSP_singleton_differentiate_reduced)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = propagate_2_getargs,
          testanswer = propagate_2_testanswer,
          expected_val = (str(propagate_2_expected)
                          + " (with domains reduced in original csp)"),
          name = 'propagate')

#test with lambda var = "B" (because why not have an arbitrary enqueue condition)
propagate_3_input_csp = CSP_singleton_differentiate.copy()
propagate_3_expected = list('AB')
def propagate_3_getargs() :  #TEST 49
    return [lambda p,v: v=='B', propagate_3_input_csp, ['A']]
def propagate_3_testanswer(val, original_val = None) :
    return (val == propagate_3_expected
            and propagate_3_input_csp == CSP_singleton_differentiate_reduced)
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = propagate_3_getargs,
          testanswer = propagate_3_testanswer,
          expected_val = (str(propagate_3_expected)
                          + " (with domains reduced in original csp)"),
          name = 'propagate')


## condition_domain_reduction
#nonsense input -> True
def condition_domain_reduction_0_getargs() :  #TEST 50
    return [CSP([3]), 3]
def condition_domain_reduction_0_testanswer(val, original_val = None) :
    return val == True
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = condition_domain_reduction_0_getargs,
          testanswer = condition_domain_reduction_0_testanswer,
          expected_val = "True",
          name = 'condition_domain_reduction')

def condition_domain_reduction_1_getargs() :  #TEST 51
    return [None, None]
def condition_domain_reduction_1_testanswer(val, original_val = None) :
    return val == True
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = condition_domain_reduction_1_getargs,
          testanswer = condition_domain_reduction_1_testanswer,
          expected_val = "True (Hint: the inputs don't matter)",
          name = 'condition_domain_reduction')


## condition_singleton
#var is singleton, assigned val -> True
def condition_singleton_0_getargs() :  #TEST 52
    return [CSP_one_var_assigned.copy(), 'A']
def condition_singleton_0_testanswer(val, original_val = None) :
    return val == True
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = condition_singleton_0_getargs,
          testanswer = condition_singleton_0_testanswer,
          expected_val = "True",
          name = 'condition_singleton')

#var is singleton, not assigned -> True
def condition_singleton_3_getargs() :  #TEST 53
    return [CSP_singleton.copy(), 'C']
def condition_singleton_3_testanswer(val, original_val = None) :
    return val == True
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = condition_singleton_3_getargs,
          testanswer = condition_singleton_3_testanswer,
          expected_val = "True",
          name = 'condition_singleton')

#var has multiple values in domain -> False
def condition_singleton_1_getargs() :  #TEST 54
    return [triangle_problem.copy(), 'A']
def condition_singleton_1_testanswer(val, original_val = None) :
    return val == False
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = condition_singleton_1_getargs,
          testanswer = condition_singleton_1_testanswer,
          expected_val = "False",
          name = 'condition_singleton')

#var has no values in domain -> False
def condition_singleton_2_getargs() :  #TEST 55
    return [CSP_empty_domain.copy(), 'B']
def condition_singleton_2_testanswer(val, original_val = None) :
    return val == False
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = condition_singleton_2_getargs,
          testanswer = condition_singleton_2_testanswer,
          expected_val = "False",
          name = 'condition_singleton')


## condition_forward_checking
#nonsense input -> False
def condition_forward_checking_0_getargs() :  #TEST 56
    return [CSP(['any variable']), 'any variable']
def condition_forward_checking_0_testanswer(val, original_val = None) :
    return val == False
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = condition_forward_checking_0_getargs,
          testanswer = condition_forward_checking_0_testanswer,
          expected_val = "False",
          name = 'condition_forward_checking')

def condition_forward_checking_1_getargs() :  #TEST 57
    return [None, None]
def condition_forward_checking_1_testanswer(val, original_val = None) :
    return val == False
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = condition_forward_checking_1_getargs,
          testanswer = condition_forward_checking_1_testanswer,
          expected_val = "False (Hint: the inputs don't matter)",
          name = 'condition_forward_checking')


#### PART 6
## solve_constraint_generic

#triangle problem DFS  #TEST 58
solve_constraint_generic_01_expected = (triangle_problem_soln.assigned_values, 15)
def solve_constraint_generic_01_getargs() :
    return [triangle_problem.copy(), None]
def solve_constraint_generic_01_testanswer(val, original_val = None) :
    return val == solve_constraint_generic_01_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_generic_01_getargs,
          testanswer = solve_constraint_generic_01_testanswer,
          expected_val = str(solve_constraint_generic_01_expected),
          name = 'solve_constraint_generic')

#triangle problem DFS+FC  #TEST 59
solve_constraint_generic_02_expected = (triangle_problem_soln.assigned_values, 7)
def solve_constraint_generic_02_getargs() :
    return [triangle_problem.copy(), lambda p,v: False]
def solve_constraint_generic_02_testanswer(val, original_val = None) :
    return val == solve_constraint_generic_02_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_generic_02_getargs,
          testanswer = solve_constraint_generic_02_testanswer,
          expected_val = str(solve_constraint_generic_02_expected),
          name = 'solve_constraint_generic')

#triangle problem DFS+FC+PROP-1  #TEST 60
solve_constraint_generic_03_expected = (triangle_problem_soln.assigned_values, 5)
def solve_constraint_generic_03_getargs() :
    return [triangle_problem.copy(), lambda p,v: len(p.get_domain(v))==1]
def solve_constraint_generic_03_testanswer(val, original_val = None) :
    return val == solve_constraint_generic_03_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_generic_03_getargs,
          testanswer = solve_constraint_generic_03_testanswer,
          expected_val = str(solve_constraint_generic_03_expected),
          name = 'solve_constraint_generic')

#triangle problem DFS+FC+PROP-ANY  #TEST 61
solve_constraint_generic_04_expected = (triangle_problem_soln.assigned_values, 5)
def solve_constraint_generic_04_getargs() :
    return [triangle_problem.copy(), lambda p,v: True]
def solve_constraint_generic_04_testanswer(val, original_val = None) :
    return val == solve_constraint_generic_04_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_generic_04_getargs,
          testanswer = solve_constraint_generic_04_testanswer,
          expected_val = str(solve_constraint_generic_04_expected),
          name = 'solve_constraint_generic')


#pokemon problem DFS  #TEST 62
solve_constraint_generic_21_expected = ({'Q1':'B', 'Q3':'D', 'Q2':'B', 'Q5':'C',
                                        'Q4':'C'}, 20)
def solve_constraint_generic_21_getargs() :
    return [get_pokemon_problem(), None]
def solve_constraint_generic_21_testanswer(val, original_val = None) :
    return val == solve_constraint_generic_21_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_generic_21_getargs,
          testanswer = solve_constraint_generic_21_testanswer,
          expected_val = (str(solve_constraint_generic_21_expected)
                          + " (Note: This is the Pokemon problem.)"),
          name = 'solve_constraint_generic')

#pokemon problem DFS+FC  #TEST 63
solve_constraint_generic_22_expected = ({'Q1':'B', 'Q3':'D', 'Q2':'B', 'Q5':'C',
                                        'Q4':'C'}, 9)
def solve_constraint_generic_22_getargs() :
    return [get_pokemon_problem(), lambda p,v: False]
def solve_constraint_generic_22_testanswer(val, original_val = None) :
    return val == solve_constraint_generic_22_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_generic_22_getargs,
          testanswer = solve_constraint_generic_22_testanswer,
          expected_val = (str(solve_constraint_generic_22_expected)
                          + " (Note: This is the Pokemon problem.)"),
          name = 'solve_constraint_generic')

#pokemon problem DFS+FC+PROP-1  #TEST 64
solve_constraint_generic_23_expected = ({'Q1':'B', 'Q3':'D', 'Q2':'B', 'Q5':'C',
                                        'Q4':'C'}, 8)
def solve_constraint_generic_23_getargs() :
    return [get_pokemon_problem(), lambda p,v: len(p.get_domain(v))==1]
def solve_constraint_generic_23_testanswer(val, original_val = None) :
    return val == solve_constraint_generic_23_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_generic_23_getargs,
          testanswer = solve_constraint_generic_23_testanswer,
          expected_val = (str(solve_constraint_generic_23_expected)
                          + " (Note: This is the Pokemon problem.)"),
          name = 'solve_constraint_generic')

#pokemon problem DFS+FC+PROP-ANY  #TEST 65
solve_constraint_generic_24_expected = ({'Q1':'B', 'Q3':'D', 'Q2':'B', 'Q5':'C',
                                        'Q4':'C'}, 7)
def solve_constraint_generic_24_getargs() :
    return [get_pokemon_problem(), lambda p,v: True]
def solve_constraint_generic_24_testanswer(val, original_val = None) :
    return val == solve_constraint_generic_24_expected
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = solve_constraint_generic_24_getargs,
          testanswer = solve_constraint_generic_24_testanswer,
          expected_val = (str(solve_constraint_generic_24_expected)
                          + " (Note: This is the Pokemon problem.)"),
          name = 'solve_constraint_generic')


## ANSWER_5
ANSWER_5_getargs = 'ANSWER_5'  #TEST 66
def ANSWER_5_testanswer(val, original_val = None):
    return val == 9
make_test(type = 'VALUE',
          getargs = ANSWER_5_getargs,
          testanswer = ANSWER_5_testanswer,
          expected_val = ('(correct number of extensions for Pokemon problem, '
                          +'solved with DFS+FC)'),
          name = ANSWER_5_getargs)


#### PART 7
## constraint_adjacent
#randint a, a+1 -> True
def constraint_adjacent_0_getargs() :  #TEST 67
    a = randint(-100, 100)
    return [a, a+1]
def constraint_adjacent_0_testanswer(val, original_val = None) :
    return val == True
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = constraint_adjacent_0_getargs,
          testanswer = constraint_adjacent_0_testanswer,
          expected_val = "True",
          name = 'constraint_adjacent')

#randint a, a-1 -> True
def constraint_adjacent_1_getargs() :  #TEST 68
    a = randint(-100, 100)
    return [a, a-1]
def constraint_adjacent_1_testanswer(val, original_val = None) :
    return val == True
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = constraint_adjacent_1_getargs,
          testanswer = constraint_adjacent_1_testanswer,
          expected_val = "True",
          name = 'constraint_adjacent')

#randint a, a -> False
def constraint_adjacent_2_getargs() :  #TEST 69
    return [randint(-42, 42)]*2
def constraint_adjacent_2_testanswer(val, original_val = None) :
    return val == False
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = constraint_adjacent_2_getargs,
          testanswer = constraint_adjacent_2_testanswer,
          expected_val = "False",
          name = 'constraint_adjacent')

#randint a, a+b (b>1) -> False
def constraint_adjacent_3_getargs() :  #TEST 70
    a = randint(-60, 60)
    return [a, a+randint(2,10)]
def constraint_adjacent_3_testanswer(val, original_val = None) :
    return val == False
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = constraint_adjacent_3_getargs,
          testanswer = constraint_adjacent_3_testanswer,
          expected_val = "False",
          name = 'constraint_adjacent')


## constraint_not_adjacent
#(same tests as constraint_adjacent, but opposite)
#randint a, a+1 -> False
def constraint_not_adjacent_0_getargs() :  #TEST 71
    a = randint(-100, 100)
    return [a, a+1]
def constraint_not_adjacent_0_testanswer(val, original_val = None) :
    return val == False
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = constraint_not_adjacent_0_getargs,
          testanswer = constraint_not_adjacent_0_testanswer,
          expected_val = "False",
          name = 'constraint_not_adjacent')

#randint a, a-1 -> False
def constraint_not_adjacent_1_getargs() :  #TEST 72
    a = randint(-100, 100)
    return [a, a-1]
def constraint_not_adjacent_1_testanswer(val, original_val = None) :
    return val == False
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = constraint_not_adjacent_1_getargs,
          testanswer = constraint_not_adjacent_1_testanswer,
          expected_val = "False",
          name = 'constraint_not_adjacent')

#randint a, a -> True
def constraint_not_adjacent_2_getargs() :  #TEST 73
    return [randint(-42, 42)]*2
def constraint_not_adjacent_2_testanswer(val, original_val = None) :
    return val == True
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = constraint_not_adjacent_2_getargs,
          testanswer = constraint_not_adjacent_2_testanswer,
          expected_val = "True",
          name = 'constraint_not_adjacent')

#randint a, a+b (b>1) -> True
def constraint_not_adjacent_3_getargs() :  #TEST 74
    a = randint(-60, 60)
    return [a, a+randint(2,10)]
def constraint_not_adjacent_3_testanswer(val, original_val = None) :
    return val == True
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = constraint_not_adjacent_3_getargs,
          testanswer = constraint_not_adjacent_3_testanswer,
          expected_val = "True",
          name = 'constraint_not_adjacent')


## all_different
#no variables -> []
def all_different_0_getargs() :  #TEST 75
    return [[]]
def all_different_0_testanswer(val, original_val = None) :
    return val == []
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = all_different_0_getargs,
          testanswer = all_different_0_testanswer,
          expected_val = "[]",
          name = 'all_different')

#one variable -> []
def all_different_1_getargs() :  #TEST 76
    return [['var1']]
def all_different_1_testanswer(val, original_val = None) :
    return val == []
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = all_different_1_getargs,
          testanswer = all_different_1_testanswer,
          expected_val = "[]",
          name = 'all_different')

def get_vars_sorted_from_constraint(constraint):
    "Assumes constraint is a Constraint object. Returns a sorted list of var1, var2"
    return sorted([constraint.var1, constraint.var2])

def is_constraint_between(constraint, varA, varB):
    """Assumes constraint is a Constraint object. Returns True if constraint
    has specified vars (in either order), otherwise False."""
    return (isinstance_Constraint(constraint)
            and get_vars_sorted_from_constraint(constraint) == sorted([varA, varB]))

def is_difference_constraint(constraint):
    """Assumes constraint is a Constraint object. Returns True if constraint
    passes tests for being a difference constraint, or False if it fails a test."""
    check = constraint.check
    a, b, c, d = randint(-5,5), randint(-10,10), randint(-100,100), random()
    return (check(0,1) and check(1,0) and check(a, a+1) and check(b, b-1)
            and check('x','abc') and check('abc','x')
            and check(c, c+randint(1,100)) and check (d, d*random())
            and not check(0,0) and not check(1,1)
            and not check(*([randint(-40,40)]*2))
            and not check('abc','abc') and not check('x','x'))

#two vars -> [(one constraint b/w A,B OR b/w B,A)]
def all_different_2_getargs() :  #TEST 77
    return [['A','B']]
def all_different_2_testanswer(val, original_val = None) :
    return (isinstance(val, (list, tuple)) and len(val) == 1
            and isinstance_Constraint(val[0])
            and is_constraint_between(val[0], 'A', 'B')
            and is_difference_constraint(val[0]))
make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = all_different_2_getargs,
          testanswer = all_different_2_testanswer,
          expected_val = "(list containing one difference constraint between A and B)",
          name = 'all_different')

#lots of vars -> [(constraints b/w all pairs)]
def all_different_3_getargs() :  #TEST 78
    return [list('CBAD')]

def all_different_3_testanswer(val, original_val = None) :
    if (not isinstance(val, (list, tuple)) or len(val) != 6
        or not all(map(isinstance_Constraint, val))):
        return False
    constraints_sorted = sorted(val, key=get_vars_sorted_from_constraint)
    var_pairs = map(list, ['AB','AC','AD','BC','BD','CD'])
    return (all([is_constraint_between(c, *var_pair)
                 for c, var_pair in zip(constraints_sorted, var_pairs)])
            and all(map(is_difference_constraint, constraints_sorted)))

make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = all_different_3_getargs,
          testanswer = all_different_3_testanswer,
          expected_val = "(list containing six difference constraints between A, B, C, D)",
          name = 'all_different')


#### SURVEY ###################################################
# TESTS 79-83

NAME_getargs = 'NAME'
def NAME_testanswer(val, original_val = None):
    return ( isinstance(val, str) and val != '')
make_test(type = 'VALUE',
          getargs = NAME_getargs,
          testanswer = NAME_testanswer,
          expected_val = '(your name, as a string)',
          name = NAME_getargs)

COLLABORATORS_getargs = 'COLLABORATORS'
def COLLABORATORS_testanswer(val, original_val = None):
    return isinstance(val, str)
make_test(type = 'VALUE',
          getargs = COLLABORATORS_getargs,
          testanswer = COLLABORATORS_testanswer,
          expected_val = "(names of people you worked with, as a string, or empty string if you worked alone)",
          name = COLLABORATORS_getargs)

HOW_MANY_HOURS_THIS_LAB_TOOK_getargs = 'HOW_MANY_HOURS_THIS_LAB_TOOK'
def HOW_MANY_HOURS_THIS_LAB_TOOK_testanswer(val, original_val = None):
    return isinstance(val, (int, float, str)) and val != ''
make_test(type = 'VALUE',
          getargs = HOW_MANY_HOURS_THIS_LAB_TOOK_getargs,
          testanswer = HOW_MANY_HOURS_THIS_LAB_TOOK_testanswer,
          expected_val = '(number of hours you spent on this lab, as a number or string)',
          name = HOW_MANY_HOURS_THIS_LAB_TOOK_getargs)

WHAT_I_FOUND_INTERESTING_getargs = 'WHAT_I_FOUND_INTERESTING'
def WHAT_I_FOUND_INTERESTING_testanswer(val, original_val = None):
    return isinstance(val, str)
make_test(type = 'VALUE',
          getargs = WHAT_I_FOUND_INTERESTING_getargs,
          testanswer = WHAT_I_FOUND_INTERESTING_testanswer,
          expected_val = '(an interesting thing)',
          name = WHAT_I_FOUND_INTERESTING_getargs)

WHAT_I_FOUND_BORING_getargs = 'WHAT_I_FOUND_BORING'
def WHAT_I_FOUND_BORING_testanswer(val, original_val = None):
    return isinstance(val, str)
make_test(type = 'VALUE',
          getargs = WHAT_I_FOUND_BORING_getargs,
          testanswer = WHAT_I_FOUND_BORING_testanswer,
          expected_val = '(a boring thing)',
          name = WHAT_I_FOUND_BORING_getargs)


#### Moose Problem ###################################################
# TESTS 84-94

if TEST_MOOSE_PROBLEM:

    moose_expected_assigned_values = {'Moose': 2, 'McCain': 1, 'Biden': 3,
                                      'Palin': 6, 'You': 5, 'Obama': 4}

    moose_answer_dfs_getargs = 'moose_answer_dfs'
    def moose_answer_dfs_testanswer(val, original_val = None):
        return val == (moose_expected_assigned_values, 24)
    make_test(type = 'VALUE',
              getargs = moose_answer_dfs_getargs,
              testanswer = moose_answer_dfs_testanswer,
              expected_val = str((moose_expected_assigned_values, 24)),
              name = moose_answer_dfs_getargs)

    moose_answer_propany_getargs = 'moose_answer_propany'
    def moose_answer_propany_testanswer(val, original_val = None):
        return val == (moose_expected_assigned_values, 9)
    make_test(type = 'VALUE',
              getargs = moose_answer_propany_getargs,
              testanswer = moose_answer_propany_testanswer,
              expected_val = str((moose_expected_assigned_values, 9)),
              name = moose_answer_propany_getargs)

    moose_answer_prop1_getargs = 'moose_answer_prop1'
    def moose_answer_prop1_testanswer(val, original_val = None):
        return val == (moose_expected_assigned_values, 9)
    make_test(type = 'VALUE',
              getargs = moose_answer_prop1_getargs,
              testanswer = moose_answer_prop1_testanswer,
              expected_val = str((moose_expected_assigned_values, 9)),
              name = moose_answer_prop1_getargs)

    moose_answer_generic_dfs_getargs = 'moose_answer_generic_dfs'
    def moose_answer_generic_dfs_testanswer(val, original_val = None):
        return val == (moose_expected_assigned_values, 24)
    make_test(type = 'VALUE',
              getargs = moose_answer_generic_dfs_getargs,
              testanswer = moose_answer_generic_dfs_testanswer,
              expected_val = str((moose_expected_assigned_values, 24)),
              name = moose_answer_generic_dfs_getargs)

    moose_answer_generic_propany_getargs = 'moose_answer_generic_propany'
    def moose_answer_generic_propany_testanswer(val, original_val = None):
        return val == (moose_expected_assigned_values, 9)
    make_test(type = 'VALUE',
              getargs = moose_answer_generic_propany_getargs,
              testanswer = moose_answer_generic_propany_testanswer,
              expected_val = str((moose_expected_assigned_values, 9)),
              name = moose_answer_generic_propany_getargs)

    moose_answer_generic_prop1_getargs = 'moose_answer_generic_prop1'
    def moose_answer_generic_prop1_testanswer(val, original_val = None):
        return val == (moose_expected_assigned_values, 9)
    make_test(type = 'VALUE',
              getargs = moose_answer_generic_prop1_getargs,
              testanswer = moose_answer_generic_prop1_testanswer,
              expected_val = str((moose_expected_assigned_values, 9)),
              name = moose_answer_generic_prop1_getargs)

    moose_answer_generic_fc_getargs = 'moose_answer_generic_fc'
    def moose_answer_generic_fc_testanswer(val, original_val = None):
        return val == (moose_expected_assigned_values, 9)
    make_test(type = 'VALUE',
              getargs = moose_answer_generic_fc_getargs,
              testanswer = moose_answer_generic_fc_testanswer,
              expected_val = str((moose_expected_assigned_values, 9)),
              name = moose_answer_generic_fc_getargs)


    # domain reduction before search

    moose_reduced_domains = {'You':[2,3,4,5,6], 'Moose':[2,3,4,5,6], 'McCain':[1],
                             'Palin':[2,6], 'Obama':[3,4,5], 'Biden':[3,4,5]}

    moose_instance_for_domain_reduction_getargs = 'moose_instance_for_domain_reduction'
    def moose_instance_for_domain_reduction_testanswer(val, original_val = None):
        return val.domains == moose_reduced_domains
    make_test(type = 'VALUE',
              getargs = moose_instance_for_domain_reduction_getargs,
              testanswer = moose_instance_for_domain_reduction_testanswer,
              expected_val = 'csp with domains reduced to: ' + str(moose_reduced_domains),
              name = moose_instance_for_domain_reduction_getargs)

    moose_answer_domain_reduction_getargs = 'moose_answer_domain_reduction'
    def moose_answer_domain_reduction_testanswer(val, original_val = None):
        return val == ['Biden', 'McCain', 'Moose', 'Obama', 'Palin', 'You', 'Biden']
    make_test(type = 'VALUE',
              getargs = moose_answer_domain_reduction_getargs,
              testanswer = moose_answer_domain_reduction_testanswer,
              expected_val = str(['Biden', 'McCain', 'Moose', 'Obama', 'Palin', 'You', 'Biden']),
              name = moose_answer_domain_reduction_getargs)

    moose_instance_for_domain_reduction_singleton_getargs = 'moose_instance_for_domain_reduction_singleton'
    def moose_instance_for_domain_reduction_singleton_testanswer(val, original_val = None):
        return val.domains == moose_reduced_domains
    make_test(type = 'VALUE',
              getargs = moose_instance_for_domain_reduction_singleton_getargs,
              testanswer = moose_instance_for_domain_reduction_singleton_testanswer,
              expected_val = 'csp with domains reduced to: ' + str(moose_reduced_domains),
              name = moose_instance_for_domain_reduction_singleton_getargs)

    moose_answer_domain_reduction_singleton_getargs = 'moose_answer_domain_reduction_singleton'
    def moose_answer_domain_reduction_singleton_testanswer(val, original_val = None):
        return val == ['Biden', 'McCain', 'Moose', 'Obama', 'Palin', 'You']
    make_test(type = 'VALUE',
              getargs = moose_answer_domain_reduction_singleton_getargs,
              testanswer = moose_answer_domain_reduction_singleton_testanswer,
              expected_val = str(['Biden', 'McCain', 'Moose', 'Obama', 'Palin', 'You', 'Biden']),
              name = moose_answer_domain_reduction_singleton_getargs)

