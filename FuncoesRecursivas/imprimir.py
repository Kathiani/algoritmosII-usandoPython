
def imprimeLista(lista):
    print(lista)
    if len(lista)!= 0:
        imprimeLista(lista[:-1])


#exemplo de chamada da função
imprimeLista([9,8,7,6,5,4,3])