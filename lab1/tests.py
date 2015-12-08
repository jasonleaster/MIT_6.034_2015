from production import IF, AND, OR, NOT, THEN, run_conditions
import production as lab
from tester import make_test, get_tests, type_encode, type_decode
from data import *
import random
random.seed()

try:
    set()
except NameError:
    from sets import Set as set, ImmutableSet as frozenset


### TEST 1 ###

# The antecedent checks data, it does not add any -- it lists the
# questions asked to see if the rule should fire.

test_short_answer_1_getargs = "ANSWER_1"

def test_short_answer_1_testanswer(val, original_val = None):
    return str(val) == '2'

make_test(type = 'VALUE',
          getargs = test_short_answer_1_getargs,
          testanswer = test_short_answer_1_testanswer,
          expected_val = "correct value of ANSWER_1 ('1', '2', or '3')",
          name = test_short_answer_1_getargs
          )


### TEST 2 ###

# Because 'not' is coded in two separate ways.  You and I can
# tell what was meant to happen, but the forward chaining doesn't
# understand English, it just sees meaningless bits, and those do
# not match, in this case.

test_short_answer_2_getargs = "ANSWER_2"

def test_short_answer_2_testanswer(val, original_val = None):
    return str(val) == 'no'

make_test(type = 'VALUE',
          getargs = test_short_answer_2_getargs,
          testanswer = test_short_answer_2_testanswer,
          expected_val = "correct value of ANSWER_2 ('yes' or 'no')",
          name = test_short_answer_2_getargs
          )


### TEST 3 ###

# The answer is 2 because, as it says in the lab description, "A
# NOT clause should not introduce new variables - the matcher
# won't know what to do with them."  In forward chaining, let's
# suppose there were no assertions of the form '(?x) is dead',
# then we would try to instantiate the consequent, but what would
# we fill the variable with?  So we cannot forward chain.  Let's
# suppose instead that we found 'Polly is dead' so we did not
# instantiate the consequent.  But then in backward chaining, we
# might need 'Martha is pining for the fjords', and nothing says
# that 'Martha is dead' so it would work -- and different forward
# and backward chaining results would be a disaster.  So NOT
# statements in the antecedent must not have any unbound variables.
# 
# You will also note that one pines for the fjords,
# metaphorically speaking, when one *is* dead.  But that's an
# error in knowledge discovery or entry, not in programming.

test_short_answer_3_getargs = "ANSWER_3"

def test_short_answer_3_testanswer(val, original_val = None):
    return str(val) == '2'

make_test(type = 'VALUE',
          getargs = test_short_answer_3_getargs,
          testanswer = test_short_answer_3_testanswer,
          expected_val = "correct value of ANSWER_3 ('1' or '2')",
          name = test_short_answer_3_getargs
          )


### TEST 4 ###

# Rule 1's preconditions, that some one thing both have feathers
# and a beak, are met by the data when that thing is Pendergast.
# The consequent changes the data, so the rule fires.

test_short_answer_4_getargs = "ANSWER_4"

def test_short_answer_4_testanswer(val, original_val = None):
    return str(val) == '1'

make_test(type = 'VALUE',
          getargs = test_short_answer_4_getargs,
          testanswer = test_short_answer_4_testanswer,
          expected_val = "correct value of ANSWER_4 ('0', '1', or '2')",
          name = test_short_answer_4_getargs
          )


### TEST 5 ###

# The preconditions for Rule 2 are met, but the consequent is
# already present, so it doesn't fire.  Same for Rule 1.  So no
# rule fires.

test_short_answer_5_getargs = "ANSWER_5"

def test_short_answer_5_testanswer(val, original_val = None):
    return str(val) == '0'

make_test(type = 'VALUE',
          getargs = test_short_answer_5_getargs,
          testanswer = test_short_answer_5_testanswer,
          expected_val = "correct value of ANSWER_5 ('0', '1', or '2')",
          name = test_short_answer_5_getargs
          )


