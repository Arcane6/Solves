from app.models.overdue import Overdue
from app.models.invoice import Invoice
from datetime import datetime


class OverdueService:

    @staticmethod
    async def mark_all_overdue_invoices() -> None:
        overdue_invoices = []


        for invoice in await Invoice.all():
            if invoice.status == "vencida" and not Overdue.filter(invoice=invoice).exists():

                days_late = (datetime.now() - invoice.due_date).days

                overdue_invoices.append(
                    Overdue(
                        invoice=invoice,
                        status="pendente",
                        days_late=days_late
                    )
                )
        Overdue.bulk_create(overdue_invoices, 500)
        return overdue_invoices
    
    @staticmethod
    async def get_overdue_invoices() -> list[Overdue]:
        return await Overdue.all().prefetch_related("invoice")
    
    @staticmethod
    async def get_overdue_invoice_by_id(id: int) -> Overdue:
        return await Overdue.get(id=id)

    @staticmethod
    async def update_status_all_overdue_invoice() -> None:

        updated_overdue_invoices = []

        overdue_invoices = await Overdue.all()
        for overdue_invoice in overdue_invoices:
            if overdue_invoice.status == "pendente" and (overdue_invoice.invoice.status == "paga"):
                overdue_invoice.status = "quitado"
                updated_overdue_invoices.append(overdue_invoice)
                Overdue.bulk_update(updated_overdue_invoices, fields=["status"], batch_size=500)
        return updated_overdue_invoices


    @staticmethod
    async def update_days_late_overdue_invoice() -> None:
        updated_overdue_invoices = []
        overdue_invoices = await Overdue.all()
        for overdue_invoice in overdue_invoices:
            if overdue_invoice.status == "pendente":
                overdue_invoice.days_late += 1
                updated_overdue_invoices.append(overdue_invoice)
                Overdue.bulk_update(updated_overdue_invoices, fields=["days_late"], batch_size=500)
        return updated_overdue_invoices


