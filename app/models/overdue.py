# app/models/overdue.py
from tortoise import fields, models

class Overdue(models.Model):
    """Faturas em atraso."""
    id = fields.IntField(pk=True)
    invoice = fields.ForeignKeyField("models.Invoice", related_name="overdues", on_delete=fields.CASCADE)
    days_late = fields.IntField()
    status = fields.CharField(max_length=20, description="pendente, negociado, quitado")
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
