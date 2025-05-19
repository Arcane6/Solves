from app.models.invoice import Invoice
from app.models.subscription import Subscription


class InvoiceService:

    

    @staticmethod
    async def generate_invoice(subscription: Subscription, month: int, year: int, due_date, status="pendente"):
        return await Invoice.create(
            subscription=subscription,
            month=month,
            year=year,
            due_date=due_date,
            status=status
        )
    
    @staticmethod
    async def get_by_month_and_year(month: int, year: int):
        return await Invoice.filter(month=month, year=year).all()
    
    @staticmethod
    async def generate_all_invoices(subscription_id: Subscription, year: int):
        sub = await Subscription.get(id=subscription_id)

        if sub.plan.recurrence == "mensal":
            for month in range(1, 13):
                await InvoiceService.generate_invoice(sub, month, year)

    @staticmethod
    async def get_pending_by_subscription(subscription: Subscription):
        return await Invoice.filter(subscription=subscription, status="pendente").all()
