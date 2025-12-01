def contar_circular(head):
    if head is None:
        return 0
    atual = head
    cont = 1
    while atual.next != head:
        atual = atual.next
        cont += 1
    return cont
