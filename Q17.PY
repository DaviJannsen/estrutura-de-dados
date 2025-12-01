def reverter_lista(head):
    if head is None or head.next is None:
        return head
    novo_head = reverter_lista(head.next)
    head.next.next = head
    head.next = None
    return novo_head
