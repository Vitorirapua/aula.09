class VeiculoMotor:

    def __init__(self, minhaMarca, meuModelo):
        
        self.marca = minhaMarca
        self.modelo = meuModelo

    def ligar(self, barulho = "Vrum Vrum!"):
        print('Ligando com', barulho)

    def desligar(self, barulho = "Cof! Cof!"):
        print('Desligando com', barulho)

class Motoca(VeiculoMotor):

    qdtRodas = 2

    def ligar(self, grau):
        print(grau, 'Tibum!')

class Carreta(VeiculoMotor):

    qdtRodas = 12
    capacidade = 8000


# Instância de Motoca
hondinha = Motoca('Honda', 'CG125')
hondinha.ligar('Tuim! Tuim!')
print(hondinha.qdtRodas)

print('-------------------------')

# Instancia de Carreta
scanao = Carreta('Scania', 'RSRR3200')
scanao.ligar("Brão! Brão!")
print(scanao.qdtRodas)