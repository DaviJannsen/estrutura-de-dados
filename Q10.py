
def eh_operador(c):
    return c in {"+", "-", "*", "/", "^"}

def precedencia(op):
    if op in ("+", "-"):
        return 1
    if op in ("*", "/"):
        return 2
    if op == "^":
        return 3
    return 0

def infixa_para_posfixa(expr):
    saida = []
    pilha = []
    for tok in expr.split():
        if tok.lstrip("-").isdigit():
            saida.append(tok)
        elif tok == "(":
            pilha.append(tok)
        elif tok == ")":
            while pilha and pilha[-1] != "(":
                saida.append(pilha.pop())
            if pilha and pilha[-1] == "(":
                pilha.pop()
        elif eh_operador(tok):
            while pilha and eh_operador(pilha[-1]) and precedencia(pilha[-1]) >= precedencia(tok):
                saida.append(pilha.pop())
            pilha.append(tok)
    while pilha:
        saida.append(pilha.pop())
    return saida

def avalia_posfixa(tokens):
    pilha = []
    for tok in tokens:
        if tok.lstrip("-").isdigit():
            pilha.append(int(tok))
        else:
            b = pilha.pop()
            a = pilha.pop()
            if tok == "+":
                pilha.append(a + b)
            elif tok == "-":
                pilha.append(a - b)
            elif tok == "*":
                pilha.append(a * b)
            elif tok == "/":
                pilha.append(int(a / b))
            elif tok == "^":
                pilha.append(a ** b)
    return pilha[-1]

if __name__ == "__main__":
    expr = "3 + 4 * 2 - ( 10 - 6 )"
    pos = infixa_para_posfixa(expr)
    print("Expressão infixa   :", expr)
    print("Expressão pós-fixa :", " ".join(pos))
    print("Resultado          :", avalia_posfixa(pos))
