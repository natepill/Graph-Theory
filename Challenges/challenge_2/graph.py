#!python

class Vertex(object):

    def __init__(self, vertex):
        """Initialize a vertex and its neighbors.
        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}


    def __str__(self):
            """Output the list of neighbors of this vertex."""
            return f'{self.id} adjacent to {[x.id for x in self.neighbors]}'


    def add_neighbor(self, vertex, weight=0):
        """Add a neighbor along a weighted edge."""
        self.neighbors[vertex] = weight


    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return self.neighbors.keys()

    def get_id(self):
        """Return the id of this vertex."""
        return self.id

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        # vertex to the given vertex.
        return self.neighbors[vertex]

    def get_edges(self):
        """Return number of edges of one vertex"""
        return len(self.neighbors.keys())




""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""

# NOTE: id is the key and vertecies are the values
class Graph:
    def __init__(self):
        """Initialize a graph object with an empty dictionary."""
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax: for v in g"""
        return iter(self.vert_dict.values())

    def add_vertex(self, key):
        """Add a new vertex object to the graph with the given key and return the vertex."""
        # increment the number of vertices
        self.num_vertices += 1
        # create a new vertex
        new_vertex = Vertex(key)
        # add the new vertex to the vertex dictionry
        self.vert_dict[key] = new_vertex
        # return the new vertex
        return new_vertex

    def get_vertex(self, key):
        """Return the vertex if it exists"""
        # return the vertex if it is in the graph
        if key in self.vert_dict.keys():
            return key
        else:
            raise ValueError("No vertex found!")

    def add_edge(self, from_vert, to_vert, weight=0):
        """Add an edge from vertex with key `key1` to vertex with key `key2` with a weight."""
        if from_vert not in self.vert_dict or to_vert not in self.vert_dict:
            # add it - or return an error (choice is up to you).
            raise ValueError("One of the key doesn't exist!")
        else:
            # edge by making key2 a neighbor of key1
            # and using the addNeighbor method of the Vertex class.

            self.vert_dict[from_vert].add_neighbor(self.vert_dict[to_vert], weight)
            # self.vert_dict[to_vert].add_neighbor(self.vert_dict[from_vert], weight)

    def get_vertices(self):
        """Return all the vertices in the graph"""
        return self.vert_dict.keys()

    def get_all_edges(self):
        """Return number of all edges in the graph"""
        sum = 0
        for v in self:
            sum += v.get_edges()
        return sum

    def dfs_recursive(self, from_vertex, visited=None, order=None):
        """Traverse the graph and get all vertices using DFS algorithm
        """

        if from_vertex not in self.vert_dict:
            raise KeyError(
                "One of the given vertices does not exist in graph!")

        current_vertex = self.vert_dict[from_vertex]
        # check if its first iteration
        if visited is None and order is None:
            visited = set()
            order = []

        visited.add(current_vertex.data)
        order.append(current_vertex.data)

        for neigbor in current_vertex.neighbors:
            if neigbor.data not in visited:
                self.dfs_recursive(neigbor.data, visited, order=order)

        # print(order)
        return order

    def dfs_paths(self, from_vertex, to_vertex, visited=None):
        """
        Find a path between two vertices using Depth First Search
        """
        if from_vertex not in self.vert_dict or to_vertex not in self.vert_dict:
            raise KeyError("A vertex does not exist")

        # check if you are at the location
        if from_vertex == to_vertex:
            return [from_vertex]
        if visited is None:
            visited = set()
        current_vertex = self.vert_dict[from_vertex]
        visited.add(current_vertex.data)

        for neighbor in current_vertex.neighbors:

            if neighbor.data not in visited:
                path = self.dfs_paths(neighbor.data, to_vertex, visited)
                # print("after path updated")
                if path:
                    path.append(current_vertex.data)
                    return path

        return []






if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.addVertex("Friend 1")
    g.addVertex("Friend 2")
    g.addVertex("Friend 3")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.addEdge("Friend 1", "Friend 2")
    g.addEdge("Friend 2", "Friend 3")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.getVertices(), "\n")

    print("The edges are: ")
    for v in g:
        for w in v.getNeighbors():
            print("( %s , %s )" % (v.getId(), w.getId()))
