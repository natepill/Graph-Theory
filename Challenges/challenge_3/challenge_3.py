import sys
from graph import Graph, Vertex, build_graph, read_file


def recursive_depth_first(filename, from_vertex, to_vertex):

    # Build Graph
    graph, vertices, edges = read_file(filename)
    graph = build_graph(graph, vertices, edges)


    # Evaluate Path using DFS recursively
    path = graph.dfs_paths(from_vertex, to_vertex)

    # Does path exist?
    print("A path between vertex {} and {}: {}".format(from_vertex, to_vertex, bool(path)))

    # Print path if it exists
    if path:
        print("Verticies in the path: ", end="")
        for i, vert in enumerate(path[::-1]):
            if i < len(path)-1:
                print(vert, end=",")
            else:
                print(vert)

if __name__ == "__main__":

    filename = sys.argv[1]
    from_vertex = sys.argv[2]
    to_vertex = sys.argv[3]

    recursive_depth_first(filename, from_vertex, to_vertex)
