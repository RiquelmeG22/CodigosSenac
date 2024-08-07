from classificacao.filo import Filo

class Classe(Filo):
    def __init__(self, reino: str, nutricao: str, organizacao_celular: str,  filo: str, caracteristicas_distintas: str, classe: str, descricao_classe: str):
        super().__init__(reino, nutricao, organizacao_celular,  filo, caracteristicas_distintas)
        self.descricao_classe = descricao_classe
        self.classe = classe
    def __str__(self) -> str:
        return super().__str__() + f', Classe: {self.classe}'