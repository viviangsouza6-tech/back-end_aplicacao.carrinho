class CarrinhoRepository:

    def adicionar_produto(
        self,
        idpedido: int,
        idproduto: int,
        quantidade: int
    ):
        pass

    def listar_produtos(
        self,
        idpedido: int
    ):
        pass

    def alterar_quantidade(
        self,
        idpedido: int,
        idproduto: int,
        quantidade: int
    ):
        pass

    def remover_produto(
        self,
        idpedido: int,
        idproduto: int
    ):
        pass

    def calcular_total(
        self,
        idpedido: int
    ):
        pass