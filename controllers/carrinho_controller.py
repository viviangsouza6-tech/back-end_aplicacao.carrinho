
class CarrinhoController:

    def __init__(self, service):
        self.service = service

    def adicionar_produto(
        self,
        idpessoa: int,
        idproduto: int,
        quantidade: int
    ):
        return self.service.adicionar_produto(
            idpessoa,
            idproduto,
            quantidade
        )

    def listar_produtos(self, idpessoa: int):
        return self.service.listar_produtos(
            idpessoa
        )

    def alterar_quantidade(
        self,
        idpessoa: int,
        idproduto: int,
        quantidade: int
    ):
        return self.service.alterar_quantidade(
            idpessoa,
            idproduto,
            quantidade
        )

    def remover_produto(
        self,
        idpessoa: int,
        idproduto: int
    ):
        return self.service.remover_produto(
            idpessoa,
            idproduto
        )

    def calcular_total(self, idpessoa: int):
        return self.service.calcular_total(
            idpessoa
        )

    def finalizar_carrinho(self, idpessoa: int):
        return self.service.finalizar_carrinho(
            idpessoa
        )

