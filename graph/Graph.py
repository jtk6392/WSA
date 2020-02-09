import sys

from graph.Node import Node
from graph.PathTuple import PathTuple


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

    def add_values(self, *aisles):
        for aisle in aisles:
            self.add_value(aisle)

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
        """
        Finds the shortest path from start to end with a weight of 1 for each
        :param start_aisle:(String) the starting_aisle
        :param end_aisle:(String) the ending value
        :return: the shortest path
        """

        #initalizing key variable
        start=self.vertices.get(start_aisle)
        end=self.vertices.get(end_aisle)
        predecessors=dict()
        queue=[]

        #builds PathTuples for every aisle and puts them in a queue
        for aisle in self.vertices.values():
            temp=PathTuple(aisle)
            predecessors[aisle]=temp
            queue.append(temp)

        start_tuple=predecessors[start]
        start_tuple.update(None, 0)
        queue.sort(key=PathTuple.get_dist_from_start)

        # goes over every aisle update information for all its neighbors
        while(len(queue)>0):
            next=queue.pop(0)
            if next.get_dist_from_start()==sys.maxsize:
                continue
            next_aisle=next.get_node()
            for neighbor in next_aisle.get_neighbors():
                distance=1+next.get_dist_from_start()
                neighbor_path=predecessors[neighbor]
                neighbor_path.update(next_aisle, distance)
            queue.sort(key=PathTuple.get_dist_from_start)


        next=predecessors[end]
        path=[]

        #builds the path backwards then flips it
        if next.get_predecessor() is not None:
            while(True):
                path.append(next.get_node().get_value())
                if next.get_predecessor() is None:
                    break
                next=predecessors[next.get_predecessor()]

        path.reverse()
        return path

    def store_path(self, start, items):
        """
        Builds the path around the store
        :param start:(String) the starting aisle
        :param items:(list)
        :return: the path to all the items
        """
        path=[]
        shortest_path=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        next=None
        while(items !=[]):
            for ailse in items:
                end=ailse
                temp_path=self.dijkstras_shortest_path(start, end)
                if len(temp_path)<len(shortest_path):
                    shortest_path=temp_path
                    next=end
            path.extend(shortest_path)
            start=next
            items.remove(next)
            shortest_path=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        return path

def scrub_results(list):
