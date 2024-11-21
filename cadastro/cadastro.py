import sys 
from PyQt5 import uic, QtWidgets 
from database.database import Database

class Cadastro:
    win = "cadastro/cadastro.ui"
    
    def __init__(self, username, password):
        self.username = username 
        self.password = password 
    
    def register(self):
        Database(self.username, self.password).new_user()
        return "Usuário cadastrado!"