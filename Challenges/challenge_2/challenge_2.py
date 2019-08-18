import sys
from graph import Graph, Vertex, build_graph, read_file


def shortest_path(filename, from_vertex, to_vertex):

    # parse file and build graph
    graph, vertices, edges = read_file(filename)
    graph = build_graph(graph, vertices, edges)


    # Finds shortest between two verticies and stores path in array and length of path as an int
    path, path_length = graph.find_shortest_path(from_vertex, to_vertex)


    # If path exists, print the verticies
    if path:
        for i, vert in enumerate(path):
            if i < len(path)-1:
                print(vert, end=", ")
            else:
                print(vert)


if __name__ == "__main__":
    filename = sys.argv[1]
    from_vertex = sys.argv[2]
    to_vertex = sys.argv[3]
    shortest_path(filename, from_vertex, to_vertex)
