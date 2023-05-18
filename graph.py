from typing import List, Tuple, Dict, Any, Union, Optional

class Graph:
    def __init__(self, size: int = 0) -> None:
        self.sending_neighbors = {}
        self.receiving_neighbors = {}
        self.vertexes = []
        self.size = size

    def find_source(self) -> int:
        """
        Find and return a source for a given graph if it exists.
        Return -1 otherwise.
        """
        source = -1
        for vertex in self.vertexes:
            if vertex not in self.receiving_neighbors:
                source = vertex
                break
            elif len(self.receiving_neighbors[vertex]) == 0:
                source = vertex
                break
        return source

    def has_edge(self, origin: int, destination: int) -> bool:
        if destination in self.sending_neighbors[origin]:
            return True
        return False

    def has_vertex(self, vertex: int) -> bool:
        if vertex in self.vertexes:
            return True
        return False
    
    def add_vertex(self, index: int) -> None:
        self.vertexes.append(index)
        self.size += 1

    def remove_vertex(self, index: int) -> None:
        self.vertexes.remove(index)
        self.size -= 1

    def add_edge(self, origin: int, destination: int) -> None:
        if destination not in self.receiving_neighbors:
            self.receiving_neighbors.update({destination: []})
        self.receiving_neighbors[destination].append(origin)
        if origin not in self.sending_neighbors:
            self.sending_neighbors.update({origin: []})
        self.sending_neighbors[origin].append(destination)

    def remove_edge(self, origin: int, destination: int) -> None:
        self.sending_neighbors[origin].remove(destination)
        self.receiving_neighbors[destination].remove(origin)

    def vertex_in_degree(self, vertex: int) -> int:
        return len(self.receiving_neighbors[vertex])
    
    def vertex_out_degree(self, vertex: int) -> int:
        return len(self.sending_neighbors[vertex])

    def get_sending_neighbors(self, vertex: int) -> List[Optional[int]]:
        try:
            neighbors = self.sending_neighbors[vertex]
        except KeyError:
            return []
        return neighbors