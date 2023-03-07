from ipaddress import IPv4Address # para su dirección IP 
from pyairmore.request import AirmoreSession # para crear una AirmoreSession 
from pyairmore.services.messaging import MessagingService # para enviar mensajes

class SmsAirMore():
    
    def __init__(self):
        self.ip = IPv4Address("192.168.1.145")
        self.session = AirmoreSession(self.ip)
        print("ssion abierta",self.session.is_server_running)
        self.was_accepted = self.session.request_authorization()
        print("Autorización aceptada",self.was_accepted)
        self.service = MessagingService(self.session)
    def enviar(self, para, mensaje):
        try:
            self.service.send_message(para, mensaje)
        except Exception as  e:
            print("error en {0} ".format(e))        
        
if __name__ == '__main__':
    smsAirMore = SmsAirMore()
    smsAirMore.enviar("+584127239359", "message content  as tú")
    
#ip = IPv4Address("192.168.1.145") # vamos a crear un objeto de dirección IP
# ahora crea una sesión 
#session = AirmoreSession(ip)
# si su puerto no es 2333 
# sesión = AirmoreSession(ip, 2334) # asumiendo que es 2334
#print(session.is_server_running)
#was_accepted = session.request_authorization()
#print(was_accepted)
#service = MessagingService(session)
#print(service.send_message("+584127239359", "message contenttú"))
