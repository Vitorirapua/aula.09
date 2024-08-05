class Carro:
    
    # Método construtor
    def __init__(self):

         # Atributos
         self.cor = ""
         self.marca = ""
         self.modelo = None
         pass

    # Métodos
    def ligar(self):
        print("Vrum vrum")

    def desligar(self):
        print("Cof cof")


# Cria um objeto 'fuscao'
fuscao = Carro()

#cor do meu carro
fuscao.cor = "preto"

#ligar carro
fuscao.ligar()

#desligar carro
fuscao.desligar()

#ler cor do carro 
print(fuscao.cor)


#cria outro objeto
opalao = carro()
opalao.cor = 'vermelho'
opalao.ligar()
print(opalao.cor)
opalao.desligar()