from binary_tree import *

def main():
    drzewo_binarne = BinaryNode(10)
    drzewo_binarne.add_left_child(9)
    drzewo_binarne.add_right_child(2)
    drzewo_binarne.left_child.add_left_child(1)
    drzewo_binarne.left_child.add_right_child(3)
    drzewo_binarne.right_child.add_right_child(6)
    drzewo_binarne.right_child.add_left_child(4)

    drzewo_binarne.traverse_in_order(print)
    print("---------------")
    drzewo_binarne.traverse_post_order(print)
    print("---------------")
    drzewo_binarne.traverse_pre_order(print)

    drzewo = BinaryTree(drzewo_binarne)
    print("---------------")
    drzewo.traverse_pre_order(print)
    print("---------------")
    drzewo.traverse_post_order(print)
    print("---------------")
    drzewo.traverse_in_order(print)

if __name__ == "__main__":
    main()
