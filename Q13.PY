def penultimo_no(head):
    if head is None or head.next is None:
        return None
    atual = head
    while atual.next.next is not None:
        atual = atual.next
    return atual
