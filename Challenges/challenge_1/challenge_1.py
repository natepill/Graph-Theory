from graph import Graph, Vertex

import sys



def read_graph(filename):
    """ Read and parse file containing Graph information"""

    with open(filename, "r") as file:
        graph_info = file.read().split("/n")

    return graph_info


def construct_graph(filename):
    """ Construct graph based on information in the filename """

    graph_info = read_graph(filename) # parsed graph info file

    type_of_graph = graph_info[0] # Graph or DiGraph
    list_of_verticies = graph_info[1] # Verticies to add to the Graph
    list_of_edges = graph_info[2:] # Describe the edges that connect verticies including possible weight

    # if type_of_graph == "G":

    graph = Graph()

    # Add verticies to the Graph
    for vert in list_of_verticies:
        graph.addVertex(vert)

    # Connect the Verticies with edges
    for edge_tuple in list_of_edges:

        if len(edge_tuple) == 3:
            graph.addEdge(edge_tuple[0], edge_tuple[1], edge_tuple[1])

        if len(edge_tuple) == 2:
            graph.addEdge(edge_tuple[0], edge_tuple[1])







if __name__ == "__main__":
