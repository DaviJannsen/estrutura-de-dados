def concatenar(L, M):
    if L is None:
        return M
    atual = L
    while atual.next is not None:
        atual = atual.next
    atual.next = M
    return L
