class Automoveis:
    def __init__(self,Automoveis: str, nome: str, marca: str, cor: str, Habilitacao: str) -> None:
        self.automoveis = Automoveis
        self.nome = nome
        self.marca = marca
        self.cor = cor 
        self.habilitacao = Habilitacao

    def __str__(self) -> str:
            return f'Automoveis {self.automoveis}, {self.nome}, {self.marca}, {self.cor}, {self.habilitacao}' 
    
class Habilitacao:
    __lista = ['TipoA: Permite conduzir veículos com duas rodas ou três rodas, ou seja, motos, motonetas e triciclos' , 
               'TipoB: Permite a condução de veículos de 4 rodas (carros) com peso total de 35,5 toneladas'
               'TipoC: Permite dirigir veículos de carga (como caminhões e tratores) e veículos agrícolas com mais de 3,5 toneladas e que não passem de 6 toneladas em conjuto, além de todos os descritos na categoria B'
               'TipoD: Permite dirigir todos os veículos dos grupos B e C, além de ônibus, vans e micro-ônibus'
               'TipoE: Permmite dirigir todos os tipos de veículos das outras categorias, exceto da A, além de autorizar que seja acoplada uma carga superior a 6 toneladas, como um veículo com dois reboques, por exemplo']
    def __init__(self, modelo: str = 'A'  'B'  'C'  'D'  'E' 'nenhuma') -> None:
        self.modelo = modelo

    def testeVal(self, hab: str):
        match hab: 
            case 'A':
                return self.modelo == 'A'
            case 'B':
                return self.modelo in ['B', 'C', 'D', 'E']
            case 'C':
                return self.modelo in ['C', 'D', 'E']
            case 'D':
                return self.modelo in ['D', 'E']
            case 'E':
                return self.modelo == 'E'
            case 'nenhuma':
                return True
            
        

class Motocicleta(Automoveis):
    def __init__(self, Automoveis: str, nome: str, marca: str, cor: str, Habilitacao: str, tipodefreio: str) -> None:
        self.tipodefrio = tipodefreio
        super().__init__(Automoveis, nome, marca, cor, Habilitacao)
    def __str__(self) -> str:
        return super().__str__() + f', {self.tipodefrio}'
        

class Caminhão(Automoveis):
    def __init__(self, Automoveis: str, nome: str, marca: str, cor: str, Habilitacao: str,carroceria: str) -> None:
        self.carroceria = carroceria
        super().__init__(Automoveis, nome, marca, cor, Habilitacao)
    def __str__(self) -> str:
        return super().__str__() + f', {self.carroceria}'

class Tracao(Automoveis):
    def __init__(self, Automoveis: str, nome: str, marca: str, cor: str, Habilitacao: str, Tracao: str, motor: str) -> None:
        self.tracao = Tracao
        self.motor = motor
        super().__init__(Automoveis, nome, marca, cor, Habilitacao)
    def __str__(self) -> str:
        return super().__str__() + f', {self.tracao}, {self.motor}'


class Especial(Automoveis):
    def __init__(self, Automoveis: str, nome: str, marca: str, cor: str, Habilitacao: str, Especial: str, farol: str) -> None:
        self.especial = Especial
        self.farol = farol
        super().__init__(Automoveis, nome, marca, cor, Habilitacao)
    def __str__(self) -> str:
        return super().__str__() + f', {self.especial}, {self.farol}'


class Aluguel(Automoveis):
    def __init__(self, Automoveis: str, nome: str, marca: str, cor: str, Habilitacao: str, Aluguel: str, passageiros: str) -> None:
        self.aluguel = Aluguel
        self.passageiros = passageiros
        super().__init__(Automoveis, nome, marca, cor, Habilitacao)
    def __str__(self) -> str:
        return super().__str__() + f', {self.aluguel}, {self.automoveis}'


class Colecao(Automoveis):
    def __init__(self, Automoveis: str, nome: str, marca: str, cor: str, Habilitacao: str, Colecao: str, ano: str) -> None:
        self.colecao = Colecao
        self.ano = ano
        super().__init__(Automoveis, nome, marca, cor, Habilitacao)
    def __str__(self) -> str:
        return super().__str__() + f', {self.colecao}, {self.ano}'



