from trees.binary_tree import *

def test():
    tree = BinaryTree()

    tree.insert(15)
    tree.insert(17)
    tree.insert(13)
    tree.insert(16)
    tree.insert(11)
    tree.insert(23)
    tree.insert(3)

    # binary_search_result = binary_search(tree, 16)
    # depth_first_search_result = depth_first_search(tree, 16)
    breadth_first_search_result = breadth_first_search(tree, 16)
    # print_in_order(tree)
    print()


if __name__ == '__main__':
    test()
