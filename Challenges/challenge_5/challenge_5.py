import sys
from graph import Graph, Vertex, build_graph, read_file


def eulerian(filename):

    """ Return wheter or not the graph built from the given file contains a eulerian cycle """

    # read from a file to grab graph properties
    graph, vertices, edges = read_file(filename)
    # builded graph object
    graph = build_graph(graph, vertices, edges)

    eulerian = graph.is_eulerian()

    print("This graph is Eulerian: {}".format(eulerian))

if __name__ == "__main__":
    filename = sys.argv[1]
    eulerian(filename)
