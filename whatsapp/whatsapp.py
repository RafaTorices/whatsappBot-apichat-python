import json
import requests
from config import ApiConfig
from opciones import Opciones


class whatsapp():
    def __init__(self, json):
        self.json = json
        self.dict_messages = json['messages']
        config = ApiConfig()
        opciones = Opciones()
        self.ApiUrl = config.APIURL
        self.token = config.TOKEN
        self.tituloApp = config.TITULO_APP
        self.emailApp = config.EMAIL_SOPORTE
        self.enviarOpciones = opciones.enviarOpciones()

    def send_requests(self, method, data):
        url = f"{self.ApiUrl}{method}?token={self.token}"
        headers = {'Content-type': 'application/json'}
        answer = requests.post(url, data=json.dumps(data), headers=headers)
        # Guardo el mensaje recibido en un fichero json
        # with open('data.json', 'w') as file:
        #     json.dump(self.dict_messages, file, indent=4)
        return answer.json()

    def send_message(self, chatId, text):
        data = {"chatId": chatId,
                "body": text}
        answer = self.send_requests('sendMessage', data)
        return answer

    def processing(self):
        if self.dict_messages != []:
            for message in self.dict_messages:
                body = message['body']
                chatId = message['chatId']
                author = message['author']
                author = author[2:11]
                fromMe = message['fromMe']
                chatName = message['chatName']
                if not fromMe:
                    if body.lower() == 'hola':
                        return self.send_message(chatId, self.tituloApp+'Hooola !!')
                    else:
                        return self.send_message(chatId, self.tituloApp+'No entiendo tu mensaje: *'+body+'*, estas son las opciones que tengo:\n'+self.enviarOpciones)
