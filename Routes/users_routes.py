from fastapi import APIRouter, status, Request
from Services.users_service import UsersService
_service = UsersService()

router = APIRouter()

@router.get("")
async def listar_usuarios():
    return _service.listar_usuarios()

@router.get("/{id}")
def obtener_usuario(id):
    return _service.obtener_usuario(int(id))

@router.get("/{id}/gustos-musicales")
def listar_gustos(id):
    return _service.listar_gustos(int(id))

# ●  GET /usuarios/:id/amigos devuelve los amigos que tiene un usuario 
@router.get("/{id}/amigos")
async def listar_amigos(id):
    return _service.listar_amigos(int(id))

# ●  GET /usuarios/:id/amigos-pendientes devuelve las solicitudes de amistad enviadas que estén pendientes de aceptación 
@router.get("/{id}/amigos-pendientes")
async def listar_solicitudes_enviadas_pendientes(id):
    return _service.listar_solicitudes_enviadas_pendientes(int(id))

# ●  GET /usuarios/:id/solicitudes-de-amistad devuelve las solicitudes de amistades recibidas que estén pendientes de aceptación 
@router.get("/{id}/solicitudes-de-amistad")
async def listar_solicitudes_recibidas_pendientes(id):
    return _service.listar_solicitudes_recibidas_pendientes(int(id))

# ●  GET /usuarios/:id/falsos-amigos devuelve las solicitudes de amistad enviadas que hayan sido rechazadas por los receptores. 
# si pongo mi id_usuario --> muestra las solicitudes que yo envié y me rechazaron
@router.get("/{id}/falsos-amigos")
async def listar_falsos_amigos(id):
    return _service.listar_falsos_amigos(int(id))

@router.post("", status_code=status.HTTP_201_CREATED)
async def crear_usuario(request: Request):
    data = await request.json()
    return _service.crear_usuario(data)

@router.post("/{id}/gustos-musicales")
async def agregar_gustos(id, request: Request):
    data = await request.json()
    return _service.agregar_gustos(int(id), data)



@router.put("/{id}")
async def actualizar_usuario(id, request: Request):
    data = await request.json()
    return _service.actualizar_usuario(int(id), data)