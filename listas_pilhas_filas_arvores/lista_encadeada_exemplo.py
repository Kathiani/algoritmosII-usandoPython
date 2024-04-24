class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def inserir_inicio(self, dado):   #inserção sempre no início na lista
        novo_no = No(dado)
        novo_no.proximo = self.primeiro
        self.primeiro = novo_no

    def remover_inicio(self):        #remoção sempre no início na lista
        if self.primeiro is None:
            return None
        dado_removido = self.primeiro.dado
        self.primeiro = self.primeiro.proximo
        return dado_removido

    def imprimir(self):
        atual = self.primeiro
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("None")


# Exemplo de uso
lista = ListaEncadeada()
lista.inserir_inicio(3)
lista.inserir_inicio(7)
lista.inserir_inicio(12)

lista.imprimir()  # Saída: 12 -> 7 -> 3 -> None

lista.remover_inicio()

lista.imprimir()  # Saída: 7 -> 3 -> None
