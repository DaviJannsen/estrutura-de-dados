def transfer(S, T):
    
    while S:
        T.append(S.pop())

if __name__ == "__main__":
    S = [1, 2, 3, 4, 5]  
    T = []

    transfer(S, T) 

    print("Pilha S:", S)
    print("Pilha T:", T)
