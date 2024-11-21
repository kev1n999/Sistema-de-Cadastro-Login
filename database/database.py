import sqlite3 

class Database:
    def __init__(self, username, password):
        self.username = username 
        self.password = password
        self.db = sqlite3.connect("database/cadastros.db")
        self.cursor = self.db.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Cadastros (username text, password text)")

    def create(self):
        self.db.commit()
    
    def new_user(self):
        self.cursor.execute("INSERT INTO Cadastros (username, password) VALUES (?, ?)", (self.username, self.password))
        self.db.commit()

    def verify(self):
        result = self.cursor.execute("SELECT COUNT(*) FROM Cadastros WHERE username = ? and password = ?", (self.username, self.password))
        r = result.fetchone()
        if r[0] > 0:
            return True 
        else:
            return False 
