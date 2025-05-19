# app/models/user.py
from tortoise import fields, models

class User(models.Model):
    """Usuário que contratou o sistema."""
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=255, unique=True, description="Email do usuário")
    hashed_password = fields.CharField(max_length=255, description="Senha criptografada")
    full_name = fields.CharField(max_length=255, description="Nome completo")
    is_active = fields.BooleanField(default=True, description="Usuário está ativo?")
    is_superuser = fields.BooleanField(default=False, description="Usuário tem privilégios de administrador?")
    created_at = fields.DatetimeField(auto_now_add=True, description="Data de criação")
    updated_at = fields.DatetimeField(auto_now=True, description="Última atualização")
