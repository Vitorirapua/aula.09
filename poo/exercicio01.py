# Importa as dependências
import random
import re
import string

# Desenvolva a classe `User`
class User:

    # Crie o método construtor
    def __init__(self):

        # Inicialize os atributos
        self.__id = 0
        self.__name = ''
        self.__email = ''
        self.__password = ''

    # Métodos para uso interno

    # Método que valida e-mails usando Regex
    # https://catabits.com.br/view/regex_para_validar_emails
    def validate_email(self, email):

        # Regex para validar endereços de e-mail, usada pelo HTML5
        # OBS: deve estar em uma única linha
        pattern = r'^[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)*$'

        # Verifica se o e-mail corresponde ao padrão regex
        if re.match(pattern, email):
            return True
        else:
            return False
        
    def gerar_senha(self):
        # Caracteres permitidos
        minusculas = string.ascii_lowercase
        maiusculas = string.ascii_uppercase
        digitos = string.digits
        especiais = "_-.+"
        
        # Garantir que a senha tenha pelo menos um de cada requisito
        senha = [
            random.choice(minusculas),
            random.choice(maiusculas),
            random.choice(digitos),
            random.choice(especiais)
        ]
        
        # Completar a senha até ter pelo menos 7 caracteres
        todos_caracteres = minusculas + maiusculas + digitos + especiais
        while len(senha) < 7:
            senha.append(random.choice(todos_caracteres))
        
        # Embaralhar os caracteres para garantir aleatoriedade
        random.shuffle(senha)
        
        return ''.join(senha)        

    # Encapsulamento → setter
    def setId(self, id):
        # tratamentos, filtros, sanitização e validação
        self.__id = int(id)

    def setName(self, name):
        # tratamentos, filtros, sanitização e validação
        self.__name = name.strip()

    # Exemplo de setter para e-mail
    def setEmail(self, email):
        # tratamentos, filtros, sanitização e validação
        if self.validate_email(email):
            self.__email = email.strip()
        else:
            print("Erro!", "Endereço de e-mail inválido!")
            exit()

    """
    Exemplo de setter para senha
    - Pelo menos 7 caracteres
    - Pelo menos 1 letra minúscula
    - Pelo menos 1 letra maiúscula
    - Pelo menos 1 dígito numérico
    - Pelo menos 1 dos caractetes `_`, `-`, `.` ou `+`  
    """
    def setPassword(self, password):
        regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[_\-.+])[A-Za-z\d_\-.+]{7,}$'
        if re.match(regex, password) is not None:
            self.__password = password.strip()
        else:
            print("Erro!", "Senha inválida!")
            exit()



    # Métodos do objeto
    def new(self, name, email):
        self.setName(name)
        self.setEmail(email)
        self.setPassword(self.gerar_senha())
        # grava novo usuário no banco de dados
        # SQL → INSERT INTO User (name, email, password) VALUES (self.getName(), self.getEmail(), self.getPassword())

    def view(id):
        # Recebe os dados do banco de dados relativos ao Id
        # SQL → SELECT * FROM User WHERE id = id
        # insere em um dicionário
        # Retorna o dicionário
        pass

    def delete(id):
        # Busca e apaga o registro do banco de dados relativo ao Id
        # DELETE * FROM User WHERE id = id
        # Se achou e apagou retorna `True`
        pass


# Cria a classe 'Studand' que herda atributos e métodos a classe 'User' 
class Student(User):

    def __init__(self):
        super().__init__()

        self.__notas = {}
        self.__presenca = {}
        self.__curso = ""

    # Getters e Setters
    def setNotas(self, notas):
        self.__notas = notas

    def  setPresenca(self, presenca):
        self.__presenca = presenca

    def setCurso(self, curso):
        # Garantir validade e que é uma coleção
        self.__curso = curso   

    def getNotas(self):
        return self.__notas

    def getPresenca(self):
        return self.__presenca

    def getCurso(self):
        return self.__curso
                          