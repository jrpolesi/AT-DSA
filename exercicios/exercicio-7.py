class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def insert_first(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_last(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def delete_first(self):
        if self.is_empty():
            raise IndexError("lista está vazia")
        value = self.head.value
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return value

    def delete_last(self):
        if self.is_empty():
            raise IndexError("lista está vazia")
        value = self.tail.value
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return value

    def __str__(self):
        parts = []
        current = self.head
        while current:
            parts.append(str(current.value))
            current = current.next
        return " <-> ".join(parts) if parts else "vazia"


class Deque:
    def __init__(self):
        self.list = DoublyLinkedList()

    def is_empty(self):
        return self.list.is_empty()

    def insert_left(self, value):
        self.list.insert_first(value)

    def insert_right(self, value):
        self.list.insert_last(value)

    def remove_left(self):
        return self.list.delete_first()

    def remove_right(self):
        return self.list.delete_last()

    def peek_left(self):
        if self.list.is_empty():
            raise IndexError("deque está vazio")
        return self.list.head.value

    def peek_right(self):
        if self.list.is_empty():
            raise IndexError("deque está vazio")
        return self.list.tail.value

    def __str__(self):
        return str(self.list)


def check_invariants(double_linked_list):
    if double_linked_list.size == 0:
        if not (double_linked_list.head is None and double_linked_list.tail is None):
            raise ValueError("lista vazia deve ter head e tail None")
        return True

    if double_linked_list.head.prev is not None:
        raise ValueError("head.prev deve ser None")
    if double_linked_list.tail.next is not None:
        raise ValueError("tail.next deve ser None")

    current = double_linked_list.head
    count = 0
    while current:
        if current.next and current.next.prev is not current:
            raise ValueError(
                f"ponteiro inconsistente no nó {current.value}: "
                f"current.next={current.next.value}, "
                f"mas current.next.prev={current.next.prev}"
            )
        count += 1
        current = current.next

    if count != double_linked_list.size:
        raise ValueError(
            f"tamanho inconsistente: contado={count}, registrado={double_linked_list.size}"
        )
    return True


print("DoublyLinkedList:")
double_linked_list = DoublyLinkedList()

linked_list_operations = [
    ("insert_last", 1),
    ("insert_last", 2),
    ("insert_last", 3),
    ("insert_first", 0),
    ("delete_first", None),
    ("delete_last", None),
]

for operation, value in linked_list_operations:
    if operation == "insert_last":
        double_linked_list.insert_last(value)
        print(f"\ninsert_last({value}): {double_linked_list}")
    elif operation == "insert_first":
        double_linked_list.insert_first(value)
        print(f"\ninsert_first({value}): {double_linked_list}")
    elif operation == "delete_first":
        removed = double_linked_list.delete_first()
        print(f"\ndelete_first(): {double_linked_list}")
    elif operation == "delete_last":
        removed = double_linked_list.delete_last()
        print(f"\ndelete_last(): {double_linked_list}")

    try:
        check_invariants(double_linked_list)
        print(f"- invariantes ok, tamanho={double_linked_list.size}")
    except ValueError as e:
        print(f"- erro: {e}")

print("\nDeque:")
deque = Deque()

deque_operations = [
    ("insert_right", 10),
    ("insert_right", 20),
    ("insert_left", 5),
    ("insert_left", 1),
    ("remove_left", None),
    ("insert_right", 30),
    ("remove_right", None),
    ("remove_left", None),
    ("insert_left", 99),
    ("remove_right", None),
]

for operation, value in deque_operations:
    if operation == "insert_right":
        deque.insert_right(value)
        print(f"\ninsert_right({value}): {deque}")
    elif operation == "insert_left":
        deque.insert_left(value)
        print(f"\ninsert_left({value}): {deque}")
    elif operation == "remove_left":
        removed = deque.remove_left()
        print(f"\nremove_left(): {deque}")
    elif operation == "remove_right":
        removed = deque.remove_right()
        print(f"\nremove_right(): {deque}")

    try:
        check_invariants(deque.list)
        print(f"- invariantes ok, tamanho={deque.list.size}")
    except ValueError as e:
        print(f"- erro: {e}")

print(f"\npeek_left = {deque.peek_left()}")
print(f"peek_right = {deque.peek_right()}")

print("\nForçando violação:")
broken_linked_list = DoublyLinkedList()
broken_linked_list.insert_last(1)
broken_linked_list.insert_last(2)
broken_linked_list.insert_last(3)
broken_linked_list.head.next.prev = None
try:
    check_invariants(broken_linked_list)
    print("invariantes ok")
except ValueError as e:
    print(f"erro: {e}")
