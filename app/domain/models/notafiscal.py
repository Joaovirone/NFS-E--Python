from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Empresa(db.Model):
    __tablename__ = 'empresas'
    id = db.Column(db.Integer, primary_key=True)
    razao_social = db.Column(db.String(150), nullable=False)
    cnpj = db.Column(db.String(14), unique=True, nullable=False)
    inscricao_estadual = db.Column(db.String(15), nullable=False)
   

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    documento = db.Column(db.String(14), unique=True, nullable=False) # cpf ou o cnpj
    email = db.Column(db.String(100))

class NotaFiscal(db.Model):
    __tablename__ = 'notas_fiscais'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, unique=True)
    serie = db.Column(db.String(3))
    chave_acesso = db.Column(db.String(44), unique=True)
    status = db.Column(db.String(20), default='rascunho')
    valor_total = db.Column(db.Numeric(10, 2), nullable=False)
    data_emissao = db.Column(db.DateTime, default=datetime.utcnow)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresas.id'))
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))