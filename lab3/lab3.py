from game_api import *
from boards import *
INF = float('inf')

def is_game_over_connectfour(board) :
    "Returns True if game is over, otherwise False."
    rows = board.num_rows
    cols = board.num_cols
    p = board.board_array

    for i in range(rows):
        for j in range(cols -3):
            if p[i][j] != None:
                if p[i][j] == p[i][j+1] == p[i][j+2] == p[i][j+3]:
                    return True

    for j in range(cols):
        for i in range(rows - 3):
            if p[i][j] != None:
                if p[i][j] == p[i+1][j] == p[i+2][j] == p[i+3][j]:
                    return True

    i = rows - 4
    j = 0
    while (i != 0 or j != cols-4):
        m = i
        n = j
        while m < (rows-3) and n < (cols-3):
            if p[m][n] != None:
                if p[m][n] == p[m+1][n+1] == p[m+2][n+2] == p[m+3][n+3]:
                    return True
            m +=1
            n +=1

        if i != 0:
            i -= 1
        else:
            j += 1

    i = rows - 1
    j = cols - 4
    while (i != 0 or j != 0):
        m = i
        n = j
        while (m-3) >= 0 and (n+3) < cols:
            if p[m][n] != None:
                if p[m][n] == p[m-1][n+1] == p[m-2][n+2] == p[m-3][n+3]:
                    return True
            m -=1
            n +=1

        if j != 0:
            j -= 1
        else:
            i -= 1

    NotFull = False
    for i in range(0, rows):
        for j in range(0, cols):
            if p[i][j] == None:
                NotFull = True
                break
        if NotFull == True:
            break

    if NotFull == False:
        return True

    return False




def next_boards_connectfour(board) :
    """Returns a list of ConnectFourBoard objects that could result from the
    next move, or an empty list if no moves can be made."""
    cols = board.num_cols
    ans = []

    if is_game_over_connectfour(board):
        return ans

    whose_turn = board.whose_turn

    for j in range(cols):
        if not (board.is_column_full(j)):
            new_board = board.copy()
            new_board = new_board.add_piece(j, whose_turn)
            ans.append(new_board)

            if is_game_over_connectfour(new_board):
                return ans
    return ans

def endgame_score_connectfour(board, is_current_player_maximizer) :
    """Given an endgame board, returns 1000 if the maximizer has won,
    -1000 if the minimizer has won, or 0 in case of a tie."""
    if is_current_player_maximizer == False:
        return +1000
    else:
        return -1000

def endgame_score_connectfour_faster(board, is_current_player_maximizer) :
    """Given an endgame board, returns an endgame score with abs(score) >= 1000,
    returning larger absolute scores for winning sooner."""
    Total = board.count_pieces()
    x = board.count_pieces(True)
    y = Total - x 

    if is_current_player_maximizer == False:
        return +1000 * (1.0*y/x)
    else:
        return -1000 * (1.0*y/x)

def heuristic_connectfour(board, is_current_player_maximizer) :
    """Given a non-endgame board, returns a heuristic score with
    abs(score) < 1000, where higher numbers indicate that the board is better
    for the maximizer."""
    chains = board.get_all_chains()
    length = len(chains)

    if is_current_player_maximizer:
        maximizer_chain = board.get_all_chains(True)
        minimizer_chain = board.get_all_chains(False)
    else:
        maximizer_chain = board.get_all_chains(False)
        minimizer_chain = board.get_all_chains(True)

    opt_len_chain_maximizer = max([len(i) for i in maximizer_chain])
    opt_len_chain_minimizer = max([len(i) for i in minimizer_chain])

    F = opt_len_chain_maximizer * opt_len_chain_minimizer * length

    if opt_len_chain_maximizer > opt_len_chain_minimizer:
            return +1000 * 1.0 / F
    elif opt_len_chain_maximizer < opt_len_chain_minimizer:
            return -1000 * 1.0 / F
    elif opt_len_chain_maximizer == opt_len_chain_minimizer:
        if is_current_player_maximizer:
            return +1000 * 1.0/ F
        else:
            return -1000 * 1.0/ F


