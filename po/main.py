# carro = {
#     "marca":"VolksWagen",
#     "modelo": "Fusca",
#     "cor": "Azul",
#     "ano": "1945"
# }

# print(carro.get("marca"))

class Veiculo:
    def __init__(self, marca, modelo, cor, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano


fusca = Veiculo("VolksWagen", "Fusca", "Azul", 1945)

class Moto:
    def __init__(self, marca, modelo, cor, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        
        def acelerar(self):
            print('Vraaaaaaaaaau')

        def freiar(self):
            print("RRRRaaannnnnn")

class Carro(Veiculo):
    def abrirPorta(self):
        print("Abriu a porta")

class Moto(Veiculo):
    def empinar(self):
        print("Bololololo")