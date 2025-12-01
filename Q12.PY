class Node:
    def __init__(self, e, nxt=None):
        self.e = e
        self.next = nxt


class LinkedStack:
    def __init__(self):
        self.topo = None
        self.tam = 0

    def is_empty(self):
        return self.topo is None

    def push(self, e):
        self.topo = Node(e, self.topo)
        self.tam += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Pilha vazia")
        elem = self.topo.e
        self.topo = self.topo.next
        self.tam -= 1
        return elem

    def top(self):
        if self.is_empty():
            raise Exception("Pilha vazia")
        return self.topo.e

    def __len__(self):
        return self.tam

class LinkedQueue:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tam = 0

    def is_empty(self):
        return self.inicio is None

    def enqueue(self, e):
        novo = Node(e)
        if self.is_empty():
            self.inicio = novo
        else:
            self.fim.next = novo
        self.fim = novo
        self.tam += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Fila vazia")
        elem = self.inicio.e
        self.inicio = self.inicio.next
        if self.inicio is None:
            self.fim = None
        self.tam -= 1
        return elem

    def first(self):
        if self.is_empty():
            raise Exception("Fila vazia")
        return self.inicio.e

    def __len__(self):
        return self.tam

class CircularQueue:
    def __init__(self, cap=10):
        self.data = [None] * cap
        self.inicio = 0
        self.tam = 0
        self.cap = cap

    def is_empty(self):
        return self.tam == 0

    def enqueue(self, e):
        if self.tam == self.cap:
            raise Exception("Fila cheia")
        idx = (self.inicio + self.tam) % self.cap
        self.data[idx] = e
        self.tam += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Fila vazia")
        elem = self.data[self.inicio]
        self.data[self.inicio] = None
        self.inicio = (self.inicio + 1) % self.cap
        self.tam -= 1
        return elem

    def first(self):
        if self.is_empty():
            raise Exception("Fila vazia")
        return self.data[self.inicio]

    def __len__(self):
        return self.tam

class DoubleNode:
    def __init__(self, e, prev=None, nxt=None):
        self.e = e
        self.prev = prev
        self.next = nxt


class LinkedDeque:
    def __init__(self):
        self.ini = None
        self.fim = None
        self.tam = 0

    def is_empty(self):
        return self.ini is None

    def add_first(self, e):
        novo = DoubleNode(e, None, self.ini)
        if self.is_empty():
            self.fim = novo
        else:
            self.ini.prev = novo
        self.ini = novo
        self.tam += 1

    def add_last(self, e):
        novo = DoubleNode(e, self.fim, None)
        if self.is_empty():
            self.ini = novo
        else:
            self.fim.next = novo
        self.fim = novo
        self.tam += 1

    def delete_first(self):
        if self.is_empty():
            raise Exception("Deque vazio")
        elem = self.ini.e
        self.ini = self.ini.next
        if self.ini:
            self.ini.prev = None
        else:
            self.fim = None
        self.tam -= 1
        return elem

    def delete_last(self):
        if self.is_empty():
            raise Exception("Deque vazio")
        elem = self.fim.e
        self.fim = self.fim.prev
        if self.fim:
            self.fim.next = None
        else:
            self.ini = None
        self.tam -= 1
        return elem

    def first(self):
        return self.ini.e

    def last(self):
        return self.fim.e

    def __len__(self):
        return self.tam
