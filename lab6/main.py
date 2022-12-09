from binarysearchtree import *


def main():
    bst: BinarySearchTree = BinarySearchTree()
    bst.insert(8)
    bst.insert(10)
    bst.insert(14)
    bst.insert(13)
    bst.insert(3)
    bst.insert(6)
    bst.insert(4)
    bst.insert(7)
    bst.insert(1)

    list = [15, 16, 17, 18]

    bst.insert_list(list)

    bst.traverse_in_order(print)

    print(bst.contains(7))

    bst.remove(7)

    bst.traverse_in_order(print)

if __name__ == '__main__':
    main()
