class BinaryTree:
    def __init__(self, value=None):
        self.value = value

        if value is not None:
            self.left = BinaryTree()
            self.right = BinaryTree()
        else:
            self.left = None
            self.right = None

    def insert(self, value):
        if self.value is None:
            self.value = value
            self.left = BinaryTree()
            self.right = BinaryTree()
        elif value < self.value:
            self.left.insert(value)
        elif value > self.value:
            self.right.insert(value)
        elif value == self.value:
            return


class Leaf(BinaryTree):
    def __init__(self, value: int = None):
        super().__init__(value)


def binary_search(node: BinaryTree, value: int):
    if value == node.value:
        return node

    if value > node.value:
        return binary_search(node.right, value)

    if value < node.value:
        return binary_search(node.left, value)


def breadth_first_search(node: BinaryTree, value: int):
    queue = [node]

    while len(queue) > 0:
        node = queue.pop()

        if node.value is value:
            return node

        if node.left.value:
            queue.append(node.left)
        if node.right.value:
            queue.append(node.right)


def depth_first_search(node: BinaryTree, value: int, queue=None):
    if queue is None:
        queue = list()

    if len(queue) == 0:
        queue.append(node)
        current_node = queue[0]
    else:
        current_node = queue.pop()

    if current_node.value == value:
        return current_node

    if current_node.right.value:
        queue.append(current_node.right)
    if current_node.left.value:
        queue.append(current_node.left)

    return depth_first_search(current_node, value, queue)


def print_in_order(node: BinaryTree):
    if node:
        print_in_order(node.left)

        print(node.value)

        print_in_order(node.right)


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


def merge_sort():
    print()


def quick_sort():
    print()


if __name__ == '__main__':
    test()
