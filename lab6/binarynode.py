from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def min(self) -> 'BinaryNode':
        temp = self
        while temp.left_child is not None:
            temp = temp.left_child

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)


f = print


def print(adres: Any) -> None:
    if isinstance(adres, BinaryNode):
        f(adres.value)
    else:
        f(adres)
