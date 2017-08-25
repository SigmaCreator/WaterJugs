
visited_states = []

fringe = []  # (Jug3,Jug4)


def goal_test(state) :

    if state[1] == 2 : return True

    return False


def remove_front(fringe) :

    for state in fringe :
        if state not in visited_states :
            return state


def expand(state) :

    next = []





def tree_search(problem,fringe) :

    fringe.append((0,0))

    while(True) :

        if len(fringe) == 0 : return "failure"

        current = remove_front(fringe)

        if goal_test(current) : return current

        fringe.append


