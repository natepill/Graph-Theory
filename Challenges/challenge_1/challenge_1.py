import sys
from graphs.graph import Graph, Vertex, build_graph
from graphs.read_file import read_file


def file_to_graph(filename):
    """ Builds and returns a graph based on the content in the filename provided """

    # Read file content and parse graph information
    graph, vertices, edges = read_file(filename)

    # Build graph
    graph = build_graph(graph, vertices, edges)

    return graph


if __name__ == "__main__":

    filename = sys.argv[1]

    file_to_graph()
