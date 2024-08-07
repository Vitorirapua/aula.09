class Animal:

    def __init__(self) -> None:
        
        self.__especie = ''
        self.genero = ''
        self.subespecie = ''
    
# Encapsulamento com getter e setter

    # SETTERS → Definir os valores dos atributos encapsulados
        
    def setEspecie(self, especie):
        self.__especie = especie.strip() # Remove espaços antes e depois do texto da string

    def setGenero(self, genero):
        self.genero = genero.strip() # Remove espaços antes e depois do texto da string

    def setSubespecie(self, subespecie):
        self.subespecie = subespecie.strip() # Remove espaços antes e depois do texto da string

    # GETTERS → Ler os valores dos atributos encapsulados

    def getEspecie(self):
        if self.__especie != '':
            return self.__especie
        else:
            return 'Erro ao mostrar a espécie.'

    def getGenero(self):
        if self.genero != '':
            return self.genero
        else:
            return 'Erro ao mostrar o genero.'

    def getSubespecie(self):
        if self.subespecie != '':
            return self.subespecie
        else:
            return 'Erro ao mostrar a subespecie.'

    
minhoca = Animal()
minhoca.setEspecie('      taturana      ')
print(minhoca.getEspecie())

minhoca.biscoito = '       tatyranada    '
print(minhoca.biscoito)
