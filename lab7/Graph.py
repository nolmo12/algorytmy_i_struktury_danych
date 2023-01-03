from edgetype import *
from typing import Dict, List, Callable
from vertex import *
from edge import *
from linkedlist import *


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self) -> None:
        self.adjacencies = {}

    def create_vertex(self, data:Any):
        self.adjacencies[Vertex(data, len(self.adjacencies))] = []

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        edge = Edge(source, destination, weight)
        self.adjacencies[source].append(edge)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        edge = Edge(source, destination, weight)
        edge1 = Edge(destination, source, weight)
        self.adjacencies[source].append(edge)
        self.adjacencies[destination].append(edge1)

    def add(self, edge: 'EdgeType', source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge == EdgeType.directed:
            self.add_directed_edge(source, destination, weight)
        else:
            self.add_undirected_edge(source, destination, weight)

    def traverse_breadth_first(self, visit: Callable[[Any], None]) -> None:
        queue = Queue()
        visited = []

        first_vertex = list(self.adjacencies.keys())[0]

        visited.append(first_vertex)
        queue.enqueue(first_vertex)

        while queue:
            if queue.peek() is not None:
                current_vertex = queue.peek()
                queue.dequeue()
                visit(current_vertex)

            for neighbor in self.adjacencies[current_vertex]:
                if neighbor.destination not in visited:
                    queue.enqueue(neighbor.destination)
                    visited.append(neighbor.destination)

    def traverse_depth_first(self, v: Vertex, visited: List[Vertex], visit: Callable[[Any], None]) -> None:
        visited.append(v)
        visit(v.data)

        for neighbor in self.adjacencies[v]:
            if neighbor.destination not in visited:
                self.traverse_depth_first(neighbor.destination, visited, visit)


    def __str__(self) -> str:
        str = ""
        for key, values in self.adjacencies.items():
            if self.adjacencies[key] == []:
                str+=f"{key.data}\n"
            else:
                lista = self.adjacencies[key]
                last_item = lista[-1]
                str+=f"{key.data}->"
                for x in values:
                    if x == last_item:
                        str+=f"{x.destination.data}"
                    else:
                        str+=f"{x.destination.data}, "
                str+="\n"
        return str

    def print_value(self) -> str:
        return ""
