import graphviz
from typing import List, Callable, Union
from queue import *
from linkedlist import *

class Tree:
    def __init__(self, drzewo: 'TreeNode'):
        self.root: 'TreeNode' = drzewo

    def add(self, value: Any, parent_name: Any) -> None:
        if not parent_name:
            raise Exception("Nie prawidłowy rodzic")
        else:
            parent_name.children.append(TreeNode(value))

    def for_each_deep_first(self, visit: Callable[['Tree'], None]) -> None:
        self.root.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['Tree'], None]) -> None:
        self.root.for_each_level_order(visit)

    def show(self, dot):
        return self.root.show(dot)


class TreeNode:
    def __init__(self, value: Any):
        self.value = value
        self.children: List['TreeNode'] = []

    def is_leaf(self) -> bool:
        if len(self.children) == 0:
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
        if visit(self.value):
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
            p = queue.peek()
            queue.dequeue()
            visit(p)
            for x in p.children:
                queue.enqueue(x)

    def search(self, value: Any) -> Union['TreeNode', None]:
        self.for_each_deep_first_search(lambda a: a == value)
        global wezel
        if not wezel:
            return "Nie znaleziono"
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

global wezel
wezel = None
global dot
dot = graphviz.Digraph('Drzewo')

tree=Tree(TreeNode('F'))
a = tree.root.search('F')
tree.add('B', a)
tree.add('G', tree.root.search('F'))
tree.add('I', tree.root.search('G'))
tree.add('H', tree.root.search('I'))
tree.add('A', tree.root.search('B'))
tree.add('D', tree.root.search('B'))
tree.add('C', tree.root.search('D'))
tree.add('E', tree.root.search('D'))

tree.for_each_level_order(print)

print('----------------')

tree.for_each_deep_first(print)

tree.show(dot).render(directory='doctest-output', view=True).replace('\\', '/')

#list.reverse()
