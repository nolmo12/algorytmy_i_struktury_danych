from binarynode import BinaryNode, print
from typing import Any, Callable, List

class BinarySearchTree:
    root: 'BinaryNode'


    def __init__(self) -> None:
        self.root = None

    def insert(self, value: Any) -> None:
        self.root = self.__insert(self.root, value)

    def __insert(self, node: 'BinaryNode', value: Any) -> 'BinaryNode':
        if node is None:
            return BinaryNode(value)

        if node.value == value:
            return node
        elif node.value < value:
            node.right_child = self.__insert(node.right_child, value)
        else:
            node.left_child = self.__insert(node.left_child, value)

        return node

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def insert_list(self, list_: List[Any]) -> BinaryNode:
        for x in list_:
            self.insert(x)

    def contains(self, value:Any) -> bool:
        temp = self.root

        while True:
            if temp.value == value:
                return True
            if temp.value < value:
                temp = temp.right_child
            else:
                temp = temp.left_child
            if temp is None:
                return False

    def remove(self, value: Any) -> None:
        self.root = self.__remove(self.root, value)

    def __remove(self, node: 'BinaryNode', value: Any) -> None:
        if node is None:
            return node

        if node.value < value:
            node.right_child = self.__remove(node.right_child, value)
        elif node.value > value:
            node.left_child = self.__remove(node.left_child, value)
        else:
            if node.left_child is None:
                temp = node.right_child
                node = None
                return node
            if node.right_child is None:
                temp = node.left_child
                node = None
                return node

            node.value = temp.value

            temp = self.minValueNode(node.right_child)

            node.right_child = self.__remove(node.right_child, temp.value)

        return node

    def minValueNode(self, node) -> BinaryNode:
        temp = node
        while temp.left_child is not None:
            temp = temp.left_child
        return temp

