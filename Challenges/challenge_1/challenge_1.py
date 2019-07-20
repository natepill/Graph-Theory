from graph import Graph, Vertex
import sys


def read_graph(filename):
    """ Read and parse file containing Graph information"""

    with open(filename, "r") as file:
        graph_info = file.read().split("\n")

    # Remove extra new line created by Atom
    del graph_info[-1]

    return graph_info

def parse_edge(edge):

    new_edge = []

    edge = edge.split(',')
    print("edge:",edge)

    for edge_info in edge:

        curr_edge = ''
        for char in edge_info:
            if char == '(' or char == ')':
                continue
            curr_edge += char

        new_edge.append(int(curr_edge))





    print("New_edge:", edge)
    return new_edge


def construct_graph(filename):
    """ Construct graph based on information in the filename """

    graph_info = read_graph(filename) # parsed graph info file

    print("Graph Info:", graph_info)
    print(graph_info[2:])

    type_of_graph = graph_info[0] # Graph or DiGraph
    list_of_verticies = [int(vert) for vert in graph_info[1] if vert.isalnum()] # Verticies to add to the Graph
    # print("graph_info[2:]:", graph_info[2:])
    list_of_edges = [parse_edge(edge) for edge in graph_info[2:]] # Describe the edges that connect verticies including possible weight

    # print("List of Verts:", list_of_verticies)
    print("List of Edges:", list_of_edges)
    # if type_of_graph == "G":

    graph = Graph()

    # Add verticies to the Graph
    for vert in list_of_verticies:
        graph.addVertex(int(vert))

    # Connect the Verticies with edges
    for edge_tuple in list_of_edges:

        if len(edge_tuple) == 3:
            graph.addEdge(edge_tuple[0], edge_tuple[1], edge_tuple[1])

        if len(edge_tuple) == 2:
            graph.addEdge(edge_tuple[0], edge_tuple[1])


    return graph


def grab_graph_info(graph, filename):
    """ Return Tuple object with number of vertices, number of edges, and the Edge List"""

    edge_list = open(filename, 'r').read().split("/n")[2:]
    num_of_edges = len(edge_list)

    return [graph.numVertices, num_of_edges, edge_list]




if __name__ == "__main__":

    graph = construct_graph(sys.argv[1])
    graph_info = grab_graph_info(graph, sys.argv[1])

    print(graph_info)
