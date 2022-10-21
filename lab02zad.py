from typing import Any

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def print(self):
        temp=self.head
        while(temp):
            if temp.next is None:
                print(temp.data)
            else:
                print(temp.data,"-> ", end="")
            temp=temp.next

    def len(self):
        dlugosc=0
        temp=self.head
        while(temp):
            dlugosc+=1
            temp=temp.next
        return dlugosc

    def push(self, value:Any):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node

    def insert(self, value:Any, after:Node):
        if after is None:
            print("Index jest zły")
            return

        new_node=Node(value)
        new_node.next=after.next
        after.next=new_node

    def append(self, value:Any):
        new_node=Node(value)

        if self.head is None:
            self.head=new_node
            return

        last=self.head
        while(last.next):
            last=last.next

        last.next=new_node

    def pop(self):
        temp=self.head
        if temp is not None:
            self.head=temp.next
            temp=None
            return

    def remove_last(self):
        temp=self.head
        while(temp.next):
            prev=temp
            temp=temp.next
        prev.next=None

    def remove(self, after:Node):
        if after is None:
            print("Error")
            return
        temp=after.next.next
        after.next=temp
    
    def node(self,at:int)->Node:
        pom=self.head
        for x in range(at):
            pom=pom.next
        return pom


class Stack:
    def __init__(self):
            self.storage=LinkedList()

    def push(self, element:Any):
        self.storage.push(element)

    def pop(self)->Any:
        self.storage.pop()

    def print(self):
        temp = self.storage.head
        while (temp):
            if temp.next is None:
                print(temp.data)
            else:
                print(temp.data)
            temp = temp.next

    def len(self):
        dlugosc = 0
        temp = self.head
        while (temp):
            dlugosc += 1
            temp = temp.next
        return dlugosc


class Queue:
    def __init__(self):
            self.storage=LinkedList()

    def peek(self):
        return self.storage.head.data

    def enqueue(self, element:Any):
        self.storage.append(element)

    def dequeue(self):
        self.storage.pop()

    def print(self):
        temp = self.storage.head
        while (temp):
            if temp.next is None:
                 print(temp.data)
            else:
                print(temp.data, ", ", end="")
            temp = temp.next
lista=LinkedList()
lista.push(3)
lista.push(5)
lista.push('a')
lista.insert(2,lista.head)
lista.append(15)
lista.print()
lista.pop()
lista.remove_last()
lista.remove(lista.head)
lista.print()
stos=Stack()
stos.push(5)
stos.push(15)
stos.push(53)
stos.pop()
stos.push(44)
stos.print()
kolejka=Queue()
kolejka.enqueue('klient1')
kolejka.enqueue('klient2')
kolejka.enqueue('klient3')
print(kolejka.peek())
kolejka.print()
kolejka.dequeue()
print(kolejka.peek())
kolejka.print()
