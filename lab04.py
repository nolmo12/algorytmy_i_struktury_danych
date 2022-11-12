import graphviz
from typing import List, Callable, Union
from queue import *
from linkedlist import *

global wezel
wezel = None
global dot
dot = graphviz.Digraph('Drzewo')


class Tree:
    def __init__(self, drzewo: 'TreeNode'):
        self.root: 'TreeNode' = drzewo

    def add(self, value: Any, parent_name: Any) -> None:
        parent_name.children.append(TreeNode(value))

    def for_each_deep_first(self, visit: Callable[['Tree'], None]) -> None:
        self.root.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['Tree'], None]) -> None:
        self.root.for_each_level_order(visit)


class TreeNode:
    def __init__(self, value: Any):
        self.value = value
        self.children: List['TreeNode'] = []

    def is_leaf(self) -> bool:
        if len(self.children)==0:
            return True
        else:
            return False

    def add(self, child : 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for x in self.children:
             x.for_each_deep_first(visit)

    def for_each_deep_first_search(self, visit: Callable[['TreeNode'], None]) -> 'TreeNode':
        if visit(self.value) == True:
            global wezel
            wezel = self
            return wezel
        else:
            for x in self.children:
                x.for_each_deep_first_search(visit)
                if wezel:
                    break

    def for_each_level_order(self,visit: Callable[['TreeNode'], None]) -> None:
        queue = Queue()
        queue.enqueue(self)
        while queue.storage.len()>0:
            n = queue.storage.len()
            while n>0:
                p = queue.peek()
                queue.dequeue()
                visit(p)
                for x in range(len(p.children)):
                    queue.enqueue(p.children[x])
                n-=1

    def search(self, value: Any) -> Union['TreeNode', None]:
        self.for_each_deep_first_search(lambda a: a == value)
        global wezel
        wynik = wezel
        wezel = None
        return wynik

    def show(self, dot):
        dot.node(str(self), str(self.value))
        for x in self.children:
            dot.edge(str(self), str(x))
            x.show(dot)
        return dot

f=print

def print(adres:'TreeNode')->None:
    if isinstance(adres, TreeNode):
        f(adres.value)
    else:
        f(adres)

drzewo = TreeNode(1)
drzewo.add(TreeNode(2))
drzewo.add(TreeNode(3))
drzewo.add(TreeNode(4))
drzewo.children[0].add(TreeNode(5))
drzewo.children[0].add(TreeNode(6))
drzewo.children[2].add(TreeNode(7))
drzewo.children[0].children[0].add(TreeNode(8))
drzewo.children[0].children[0].add(TreeNode(9))

drzewo.for_each_deep_first(print)

print("-------")

drzewo.for_each_level_order(print)

a = drzewo.search(4)
b = drzewo.search(6)
caledrzewo = Tree(drzewo)

caledrzewo.add(10, a)
caledrzewo.add(11, b)

drzewo.show(dot).render(directory='doctest-output', view=True).replace('\\', '/')
