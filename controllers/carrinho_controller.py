class CarrinhoController:

    def __init__(self, service):
        self.service = service

    def adicionar_produto(self, idpedido, idproduto, quantidade):

        return self.service.adicionar_produto(
            idpedido,
            idproduto,
            quantidade
        )

    def listar_produtos(self, idpedido):

        return self.service.listar_produtos(idpedido)

    def alterar_quantidade(self, idpedido, idproduto, quantidade):

        return self.service.alterar_quantidade(
            idpedido,
            idproduto,
            quantidade
        )

    def remover_produto(self, idpedido, idproduto):

        return self.service.remover_produto(
            idpedido,
            idproduto
        )

    def calcular_total(self, idpedido):

        return self.service.calcular_total(idpedido)