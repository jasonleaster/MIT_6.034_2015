from constraint_api import *
from test_problems import get_pokemon_problem

#### PART 1: WRITE A DEPTH-FIRST SEARCH CONSTRAINT SOLVER

def has_empty_domains(csp) :
    "Returns True if the problem has one or more empty domains, otherwise False"
    domains = csp.domains

    for i in domains:
        if len(domains[i]) == 0:
            return True

    return False

def check_all_constraints(csp) :
    """Return False if the problem's assigned values violate some constraint,
    otherwise True"""
    constraints = csp.get_all_constraints()
    assigned_values = csp.assigned_values

    for i in constraints:
        if i.var1 in assigned_values and i.var2 in assigned_values:
            if i.check(csp.assigned_values[i.var1], csp.assigned_values[i.var2]) == False:
                return False
    return True

def solve_constraint_dfs(problem) :
    """Solves the problem using depth-first search.  Returns a tuple containing:
    1. the solution (a dictionary mapping variables to assigned values), and
    2. the number of extensions made (the number of problems popped off the agenda).
    If no solution was found, return None as the first element of the tuple."""
    agenda = [problem]
    count = 0
    while len(agenda) != 0:
        csp = agenda.pop(0)
        count += 1

        solvable = True
        for i in csp.domains:
            if len(csp.domains[i]) == 0:
                solvable = False
                break

        if solvable == False:
            continue

        if check_all_constraints(csp) is False:
            continue

        if len(csp.unassigned_vars) == 0:
            return (csp.assigned_values, count)
        else:
            fu_var = csp.pop_next_unassigned_var() # first unassigned variable
            new_problem = []
            for i in csp.get_domain(fu_var):
                csp_new = csp.copy()
                csp_new.set_assigned_value(fu_var, i)
                new_problem.append(csp_new)

            """
            insert the new csp into the front of the agenda
            """
            agenda = new_problem + agenda


    return (None, count)

#### PART 2: DOMAIN REDUCTION BEFORE SEARCH

def eliminate_from_neighbors(csp, var) :
    """Eliminates incompatible values from var's neighbors' domains, modifying
    the original csp.  Returns an alphabetically sorted list of the neighboring
    variables whose domains were reduced, with each variable appearing at most
    once.  If no domains were reduced, returns empty list.
    If a domain is reduced to size 0, quits immediately and returns None."""

    constraints = csp.constraints_between(var)
    ans = set()
    for c in constraints:
        satisfied = False
        satisfied_val = []
        for i in csp.domains[c.var1]:
            for j in csp.domains[c.var2]:
                if c.check(i,j) == True:
                    satisfied_val.append(j)

        if c.var1 == var:
            neighbor = c.var2
        else:
            neighbor = c.var1

        i = 0
        while i < len(csp.domains[neighbor]):
            dom = csp.domains[neighbor]
            if not(dom[i] in satisfied_val):
                csp.eliminate(neighbor, dom[i])
                ans.add(neighbor)
            else:
                i+= 1

    for i in csp.domains:
        if len(csp.domains[i]) == 0:
            return None

    ans = list(ans)
    ans.sort()
    return ans

def domain_reduction(csp, queue=None) :
    """Uses constraints to reduce domains, modifying the original csp.
    If queue is None, initializes propagation queue by adding all variables in
    their default order.  Returns a list of all variables that were dequeued,
    in the order they were removed from the queue.  Variables may appear in the
    list multiple times.
    If a domain is reduced to size 0, quits immediately and returns None."""

    ans = []
    if queue == None:
        queue = csp.get_all_variables()

    while len(queue) != 0:
        var = queue.pop(0)
        ans.append(var)
        constraints = csp.constraints_between(var)
        
        for c in constraints:
            if c.var1 == var:
                neighbor = c.var2
            else:
                neighbor = c.var1

            i = 0
            while i < len(csp.domains[neighbor]):
                l = csp.get_domain(neighbor)
                violate_every_val = True
                for j in csp.domains[var]:
                    if c.check(l[i], j) == True:
                        violate_every_val = False
                        break

                if violate_every_val == True:
                    csp.eliminate(neighbor, l[i])
                    if not (neighbor in queue):
                        queue.append(neighbor)
                        queue.sort()
                else:
                    i += 1
        
        for i in csp.domains:
            if len(csp.domains[i]) == 0:
                return None

    return ans

# QUESTION 1: How many extensions does it take to solve the Pokemon problem
#    with dfs if you DON'T use domain reduction before solving it?

# Hint: Use get_pokemon_problem() to get a new copy of the Pokemon problem
#    each time you want to solve it with a different search method.

ANSWER_1 = 20

