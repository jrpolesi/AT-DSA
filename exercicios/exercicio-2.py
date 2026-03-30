import random


def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    copies = 0

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                copies += 3
                swapped = True
        if not swapped:
            break

    return arr, comparisons, copies


def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    copies = 0

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            copies += 3

    return arr, comparisons, copies


def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    copies = 0

    for i in range(1, n):
        key = arr[i]
        copies += 1
        j = i - 1

        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                copies += 1
                j -= 1
            else:
                break

        arr[j + 1] = key
        copies += 1

    return arr, comparisons, copies


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.comparisons = 0
        self.traversal_calls = 0

    # Versão recursiva
    # Ao executar utilizando recursão, recebemos um RecursionError de n >= 1000, pois a call stack do Python atinge seu limite (1000). Seria possível aumentar esse limite usando sys.setrecursionlimit(), mas isso não é recomendado.
    #
    # def insert(self, value):
    #     if self.root is None:
    #         self.root = BSTNode(value)
    #         return
    #     self.insert_recursive(self.root, value)
    #
    # def insert_recursive(self, node, value):
    #     self.comparisons += 1
    #     if value < node.value:
    #         if node.left is None:
    #             node.left = BSTNode(value)
    #         else:
    #             self.insert_recursive(node.left, value)
    #     else:
    #         if node.right is None:
    #             node.right = BSTNode(value)
    #         else:
    #             self.insert_recursive(node.right, value)
    #
    #
    # def inorder(self):
    #     result = []
    #     self.inorder_recursive(self.root, result)
    #     return result
    #
    # def inorder_recursive(self, node, result):
    #     self.traversal_calls += 1
    #     if node is None:
    #         return
    #     self.inorder_recursive(node.left, result)
    #     result.append(node.value)
    #     self.inorder_recursive(node.right, result)

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
            return

        node = self.root
        while True:
            self.comparisons += 1
            if value < node.value:
                if node.left is None:
                    node.left = BSTNode(value)
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = BSTNode(value)
                    return
                node = node.right

    def inorder(self):
        result = []
        stack = []
        node = self.root

        while stack or node:
            self.traversal_calls += 1
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.value)
                node = node.right

        return result


def bst_sort(arr):
    tree = BST()
    for value in arr:
        tree.insert(value)
    result = tree.inorder()
    return result, tree.comparisons, tree.traversal_calls


def generate_sorted_array(n):
    return list(range(n))


def generate_reversed_array(n):
    return list(range(n, 0, -1))


def generate_nearly_sorted_array(n):
    arr = list(range(n))
    num_swaps = max(1, n // 20)

    for _ in range(num_swaps):
        i, j = random.sample(range(n), 2)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


def generate_random_array(n):
    return random.sample(range(n * 10), n)


sizes = [1000, 10_000, 25_000, 50_000]
patterns = ["ordenado", "reverso", "quase ordenado", "aleatório"]

algorithms = [
    ("bubble_sort", bubble_sort),
    ("selection_sort", selection_sort),
    ("insertion_sort", insertion_sort),
    ("bst_sort", bst_sort),
]

for n in sizes:
    arrays = {
        "ordenado": generate_sorted_array(n),
        "reverso": generate_reversed_array(n),
        "quase ordenado": generate_nearly_sorted_array(n),
        "aleatório": generate_random_array(n),
    }

    print(f"\nn = {n}")

    for pattern in patterns:
        results = []

        for algo_name, func in algorithms:
            arr = arrays[pattern][:]
            _, comp, extra = func(arr)
            results.append((algo_name, comp, extra))

        print(f"\n{pattern}:")

        print("resultado por comparação")
        sorted_by_comp = sorted(results, key=lambda x: x[1])
        for i, (algo_name, comp, _) in enumerate(sorted_by_comp, start=1):
            print(f"{i}. {algo_name}: {comp}")

        print("\nresultado por cópia")
        sorted_by_copies = sorted(results, key=lambda x: x[2])
        for i, (algo_name, _, extra) in enumerate(sorted_by_copies, start=1):
            print(f"{i}. {algo_name}: {extra}")
