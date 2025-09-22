from fastapi import APIRouter, status, Request
#from Services.stats_service import StatsService
from Services.friend_requests_service import FriendRequestsService
_service = FriendRequestsService()

router = APIRouter()

#CODIGO:
@router.get("")
async def listar_friend_requests():
    return _service.listar_friend_requests()


# ●  POST /solicitudes-de-amistad permite que un usuario cree una solicitud de amistad hacia otro usuario. 
@router.post("")
async def crear_friend_request(request:Request):
    data = await request.json()
    return _service.crear_friend_request(data)

# ●  PUT /solicitudes-de-amistad/:id se utiliza para poder aceptar o rechazar una solicitud de amistad 
@router.put("/{id}")
async def responder_friend_request(id, request:Request):
    data = await request.json()
    return _service.responder_friend_request(int(id), data)
