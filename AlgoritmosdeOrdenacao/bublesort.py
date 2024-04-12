def bublesort(lista):

    n = len(lista)

    for i in range(n):
            # Últimos i elementos já estão no lugar certo, então não precisamos compará-los novamente
            for j in range(0, n-i-1):
                # Troca se o elemento atual for maior que o próximo
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

# Chamar a função:
lista = [12, 34, 98, 5, 1, 4]
bublesort(lista)
print("Lista ordenada:", lista)
