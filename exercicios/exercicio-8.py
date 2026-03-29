class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def insert_or_update(self, key, value):
        current = self.head
        while current:
            if current.key == key:
                current.value = value
                return False
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return True


class HashTableChained:
    max_load_factor = 0.75

    def __init__(self, capacity=8):
        self.capacity = capacity
        self.buckets = [LinkedList() for _ in range(self.capacity)]
        self.num_elements = 0

    def _hash(self, key):
        return key % self.capacity

    def load_factor(self):
        return self.num_elements / self.capacity

    def _rehash(self):
        new_capacity = self.capacity * 2
        new_buckets = [LinkedList() for _ in range(new_capacity)]

        for bucket in self.buckets:
            current = bucket.head
            while current:
                new_idx = current.key % new_capacity
                new_buckets[new_idx].insert_or_update(
                    current.key, current.value)
                current = current.next

        self.capacity = new_capacity
        self.buckets = new_buckets

    def _validate_key(self, key):
        if not isinstance(key, int):
            raise TypeError(f"key must be int, got {type(key).__name__!r}")

    def put(self, key, value):
        self._validate_key(key)
        idx = self._hash(key)
        inserted = self.buckets[idx].insert_or_update(key, value)
        if inserted:
            self.num_elements += 1
        if self.load_factor() > self.max_load_factor:
            self._rehash()

    def get(self, key):
        self._validate_key(key)
        idx = self._hash(key)
        return self.buckets[idx].search(key)

    def __len__(self):
        return self.num_elements


items = [
    (6, 2), (10, 4), (12, 3), (7, 1),
    (8, 3), (15, 5), (3, 1), (20, 6),
    (11, 4), (5, 2), (9, 3), (14, 5),
    (4, 1), (18, 6), (13, 4), (2, 1),
]

knapsack_capacity = 15

recursive_calls = 0
seen_subproblems = set()


def knapsack_recursive(i, remaining_capacity):
    global recursive_calls
    recursive_calls += 1
    seen_subproblems.add((i, remaining_capacity))

    if i == 0 or remaining_capacity == 0:
        return 0

    item_value, item_weight = items[i - 1]

    if item_weight > remaining_capacity:
        return knapsack_recursive(i - 1, remaining_capacity)

    without_item = knapsack_recursive(i - 1, remaining_capacity)
    with_item = item_value + \
        knapsack_recursive(i - 1, remaining_capacity - item_weight)

    return max(without_item, with_item)


memo_calls = 0
cache = HashTableChained()
cached_calls = 0


def knapsack_memoized(i, remaining_capacity):
    global memo_calls, cached_calls
    memo_calls += 1

    key = i * (knapsack_capacity + 1) + remaining_capacity
    cached_result = cache.get(key)
    if cached_result is not None:
        cached_calls += 1
        return cached_result

    if i == 0 or remaining_capacity == 0:
        cache.put(key, 0)
        return 0

    item_value, item_weight = items[i - 1]

    if item_weight > remaining_capacity:
        result = knapsack_memoized(i - 1, remaining_capacity)
    else:
        without_item = knapsack_memoized(i - 1, remaining_capacity)
        with_item = item_value + \
            knapsack_memoized(i - 1, remaining_capacity - item_weight)
        result = max(without_item, with_item)

    cache.put(key, result)
    return result


n = len(items)

print(f"{n} itens (valor, peso)")
print(items)
print(f"capacidade da mochila: {knapsack_capacity}\n")

result_recursive = knapsack_recursive(n, knapsack_capacity)
print("knapsack recursivo")
print(f"- valor máximo: {result_recursive}")
print(f"- chamadas: {recursive_calls}")
print(f"- subproblemas únicos: {len(seen_subproblems)}")
print("- chamadas em cache: -")

result_memo = knapsack_memoized(n, knapsack_capacity)
print("\nknapsack com memoization")
print(f"- valor máximo: {result_memo}")
print(f"- chamadas: {memo_calls}")
print(f"- subproblemas únicos: {len(cache)}")
print(f"- chamadas em cache: {cached_calls}")

reduction = 100 * (1 - memo_calls / recursive_calls)
print(
    f"\nchamadas reduzidas de {recursive_calls} para {memo_calls} ({reduction:.1f}% menos)")