### TEST 6 ###

# This test checks to make sure that your transitive rule
# produces the correct set of statements given the a/b/c data.

abc_answer = ( 'a beats b', 'b beats c', 'a beats c' )

def transitive_rule_abc_testanswer(val, original_val = None):
    return ( set(val)  == set(abc_answer) )

make_test(type = 'VALUE',
          getargs = 'transitive_rule_abc',
          testanswer = transitive_rule_abc_testanswer,
          expected_val = str(abc_answer),
          name = 'transitive_rule_abc'
          )


### TEST 7 ###

# This test checks to make sure that your transitive rule produces
# the correct set of statements given the rock-paper-scissors data.

poker_answer = ('flush beats pair', 'flush beats straight', 
                'flush beats three-of-a-kind', 'flush beats two-pair', 
                'full-house beats flush', 'full-house beats pair', 
                'full-house beats straight', 'full-house beats three-of-a-kind', 
                'full-house beats two-pair', 'straight beats pair', 
                'straight beats three-of-a-kind', 'straight beats two-pair', 
                'straight-flush beats flush', 'straight-flush beats full-house', 
                'straight-flush beats pair', 'straight-flush beats straight', 
                'straight-flush beats three-of-a-kind', 
                'straight-flush beats two-pair', 'three-of-a-kind beats pair', 
                'three-of-a-kind beats two-pair', 'two-pair beats pair')

def transitive_rule_poker_testanswer(val, original_val = None):
    return ( set(val) == set(poker_answer) )

make_test(type = 'VALUE',
          getargs = 'transitive_rule_poker',
          testanswer = transitive_rule_poker_testanswer,
          expected_val = str(poker_answer),
          name = 'transitive_rule_poker'
          )


### TEST 8 ###

# This test checks that your family rules produce the correct set of
# statements given the sibling data.
# Note that it ignores all statements that don't contain any of
# the words 'parent', 'child', or 'sibling', so you can include 
# extra statements (such as 'self') if it helps you.

sibling_answer = ['child luigi papa', 'child mario papa', 
                  'parent papa luigi', 'parent papa mario', 
                  'sibling luigi mario', 'sibling mario luigi']
    
def family_rules_sibling_testanswer(val, original_val = None):
    return ( set( [ x for x in val
                    if x.split()[0] in ('parent', 'child', 'sibling') ] )
             == set(sibling_answer))

make_test(type = 'VALUE',
          getargs = 'family_rules_sibling',
          testanswer = family_rules_sibling_testanswer,
          expected_val = "family relations should include: " + str(sibling_answer),
          name = 'family_rules_sibling'
          )


### TEST 9 ###

# This test checks that your family rules produce the correct set of
# statements given the grandparent data.

grandparent_answer = ['child alex claire', 'child claire jay', 
                      'grandchild alex jay', 'grandparent jay alex', 
                      'parent claire alex', 'parent jay claire']

def family_rules_grandparent_testanswer(val, original_val = None):
    return ( set( [ x for x in val
                    if x.split()[0] in ('parent', 'child', 'grandparent',
                                        'grandchild') ] )
             == set(grandparent_answer))

make_test(type = 'VALUE',
          getargs = 'family_rules_grandparent',
          testanswer = family_rules_grandparent_testanswer,
          expected_val = "family relations should include: " + str(grandparent_answer),
          name = 'family_rules_grandparent'
          )


### TEST 10 ###

# This test checks that your family rules produce the correct set of
# statements given the a/b/c/d anonymous family data.

anonymous_family_answer = [ 'cousin c1 c3',
                            'cousin c1 c4',
                            'cousin c2 c3',
                            'cousin c2 c4',
                            'cousin c3 c1',
                            'cousin c3 c2',
                            'cousin c4 c1',
                            'cousin c4 c2',
                            'cousin d1 d2',
                            'cousin d2 d1',
                            'cousin d3 d4',
                            'cousin d4 d3' ]

