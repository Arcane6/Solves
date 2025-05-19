# app/models/plan.py
from tortoise import fields, models

class Plan(models.Model):
    """Planos de assinatura oferecidos."""
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="plans", on_delete=fields.CASCADE)
    name = fields.CharField(max_length=255)
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    recurrence = fields.CharField(max_length=20, description="mensal ou anual")
    description = fields.TextField(null=True)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