# Now we can create AbstractGameState objects for Connect Four, using some of
# the functions you implemented above.  You can use the following examples to
# test your dfs and minimax implementations in Part 2.

# This AbstractGameState represents a new ConnectFourBoard, before the game has started:
state_starting_connectfour = AbstractGameState(snapshot = ConnectFourBoard(),
                                 is_game_over_fn = is_game_over_connectfour,
                                 generate_next_states_fn = next_boards_connectfour,
                                 endgame_score_fn = endgame_score_connectfour_faster)

# This AbstractGameState represents the ConnectFourBoard "NEARLY_OVER" from boards.py:
state_NEARLY_OVER = AbstractGameState(snapshot = NEARLY_OVER,
                                 is_game_over_fn = is_game_over_connectfour,
                                 generate_next_states_fn = next_boards_connectfour,
                                 endgame_score_fn = endgame_score_connectfour_faster)

# This AbstractGameState represents the ConnectFourBoard "BOARD_UHOH" from boards.py:
state_UHOH = AbstractGameState(snapshot = BOARD_UHOH,
                                 is_game_over_fn = is_game_over_connectfour,
                                 generate_next_states_fn = next_boards_connectfour,
                                 endgame_score_fn = endgame_score_connectfour_faster)


#### PART 2 ###########################################
# Note: Functions in Part 2 use the AbstractGameState API, not ConnectFourBoard.

def dfs_maximizing(state) :
    """Performs depth-first search to find path with highest endgame score.
    Returns a tuple containing:
     0. the best path (a list of AbstractGameState objects),
     1. the score of the leaf node (a number), and
     2. the number of static evaluations performed (a number)"""

    if state.is_game_over():
        new_score = state.get_endgame_score(is_current_player_maximizer = True)
        return ([state], new_score, 1)
    else:
        best_path = []
        score = 0
        performed = 0
        queue = state.generate_next_states()
        parent = [state]
        while len(queue) != 0:
            state = queue.pop(0)
            (node, new_score, num) = dfs_maximizing(state)
            if new_score > score:
                best_path = parent + node
                score = new_score

            performed += num

        return (best_path, score, performed)



def minimax_endgame_search(state, maximize=True) :
    """Performs minimax search, searching all leaf nodes and statically
    evaluating all endgame scores.  Same return type as dfs_maximizing."""
    if state.is_game_over():
        new_score = state.get_endgame_score(is_current_player_maximizer = True)
        return ([state], new_score, 1)

    performed = 0
    score = 0
    best_path = []
    child = state.generate_next_states()
    parent = [state]

    if maximize == True:
        score = -INF
        for i in child:
            (node, new_score, num) = minimax_endgame_search(i, False)
            if new_score > score:
                score = new_score
                best_path = parent + node

            performed += num
        return (best_path, score, performed)
    else:
        score = +INF

        for i in child:
            (node, new_score, num) = minimax_endgame_search(i, True)
            if new_score < score:
                score = new_score
                best_path = parent + node

            performed += num

        return (best_path, score, performed)


# Uncomment the line below to try your minimax_endgame_search on an
# AbstractGameState representing the ConnectFourBoard "NEARLY_OVER" from boards.py:


#pretty_print_dfs_type(minimax_endgame_search(state_NEARLY_OVER))


def minimax_search(state, heuristic_fn=always_zero, depth_limit=INF, maximize=True) :
    "Performs standard minimax search.  Same return type as dfs_maximizing."

    if state.is_game_over():
        new_score = state.get_endgame_score(is_current_player_maximizer = maximize)
        return ([state], new_score, 1)

    if not (depth_limit):
        new_score = heuristic_fn(state.snapshot, maximize)
        return ([state], new_score, 1)

    performed = 0
    score = 0
    best_path = []
    child = state.generate_next_states()
    parent = [state]

    if maximize == True:
        score = -INF
        for i in child:
            (node, new_score, num) = minimax_search(i, heuristic_fn, depth_limit - 1, False)
            if new_score > score:
                score = new_score
                best_path = parent + node

            performed += num
        return (best_path, score, performed)
    else:
        score = +INF

        for i in child:
            (node, new_score, num) = minimax_search(i, heuristic_fn, depth_limit - 1, True)
            if new_score < score:
                score = new_score
                best_path = parent + node

            performed += num

        return (best_path, score, performed)
        

