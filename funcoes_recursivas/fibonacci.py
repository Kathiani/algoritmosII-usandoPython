def fibonacciv1(lista, n):
   if n!=0:
        print(lista[0] + lista[1])
        lista = [lista[1], lista[0] + lista[1]]
        n = n - 1
        fibonacciv1(lista, n)
   else:
        print("fim da execução da primeira função . . . \n ")


def fibonacci2(n):
    if n <= 1:
        return n
    return fibonacci2(n - 1) + fibonacci2(n - 2)



#chamada da função
fibonacciv1([1, 2], 10)  #fibonacci apenas imprimindo valores na sequência a partir da sequência fornecida

seq = 10
print("Segunda função até o", seq, "-ésimo termo:")
for i in range(seq):
    print(fibonacci2(i), end=" ")