from graph import Graph
from sortings import topological_sort
from searches import bfs

test_graph = Graph()

for i in range(5):
    test_graph.add_vertex(i)

test_graph.add_edge(4, 3)
test_graph.add_edge(4, 2)
test_graph.add_edge(3, 0)
test_graph.add_edge(0, 2)
test_graph.add_edge(0, 1)
test_graph.add_edge(2, 1)

top = topological_sort(test_graph)
assert top == [4, 3, 0, 2, 1], top

test_graph = Graph()

for i in range(1,9):
    test_graph.add_vertex(i)

test_graph.add_edge(1, 2)
test_graph.add_edge(2, 1)
test_graph.add_edge(1, 4)
test_graph.add_edge(4, 1)
test_graph.add_edge(1, 5)
test_graph.add_edge(5, 1)
test_graph.add_edge(3, 5)
test_graph.add_edge(5, 3)
test_graph.add_edge(5, 7)
test_graph.add_edge(7, 5)
test_graph.add_edge(2, 6)
test_graph.add_edge(6, 2)
test_graph.add_edge(2, 8)
test_graph.add_edge(8, 2)
test_graph.add_edge(6, 8)
test_graph.add_edge(8, 6)

bfs, edges = bfs(test_graph, 1)
print(edges)