from graph.Node import Node


class Graph:
    """
    implantation of a graph for searching
    """
    def __init__(self):
        """
        constructor for the graph
        """
        self.vertices=dict()

    def __contains__(self, aisle):
        """
        checks if the graph contains an aisle
        :param aisle:(String) the aisle name
        :return: true or false
        """
        return aisle in self.vertices.keys()

    def add_value(self, aisle):
        """
        adds aisle to graph
        :param aisle:(String) name of the aisle
        :return: Nothing
        """
        node=Node(aisle)
        self.vertices[aisle]=node

    def connect_undirected(self, aisle, *aisles):
        """
        Makes connections between aisles in the store
        :param aisle:(String) the current Aisle
        :param aisles:(list) the list of an aisles neighboring aisles
        :return: nothing
        """
        node=self.vertices.get(aisle)
        for neighbor in aisles:
            next_aisle=self.vertices.get(neighbor)
            node.add_neighbor(next_aisle)
            next_aisle.add_neighbor(node)

    def dijkstras_shortest_path(self, start_aisle, end_aisle):
        start=self.vertices.get(start_aisle)
        end=self.vertices.get(end_aisle)
        predecessors=dict()
        queue=[]

        for aisle in self.vertices