# QUESTION 2: How many extensions does it take to solve the Pokemon problem
#    with dfs if you DO use domain reduction before solving it?

ANSWER_2 = 6


#### PART 3: PROPAGATION THROUGH REDUCED DOMAINS

def solve_constraint_propagate_reduced_domains(problem) :
    """Solves the problem using depth-first search with forward checking and
    propagation through all reduced domains.  Same return type as
    solve_constraint_dfs."""

    agenda = [problem]
    count = 0

    while len(agenda) != 0:
        csp = agenda.pop(0)
        count += 1

        solvable = True
        for i in csp.domains:
            if len(csp.domains[i]) == 0:
                solvable = False
                break

        if solvable == False:
            continue

        if check_all_constraints(csp) is False:
            continue

        if len(csp.unassigned_vars) == 0:
            return (csp.assigned_values, count)
        else:
            fu_var = csp.pop_next_unassigned_var() # first unassigned variable
            new_problem = []
            for i in csp.get_domain(fu_var):
                csp_new = csp.copy()
                csp_new.set_assigned_value(fu_var, i)

                # different from dfs() before
                queue = None
                if len(csp_new.assigned_values.keys()) != 0:
                    queue = [x for x in csp_new.assigned_values]

                domain_reduction(csp_new, queue)

                new_problem.append(csp_new)

            agenda = new_problem + agenda 

    return (None, count)

# QUESTION 3: How many extensions does it take to solve the Pokemon problem
#    with propagation through reduced domains? (Don't use domain reduction
#    before solving it.)

ANSWER_3 = 7


#### PART 4: PROPAGATION THROUGH SINGLETON DOMAINS

def domain_reduction_singleton_domains(csp, queue=None) :
    """Uses constraints to reduce domains, modifying the original csp.
    Only propagates through singleton domains.
    Same return type as domain_reduction."""
    ans = []
    if queue == None:
        queue = csp.get_all_variables()

    while len(queue) != 0:
        var = queue.pop(0)
        ans.append(var)
        constraints = csp.constraints_between(var)
        
        for c in constraints:
            if c.var1 == var:
                neighbor = c.var2
            else:
                neighbor = c.var1

            i = 0
            while i < len(csp.domains[neighbor]):
                l = csp.get_domain(neighbor)
                violate_every_val = True
                for j in csp.domains[var]:
                    if c.check(l[i], j) == True:
                        violate_every_val = False
                        break

                if violate_every_val == True:
                    csp.eliminate(neighbor, l[i])
                    if not (neighbor in queue):
                        # modified this 3 lines from domain_reduction()
                        if len (csp.domains[neighbor]) == 1:
                            queue.append(neighbor)
                            queue.sort()
                else:
                    i += 1
        
        for i in csp.domains:
            if len(csp.domains[i]) == 0:
                return None

    return ans

def solve_constraint_propagate_singleton_domains(problem) :
    """Solves the problem using depth-first search with forward checking and
    propagation through singleton domains.  Same return type as
    solve_constraint_dfs."""

    agenda = [problem]
    count = 0
    while len(agenda) != 0:
        csp = agenda.pop(0)
        count += 1

        solvable = True
        for i in csp.domains:
            if len(csp.domains[i]) == 0:
                solvable = False
                break

        if solvable == False:
            continue

        if check_all_constraints(csp) is False:
            continue

        if len(csp.unassigned_vars) == 0:
            return (csp.assigned_values, count)
        else:
            fu_var = csp.pop_next_unassigned_var() # first unassigned variable
            new_problem = []
            for i in csp.get_domain(fu_var):
                csp_new = csp.copy()
                csp_new.set_assigned_value(fu_var, i)

                queue = None
                if len(csp_new.assigned_values.keys()) != 0:
                    queue = [x for x in csp_new.assigned_values]

                domain_reduction_singleton_domains(csp_new, queue)

                new_problem.append(csp_new)

            agenda = new_problem + agenda


    return (None, count)

# QUESTION 4: How many extensions does it take to solve the Pokemon problem
#    with propagation through singleton domains? (Don't use domain reduction
#    before solving it.)

ANSWER_4 = 8


#### PART 5: FORWARD CHECKING

