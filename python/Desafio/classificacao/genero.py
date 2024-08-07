from classificacao.familia import Familia

class Genero(Familia):
    def __init__(self, reino: str, nutricao: str, organizacao_celular: str, filo: str, caracteristicas_distintas: str, classe: str, descricao_classe: str,
                  ordem: str, descricao_ordem: str, familia: str, descricao_familia: str, genero: str, descricao_genero: str ):
        super().__init__(reino, nutricao, organizacao_celular, filo, caracteristicas_distintas, classe, descricao_classe, ordem, descricao_ordem, familia, descricao_familia)
        self.descricao_genero = descricao_genero
        self.genero = genero
    def __str__(self) -> str:
        return super().__str__() + f', Genero: {self.genero}'
