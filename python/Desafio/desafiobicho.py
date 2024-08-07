from classificacao.especie import Especie

cachorro = Especie('Animalia', 'Heterotrófico', 'Multicelular', 'Chordata', 'Espinha dorsal oca percorrida por um cordão nervoso',
                    'Mammalia', 'Uma caracteristicas destintiva dos mamiferos é a presença de glandulas mamárias que produzem leite para alimentar os filhotes',
                      'Carnivora','Que seus membros são carnívoros ou tem uma dieta predominantemente baseada em carne',
                        'Canidae', 'Presença de dentes afiados e adaptados para cortar carne, o que reflete sua adptação como carnívoros',
                        'Canis', 'É sua natureza social e a capacidade de formar laços fortes com outros membros do grupo', 'Canis lupos')  

print(cachorro)


gato = Especie('Animalia', 'Heterotrófico', 'Multicelular',
                'Chordata', '. A principal característica do grupo é a presença da medula espinhal e coluna vertebral.',
                'Mammalia', 'onde inclui uma divisão dos animais que possuem sangue, respiram por pulmões, apresentam dois ventrículos no coração e são vivíparos.',
                'Carnivora', 'Sendo os felinos específicos predadores agéis, com dentes especializados para caprturar e rasgar presas',
                  'Felidae', 'Como os gatos domésticos(Felis catus) e seus parentes selvagens como o leão e o tigre é a presença de garras retráteis',
                'Felis', 'Presença de garras retráteis',
                  'Felis catus')

print(gato)



class Carro:
    def __init__(self, Marca, Cor, Nome) -> None:
        pass
        self.marca = Marca
        self.cor = Cor
        self.nome = Nome
   
    def __str__(self) -> str:
        return 'Marca:', 'Cor:', 'Nome:'
 
    def Ligar(self):
        print('estou ligando ')
 
    def Desligar(self):
        print('estou desligando ')
 
    def Exibirinformacoes(self):
        print(self.marca, self.cor, self.nome)
 
Carro1 = Carro('Range Rover', 'Preta', 'Evoque')
Carro1.Ligar()
Carro1.Desligar()
Carro1.Exibirinfor
