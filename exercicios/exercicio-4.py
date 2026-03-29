import random


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
        comparisons = 0
        current = self.head
        while current:
            comparisons += 1
            if current.key == key:
                return current.value, comparisons
            current = current.next
        return None, comparisons

    def insert_or_update(self, key, value):
        comparisons = 0
        current = self.head
        while current:
            comparisons += 1
            if current.key == key:
                current.value = value
                return False, comparisons
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return True, comparisons

    def remove(self, key):
        comparisons = 0
        current = self.head
        prev = None
        while current:
            comparisons += 1
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.size -= 1
                return True, comparisons
            prev = current
            current = current.next
        return False, comparisons


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
        inserted, _ = self.buckets[idx].insert_or_update(key, value)
        if inserted:
            self.num_elements += 1
        if self.load_factor() > self.max_load_factor:
            self._rehash()

    def get(self, key):
        self._validate_key(key)
        idx = self._hash(key)
        value, _ = self.buckets[idx].search(key)
        return value

    def delete(self, key):
        self._validate_key(key)
        idx = self._hash(key)
        removed, _ = self.buckets[idx].remove(key)
        if removed:
            self.num_elements -= 1
        return removed

    def __len__(self):
        return self.num_elements

    def bucket_comparisons(self, key):
        self._validate_key(key)
        idx = self._hash(key)
        _, comp = self.buckets[idx].search(key)
        return comp


table = HashTableChained()

pairs = [
    (10, "Alice"), (20, "Bruno"), (30, "Carla"), (40, "Ana"),
    (50, "Eduardo"), (60, "Fernanda"), (70, "Gustavo"), (80, "Helena"),
    (90, "Igor"), (100, "Julia"),
]

print("TESTE 1 — inserção")
for key, value in pairs:
    table.put(key, value)
    print(f"- put({key:>3}, {value!r:<10}) | elementos: {len(table):>2} | fator de carga: {table.load_factor():.2f}")

print("\nTESTE 2 — busca")
for key, _ in pairs:
    print(f"- get({key:>3}) = {table.get(key)}")

print("\nTESTE 3 — atualização (chave 10)")
print(f"- antes: get(10) = {table.get(10)}")
table.put(10, "Alice Updated")
print(f"- depois: get(10) = {table.get(10)}")

print("\nTESTE 4 — remoção (chave 20)")
print(f"- antes: get(20) = {table.get(20)} | elementos: {len(table)}")
table.delete(20)
print(f"- depois: get(20) = {table.get(20)} | elementos: {len(table)}")

print("\nTESTE 5 — rehash (20 inserções, capacidade inicial 4)")
table2 = HashTableChained(capacity=4)
print(
    f"- capacidade INICIAL: {table2.capacity} | elementos: {len(table2)} | fator de carga: {table2.load_factor():.2f}\n")
test_keys = list(range(1, 8))
for k in test_keys:
    print(f"- inserindo chave {k}...")
    table2.put(k, "value_" + str(k))
    print(
        f"- capacidade atual: {table2.capacity} | elementos: {len(table2)} | fator de carga: {table2.load_factor():.2f}")

print(
    f"\n- capacidade FINAL: {table2.capacity} | elementos: {len(table2)} | fator de carga: {table2.load_factor():.2f}")

print("\n- verificando chaves após rehash:")
for k in test_keys:
    print(f" - get({k}) = {table2.get(k)}")

print("\nTESTE 6 — custo médio de busca por fator de carga")
print(f"\n{'elementos':>9} | {'capacidade':>10} | {'fator de carga':>14} | {'média comparações':>17} | {'comparações esperadas':>21}")

scenarios = [
    (10,  200),
    (25,  200),
    (50,  200),
    (75,  200),
    (100, 200),
    (125, 200),
    (150, 200),
]

for num_elements, capacity in scenarios:
    table3 = HashTableChained(capacity=capacity)

    keys = random.sample(range(capacity * 1000), num_elements)

    for k in keys:
        table3.put(k, k)

    total = sum(table3.bucket_comparisons(k) for k in keys)
    avg = total / num_elements
    load_factor = table3.load_factor()
    print(f"{num_elements:>9} | {capacity:>10} | {load_factor:>14.2f} | {avg:>17.2f} | {1 + load_factor/2:>21.2f}")
