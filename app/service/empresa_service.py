from fastapi import HTTPException
from app.repositories.empresa_repository import EmpresaRepository
from app.domain.models.empresa import Empresa
from app.domain.schemas.empresa_schema import EmpresaCreate

class EmpresaService:
    def __init__(self, repository: EmpresaRepository):
        self.repository = repository

    def criar_empresa(self, schema: EmpresaCreate):
        
        if self.repository.get_by_cnpj(schema.cnpj):
            raise HTTPException(status_code=400, detail="CNPJ já cadastrado no sistema.")
        
        nova_empresa = Empresa(**schema.model_dump())
        return self.repository.create(nova_empresa)