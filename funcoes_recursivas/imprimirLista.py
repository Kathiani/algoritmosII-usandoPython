
def imprime_lista(lista):
    print(lista)
    if len(lista)!= 0:
        imprime_lista(lista[:-1])
    else:
        print("saindo da primeira função imprime!...\n")

def imprime_soma_lista(lista):
    tam = len(lista)
    if tam != 2:
        #print(lista[0])
        #print(lista[-1])
        print(lista[0] + lista[-1])
        imprime_soma_lista(lista[1:-1])
    else:
        print(lista[0] + lista[-1])
        print("saindo da segunda função soma primeiro e último!...")


def imprime_rec(l, i=0):
    if i < len(l):
        print(l[i])
        imprime_rec(l, i+1)
    print("saindo da terceira função imprime lista!...")

#chamadas
lista = [9,8,0,30,10,4,3,5]
imprime_lista(lista)
imprime_soma_lista(lista)
imprime_rec(lista)  #mostrar ordem de chamadas
