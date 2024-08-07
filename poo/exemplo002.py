class Carro:
    
    # Método contrutor
    def __init__(self, cor, marca, modelo):

        # Cores possíveis
        cores = {'preto', 'branco', 'vermelho', 'azul'}

        # Atributos
        self.cor = ''
        self.marca = ''
        self.modelo = ''
        
        # Testa cor
        if cor in cores:
            self.cor = cor
        else:
            self.cor = ''
            print('Vai te catar!')

       

    # Métodos
    def ligar(self):
        print("Vrum vrum")

    def desligar(self):
        print("Cof Cof")


# Cria um objeto `fuscao` do tipo `Carro`
fuscao = Carro('burro quando foge', 'VW', '1800') # ou criando um "instância" do tipo Carro

# Define o atributo `cor` do objeto `fuscao`
# fuscao.cor = "preto"

# Executa o método `ligar()` do objeto `fuscao`
fuscao.ligar()

# Desligar o método `desligar()` do objeto `fuscao`
fuscao.desligar()

# Recebe o atributo `cor` do objeto `fuscao`
print(fuscao.cor)

"""
# Cria outro objeto
opalao = Carro()        # Instância da classe `Carro`
opalao.cor = 'vermelho' # Define valor do atributo
opalao.ligar()          # Executa método
print(opalao.cor)       # Recebe valor do atributo
opalao.desligar()       # Executa método
"""