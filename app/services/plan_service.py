from app.models.plan import Plan
from app.models.user import User


class PlanService:
    @staticmethod
    async def get_all_by_user(user: User):
        return await Plan.filter(user=user).all()

    @staticmethod
    async def create_plan(user: User, **kwargs):
        return await Plan.create(user=user, **kwargs)

    @staticmethod
    async def get_by_id(plan_id: int, user: User):
        return await Plan.get_or_none(id=plan_id, user=user)
    