def propagate(enqueue_condition_fn, csp, queue=None) :
    """Uses constraints to reduce domains, modifying the original csp.
    Uses enqueue_condition_fn to determine whether to enqueue a variable whose
    domain has been reduced.  Same return type as domain_reduction."""
    ans = []
    if queue == None:
        queue = csp.get_all_variables()

    while len(queue) != 0:
        var = queue.pop(0)
        ans.append(var)
        constraints = csp.constraints_between(var)
        
        for c in constraints:
            if c.var1 == var:
                neighbor = c.var2
            else:
                neighbor = c.var1

            i = 0
            while i < len(csp.domains[neighbor]):
                l = csp.get_domain(neighbor)
                violate_every_val = True
                for j in csp.domains[var]:
                    if c.check(l[i], j) == True:
                        violate_every_val = False
                        break

                if violate_every_val == True:
                    csp.eliminate(neighbor, l[i])
                    if not (neighbor in queue):
                        if enqueue_condition_fn != None and \
                                enqueue_condition_fn(csp, neighbor):
                            queue.append(neighbor)
                            queue.sort()
                else:
                    i += 1
        
        for i in csp.domains:
            if len(csp.domains[i]) == 0:
                return None

    return ans

def condition_domain_reduction(csp, var) :
    """Returns True if var should be enqueued under the all-reduced-domains
    condition, otherwise False"""
    return True

def condition_singleton(csp, var) :
    """Returns True if var should be enqueued under the singleton-domains
    condition, otherwise False"""
    if len(csp.domains[var]) == 1:
        return True
    else:
        return False

def condition_forward_checking(csp, var) :
    """Returns True if var should be enqueued under the forward-checking
    condition, otherwise False"""
    return False


#### PART 6: GENERIC CSP SOLVER

def solve_constraint_generic(problem, enqueue_condition=None) :
    """Solves the problem, calling propagate with the specified enqueue
    condition (a function).  If enqueue_condition is None, uses DFS only.
    Same return type as solve_constraint_dfs."""

    if not (enqueue_condition is None):
        ans = propagate(enqueue_condition, problem)

    return solve_constraint_dfs(problem)

# QUESTION 5: How many extensions does it take to solve the Pokemon problem
#    with DFS and forward checking, but no propagation? (Don't use domain
#    reduction before solving it.)

ANSWER_5 = None


#### PART 7: DEFINING CUSTOM CONSTRAINTS

def constraint_adjacent(m, n) :
    """Returns True if m and n are adjacent, otherwise False.
    Assume m and n are ints."""
    if abs(m - n) == 1:
        return True
    else:
        return False

def constraint_not_adjacent(m, n) :
    """Returns True if m and n are NOT adjacent, otherwise False.
    Assume m and n are ints."""
    if abs(m - n) != 1:
        return True
    else:
        return False


def all_different(variables) :
    """Returns a list of constraints, with one difference constraint between
    each pair of variables."""
    ans = []
    import constraint_api
    for i in range(len(variables)):
        for j in range(i+1, len(variables)):
            ans.append(Constraint(variables[i], variables[j], constraint_api.constraint_different))

    return ans


#### PART 8: MOOSE PROBLEM (OPTIONAL)

moose_problem = ConstraintSatisfactionProblem(["You", "Moose", "McCain",
                                               "Palin", "Obama", "Biden"])

# Add domains and constraints to your moose_problem here:


# To test your moose_problem AFTER implementing all the solve_constraint
# methods above, change TEST_MOOSE_PROBLEM to True:
TEST_MOOSE_PROBLEM = False


#### SURVEY ###################################################

NAME = "EOF"
COLLABORATORS = "Myself"
HOW_MANY_HOURS_THIS_LAB_TOOK = "Three days"
WHAT_I_FOUND_INTERESTING = "Using domain reduction in DFS"
WHAT_I_FOUND_BORING = "Everything in 6.034 is interesting"
SUGGESTIONS = "More practices"


###########################################################
### Ignore everything below this line; for testing only ###
###########################################################

if TEST_MOOSE_PROBLEM:
    # These lines are used in the local tester iff TEST_MOOSE_PROBLEM is True
    moose_answer_dfs = solve_constraint_dfs(moose_problem.copy())
    moose_answer_propany = solve_constraint_propagate_reduced_domains(moose_problem.copy())
    moose_answer_prop1 = solve_constraint_propagate_singleton_domains(moose_problem.copy())
    moose_answer_generic_dfs = solve_constraint_generic(moose_problem.copy(), None)
    moose_answer_generic_propany = solve_constraint_generic(moose_problem.copy(), condition_domain_reduction)
    moose_answer_generic_prop1 = solve_constraint_generic(moose_problem.copy(), condition_singleton)
    moose_answer_generic_fc = solve_constraint_generic(moose_problem.copy(), condition_forward_checking)
    moose_instance_for_domain_reduction = moose_problem.copy()
    moose_answer_domain_reduction = domain_reduction(moose_instance_for_domain_reduction)
    moose_instance_for_domain_reduction_singleton = moose_problem.copy()
    moose_answer_domain_reduction_singleton = domain_reduction_singleton_domains(moose_instance_for_domain_reduction_singleton)
