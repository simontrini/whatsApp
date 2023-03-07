import requests
import urllib.parse

class SmsKannel():
    
    def __init__(self):
        self.username = "simontrini"
        self.password = "Refidomsa.1S"
        self.smsc = "smsc2"
        self.httpUrl = "http://127.0.0.1:13002/"
        #self.to = urllib.parse.quote("+584127239359")
        #self.text = urllib.parse.quote("TestMes")
        #http://127.0.0.1:13002/cgi-bin/sendsms?username=simontrini&password=Refidomsa.1S&smsc=smsc2&to=+584129027646&text=otraPruebaAvisameWhatsapp
        #http://127.0.0.1:13002/cgi-bin/sendsms?username=simontrini&password=Refidomsa.1S&smsc=smsc2&to=%2B584129027646&text=9Este%20mensaje%20contiene%20160%20caracteres%2C%20con%20espacios%20incluidos.%20Los%20que%20admite%20hoy%20un%20mensaje%20SMS.%20Con%20un%20coste%20medio%20de%200%2C15%20euros%2C%20aproximadamente%20%28no%20hay%20queww123009999990000777666%0Atú9
        #http://127.0.0.1:13002/cgi-bin/sendsms?username=simontrini&password=Refidomsa.1S&smsc=smsc2&to=+584129027646&text=9Este%20mensaje%20contiene%20160%20caracteres%2C%20con%20espacios%20incluidos.%20Los%20que%20admite%20hoy%20un%20mensaje%20SMS.%20Con%20un%20coste%20medio%20de%200%2C15%20euros%2C%20aproximadamente%20%28no%20hay%20queww123009999990000777666%0Atú9
        
    def setUsername (self, username):
        self.username = username
        return
    
    def getUsername (self):
        return self.username
    
    def setPassword (self, password):
        self.password = password
        return
    
    def getPassword (self):
        return self.password
    
    def setSmsc (self, smsc):
        self.smsc = smsc
        return
    
    def getSmsc (self):
        return self.smsc   
    
    def setHttpUrl (self, httpUrl):
        self.httpUrl = httpUrl
        return
    
    def getHttpUrl (self):
        return self.httpUrl  
    
    def setTo (self, to):
        self.to = to #urllib.parse.quote(to)
        return
    
    def getTo (self):
        return self.to   
    
    def setText (self, text):
        #print(text)
        self.text = urllib.parse.quote(text)
        #print(self.text)
        return
    
    def getText (self):
        return self.text 
    
    def enviar(self, to, text):
        self.setTo(to)
        self.setText(text)
        sendString = """{0}cgi-bin/sendsms?username={1}&password={2}&smsc={3}&to={4}&text={5}tú9""".format(
        self.getHttpUrl(),
        self.getUsername(),
        self.getPassword(),
        self.getSmsc(),
        self.getTo(),
        self.getText())  
        print(sendString)
        #print("Sending html request: " + sendString)
        requests.packages.urllib3.disable_warnings()
        response = requests.get(sendString, verify=False)
        print("Http response received: ")
        print(response.text)
        return

if __name__ == '__main__':

    #kannel = SmsKannel()
    #print()
    #kannel.enviar("+584127239359","hola mundo cruel22")
    print(urllib.parse.unquote("Miranda%20.%0ASi%20no%20eres%20tú%20ignora%20este%20mensaje.%0A"))
    print(len("Este mensaje contiene 160 caracteres, con espacios incluidos. Los que admite hoy un mensaje SMS. Con un coste medio de 0,15 euros, aproximadamente (no hay queww"))
    