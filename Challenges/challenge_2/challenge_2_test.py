from graph import Vertex, Graph
import unittest


class VertexTest(unittest.TestCase):


    def test_shortest_path(self):
        graph = Graph(directed=False)

        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_vertex('C')
        graph.add_vertex('D')
        graph.add_vertex('E')
        graph.add_vertex('F')
        graph.add_vertex('G')

        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')
        graph.add_edge('C', 'A')
        graph.add_edge('C', 'D')
        graph.add_edge('D', 'E')
        graph.add_edge('E', 'F')
        graph.add_edge('F', 'D')

        from_vertex = 'A'
        to_vertex = 'D'

        path, path_length = graph.find_shortest_path(from_vertex, to_vertex)

        assert len(path) == 3
