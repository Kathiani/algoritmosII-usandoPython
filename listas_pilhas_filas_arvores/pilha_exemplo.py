#As pilhas são usadas em situações em que é necessário rastrear um histórico de operações ou implementar um mecanismo de "desfazer" (undo).
class Pilha():
    def __init__(self):
        self.data = []

#push
    def push(self, x):
        self.data.append(x)   #cada elemento é inserido após o último elemento que foi colocado
#pop
    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(-1)
#top
    def top(self):
            return self.data[-1]   #o último que entra é o primeiro que sai

#empty
    def empty(self):
        return not len(self.data) > 0   #retorna true se a pilha estiver vazia



#Coverter número inteiro para binário
#usando a estrutura de pilha
p = Pilha()
p.push(4)
p.push(5)
p.push(6)
p.push(12)
p.pop()
print(p.data)
