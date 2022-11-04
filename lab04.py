from typing import Any, List, Callable

from queue import *

from linkedlist import *

class TreeNode:
    def __init__(self, value:Any):
        self.value=value
        self.children=[]

    def is_leaf(self)->bool:
        if(len(self.children)==0):
            return True
        else:
            return False

    def add(self, child:'TreeNode')->None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for x in self.children:
            self.for_each_deep_first(visit)

drzewo=TreeNode(10)
drzewo.add(TreeNode(9))
drzewo.add(TreeNode(8))

drzewo.children[0].add(TreeNode(7))

print(drzewo.children[0].is_leaf())

drzewo.for_each_deep_first(print)

