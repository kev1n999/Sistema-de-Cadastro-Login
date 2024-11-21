import sys 
from PyQt5 import QtWidgets, uic
from cadastro.cadastro import Cadastro
from database.database import Database 

class Login(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.window = uic.loadUi("login.ui")
        self.window.pushButton_2.clicked.connect(self.quit)
        self.username = self.window.lineEdit_2 
        self.password = self.window.lineEdit
        self.window.pushButton.clicked.connect(self.login)
        self.window.pushButton_3.clicked.connect(self.cadastro)
        self.browser = self.window.textBrowser
        self.window.show()
        
        self.winCadastro = uic.loadUi(Cadastro.win)
        self.name = self.winCadastro.lineEdit_2
        self.senha = self.winCadastro.lineEdit
        self.winCadastro_create = self.winCadastro.pushButton.clicked.connect(self.add)
        self.winCadastro.pushButton_2.clicked.connect(self.winCadastro.close)
        self.browser2 = self.winCadastro.textBrowser

    def login(self):
        username = self.username.text()
        password = self.password.text()
        if username == "" or password == "":
            self.browser.append("erro: informações vazias;")
            return 
        
        v = Database(username, password).verify()
        if v is True: 
            self.browser.append("Login efetuado!")
        else:
            self.browser.append("Essa conta não existe!")

    def cadastro(self):
       self.winCadastro.show()
    
    def add(self):
        if self.name.text() == "" or self.senha.text() == "":
            self.browser2.append("erro: Informações vazias;")
            return 
        
        self.browser2.append(Cadastro(self.name.text(), self.senha.text()).register())
        
login = Login()
sys.exit(login.exec_())