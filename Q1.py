class Empty(Exception):
    # Pra quando estiver vazio
    pass 

class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("A pilha está vazia")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("A pilha está vazia")
        return self._data.pop()

class ArrayQueue:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        if self.is_empty():
            raise Empty("A fila está vazia")
        return self._data.pop(0)

    def first(self):
        if self.is_empty():
            raise Empty("A fila está vazia")
        return self._data[0]

class ArrayDeque:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def add_first(self, elemento):
        self._data.insert(0, elemento)

    def add_last(self, elemento):
        self._data.append(elemento)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque vazio")
        return self._data.pop(0)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque vazio")
        return self._data.pop()

    def first(self):
        if self.is_empty():
            raise Empty("Deque vazio")
        return self._data[0]

    def last(self):
        if self.is_empty():
            raise Empty("Deque vazio")
        return self._data[-1]
