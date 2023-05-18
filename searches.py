from typing import List
from graph import Graph


def bfs(graph: Graph, start: int = 1) -> List[int]:
    iteration = 1
    graph_size = graph.size
    visit_order = [0 for i in range(graph_size+1)]
    parents = [0 if i != start else start for i in range(graph_size+1)]
    edges_visited = []
    queue = [start]
    # sanity check
    if start not in graph.vertexes:
        print(f'Cannot start BFS from vertex {start} \
               since the graph only has {graph_size} vertexes.')
        return
    while queue:
        current = queue.pop(0)
        visit_order[current] = iteration
        possible_sons = graph.get_sending_neighbors(current)
        for son in possible_sons:
            # still does not have a father
            if parents[son] == 0:
                parents[son] = current
            # needs to be visited and not yet in queue
            if visit_order[son] == 0 and son not in queue:
                queue.append(son)
            # checks if edge needs to be visited
            if visit_order[son] != 0:
                edges_visited.append(f'{current} <-> {son}')
        iteration += 1
    return visit_order, edges_visited
