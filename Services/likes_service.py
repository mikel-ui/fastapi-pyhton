from entities.like import Like
from fastapi import HTTPException
from repositories.repository import users_repo,likes_repo,posts_repo

_users = users_repo
_posts = posts_repo._posts
_likes = likes_repo._likes

class LikesService:
    def listar_likes(self):
        return [like for like in _likes.values()]        
    
    def dar_like(self, id_post, data):
        id_emisor = int(data.get("id_emisor"))        
        
        if likes_repo.contar_likes_emisor_destinatario(id_post, id_emisor) >= 1:
            raise HTTPException(status_code=400, detail="Este usuario ya ha dado like a la publicacion")                
        
        like = Like(
            id = likes_repo.next_id(),
            id_emisor=id_emisor,
            id_post_destinatario=id_post
        )
        like_guardado = likes_repo.guardar(like)
        return like_guardado
    
    def listar_likes_de_post(self, id_post):
        return likes_repo.listar_likes_de_post(id_post)