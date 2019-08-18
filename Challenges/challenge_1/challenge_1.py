import sys
from graph import Graph, Vertex, build_graph, read_file



def file_to_graph(filename):
    """ Builds and returns a graph based on the content in the filename provided """

    # Read file content and parse graph information
    graph, vertices, edges = read_file(filename)

    # Build graph
    graph = build_graph(graph, vertices, edges)



    # Resulting Graph info
    print('Number of vertices: {}'.format(len(graph.get_vertices())))
    print('Number of edges: {}'.format(len(graph.edge_list)))
    print("The Edge List:")

    for edge in graph.get_vertices():
        print(edge)



    return graph


if __name__ == "__main__":

    filename = sys.argv[1]
    file_to_graph(filename)
