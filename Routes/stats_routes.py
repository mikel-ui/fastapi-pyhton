from fastapi import APIRouter, status, Request
from Services.stats_service import StatsService
_service = StatsService()

router = APIRouter()

@router.get("/gustos-musicales")
async def obtener_cantidad_usuarios_por_gustos(request:Request):
    data = await request.json()
    return _service.obtener_cantidad_usuarios_por_gustos(data)

@router.get("/spammers")
async def top_n_usuarios_mas_spammers(request:Request):
    data = await request.json()
    return _service.top_n_usuarios_mas_spammers(data)

@router.get("/callados")
async def top_n_usuarios_mas_callados(request:Request):
    data = await request.json()
    return _service.top_n_usuarios_mas_callados(data)

@router.get("/rechazados")
async def top_n_usuarios_rechazados(request:Request):
    data = await request.json()
    return _service.top_n_usuarios_rechazados(data)

# estadísticas de los posts:
#usuarios que más postean --> activos
@router.get("/activos")
async def obtener_activos():
    return _service.obtener_activos()

#usuarios que menos postean --> pasivos
@router.get("/pasivos")
async def obtener_pasivos():
    return _service.obtener_pasivos()

#usuarios que "escriben mucho" --> escritores
@router.get("/escritores")
async def obtener_escritores():
    return _service.obtener_escritores()


# Cuál fue el post más “likeado” de un día en particular
@router.get("/posts/likeado")
async def post_mas_likeado_fecha(request:Request):
    data = await request.json()
    return _service.post_mas_likeado_fecha(data)

# Cuál fue el post más “comentado” de un día en particular
@router.get("/posts/comentado")
async def post_mas_comentado_fecha(request:Request):
    data = await request.json()
    return _service.post_mas_comentado_fecha(data)

# Cuáles son los posts que contienen más de X comentarios
#no quise poner la cantidad de comentarios dentro de la ruta porque queda re villero (opinion personal)
@router.get("/posts/supera-comentarios")
async def obtener_posts_mas_x_comentarios(request:Request):
    data = await request.json()
    return _service.obtener_posts_mas_x_comentarios(data)

# Cuáles son los posts que tienen más de X cantidad de likes
@router.get("/posts/supera-likes")
async def obtener_posts_mas_x_likes(request:Request):
    data = await request.json()
    return _service.obtener_posts_mas_x_likes(data)