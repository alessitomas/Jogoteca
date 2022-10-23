from model.sql_alchemy_para_db import db

class JogoModel(db.Model):
    __tablename__ = "Jogo_Model"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True )
    nome = db.Column(db.String(50), nullable = False)
    categoria = db.Column(db.String(40), nullable = False)
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
    
    def __repr__(self) -> str:
        return '<Name %r>' % self.nome

class UsuarioModel(db.Model):
    __tablename__ = "Usuario_Model"

    username = db.Column(db.String(8), primary_key =True)
    nome = db.Column(db.String(20), nullable = False)
    senha = db.Column(db.String(100), nullable = False)

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
    
    def __repr__(self) -> str:
        return '<Name %r>' % self.nome
