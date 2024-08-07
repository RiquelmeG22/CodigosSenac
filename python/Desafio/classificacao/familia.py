from classificacao.ordem import Ordem

class Familia(Ordem):
    def __init__(self, reino: str, nutricao: str, organizacao_celular: str, filo: str, caracteristicas_distintas: str, classe: str, descricao_classe: str, ordem: str, descricao_ordem: str,\
                 familia: str, descricao_familia: str):
        super().__init__(reino, nutricao, organizacao_celular, filo, caracteristicas_distintas, classe, descricao_classe, ordem, descricao_ordem)
        self.descricao_familia = descricao_familia
        self.familia = familia
    def __str__(self) -> str:
        return super().__str__() + f', Familia: {self.familia}'