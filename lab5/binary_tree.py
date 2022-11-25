from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self) -> bool:
        return not self.left_child and not self.right_child

    def add_left_child(self, value: Any) -> None:
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any) -> None:
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)

        visit(self)

        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)

        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)

        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self)

        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit)

        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit)


class BinaryTree:
    root: 'BinaryNode'

    def __init__(self, drzewo: 'BinaryNode') -> None:
        self.root = drzewo

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)


f = print


def print(adres: 'TreeNode') -> None:
    if isinstance(adres, BinaryNode):
        f(adres.value)
    else:
        f(adres)
