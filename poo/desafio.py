class User:

    # Metodo contrutor
    def __init__(self,):
    
        self.__id = 0
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
            return self.__id 

        def setName(self, name):
           return self.__name   

        def getEmail(self, email):
           return self.__email  

        def getPassword(self, password):
           return self.__password 


    def new(self, name, email):
        pass

    def view(self, id):
        pass

    def delete(self, id):
        pass


class Studant(User):

    def __init__(self):

        self.__notas = {}
        self.__presenca = {}
        self.__cursos = ""

# get       
    def getNotas(self, notas):
        return self.__notas

    def getPresenca(self, presenca):
        return self.__presenca

    def getcursoss(self, cursos):
        return self.__cursos

# set
    def setNotas(self, notas):
        self.__notas

    def setPresenca(self, presenca):
        self.__presenca    

    def setcursos(self, cursos):
        self.__cursos