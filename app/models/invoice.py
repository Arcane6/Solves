# app/models/invoice.py
from tortoise import fields, models

class Invoice(models.Model):
    """Faturas geradas para assinaturas."""
    id = fields.IntField(pk=True)
    subscription = fields.ForeignKeyField("models.Subscription", related_name="invoices", on_delete=fields.CASCADE)
    month = fields.IntField()
    year = fields.IntField()
    due_date = fields.DatetimeField()
    status = fields.CharField(max_length=20, description="pendente, paga, vencida")
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)