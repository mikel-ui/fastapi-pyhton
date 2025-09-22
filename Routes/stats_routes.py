from fastapi import APIRouter, status, Request
from Services.stats_service import StatsService
_service = StatsService()

router = APIRouter()

@router.get("/gustos-musicales")
async def obtener_cantidad_usuarios_por_gustos(request:Request):
    data = await request.json()
    return _service.obtener_cantidad_usuarios_por_gustos(data)