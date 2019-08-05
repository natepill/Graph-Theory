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
    # print("edge:",edge)

    for edge_info in edge:

        curr_edge = ''
        for char in edge_info:
            if char == '(' or char == ')':
                continue
            curr_edge += char

        new_edge.append(int(curr_edge))

    # print("New_edge:", edge)
    return new_edge


def construct_graph(filename):
    """ Construct graph based on information in the filename """

    graph_info = read_graph(filename) # parsed graph info file
    #
    # print("Graph Info:", graph_info)
    # print(graph_info[2:])

    type_of_graph = graph_info[0] # Graph or DiGraph
    list_of_verticies = [int(vert) for vert in graph_info[1] if vert.isalnum()] # Verticies to add to the Graph
    # print("graph_info[2:]:", graph_info[2:])
    list_of_edges = [parse_edge(edge) for edge in graph_info[2:]] # Describe the edges that connect verticies including possible weight

    graph = Graph()

    # Add verticies to the Graph
    for vert in list_of_verticies:
        graph.add_vertex(int(vert))

    # Connect the Verticies with edges
    for edge_list in list_of_edges:

        if len(edge_list) == 3:
            graph.add_edge(edge_list[0], edge_list[1], edge_list[2])

        if len(edge_list) == 2:
            graph.add_edge(edge_list[0], edge_list[1])


    return graph


def grab_graph_info(graph, filename):
    """ Return Tuple object with number of vertices, number of edges, and the Edge List"""

    edge_list = open(filename, 'r').read().split("\n")[2:-1]
    num_of_edges = len(edge_list)

    return [graph.num_vertices, num_of_edges, edge_list]





if __name__ == "__main__":

    graph = construct_graph(sys.argv[1])
    graph_info = grab_graph_info(graph, sys.argv[1])

    print("Vertices:", graph_info[0])
    print("Edges:", graph_info[1])
    print("Edge List:")
    for edge in graph_info[2]:
        print(edge)

    # print(graph_info)
