from binarynode import BinaryNode, print
from typing import Any, Callable

class BinarySearchTree:
    root: 'BinaryNode'


    def __init__(self, root: 'BinaryNode') -> None:
        self.root = root

    def insert(self, value: Any) -> None:
        self.root = self.__insert(self.root, value)

    def __insert(self, node: 'BinaryNode', value: Any) -> 'BinaryNode':
        if node is None:
            return BinaryNode(value)
        else:
            if node.value == value:
                return node
            elif node.value < value:
                node.right = self.__insert(node.right, value)
            else:
                node.left = self.__insert(node.left, value)
        return node

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)
