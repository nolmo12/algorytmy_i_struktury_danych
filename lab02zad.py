#zadanie1
from typing import Any

class Node:
    value: Any
    next: 'Node'

    def __init__(self, value:Any):
        self.value=value
        self.next=None

class LinkedList:
    head: None
    tail: None

    def __init__(self):
        head=None


list_=LinkedList()
list_.head=None

assert list_.head == None
