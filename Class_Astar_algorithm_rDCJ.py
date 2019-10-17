from Class_Astar_Node_rDCJ import Node


class AstarAlgorithm:

    def __init__(self, start_state, end_state):
        self.start_state = start_state
        self.end_state = end_state
        self.start_node = Node(start_state)
        self.target_node = Node(end_state)
        self.Paths = []
        self.Actions = []
        print()
        print('start: ', self.start_node)
        print('end: ', self.target_node)
        print()

    def astar(self, k):
        '''print()
        print('start: ', self.start_node)
        print('end: ', self.target_node)
        print()

        :param k: the maximum number of shortest paths desired as output
        :return: 2 lists. A list of paths and the associated list of actions taken
        '''

        # create start and end node
        start_node = Node(self.start_state, None)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(self.end_state, None)
        end_node.g = end_node.h = end_node.f = 0
        print()
        print('start: ', start_node)
        print('end: ', end_node)
        print()

        # initialize open and closed lists
        open_list = []
        closed_list = []

        # add start_node
        open_list.append(start_node)
        print('open list: ', open_list)

        # loop until find end state
        while len(open_list) > 0:

            # %%%
            # get current node (the node with the lowest f in the openlist)
            current_node = open_list[0]
            print()
            print('current_node: ', current_node)
            print('___________________________________________')
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # remove current node from open list and add it to the closed list
            open_list.pop(current_index)
            closed_list.append(current_node)

            # if the end state is achieved:
            if current_node.is_equivalent(self.end_state):
                path = []
                actions_taken = []
                current = current_node
                while current is not None:
                    path.append(current.state)
                    actions_taken.append(current.parent_operation)
                    current = current.parent

                self.Paths.append(path[::-1])
                self.Actions.append(actions_taken[::-1])
                # return path[::-1], actions_taken[::-1]

                if len(self.Paths) == k:
                    return self.Paths, self.Actions
                # CONTINUE AT %%% PART OF THE CODE

            children = []
            if current_node.next_operation:
                print('     there is a n_O: ', current_node.next_operation)
                new_state = current_node.take_action(current_node.next_operation)
                new_node = Node(new_state, current_node)
                print('     new_node: ', new_node)
                new_node.parent_operation = current_node.next_operation
                children.append(new_node)
                print('     children: ', children)
                print('     **************************')


            else:
                print('     no n_0')

                for operation in current_node.get_legal_operations(self.end_state):
                    print(len(current_node.get_legal_operations(self.end_state)))
                    print()
                    print('         operation: ', operation)

                    new_state = current_node.take_action(operation)
                    new_node = Node(new_state, current_node)
                    print('         new_node: ', new_node)


                    new_node.find_chromosomes(new_node.state)
                    if len(new_node.circular_chromosomes) !=0:
                        print('         cicular chromosome was formed')

                        # get legal reinsertion operation
                        for adjacency in operation[-1]:
                            if adjacency in new_node.circular_chromosomes[0]:
                                circular_join = adjacency
                                potential_operation = new_node.check_if_operation_exists(circular_join, self.end_state)

                                if potential_operation:
                                    print('         legal op exists')
                                    new_node.next_operation = potential_operation
                                    new_node.parent_operation = operation
                                    children.append(new_node)
                                    print('         children: ', children)
                                else:
                                    print('         no legal op exists')
                                    pass
                    else:
                        print('         no circular chromosomes')
                        new_node.parent_operation = operation
                        children.append(new_node)
                        print('         children: ', children)


            print()
            print('looping through children')
            print('CHILDREN:')
            print(children)

            # loop through children
            for child in children:

                # child is on the closed list
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                # calculate f, g, and h values
                child.g = current_node.g + 1
                child.h = child.get_Astar_heuristic(child.state)
                child.f = child.g + child.h

                # child is already in the open list
                # can use hash table hear if run out of memory

                # add child to open list
                open_list.append(child)

        else:
            print('There are fewer solutions than the k specified')
            return self.Paths, self.Actions