from entities.post import Post
from fastapi import HTTPException
from repositories.repository import posts_repo
from datetime import date

_repo = posts_repo

class PostsService:
    
    def crear_post(self, data):
        cuerpo = data.get("cuerpo").strip()
        if len(cuerpo) > 3000:
            raise HTTPException(status_code=400, detail="El cuerpo del post no puede tener más de 3000 caracteres")                
        #evitar que el usuario tenga 
        id_creador = int(data.get("id_creador", "").strip())
        fecha_creacion = date.today().strftime('%Y-%m-%d')
        if(_repo.se_puede_agregar(self,id_creador,fecha_creacion)):                    
            # Crear instancia de Post
            post = Post(
                id=_repo.next_id(),
                id_creador=id_creador,
                titulo=data.get("titulo", "").strip(),
                cuerpo=data.get("cuerpo", "").strip()
            )
            post_guardado = _repo.guardar(post)
            return post_guardado
        else:
            raise HTTPException(status_code=400, detail="El usuario tiene más de 5 posts hechos el día de la fecha")
        
    def listar_posts_de_un_usuario(self,id):
        return _repo.listar_posts_de_un_usuario(id)
    
    def obtener_post(self,id):
        return _repo.obtener_post(id)    