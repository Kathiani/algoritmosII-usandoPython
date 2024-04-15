
def imprimeLista(lista):
    print(lista)
    if len(lista)!= 0:
        imprimeLista(lista[:-1])


#chamando função
imprimeLista([9,8,7,6,5,4,3])