class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_last(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.size += 1

    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def delete(self, value):
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next
        return False

    def insert_at(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError(
                f"índice {index} fora do intervalo válido (0 - {self.size})")
        if index == 0:
            self.insert_first(value)
            return
        if index == self.size:
            self.insert_last(value)
            return
        new_node = Node(value)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def delete_at(self, index):
        if self.size == 0:
            raise IndexError("lista está vazia")
        if index < 0 or index >= self.size:
            raise IndexError(
                f"índice {index} fora do intervalo válido (0 - {self.size - 1})")
        if index == 0:
            value = self.head.value
            self.head = self.head.next
            self.size -= 1
            return value
        current = self.head
        for _ in range(index - 1):
            current = current.next
        value = current.next.value
        current.next = current.next.next
        self.size -= 1
        return value

    def __len__(self):
        return self.size

    def __str__(self):
        parts = []
        current = self.head
        while current:
            parts.append(str(current.value))
            current = current.next
        return " -> ".join(parts) + " -> None"


linked_list = SinglyLinkedList()

print("insert_last(10), insert_last(30), insert_last(40):")
linked_list.insert_last(10)
linked_list.insert_last(30)
linked_list.insert_last(40)
print(f"{linked_list}")

print("\ninsert_first(0):")
linked_list.insert_first(0)
print(f"{linked_list}")

print("\nsearch(30):", linked_list.search(30))
print("search(99):", linked_list.search(99))

print("\ninsert_at(2, 20):")
linked_list.insert_at(2, 20)
print(f"{linked_list}")

print("\ninsert_at(-1, 50) com índice inválido:")
try:
    linked_list.insert_at(-1, 50)
except IndexError as e:
    print(f"erro: {e}")

print("\ndelete(20):")
linked_list.delete(20)
print(f"{linked_list}")

print("\ndelete_at(1):")
removed = linked_list.delete_at(1)
print(f"removido: {removed}")
print(f"{linked_list}")

print("\ndelete_at(-1) com índice inválido:")
try:
    linked_list.delete_at(-1)
except IndexError as e:
    print(f"erro: {e}")

print("\nmétodo __len__():")
print(f"tamanho: {len(linked_list)}")
