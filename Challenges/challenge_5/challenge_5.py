import sys
from graph import Graph, Vertex, build_graph, read_file


def main():
    filename = sys.argv[1]
    # read from a file to grab graph properties
    graph, vertices, edges = read_file(filename)
    # builded graph object
    graph = build_graph(graph, vertices, edges)

    eulerian = graph.is_eulerian()
    
    print(f"This graph is Eulerian: {eulerian}")

if __name__ == "__main__":
    main()
