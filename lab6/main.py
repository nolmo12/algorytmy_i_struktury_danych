from binarysearchtree import *
from binarynode import print


def main():
    bst: BinarySearchTree = BinarySearchTree(BinaryNode(8))
    bst.insert(10)
    bst.insert(14)
    bst.insert(13)
    bst.insert(3)
    bst.insert(6)
    bst.insert(4)
    bst.insert(7)
    bst.insert(1)
    bst.traverse_in_order(print)

if __name__ == '__main__':
    main()
