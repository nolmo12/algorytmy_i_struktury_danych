from typing import Any

class Vertex:
    data: Any
    index: int

    def __init__(self, value: Any, index: int) -> None:
        self.data = value
        self.index = index