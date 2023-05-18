from typing import List, Optional
from graph import Graph

def topological_sort(graph: Graph) -> List[Optional[int]]:
    # finds starting source
    source = graph.find_source()  # O(n)
    if source == -1:
        print("The graph is cyclic, can't find a top sort.")
        return []
    top_sort = [source]
    while source != -1 and graph.size > 1:
        out_neighbors = graph.get_sending_neighbors(source)  # O(1)
        total_neighbors = len(out_neighbors)  # O(1)
        for _ in range(total_neighbors):  # O(m)
            graph.remove_edge(source, out_neighbors[0])  # O(1)
        graph.remove_vertex(source)  # O(1)
        source = graph.find_source()
        top_sort.append(source)
    return top_sort