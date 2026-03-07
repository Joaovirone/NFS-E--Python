from sqlalchemy.orm import Session
from app.domain.models.empresa import Empresa

class EmpresaRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, empresa: Empresa):
        self.db.add(empresa)
        self.db.commit()
        self.db.refresh(empresa)
        return empresa

    def get_by_cnpj(self, cnpj: str):
        return self.db.query(Empresa).filter(Empresa.cnpj == cnpj).first()