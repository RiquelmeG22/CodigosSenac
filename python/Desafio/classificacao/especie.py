from classificacao.genero import Genero


class Especie(Genero):
        def __init__(self, reino: str, nutricao: str, organizacao_celular: str, filo: str, caracteristicas_distintas: str, classe: str, descricao_classe: str, ordem: str, descricao_ordem: str, familia: str, descricao_familia: str, genero: str, descricao_genero: str, especie: str):
            super().__init__(reino, nutricao, organizacao_celular, filo, caracteristicas_distintas, classe, descricao_classe, ordem, descricao_ordem, familia, descricao_familia, genero, descricao_genero)
            self.especie = especie
        def __str__(self) -> str:
            return super().__str__() + f', Especie: {self.especie}'