# Uncomment the line below to try minimax_search with "BOARD_UHOH" and
# depth_limit=1.  Try increasing the value of depth_limit to see what happens:

#pretty_print_dfs_type(minimax_search(state_UHOH, heuristic_fn=heuristic_connectfour, depth_limit=1))


def minimax_search_alphabeta(state, alpha=-INF, beta=INF, heuristic_fn=always_zero,
                             depth_limit=INF, maximize=True) :
    "Performs minimax with alpha-beta pruning.  Same return type as dfs_maximizing."

    if state.is_game_over():
        new_score = state.get_endgame_score(is_current_player_maximizer = maximize)
        return ([state], new_score, 1)

    if not (depth_limit):
        new_score = heuristic_fn(state.snapshot, maximize)
        return ([state], new_score, 1)

    performed = 0
    score = 0
    best_path = []
    child = state.generate_next_states()
    parent = [state]

    if maximize == True:
        score = -INF
        for i in child:
            (node, new_score, num) = minimax_search_alphabeta(i, alpha, beta, heuristic_fn, depth_limit - 1, False)
            if new_score > score:
                score = new_score
                best_path = parent + node

            performed += num

            if score > alpha:
                alpha = score

            if alpha >= beta:
                return (best_path, alpha, performed)

        return (best_path, score, performed)
    else:
        score = +INF

        for i in child:
            (node, new_score, num) = minimax_search_alphabeta(i, alpha, beta, heuristic_fn, depth_limit - 1, True)
            if new_score < score:
                score = new_score
                best_path = parent + node

            performed += num

            if score < beta:
                beta = score

            if alpha >= beta:
                return (best_path, beta, performed)

        return (best_path, score, performed)
        

# Uncomment the line below to try minimax_search_alphabeta with "BOARD_UHOH" and
# depth_limit=4.  Compare with the number of evaluations from minimax_search for
# different values of depth_limit.

#pretty_print_dfs_type(minimax_search_alphabeta(state_UHOH, heuristic_fn=heuristic_connectfour, depth_limit=4))


def progressive_deepening(state, heuristic_fn=always_zero, depth_limit=INF,
                          maximize=True) :
    """Runs minimax with alpha-beta pruning. At each level, updates anytime_value
    with the tuple returned from minimax_search_alphabeta. Returns anytime_value."""
    anytime_value = AnytimeValue()   # TA Note: Use this to store values.
    raise NotImplementedError
    return anytime_value

# Uncomment the line below to try progressive_deepening with "BOARD_UHOH" and
# depth_limit=4.  Compare the total number of evaluations with the number of
# evaluations from minimax_search or minimax_search_alphabeta.

#progressive_deepening(state_UHOH, heuristic_fn=heuristic_connectfour, depth_limit=4).pretty_print()


#### SURVEY ###################################################

NAME = "EOF"
COLLABORATORS = "None"
HOW_MANY_HOURS_THIS_LAB_TOOK = 24
WHAT_I_FOUND_INTERESTING = "Everything in 6.034"
WHAT_I_FOUND_BORING = ""
SUGGESTIONS = "More exercise"


###########################################################
### Ignore everything below this line; for testing only ###
###########################################################

# The following lines are used in the tester. DO NOT CHANGE!

def wrapper_connectfour(board_array, players, whose_turn = None) :
    board = ConnectFourBoard(board_array = board_array,
                             players = players,
                             whose_turn = whose_turn)
    return AbstractGameState(snapshot = board,
                             is_game_over_fn = is_game_over_connectfour,
                             generate_next_states_fn = next_boards_connectfour,
                             endgame_score_fn = endgame_score_connectfour_faster)
