# 6.034 2015: Optional Bayesian Inference Lab

from nets import *


def get_descendants(net, var) :
    "Return a set containing the descendants of var"
    descendants = set()
    children = list(net.get_children(var))

    while len(children) != 0:
        child = children.pop(0)
        descendants.add(child)
        children += list(net.get_children(child))

    return descendants

def get_nondescendants(net, var):
    "Return a set containing the non-descendants of var"
    nondescendants = set()
    parents = list(net.get_parents(var))

    while len(parents) != 0:
        p = children.pop(0)
        descendants.add(p)
        children += list(net.get_parents(p))

    return descendants

def remove_nondescendants_given_parents(net, var, givens):
    """If all parents are given, removes any non-descendants of var (except
    parents) from the list of givens. Otherwise, returns False. Does not modify
    original givens."""
    raise NotImplementedError


def probability_lookup(net, hypothesis, givens=None) :
    "Looks up a probability in the Bayes net."
    raise NotImplementedError

def probability_joint(net, hypothesis) :
    "Uses the chain rule to compute a joint probability"
    raise NotImplementedError

def probability_marginal(net, hypothesis) :
    "Computes a marginal probability as a sum of joint probabilities"
    raise NotImplementedError

def probability_conditional(net, hypothesis, givens=None) :
    "Computes a conditional probability as a ratio of marginal probabilities"
    raise NotImplementedError

def probability(net, hypothesis, givens=None) :
    "Calls previous functions to compute any probability"
    raise NotImplementedError


def number_of_parameters(net) :
    "Computes minimum number of parameters required for net"
    raise NotImplementedError


def is_independent(net, var1, var2, givens=None) :
    """Return True if var1, var2 are conditionally independent given givens,
    otherwise False.  Uses numerical independence only (not structural
    independence)."""
    raise NotImplementedError
