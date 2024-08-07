from classificacao.reino import Reino
class Filo(Reino):
  
    def __init__(self, reino: str, nutricao: str, organizacao_celular: str,  filo: str, caracteristicas_distintas: str ):
        super().__init__(reino, nutricao, organizacao_celular, )
        self.filo = filo
        self.caracteristicas = caracteristicas_distintas
    def __str__(self):
        return super().__str__() + f', Filo: {self.filo}'