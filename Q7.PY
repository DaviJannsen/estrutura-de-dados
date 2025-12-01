from q1ArrayStackQueueDeque import ArrayDeque

if __name__ == "__main__":
    D = ArrayDeque()

    print("Deque inicial:", D._data)

    D.add_first(4)
    print("add_first(4) ->", D._data)

    D.add_last(8)
    print("add_last(8) ->", D._data)

    D.add_last(9)
    print("add_last(9) ->", D._data)

    D.add_first(5)
    print("add_first(5) ->", D._data)

    print("back() =", D.last(), "->", D._data)

    D.delete_first()
    print("delete_first() ->", D._data)

    D.delete_last()
    print("delete_last() ->", D._data)

    D.add_last(7)
    print("add_last(7) ->", D._data)

    print("first() =", D.first(), "->", D._data)
    print("last()  =", D.last(),  "->", D._data)

    D.add_last(6)
    print("add_last(6) ->", D._data)

    D.delete_first()
    print("delete_first() ->", D._data)

    D.delete_first()
    print("delete_first() ->", D._data)

    print("\nDeque final:", D._data)
