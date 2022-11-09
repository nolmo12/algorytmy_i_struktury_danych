from typing import Any, List, Callable, Union
from types import BuiltinFunctionType
from queue import *
from linkedlist import *

global wezel
wezel=None

class Tree:
    def __init__(self, drzewo):
        self.root:'TreeNode'=drzewo

    def add(self, value:Any, parent_name:Any):
        parent_name.children.append(TreeNode(value))

    def for_each_deep_first(self, visit:Callable[['TreeNode'], None]) -> None:
        visit(self)
        for x in self.root.children:
            x.for_each_deep_first(visit)
    def for_each_level_order(self,visit: Callable[['TreeNode'], None]) -> None:
        queue=Queue()
        queue.enqueue(self.root)
        while(queue.storage.len()>0):
            n=queue.storage.len()
            while(n>0):
                p=queue.peek()
                queue.dequeue()
                visit(p)
                for x in range(len(p.children)):
                    queue.enqueue(p.children[x])
                n-=1


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

    def for_each_deep_first_search(self, visit: Callable[['TreeNode'], None]) -> None:
        if(visit(self.value)==True):
            global wezel
            wezel=self
            return wezel
        else:
            for x in self.children:
                x.for_each_deep_first_search(visit)
                if(wezel):
                    break

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for x in self.children:
             x.for_each_deep_first(visit)

    def for_each_level_order(self,visit: Callable[['TreeNode'], None]) -> None:
        queue=Queue()
        queue.enqueue(self)
        while(queue.storage.len()>0):
            n=queue.storage.len()
            while(n>0):
                p=queue.peek()
                queue.dequeue()
                visit(p)
                for x in range(len(p.children)):
                    queue.enqueue(p.children[x])
                n-=1

    def search(self, value:Any) -> Union['TreeNode', None]:
        self.for_each_deep_first_search(lambda a: a == value)
        global wezel
        wynik=wezel
        wezel=None
        return wynik

f=print

def print(adres:'TreeNode')->None:
    if(isinstance(adres, TreeNode)):
        f(adres.value)

drzewo=TreeNode(10)
drzewo.add(TreeNode(9))
drzewo.add(TreeNode(8))

drzewo.children[0].add(TreeNode(7))
drzewo.children[0].children[0].add(TreeNode(5))
drzewo.children[0].add(TreeNode(6))
drzewo.children[1].add(TreeNode(4))
#
# print(drzewo.children[0].is_leaf())
#
# drzewo.for_each_deep_first(print)
#drzewo.for_each_level_order(print)
a=drzewo.search(7)
print(a)
# b=drzewo.search(4)
# print(b)
# c=drzewo.search(122)
# print(c)
# d=drzewo.search(5)
# print(d)
# e=drzewo.search(5)
# print(e)
#drzewo.for_each_level_order(print)
tree=Tree(drzewo)
tree.add(3, a)
#tree.for_each_deep_first(f)
#tree.for_each_level_order(print)
