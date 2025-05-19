from fastapi import APIRouter, Depends, HTTPException, status, Response
from app.schemas.client import ClientCreate, ClientRead, ClientUpdate
from app.dependencies.get_current_user import get_current_user
from app.models.user import User
from app.services.client_service import ClientService

router = APIRouter(prefix="/clients", tags=["clients"])

@router.post("/", response_model=ClientRead)
async def create_client(client_in: ClientCreate, user: User = Depends(get_current_user)):
    client = await ClientService.create_client(user=user, **client_in.model_dump())
    return client


@router.get("/", response_model=list[ClientRead])
async def list_clients(user: User = Depends(get_current_user)):
    return await ClientService.get_all_by_user(user=user)


@router.get("/{client_id}", response_model=ClientRead)
async def get_client(client_id: int, user: User = Depends(get_current_user)):
    client = await ClientService.get_by_id(client_id, user=user)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado")
    return client


@router.put("/{client_id}", response_model=ClientUpdate)
async def update_client(client_id: int, client_in: ClientCreate, user: User = Depends(get_current_user)):
    client = await ClientService.get_by_id(client_id, user=user)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado")
    await client.update_from_dict(**client_in.model_dump())
    await client.save()
    return client


@router.delete("/{client_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_client(client_id: int, user: User = Depends(get_current_user)):
    client = await ClientService.get_by_id(client_id, user=user)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado")
    await client.delete()
    return Response(status_code=status.HTTP_204_NO_CONTENT)