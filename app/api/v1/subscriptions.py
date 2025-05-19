from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.subscription import SubscriptionCreate, SubscriptionRead
from app.dependencies.get_current_user import get_current_user
from app.models.user import User
from app.services.subscription_service import SubscriptionService

router = APIRouter(prefix="/subscriptions", tags=["subscriptions"])

@router.post("/", response_model=SubscriptionRead)
async def create_subscription(sub_in: SubscriptionCreate, user: User = Depends(get_current_user)):
    subscription = await SubscriptionService.create_subscription(**sub_in.model_dump())
    return subscription


@router.get("/{subscription_id}", response_model=SubscriptionRead)
async def get_subscription(subscription_id: int, user: User = Depends(get_current_user)):
    subscription = await SubscriptionService.get_by_id(subscription_id)
    if not subscription:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Subscription not found")
    return subscription


@router.get("/", response_model=list[SubscriptionRead])
async def list_subscriptions(user: User = Depends(get_current_user)):
    return await SubscriptionService.get_all()


@router.put("/{subscription_id}", response_model=SubscriptionRead)
async def update_subscription(subscription_id: int, sub_in: SubscriptionCreate, user: User = Depends(get_current_user)):
    subscription = await SubscriptionService.update_subscription(subscription_id, **sub_in.model_dump())
    if not subscription:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Subscription not found")
    return subscription