class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = No(chave)
        else:
            self._inserir_recursivo(chave, self.raiz)

    def _inserir_recursivo(self, chave, no_atual):
        if chave < no_atual.chave:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(chave)
            else:
                self._inserir_recursivo(chave, no_atual.esquerda)
        elif chave > no_atual.chave:
            if no_atual.direita is None:
                no_atual.direita = No(chave)
            else:
                self._inserir_recursivo(chave, no_atual.direita)
        else:
            # Chave já existe na árvore, tratamento opcional
            pass

    def buscar(self, chave):
        return self._buscar_recursivo(chave, self.raiz)

    def _buscar_recursivo(self, chave, no_atual):
        if no_atual is None:
            return False
        if chave == no_atual.chave:
            return True
        elif chave < no_atual.chave:
            return self._buscar_recursivo(chave, no_atual.esquerda)
        else:
            return self._buscar_recursivo(chave, no_atual.direita)

# Exemplo de uso
arvore = ArvoreBinariaBusca()
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)
arvore.inserir(3)
arvore.inserir(7)

print(arvore.buscar(7))  # Saída: True
print(arvore.buscar(11)) # Saída: False

#operações:
#inserção
#remoção
#busca
#travessia