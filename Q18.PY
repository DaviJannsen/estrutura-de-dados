class Node:
    def __init__(self, e, nxt=None):
        self.e = e
        self.next = nxt

def separar_pos_neg(head):
    pos_inicio = pos_fim = None
    neg_inicio = neg_fim = None

    atual = head
    while atual:
        novo = Node(atual.e)

        if atual.e >= 0:
            if pos_inicio is None:
                pos_inicio = pos_fim = novo
            else:
                pos_fim.next = novo
                pos_fim = novo
        else:
            if neg_inicio is None:
                neg_inicio = neg_fim = novo
            else:
                neg_fim.next = novo
                neg_fim = novo

        atual = atual.next

    return pos_inicio, neg_inicio
