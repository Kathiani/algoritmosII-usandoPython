def fibonacciv1(lista, n):
   if n!=0:
        print(lista[0] + lista[1])
        lista = [lista[1], lista[0] + lista[1]]
        n = n - 1
        fibonacciv1(lista, n)
   else:
        print("Fim da execução da primeira função . . . \n ")


def fibonacci2(n):
    if n <= 1:
        return n
    else:
        return fibonacci2(n - 1) + fibonacci2(n - 2)



#primeira versão
fibonacciv1([1, 2], 10)  #fibonacci apenas imprimindo valores na sequência a partir da sequência fornecida

#segunda versão
seq = 5     #os n primeiros números (f2)
print("Segunda função fibonacci até o", seq, "-ésimo termo:")
for i in range(seq):
    print(fibonacci2(i), end=" ")
    fibonacci2(i)