from app.models.subscription import Subscription



class SubscriptionService:
    @staticmethod
    async def create_subscription(**kwargs):
        return await Subscription.create(**kwargs)

    @staticmethod
    async def get_by_id(subscription_id: int):
        return await Subscription.get_or_none(id=subscription_id)
    

    @staticmethod
    async def get_all():
        return await Subscription.all().prefetch_related("client", "plan")


    @staticmethod
    async def update_subscription(subscription_id: int, **kwargs):
        subscription = await SubscriptionService.get_by_id(subscription_id)
        if not subscription:
            return None
        
        subscription.update_from_dict(kwargs)
        