moto = Motocicleta('Moto', 'Xre', 'Honda', 'Preta', 'A', 'Abs' )
pcx = Motocicleta('Moto', 'Pcx', 'Honda', 'Azul', 'A', 'Kit Pastilha D Freio Diafrag Honda Pcx 150 2019 A 2022 C/abs')
adv = Motocicleta('Moto', 'Adv', 'Honda', 'Vermelha', 'A', 'Kit Pastilha De Freio Potenza Honda Adv 150 Ano 2021-2022')
bmw = Motocicleta('Moto', 'F-800 GS', 'BMW', 'Verde', 'A', 'Pastilha De Freio Sinterizada Potenza Bmw F 800gs')
bmw1200 = Motocicleta('Moto', 'R-1200', 'BWM', 'Cinza', 'A', 'Pastilha Freio Dianteiro Bmw R 1200 Gs Lc 2015-2019')
fazer = Motocicleta('Moto', 'Fazer', 'Yamaha', 'Preta', 'A', 'Pinça Freio Traseira Fazer Ys 250 2011 2012 2013 2014')
quadriciclo = Motocicleta('Quadriciclo', 'Atv', 'Tander', 'Azul', 'A', 'Freio a disco' )
caminhao = Caminhão('Caminhão', '1513', 'Mercedes-Benz', 'Preta', 'E', 'Boiadeiro' )
reboque = Caminhão('Caminhão', 'Vw', 'Volkswagen', 'Branco', 'E', 'Platarforma, asa delta' )
frios = Caminhão('Caminhão', 'Vw Constalation 30.330 Prime', 'Volkswagen', 'Branco', 'E', 'Câmara Fria')
trator = Tracao('Trator', 'TL5.80', 'New Holland', 'Azul', 'C', 'Trator de rodas', 'Motores FPT S8000' )
esteira = Tracao('Trator', '700J-II', 'John Deere', 'Amarelo', 'C', 'Trator de esteira', '93 kW (125 HP) a 1.800 rpm' )
colheitadeira = Tracao('Colheidateira', 'S790', 'John Deere', 'Verde', 'Colhedateira de milho', 'C', 'PowerTech Plus de 9 L (549 pol³) e 13,5 L (824 pol³' )
viatura = Especial('Carro', 'Corrola', 'Toyota', 'Preta', 'B', 'Viatura', 'Farol toyota corolla Masc Negra' )
ambulancia = Especial('Van', 'Sprinter 19+1', 'Mercedes-Benz', 'Brancos', 'B', 'Ambulância', 'Farol Sprinter 2019 Com Auxiliar Preto' )
funerario = Especial('Carro', 'Montana', 'Chevrolet', 'Preta', 'B', 'Carros Funerários', 'Farol Agile Montana 2009 2010 11 12 13 14 Foco Duplo Cromado')
pax = Especial('Carro', 'Spin', 'Chevrolet', 'Branco', 'B', 'Carro Funerário', 'Farol Chevrolet Spin 2019 2020 2021 2022 2023 2024 Com Led')
toro = Especial('Carro', 'Toro', 'Fiat', 'Vermelha', 'B', 'Carro Funerário', 'Farol Direito Fiat Toro Led Novo Original 2019/2023')
strada = Especial('Carro', 'Strada', 'Chevrolet', 'Cinza', 'B', 'Carro Funerário', 'Par Farol Strada Working 2014 2015 2016 2017 2018 2019')
saveiro = Especial('Carro', 'Saveiro', 'Volkswagen', 'Branco', 'B', 'Carro Funerário', 'Farol vw saveiro 2020 foco simples') 


oi = [moto,quadriciclo,caminhao,reboque,frios,trator,esteira,colheitadeira,viatura,ambulancia,funerario,pax,toro,strada,saveiro,pcx,adv,bmw,bmw1200,fazer]
selecionadas = []

while True:
    p1 = input('Qual veículo você deseja ultizar ? moto, caminhao, trator, ambulância, viatura, funerario ?')
    if p1 in ['moto', 'caminhao', 'trator', 'ambulância', 'viatura', 'funerario',]:
        break

match p1:
    case 'moto':
        for item in oi:
            if isinstance(item,Motocicleta):
                selecionadas.append(item)
    
    case 'caminhao':
        for item in oi:
            if isinstance(item,Caminhão):
                selecionadas.append(item)

    case 'trator':
        for item in oi:
            if isinstance(item,Tracao):
                selecionadas.append(item)

    case 'ambulância':
        for item in oi:
            if isinstance(item,Especial):
                if item.especial == 'Ambulância':
                    selecionadas.append(item)

    case 'viatura':
         for item in oi:
            if isinstance(item,Especial):
                if item.especial == 'Viatura':
                    selecionadas.append(item)

    case 'funerario':
         for item in oi:
            if isinstance(item,Especial):
                if item.especial == 'Carro Funerário':
                    selecionadas.append(item)



while True:
    p2 = input('Qual a cor do veiculo que voce deseja ? Preta, Branco, Vermelha, Cinza, Verde, Azul, Amarelo, Verde ?')
    if p2 in ['Preta', 'Branco', 'Vermelha', 'Cinza', 'Verde', 'Azul', 'Amarelo', 'Verde',]:
        break


selecionadas = [item for item in selecionadas if item.cor == p2]

for i, valor in enumerate(selecionadas):
    print(f'{i}: {valor.nome}')


while True:
    carselec = input('Digite um número correspondente ao veículo que voce deseja ? ')
    if carselec in [str (i) for i in range(len(selecionadas))]:
        break

while True:
    p3 = input('Qual habilitação você possui ? A, B, C, D, E ou nenhuma ?')
    if p3 in ['A', 'B', 'C', 'D', 'E', 'nenhuma']:
        usuariohab = Habilitacao(p3)
        break
    
if not usuariohab.testeVal(selecionadas[int(carselec)].habilitacao):

    print('Sua habilitação esta incorreta')
    quit()


print(f'Parabéns o seu veículo selecionado com sucesso: {selecionadas[int(carselec)]}  ')






   











        
        