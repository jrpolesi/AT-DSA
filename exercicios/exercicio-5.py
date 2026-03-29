import random


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)


def breadth_traversal(tree):
    if tree.root is None:
        return []

    result = []
    nodes_visited = 0
    queue = Queue()
    queue.enqueue(tree.root)

    while not queue.is_empty():
        node = queue.dequeue()
        result.append(node.value)
        nodes_visited += 1

        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)

    return result, nodes_visited


def depth_traversal(tree):
    if tree.root is None:
        return []

    result = []
    nodes_visited = 0
    stack = Stack()
    stack.push(tree.root)

    while not stack.is_empty():
        node = stack.pop()
        result.append(node.value)
        nodes_visited += 1

        if node.right:
            stack.push(node.right)
        if node.left:
            stack.push(node.left)

    return result, nodes_visited


elements = random.sample(range(1, 1000), 15)

tree = BinarySearchTree()
for e in elements:
    tree.insert(e)

print(f"{len(elements)} elementos inseridos:")
print(elements)

breadth_traversal_result, breadth_traversal_visited = breadth_traversal(tree)
print("\ntraversal em largura (BFS):")
print(f"- visitados: {breadth_traversal_visited}")
print(f"- ordem: {breadth_traversal_result}")

depth_traversal_result, depth_traversal_visited = depth_traversal(tree)
print("\ntraversal em profundidade (DFS):")
print(f"- visitados: {depth_traversal_visited}")
print(f"- ordem: {depth_traversal_result}")
