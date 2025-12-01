

class Node:
    def __init__(self, element, prev, nxt):
        self.element = element
        self.prev = prev
        self.next = nxt


class DoublyLinkedBase:
    def __init__(self):
        self.header = Node(None, None, None)
        self.trailer = Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def _insert_between(self, e, predecessor, successor):
        novo = Node(e, predecessor, successor)
        predecessor.next = novo
        successor.prev = novo
        self.size += 1
        return novo

    def _delete_node(self, node):
        a = node.prev
        b = node.next
        a.next = b
        b.prev = a
        self.size -= 1
        elem = node.element
        node.prev = node.next = None
        node.element = None
        return elem

    def add_last(self, e):
        return self._insert_between(e, self.trailer.prev, self.trailer)

    def print_list(self):
        p = self.header.next
        while p is not self.trailer:
            print(p.element, end=" ")
            p = p.next
        print()

    def reverse(self):
        left = self.header.next
        right = self.trailer.prev
        while left is not right and left.prev is not right:
            left.element, right.element = right.element, left.element
            left = left.next
            right = right.prev


if __name__ == "__main__":
    lista = DoublyLinkedBase()
    for ch in ["A", "B", "C", "D", "E"]:
        lista.add_last(ch)

    print("Original:")
    lista.print_list()
    lista.reverse()
    print("Reversa:")
    lista.print_list()
