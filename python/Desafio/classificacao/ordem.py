from classificacao.classe import Classe

class Ordem(Classe):
    def __init__(self, reino: str, nutricao: str, organizacao_celular: str,  filo: str, caracteristicas_distintas: str, classe: str, descricao_classe: str, ordem: str, descricao_ordem: str):
        super().__init__(reino, nutricao, organizacao_celular,  filo, caracteristicas_distintas, classe, descricao_classe)
        self.descricao_ordem = descricao_ordem
        self.ordem = ordem
    def __str__(self) -> str:
        return super().__str__() + f', Ordem: {self.ordem}'
