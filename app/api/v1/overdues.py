from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.overdue import OverdueCreate, OverdueRead
from app.models.overdue import Overdue
from app.dependencies.get_current_user import get_current_user
from app.models.user import User
from app.services.overdue_services import OverdueService

router = APIRouter(prefix="/overdues", tags=["overdues"])

@router.post("/generate_all/", response_model=list[OverdueCreate])
async def create_overdue_list(user: User = Depends(get_current_user)):
    overdue = await OverdueService.mark_all_overdue_invoices()
    return overdue

@router.get("/", response_model=list[OverdueRead])
async def list_overdues(user: User = Depends(get_current_user)):
    return await OverdueService.get_overdue_invoices()


@router.get("/{id}", response_model=OverdueRead)
async def get_overdue_by_id(id: int, user: User = Depends(get_current_user)):
    overdue = await OverdueService.get_overdue_invoice_by_id(id)
    if overdue is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Overdue not found")
    return overdue

@router.post("/update_status/", response_model=list[OverdueRead])
async def update_overdue_status(user: User = Depends(get_current_user)):
    overdue = await OverdueService.update_status_all_overdue_invoice()
    return overdue
