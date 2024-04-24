#As filas são usadas para modelar situações em que os elementos precisam ser processados na ordem em que foram adicionados.
class Fila():
    def __init__(self):
        self.data = []

#push
    def push(self, x):
        self.data.append(x)
#pop
    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(0)   #o primeiro que entra é o primeiro que sai

#empty
    def empty(self):
        return not len(self.data) > 0   #retorna true se a pilha estiver vazia



#Coverter número inteiro para binário
#usando a estrutura de pilha
f = Fila()
f.push(4)
f.push(5)
f.push(6)
f.push(12)
f.pop()
print(f.data)
