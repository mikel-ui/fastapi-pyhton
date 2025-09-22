from fastapi import HTTPException
from repositories.repository import users_repo, friend_requests_repo
from entities.friend_request import FriendRequest

_users_repo = users_repo
_friend_requests_repo = friend_requests_repo

_users = _users_repo._usuarios
_friend_requests = _friend_requests_repo._friend_requests

class FriendRequestsService:
    def __init__(self):
        pass
    
    def crear_friend_request(self, data):
        id_emisor=int(data.get("id_emisor"))
        id_receptor=int(data.get("id_receptor"))
        
        if(id_emisor not in _users_repo.obtener_lista_de_ids() or id_receptor not in _users_repo.obtener_lista_de_ids()):
            mensaje = ("Los ids "+str(id_emisor)+" o "+str(id_receptor)+" no son corresponden a usuarios")
            raise HTTPException(status_code=400, detail=mensaje)
             
        if(_friend_requests_repo.se_puede_agregar(id_emisor,id_receptor)):
            #si esta permitido el ingreso de esa solicitud, se procede a agregarla al repo
            new_friend_request = FriendRequest(
                id= _friend_requests_repo.next_id(),
                estado= "pendiente",
                id_emisor= id_emisor,
                id_receptor= id_receptor
            )
            _friend_requests_repo.agregar(new_friend_request)
            return new_friend_request
        else:
            raise HTTPException(status_code=400, detail="Ya enviaste esta peticion pedazo de intenso")
        
    def responder_friend_request(self, id_friend_request, data):
        id_emisor=int(data.get("id_emisor"))
        id_receptor=int(data.get("id_receptor"))
        
        if(_friend_requests_repo.es_repitido(id_emisor,id_receptor)):
            #si la solicitud ya existe significa que hay que procesar la respuesta
            respuesta=str(data.get("respuesta"))
            
            id_friend_request_a_responder = (_friend_requests_repo.obtener_friend_request(id_emisor,id_receptor)).id
            if(id_friend_request==id_friend_request_a_responder):
                if(isinstance(respuesta,str)):
                    if(respuesta.lower() in ["a","aceptada","1","s","si","true"]): respuesta="aceptada"
                    if(respuesta.lower() in ["r","rechazada","0","n","no","false"]): respuesta="rechazada"    
                _friend_requests_repo.responder_solicitud(id_friend_request_a_responder,respuesta)
                
            if(respuesta=="aceptada"):
                return _users_repo.crar_amistad(id_emisor,id_receptor)
            else:
                raise HTTPException(status_code=400, detail="solicitud rechazada...")


    def listar_usuarios():
        return _users_repo.listar_usuarios()
    
    def listar_friend_requests(self):
        return _friend_requests_repo.listar_friend_requests()