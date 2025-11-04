from fastapi import APIRouter, status, Request
from Services.posts_service import PostsService
from Services.likes_service import LikesService
from Services.comentarios_service import ComentariosService

_service = PostsService()
_likes_service = LikesService()
_comentarios_service = ComentariosService()

router = APIRouter()

#POST: /posts
@router.post("", status_code=status.HTTP_201_CREATED)
async def crear_post(request:Request):
    data = await request.json()
    return _service.crear_post(data)

#GET /posts?usuarios=id permite recuperar todos los posts de un usuario
@router.get("")
async def listar_posts_de_un_usuario(id:int):
    return _service.listar_posts_de_un_usuario(id)

#GET /posts/:id permite recuperar únicamente un único post
@router.get("/{id}")
async def obtener_post(id):
    return _service.obtener_post(int(id))

##################################################################################################################
# POST /posts/:id/like permite que un usuario le de like a un post
@router.post("/{id}/like", status_code=status.HTTP_201_CREATED)
async def dar_like(id, request:Request):
    data = await request.json()
    return _likes_service.dar_like(int(id), data)

# GET /posts/:id/likes permite obtener todos los likes de un post, detallando quién dió cada uno
@router.get("/{id}/likes")
async def listar_likes_de_post(id):
    return _likes_service.listar_likes_de_post(int(id))

# POST /posts/:id/comentarios permite que un usuario deje un comentario sobre un post
@router.post("/{id}/comentarios")
async def crear_comentario(id, request:Request):
    data = await request.json()
    return _comentarios_service.crear_comentario(int(id), data)

# GET /posts/:id/comentarios permite obtener todos los comentarios asociados a un post
@router.get("/{id}/comentarios")
async def listar_comentarios_de_post(id):
    return _comentarios_service.listar_comentarios_de_post(int(id))