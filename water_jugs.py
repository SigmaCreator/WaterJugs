
visited_states = [] # (Jug3,Jug4)

frontier = []

expansion_counter = 0


class Node :

    def __init__ (self, prev, j3, j4, way) :

        self.prev = prev

        self.value = (j3,j4)

        self.way = way

def fill_3(node) : return Node(node, 3, node.value[1], 'Fill Jug3')

def fill_4(node) : return Node(node, node.value[0], 4, 'Fill Jug4')

def empty_3(node) : return Node(node, 0, node.value[1], 'Empty Jug3')

def empty_4(node) : return Node(node, node.value[0], 0, 'Empty Jug4')

def transfer_3_to_4(node) :

    sum = node.value[0] + node.value[1]

    if  sum <= 4 : return Node(node, 0, sum, 'Transfer Jug3 to Jug4')
    else : return Node(node, sum - 4, 4, 'Transfer Jug3 to Jug4')

def transfer_4_to_3(node) :

    sum = node.value[0] + node.value[1]

    if sum <= 3 : return Node(node, sum, 0, 'Transfer from Jug4 to Jug3')
    else : return Node(node, 3, sum - 3, 'Transfer from Jug4 to Jug3')

def expand(node) :

    next = []

    if node.value[0] != 3 :
        next.append(fill_3(node))

    if node.value[1] != 4 :
        next.append(fill_4(node))

    if node.value[0] != 0 :
        next.append(empty_3(node))
        next.append(transfer_3_to_4(node))

    if node.value[1] != 0 :
        next.append(empty_4(node))
        next.append(transfer_4_to_3(node))

    return next

def get_path(state) :
    if state == None : return ""
    return get_path(state.prev) + " -> [Action: " + state.way + " - State: " + str(state.value) + "]\n"

def goal_test(state) :

    if state[1] == 2 : return True

    return False

def tree_search() :

    global expansion_counter

    frontier.append(Node(None, 1, 1, 'Root'))

    while(True) :

        if len(frontier) == 0 : return "fail"

        current = frontier.pop(0)

        if current.value in visited_states : continue

        visited_states.append(current.value)

        if goal_test(current.value) : return get_path(current)


        next = expand(current)

        frontier.extend(next)


if __name__ == '__main__' :

    print(tree_search())

    print(visited_states)