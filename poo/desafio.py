class User:

    # Metodo contrutor
    def __init__(self,):
    
        self.__id = ""
        self.__name = ""
        self.__email = ""
        self.__password = ""
    # set
        def setId(self, id):
            self.__id = id

        def setName(self, name):
            self.__name - name    

        def setEmail(self, email):
            self.__email - email 
        
        def setPassword(self, password):
            self.__password - password

    # Get

        def getId(self, id):
            self.__id = id

        def setName(self, name):
            self.__name - name  

        def getEmail(self, email):
            self.__email - email 

        def getPassword(self, password):
            self.__password - password


    def new(self, name, email):
        pass

    def view(self, id):
        pass

    def delete(self, id):
        pass


class Studant(User):

    def __init__(self):

        self.__notas = ""
        self.__presenca = ""
        self.__curso = ""

# get       
    def getNotas(self, notas):
        pass

    def getPresenca(self, presenca):
        pass

    def getCursos(self, cursos):
        pass

# set
    def setNotas(self, notas):
        pass

    def setPresenca(self, presenca):
        pass    

    def setCursos(self, cursos):
        pass