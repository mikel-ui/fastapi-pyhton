from entities.friend_request import FriendRequest

class FriendRequestsRepository:
    def __init__(self):
        self._friend_requests = {}
        self._next_id = 1
    
    def responder_solicitud(self,id_friend_request_a_responder,respuesta):
        self._friend_requests[id_friend_request_a_responder].estado = respuesta        
        return self._friend_requests[id_friend_request_a_responder].estado
    
    def agregar(self,friend_request):
        self._friend_requests[friend_request.id] = friend_request
        return friend_request
    
    def se_puede_agregar(self,id_emisor,id_receptor):
        # para agregar solicitud se necesita:
        #   -no ser auto envio
        #   -no repetir emisor y receptor
        return (not(self.es_auto_solicitud(id_emisor,id_receptor)) and not(self.es_repitido(id_emisor,id_receptor)))
    
    def es_auto_solicitud(self, id_emisor, id_receptor):
        return id_emisor==id_receptor
    
    def es_repitido(self, id_emisor, id_receptor):
        for friend_request in self._friend_requests.values():
            if (id_emisor==friend_request.id_emisor and id_receptor==friend_request.id_receptor):
                return True
        return False        
    
    def next_id(self):
        current_id = self._next_id
        self._next_id += 1
        return current_id    
    
    def listar_friend_requests(self):
        return list(self._friend_requests.values())
    
    def obtener_friend_request(self, id_emisor, id_receptor):
        for fr in self._friend_requests.values():
            if(fr.id_emisor==id_emisor and fr.id_receptor==id_receptor):
                return fr
        return None
    
    def listar_solicitudes_enviadas_pendientes(self, id_usuario):
        #return [fr.id_emisor==id_usuario and fr.estado=="pendiente" for fr in self._friend_requests.values()]
        resultado = []
        for fr in self._friend_requests.values():
            if fr.id_emisor==id_usuario and fr.estado=="pendiente":
                resultado.append(fr)
        print("enviadas pendientes:")
        print(resultado)
        return resultado
    
    def listar_solicitudes_recibidas_pendientes(self, id_usuario):
        # return [fr if(fr.id_receptor==id_usuario and fr.estado=="pendiente") else None for fr in self._friend_requests.values()]
        resultado = []
        for fr in self._friend_requests.values():
            if fr.id_receptor==id_usuario and fr.estado=="pendiente":
                resultado.append(fr)
        print("recibidas pendientes:")
        print(resultado)
        return resultado
    
    def listar_falsos_amigos(self, id_usuario):
        # return [fr if(fr.id_emisor==id_usuario and fr.estado=="rechazada") else None for fr in self._friend_requests.values()]                
        resultado = []
        for fr in self._friend_requests.values():
            if fr.id_emisor==id_usuario and fr.estado=="rechazada":
                resultado.append(fr)
        print("falsos amigos:")
        print(resultado)
        return resultado