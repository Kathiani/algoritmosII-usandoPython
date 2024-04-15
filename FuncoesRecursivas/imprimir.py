
def imprimeListaAoContrario(lista):
    print(lista)
    if len(lista)!= 0:
        imprimeListaAoContrario(lista[:-1])


#chamando função
imprimeListaAoContrario([9,8,7,6,5,4])