def anonymous_family_testanswer(val, original_val = None):
    return ( set( [ x for x in val
                    if x.split()[0] == 'cousin' ] )
             == set(anonymous_family_answer) )

make_test(type = 'VALUE',
          getargs = 'family_rules_anonymous_family',
          testanswer = anonymous_family_testanswer,
          expected_val = "Results including " + str(anonymous_family_answer),
          name = 'family_rules_anonymous_family'
          )


### TEST 11 ###

# This test checks to make sure that your backchainer produces
# the correct goal tree given a hypothesis and an empty set of
# rules.  The goal tree should contain only the hypothesis.

def backchain_to_goal_tree_1_getargs():
    return [ (),  'stuff'  ]

def backchain_to_goal_tree_1_testanswer(val, original_val = None):
    return ( val == 'stuff' or val == [ 'stuff' ])

make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = backchain_to_goal_tree_1_getargs,
          testanswer = backchain_to_goal_tree_1_testanswer,
          expected_val = "'stuff'",
          name = "backchain_to_goal_tree"
          )


### TEST 12 ###

# This test checks to make sure that your backchainer produces
# the correct goal tree given the hypothesis 'alice is an
# albatross' and using the zookeeper_rules.

def tree_map(lst, fn):
    if isinstance(lst, (list, tuple)):
        return fn([ tree_map(elt, fn) for elt in lst ])
    else:
        return lst

def backchain_to_goal_tree_2_getargs():
    return [ zookeeper_rules, 'alice is an albatross' ]

result_bc_2 = OR('alice is an albatross',
                 AND(OR('alice is a bird',
                        'alice has feathers',
                        AND('alice flies',
                            'alice lays eggs')),
                     'alice is a good flyer'))

def backchain_to_goal_tree_2_testanswer(val, original_val = None):
    return ( tree_map(type_encode(val), frozenset) ==
             tree_map(type_encode(result_bc_2), frozenset))

make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = backchain_to_goal_tree_2_getargs,
          testanswer = backchain_to_goal_tree_2_testanswer,
          expected_val = str(result_bc_2)
          )


### TEST 13 ###

# This test checks to make sure that your backchainer produces
# the correct goal tree given the hypothesis 'geoff is a giraffe'
# and using the zookeeper_rules.

def backchain_to_goal_tree_3_getargs():
    return [ zookeeper_rules,  'geoff is a giraffe'  ]

result_bc_3 = OR('geoff is a giraffe',
                 AND(OR('geoff is an ungulate',
                        AND(OR('geoff is a mammal',
                               'geoff has hair',
                               'geoff gives milk'),
                            'geoff has hoofs'),
                        AND(OR('geoff is a mammal',
                               'geoff has hair',
                               'geoff gives milk'),
                            'geoff chews cud')),
                     'geoff has long legs',
                     'geoff has long neck',
                     'geoff has tawny color',
                     'geoff has dark spots'))
    
def backchain_to_goal_tree_3_testanswer(val, original_val = None):
    return ( tree_map(type_encode(val), frozenset) ==
             tree_map(type_encode(result_bc_3), frozenset))

make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = backchain_to_goal_tree_3_getargs,
          testanswer = backchain_to_goal_tree_3_testanswer,
          expected_val = str(result_bc_3)
          )

          
### TEST 14 ###

# This test checks to make sure that your backchainer produces
# the correct goal tree given the hypothesis 'gershwin could not
# ask for anything more' and using the rules defined in
# backchain_to_goal_tree_4_getargs() below.

def backchain_to_goal_tree_4_getargs():
    return [ [ IF( AND( '(?x) has (?y)',
                        '(?x) has (?z)' ),
                   THEN( '(?x) has (?y) and (?z)' ) ),
               IF( '(?x) has rhythm and music',
                   THEN( '(?x) could not ask for anything more' ) ) ], 
             'gershwin could not ask for anything more' ]

