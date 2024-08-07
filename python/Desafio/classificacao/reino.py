class Reino:
    def __init__(self, reino: str, nutricao: str, organizacao_celular: str):
        self.reino = reino
        self.nutricao = nutricao
        self.organizacao_celular = organizacao_celular
    def __str__(self) -> str:
        
        return f', Reino: {self.reino}'