from entities.comentario import Comentario
from fastapi import HTTPException
from repositories.repository import users_repo,comentarios_repo

_users = users_repo
_comentarios = comentarios_repo._comentarios

class ComentariosService:
    
    def listar_comentarios(self):
        return  [comentario for comentario in _comentarios.values()]

    def crear_comentario(self, id_post, data):
        cuerpo = data.get("cuerpo","").strip()
        id_emisor = int(data.get("id_emisor"))
        
        if len(cuerpo)>1000:
            raise HTTPException(status_code=400, detail="Tu comentario es muy largo")
        
        comentario = Comentario(
            id=comentarios_repo.next_id(),
            id_emisor=id_emisor,
            id_post_destinatario=id_post,
            cuerpo=cuerpo
        )
        
        comentario_guardado = comentarios_repo.guardar(comentario)
        return comentario_guardado
    
    def listar_comentarios_de_post(self, id_post):
        return comentarios_repo.listar_comentarios_de_post(id_post)