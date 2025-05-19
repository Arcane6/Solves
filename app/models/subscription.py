# app/models/subscription.py
from tortoise import fields, models

class Subscription(models.Model):
    """Assinatura de um cliente a um plano."""

    id = fields.IntField(pk=True)
    
    client = fields.ForeignKeyField("models.Client", related_name="subscriptions", on_delete=fields.CASCADE)
    plan = fields.ForeignKeyField("models.Plan", related_name="subscriptions", on_delete=fields.CASCADE)
    is_active = fields.BooleanField(default=True)
    payment_day = fields.IntField(description="Dia do mês para pagamento")
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    last_payment_date = fields.DatetimeField(null=True, description="Data do último pagamento")
    is_delinquent = fields.BooleanField(default=False, description="Está inadimplente?")