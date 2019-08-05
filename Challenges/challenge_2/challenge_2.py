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


def find_shortest_path(self, from_vertex, to_vertex):
    """Search for the shortest path from vertex a to b using Breadth first search

    Args:
        from_vertex (str) : starting point on the graph
        to_vertex (str) : the distanation or end of the path
    Returns:
        shortest path (tuple): List of vertices in the path and len
                                Empty list if path does not exist
    """

    if from_vertex not in self.vert_dict or to_vertex not in self.vert_dict:
        raise KeyError(
            "One of the given vertices does not exist in graph!")

    # check if you are at the location
    if from_vertex == to_vertex:
        vert_obj = self.vert_dict[from_vertex]
        return ([vert_obj.data], 0)

    # grab the start location from graph
    current_vertex = self.vert_dict[from_vertex]

    # initialize the queue, visited nodes set, a dictionary to keep track of parent
    queue = Queue(maxsize=len(self.get_vertices()))
    seen_vertex = set()
    parent_pointers = {}

    # start the traversal
    queue.put(current_vertex)
    seen_vertex.add(current_vertex.data)

    path = []
    path_found = False
    parent = None
    current_vertex.parent = parent
    # alternative way of storing the references to parent  pointers
    parent_pointers[current_vertex.data] = None

    while not queue.empty():
        # dequeue the front element
        current_vertex = queue.get()
        path.append(current_vertex)

        # check if we are at destination
        if current_vertex.data == to_vertex:
            path_found = True  # found the goal
            break

        # otherwise
        for neighbor in current_vertex.neighbors:

            if neighbor.data not in seen_vertex:
                queue.put(neighbor)
                seen_vertex.add(neighbor.data)
                neighbor.parent = current_vertex
                parent_pointers[neighbor.data] = current_vertex.data

    if path_found:
        path = []

        while current_vertex is not None:
            path.append(current_vertex.data)
            current_vertex = current_vertex.parent

        return (path[::-1], len(path) - 1)
    # if there is no path from source to destination return -1
    return ([], -1)


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
    """Find a path between two vertices using Depth First Search
    (It is just a path not necessarily the shortest path.)
    """
    if from_vertex not in self.vert_dict or to_vertex not in self.vert_dict:
        raise KeyError(
            "One of the given vertices does not exist in graph!")

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

    graph = construct_graph(sys.argv[1])
    graph_info = grab_graph_info(graph, sys.argv[1])

    print("Vertices:", graph_info[0])
    print("Edges:", graph_info[1])
    print("Edge List:")
    for edge in graph_info[2]:
        print(edge)

    # print(graph_info)
