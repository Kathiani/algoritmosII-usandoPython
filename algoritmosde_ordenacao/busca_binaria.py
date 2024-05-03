def busca_binaria(lista, alvo):
    inicio, final = 0, len(lista) - 1

    while inicio <= final:
        meio = (inicio + final) // 2
        valor_meio = lista[meio]
        print("o indice do inicio", inicio, "... e o valor do meio:", lista[meio])

        if valor_meio == alvo:
            return meio
        elif valor_meio < alvo:
            inicio = meio + 1
        else:
            final = meio - 1

    return -1  # Retorna -1 se o elemento não for encontrado

# Exemplo de uso:
lista_ordenada = [2, 5, 7, 10, 12, 15, 20, 23, 45, 67, 87, 90]   #ordenar caso não esteja ordenada
alvo = 67

resultado = busca_binaria(lista_ordenada, alvo)

if resultado != -1:
    print(f'O elemento {alvo} está na posição {resultado}.')
else:
    print(f'O elemento {alvo} não está na lista.')
