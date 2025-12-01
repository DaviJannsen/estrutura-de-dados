from collections import deque

def eh_palindromo(texto):
    texto_limpo = "".join(ch.lower() for ch in texto if not ch.isspace())
    pilha = []
    fila = deque()

    for ch in texto_limpo:
        pilha.append(ch)
        fila.append(ch)

    while pilha and fila:
        if pilha.pop() != fila.popleft():
            return False
    return True


if __name__ == "__main__":
    s = "arara"
    print("Texto:", s)
    if eh_palindromo(s):
        print("É palíndromo.")
    else:
        print("NÃO é palíndromo.")

    s2 = "estrutura de dados"
    print("\nTexto:", s2)
    if eh_palindromo(s2):
        print("É palíndromo.")
    else:
        print("NÃO é palíndromo.")
