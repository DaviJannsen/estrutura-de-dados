

class DNode:
    def __init__(self, value, prev=None, nxt=None):
        self.value = value
        self.prev = prev
        self.next = nxt


class DoublyList:
    def __init__(self):
        self.head = None

    def push_back(self, value):
        novo = DNode(value)
        if self.head is None:
            self.head = novo
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = novo
        novo.prev = p

    def show(self):
        elems = []
        p = self.head
        while p is not None:
            elems.append(str(p.value))
            p = p.next
        print(" <-> ".join(elems))

    def remove_duplicados(self):
        p = self.head
        while p is not None:
            q = p.next
            while q is not None:
                if q.value == p.value:
                    nxt = q.next
                    if q.prev is not None:
                        q.prev.next = nxt
                    if nxt is not None:
                        nxt.prev = q.prev
                    q = nxt
                else:
                    q = q.next
            p = p.next


if __name__ == "__main__":
    dl = DoublyList()
    for v in [1, 2, 3, 2, 4, 1, 5, 3]:
        dl.push_back(v)

    print("Antes:")
    dl.show()
    dl.remove_duplicados()
    print("Depois:")
    dl.show()
