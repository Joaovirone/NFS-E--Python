from sqlalchemy import Column, Integer, String
from app.infra.database import Base

class Empresa(Base):
    __tablename__ = "empresas"
    id = Column(Integer, primary_key=True, index=True)
    razao_social = Column(String, nullable=False)
    cnpj = Column(String(14), unique=True, index=True)