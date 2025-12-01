def eh_operador(c):
    return c in {"+", "-", "*", "/", "^"}

def prefixa_para_infixa(expr):
    pilha = []
    for s in reversed(expr.split()):
        if not eh_operador(s):
            pilha.append(s)
        else:
            a = pilha.pop()
            b = pilha.pop()
            pilha.append("(" + a + " " + s + " " + b + ")")
    return pilha[-1]

def prefixa_para_posfixa(expr):
    pilha = []
    for s in reversed(expr.split()):
        if not eh_operador(s):
            pilha.append(s)
        else:
            a = pilha.pop()
            b = pilha.pop()
            pilha.append(a + " " + b + " " + s)
    return pilha[-1]

if __name__ == "__main__":
    pref = "- * A B + C D"
    inf = prefixa_para_infixa(pref)
    pos = prefixa_para_posfixa(pref)
    print("Forma prefixa :", pref)
    print("Forma infixa  :", inf)
    print("Forma pós-fixa:", pos)