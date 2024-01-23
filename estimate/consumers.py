from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer


class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        self.accept()

    def websocket_receive(self, message):
        print(message)
        self.send("不要回答")

    def websocket_disconnect(self, message):
        print(message)
        raise StopConsumer()