result_bc_4 = OR('gershwin could not ask for anything more',
                 'gershwin has rhythm and music', 
                 AND('gershwin has rhythm',
                     'gershwin has music'))

def backchain_to_goal_tree_4_testanswer(val, original_val = None):
    return ( tree_map(type_encode(val), frozenset) ==
             tree_map(type_encode(result_bc_4), frozenset) )

make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = backchain_to_goal_tree_4_getargs,
          testanswer = backchain_to_goal_tree_4_testanswer,
          expected_val = str(result_bc_4)
          )
          

### TEST 15 ###

# This test checks to make sure that your backchainer produces
# the correct goal tree given the hypothesis 'zot' and using the
# rules defined in ARBITRARY_EXP below.

ARBITRARY_EXP = (
    IF( AND( 'a (?x)',
             'b (?x)' ),
        THEN( 'c d' '(?x) e' )),
    IF( OR( '(?y) f e',
            '(?y) g' ),
        THEN( 'h (?y) j' )),
    IF( AND( 'h c d j',
             'h i j' ),
        THEN( 'zot' )),
    IF( '(?z) i',
        THEN( 'i (?z)' ))
    )
  
def backchain_to_goal_tree_5_getargs():
    return [ ARBITRARY_EXP, 'zot' ]

result_bc_5 = OR('zot',
                 AND('h c d j',
                     OR('h i j', 'i f e', 'i g', 'g i')))

def backchain_to_goal_tree_5_testanswer(val, original_args = None):
    return ( tree_map(type_encode(val), frozenset) ==
             tree_map(type_encode(result_bc_5), frozenset))

make_test(type = 'FUNCTION_ENCODED_ARGS',
          getargs = backchain_to_goal_tree_5_getargs,
          testanswer = backchain_to_goal_tree_5_testanswer,
          expected_val = str(result_bc_5)
          )
          

### TEST 16 ###

def NAME_testanswer(val, original_val = None):
    return ( isinstance(val, str) and val != '')

make_test(type = 'VALUE',
          getargs = 'NAME',
          testanswer = NAME_testanswer,
          expected_val = '(your name, as a string)',
          name = 'NAME'
          )


### TEST 17 ###

def COLLABORATORS_testanswer(val, original_val = None):
    return isinstance(val, str)

make_test(type = 'VALUE',
          getargs = 'COLLABORATORS',
          testanswer = COLLABORATORS_testanswer,
          expected_val = "(names of people you worked with, as a string, or empty string if you worked alone)",
          name = 'COLLABORATORS'
          )


### TEST 18 ###

def HOW_MANY_HOURS_testanswer(val, original_val = None):
    return isinstance(val, (int, float))

make_test(type = 'VALUE',
          getargs = 'HOW_MANY_HOURS_THIS_LAB_TOOK',
          testanswer = HOW_MANY_HOURS_testanswer,
          expected_val = '(number of hours you spent on this lab, as an int or float)',
          name = 'HOW_MANY_HOURS_THIS_LAB_TOOK'
          )


### TEST 19 ###

def WHAT_I_FOUND_INTERESTING_testanswer(val, original_val = None):
    return isinstance(val, str)

make_test(type = 'VALUE',
          getargs = 'WHAT_I_FOUND_INTERESTING',
          testanswer = WHAT_I_FOUND_INTERESTING_testanswer,
          expected_val = '(an interesting thing)',
          name = 'WHAT_I_FOUND_INTERESTING'
          )


### TEST 20 ###

def WHAT_I_FOUND_BORING_testanswer(val, original_val = None):
    return isinstance(val, str)

make_test(type = 'VALUE',
          getargs = 'WHAT_I_FOUND_BORING',
          testanswer = WHAT_I_FOUND_BORING_testanswer,
          expected_val = '(a boring thing)',
          name = 'WHAT_I_FOUND_BORING'
          )
