class Node:
    """
    Node class for path algorithms
    """

    def __init__(self, aisle):
        """
        constructor for node
        :param aisle:(String) the name of the aisle
        """
        self.aisle=aisle
        self.neighbors=set()

    def get_value(self):
        """
        returns the value(aisle) in the node
        :return:(String) the value(aisle) of the node
        """
        return self.aisle

    def add_neighbor(self, node):
        """
        adds the aisle neighboring aisles
        :param node:(Node) the neighboring node
        :return: Nothing
        """
        self.neighbors.add(node)

    def get_neighbors(self):
        """
        get the node's(aisle's) neighbors
        :return:(set) neighboring aisles
        """
        return self.neighbors