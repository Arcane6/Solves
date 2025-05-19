from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.invoice import InvoiceCreate, InvoiceRead
from app.models.invoice import Invoice
from app.dependencies.get_current_user import get_current_user
from app.models.user import User
from app.services.invoice_services import InvoiceService

router = APIRouter(prefix="/invoices", tags=["invoices"])

@router.post("/", response_model=InvoiceRead)
async def create_invoice(inv_in: InvoiceCreate, user: User = Depends(get_current_user)):
    invoice = await InvoiceService.generate_invoice(**inv_in.model_dump())
    return invoice


@router.get("/", response_model=list[InvoiceRead])
async def list_invoices(user: User = Depends(get_current_user)):
    return await Invoice.all().prefetch_related("subscription")


@router.get("/{invoice_id}", response_model=InvoiceRead)
async def get_invoice_by_month(month: int, year: int,  user: User = Depends(get_current_user)):
    invoice = await InvoiceService.get_by_month_and_year(month, year)
    if not invoice:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invoice not found")
    return invoice


