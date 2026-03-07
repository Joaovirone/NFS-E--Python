from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infra.database import get_db
from app.repositories.empresa_repository import EmpresaRepository
from app.service.empresa_service import EmpresaService
from app.domain.schemas.empresa_schema import EmpresaCreate, EmpresaResponse

router = APIRouter(prefix="/empresas", tags=["Empresas"])

@router.post("/", response_model=EmpresaResponse)
def create_empresa(payload: EmpresaCreate, db: Session = Depends(get_db)):
    
    repo = EmpresaRepository(db)
    service = EmpresaService(repo)
    
    return service.criar_empresa(payload)