from fastapi import APIRouter
from app.api.v1 import auth, users, clients, plans, subscriptions, invoices, overdues

api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(clients.router)
api_router.include_router(plans.router)
api_router.include_router(subscriptions.router)
api_router.include_router(invoices.router)
api_router.include_router(overdues.router)
