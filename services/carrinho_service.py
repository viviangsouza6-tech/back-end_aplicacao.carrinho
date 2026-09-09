class CarrinhoService:

    def __init__(self, repository):
        self.repository = repository

    def adicionar_produto(self, idpedido, idproduto, quantidade):

        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero")

        return self.repository.adicionar_produto(
            idpedido,
            idproduto,
            quantidade
        )

    def listar_produtos(self, idpedido):

        return self.repository.listar_produtos(idpedido)

    def alterar_quantidade(self, idpedido, idproduto, quantidade):

        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero")

        return self.repository.alterar_quantidade(
            idpedido,
            idproduto,
            quantidade
        )

    def remover_produto(self, idpedido, idproduto):

        return self.repository.remover_produto(
            idpedido,
            idproduto
        )

    def calcular_total(self, idpedido):

        return self.repository.calcular_total(idpedido)