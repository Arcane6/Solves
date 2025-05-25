
# app/models/user_session.py
from tortoise import fields, models

class UserSession(models.Model):
    """Sessões ativas do usuário para controle e segurança."""
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="sessions", on_delete=fields.CASCADE)
    session_token = fields.CharField(max_length=255, unique=True, description="Token da sessão JWT")
    refresh_token = fields.CharField(max_length=255, unique=True, description="Token de atualização JWT")
    created_at = fields.DatetimeField(auto_now_add=True, description="Data de criação da sessão")
    last_access = fields.DatetimeField(auto_now=True, description="Último acesso da sessão")
    ip_address = fields.CharField(max_length=45, null=True, description="IP da sessão")
    user_agent = fields.TextField(null=True, description="User agent do navegador ou cliente")
