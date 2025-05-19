from app.core.celery_app import celery

@celery.task
def generate_invoice(subscription_id: int):
    print(f"[CELERY] Gerando fatura para assinatura {subscription_id}")
    return {"subscription_id": subscription_id, "status": "gerado"}
