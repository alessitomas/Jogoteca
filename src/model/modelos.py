from model.sql_alchemy_para_db import db

class JogoModel(db.Model):
    __tablename__ = "Jogo_model"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True )
    nome = db.Column(db.String(80), nullable = False)
    categoria = db.Column(db.String(20), nullable = False)
    console = db.Column(db.String(20), nullable = False)

    def __init__(self, nome, categoria,console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

    def save(self):
   
        db.session.add(self)
        
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def search_all(cls):
        return cls.query.all()        

    def toDict(self):
        return {'id': self.id, 'nome':self.nome, 'categoria':self.categoria}
    


class UsuarioModel(db.Model):
    __tablename__ = "Usuario_model"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True )
    nome = db.Column(db.String(80), nullable = False)
    username = db.Column(db.String(20), nullable = False)
    senha = db.Column(db.String(20), nullable = False)

    def __init__(self,nome, username,senha):
        
        self.nome = nome
        self.username = username
        self.senha = senha

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def search_all(cls):
        return cls.query.all()        

    def toDict(self):
        return {'id': self.id, 'nome':self.nome, 'username':self.username}
    
    def __str__(self):
        return f'{self.nome}'

