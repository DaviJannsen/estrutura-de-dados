def verifica_parenteses(expr):
    pilha = []

    for char in expr:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if not pilha:
                return False
            pilha.pop()  
    return len(pilha) == 0


exp = "(3 * (2 + 5)) - (8 / (4 - 2))"

print("Expressão:", exp)

if verifica_parenteses(exp):
    print("Resultado: Parênteses bem formados.")
else:
    print("Resultado: Parênteses MAL formados.")
