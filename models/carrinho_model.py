class Carrinho:
    def __init__(self, idpedido, idpessoa, itens=None):
        self.idpedido = idpedido
        self.idpessoa = idpessoa
        self.itens = itens or []

    def calcular_total(self):
        total = 0

        for item in self.itens:
            total += item["quantidade"] * item["preco_unitario"]

        return total