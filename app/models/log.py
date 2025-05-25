from tortoise import fields, models

class AuditLog(models.Model):
    id = fields.IntField(pk=True)
    user = fields.IntField(null=True)
    action = fields.CharField(max_length=255)
    timestamp = fields.DatetimeField(auto_now_add=True)
    metadata = fields.JSONField(null=True)
