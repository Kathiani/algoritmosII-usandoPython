#fibonacci apenas imprimindo valores na sequência a partir da sequência fornecida
def fibonacciv1(lista, n):
   if n!=0:
        print(lista[0] + lista[1])
        lista = [lista[1], lista[0] + lista[1]]
        n = n - 1
        fibonacci(lista, n)
   else:
        print("fim da execução")



#chamada da função
fibonacci([1, 2], 10)