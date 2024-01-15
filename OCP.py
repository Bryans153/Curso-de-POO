class Notificador:
    def __init__(self, usuario , mensaje ):
        self.usuario = usuario
        self.mensaje =mensaje
        
    def notificar(salf):
        raise NotImplementedError
    
class NotficadorEmail(Notificador):
    def notificar(self):
        print(f"Encaidno mensaje por Email a {self.usuario.email}")
        
        
class notficadorSMS(Notificador):
    def notificar(self):
        print(f"envaido whatsapp a{self.usuario.whatsapp}")
        
        
class NorificadorTwitter(Notificador):
    def notifcar(self):
        print(f"Enviando twit a {self.usuario.twitter}")