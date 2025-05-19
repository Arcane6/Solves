from fastapi import APIRouter, Depends, HTTPException, status, Response
from app.schemas.plan import PlanCreate, PlanRead, PlanUpdate
from app.models.plan import Plan
from app.models.user import User
from app.dependencies.get_current_user import get_current_user
from app.services.plan_service import PlanService

router = APIRouter(prefix="/plans", tags=["plans"])

@router.post("/", response_model=PlanRead)
async def create_plan(plan_in: PlanCreate, user: User = Depends(get_current_user)):
    plan = await PlanService.create_plan(user, **plan_in.model_dump())
    return plan


@router.get("/", response_model=list[PlanRead])
async def list_plans(user: User = Depends(get_current_user)):
    return await PlanService.get_all_by_user(user)


@router.get("/{plan_id}", response_model=PlanRead)
async def get_plan(plan_id: int, user: User = Depends(get_current_user)):
    plan = await PlanService.get_by_id(plan_id, user)
    if not plan:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plan not found")
    return plan


@router.put("/{plan_id}", response_model=PlanUpdate)
async def update_plan(plan_id: int, plan_in: PlanUpdate, user: User = Depends(get_current_user)):
    plan = await PlanService.get_by_id(plan_id, user)
    if not plan:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plan not found")
    await plan.update_from_dict(**plan_in.model_dump())
    await plan.save()
    return plan


@router.delete("/{plan_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_plan(plan_id: int, user: User = Depends(get_current_user)):
    plan = await PlanService.get_by_id(plan_id, user)
    if not plan:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plan not found")
    await plan.delete()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

