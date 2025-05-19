


# app/models/client.py
from tortoise import fields, models

class Client(models.Model):
    """Clientes do usuário dono do sistema."""
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="clients", on_delete=fields.CASCADE)
    name = fields.CharField(max_length=255, description="Nome do cliente")
    phone = fields.CharField(max_length=20, description="Telefone")
    email = fields.CharField(max_length=255, description="Email")
    address = fields.TextField(null=True, description="Endereço completo")
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)










