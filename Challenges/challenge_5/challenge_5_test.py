from graph import Graph, Vertex, build_graph, read_file
import unittest


class EulerianTest(unittest.TestCase):
    def test_lone_vertex(self):
        # Empty graph is not Eularian
        g = Graph(directed=False)

        # Lone Vertex is Eularian
        g.add_vertex('A')
        self.assertEqual(g.is_eulerian(), True)

    def test_separate_subgraphs(self):
        g = Graph(directed=False)

        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')
        g.add_vertex('D')
        g.add_vertex('E')
        g.add_vertex('F')
        g.add_vertex('G')

        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'A')
        g.add_edge('D', 'E')
        g.add_edge('E', 'F')
        g.add_edge('F', 'D')


        # Separate subgraphs still considered Eularian
        self.assertEqual(g.is_eulerian(), True)

        # Odd degrees are not Eularian
        g.add_edge('C', 'D')
        self.assertEqual(g.is_eulerian(), False)

        # Shoud raise error if calling is_eulerian on directed graph
        with self.assertRaises(TypeError):
            g.directed = True
            g.is_eulerian()
            
        with self.assertRaises(TypeError):
            d = Graph(weighted=False, directed=True)
            d.add_vertex("A")
            d.is_eulerian(is_connected=False)


if __name__ == '__main__':
    unittest.main()
