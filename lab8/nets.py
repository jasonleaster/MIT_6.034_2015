from bayes_api import *

# A and B are parents of C
net_basic = BayesNet(list('ABC')).link('A','C').link('B','C')

# A and B disconnected
net_disjoint = BayesNet(list('AB'))

# The Bayes net from the d-separation handout
net_dsep = BayesNet(list('ABCDEFG'))
net_dsep.adjacency = dict(A=set('C'), B=set('C'), C=set('DE'), D=set('F'),
                          F=set('G'))

# The burglar/racoon example from lecture
# see http://courses.csail.mit.edu/6.034f/ai3/bayes.pdf
net_racoon = BayesNet(list('BRDTC'))
net_racoon.adjacency = dict(B=set('D'), R=set('DT'), D=set('C'))
net_racoon.set_probability({'B':True}, {}, 0.1)
net_racoon.set_probability({'R':True}, {}, 0.5)
net_racoon.set_probability({'D':True}, {'B':True, 'R':True}, 0.9)
net_racoon.set_probability({'D':True}, {'B':True, 'R':False}, 0.8)
net_racoon.set_probability({'D':True}, {'B':False, 'R':True}, 0.6)
net_racoon.set_probability({'D':True}, {'B':False, 'R':False}, 0.01)
net_racoon.set_probability({'T':True}, {'R':True}, 0.8)
net_racoon.set_probability({'T':True}, {'R':False}, 0.01)
net_racoon.set_probability({'C':True}, {'D':True}, 0.8)
net_racoon.set_probability({'C':True}, {'D':False}, 0.01)

# net_racoon without probabilities defined
net_racoon_no_probs = net_racoon.copy()
net_racoon_no_probs.conditional_probability_table = []

# A and B are parents of C; A has 3 values, B has 2 values, C has 5 values
net_basic_nonboolean = net_basic.copy()
net_basic_nonboolean.set_domain('A', [1,2,3]).set_domain('C', range(5))

# A and B are structurally independent.
# B and C are numerically independent given A=False.
net_basic_probs = net_basic.copy()
net_basic_probs.set_probability({'A':True}, {}, 0.1)
net_basic_probs.set_probability({'B':True}, {}, 0.55)
net_basic_probs.set_probability({'C':True}, {'A':True, 'B':True}, 0.4)
net_basic_probs.set_probability({'C':True}, {'A':True, 'B':False}, 0.2)
net_basic_probs.set_probability({'C':True}, {'A':False, 'B':True}, 0.3)
net_basic_probs.set_probability({'C':True}, {'A':False, 'B':False}, 0.3)
