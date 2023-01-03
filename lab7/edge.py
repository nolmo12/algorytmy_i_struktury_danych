from typing import Optional
from vertex import Vertex


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source:'Vertex', destination:'Vertex', weight = None) -> None:
        self.source = source
        self.destination = destination
        self.weight = weight

    #def __eq__(self, other:'Edge') -> bool:
     #   return self.source == other.source and self.destination == other.destination and self.weight == other.weight
