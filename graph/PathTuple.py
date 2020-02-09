import sys


class PathTuple:
    """
    a new class for dijsktras algorithm
    """

    def __init__(self, node, dist_from_start=sys.maxsize, predecessor=None):
        """
        constructs a new pathTuple
        :param node:(Node) the current aisle
        :param dist_from_start:(int) distance from the start
        :param predecessor:(Node) the node that came before the current node
        """
        self.dist_from_start=dist_from_start
        self.node=node
        self.predecessor=predecessor

    def update(self, node , dist_thru_new_node):
        """
        if the distance to the current node through some new node is shorter than the distance from start
        update the predecessor and distance form start
        :param node:(Node) the new node we are checking the distance through
        :param dist_thru_new_node:(int)
        :return: nothing
        """
        if dist_thru_new_node<self.dist_from_start:
            self.dist_from_start=dist_thru_new_node
            self.predecessor=node

    def get_dist_from_start(self):
        """
        gets the distance from start
        :return: (int) the distance from start
        """
        return self.dist_from_start

    def get_node(self):
        """
        gets the node
        :return: (Node) the current node
        """
        return self.node

    def get_predecessor(self):
        """
        gets the predecessor
        :return: (Node) the predecessor node
        """
        return self.predecessor

    def compare_to(self, path_tuple):
        """
        compares the distance from start to the distance from start of another tuple
        :param path_tuple: (PathTuple) another path tuple
        :return: 0 if equal, positive if larger, negative if smaller
        """
        return self.dist_from_start-path_tuple.get_dist_from_start


