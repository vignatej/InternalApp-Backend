import json
from django.db.models import Q
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Message
from .serializers import MessageSerializer
from users.models import profile
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print('connection started')
        self.count = 0
        self.sender_id = int(self.scope['url_route']['kwargs']['sender_id'])
        self.receiver_id = int(self.scope['url_route']['kwargs']['reciever_id'])
        self.mi = min(self.sender_id, self.receiver_id)
        self.ma = max(self.sender_id, self.receiver_id)
        self.room_name = f"chat_{self.mi}_{self.ma}"
        old_msg = Message.objects.filter(room = self.room_name)
        ser = MessageSerializer(old_msg, many=True)
        print('begin of accept')
        self.accept()
        print('accepted')
        
        self.send(json.dumps(ser.data))
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name
        )
        print(f'sucessfully added ------------${self.mi}-${self.ma}')

    
    def disconnect(self, close_code):
        print(f'closing connection-${self.mi}-${self.ma}')
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name,
            self.channel_name
        )
        pass
    
    # receive message from WebSocket
    def receive(self, text_data):
        # if (self.count == 0):
        #     #check if user is authenticated
        #     # if not authenticated, self.close() him
        #     pass

        message_data = json.loads(text_data)
        message = message_data['message']
        print(self.room_name)
        try:
            msgobj = Message.objects.create(
                sender = profile.objects.get(id = self.sender_id),
                reciever = profile.objects.get(id = self.receiver_id),
                text = message_data['message'],
                room = self.room_name, 
            )
            msgobj.save()
            ser = MessageSerializer(msgobj, many=False)
            print(message)
            async_to_sync(self.channel_layer.group_send)(
                self.room_name,
                {
                    'type': 'chat_message_one_to_one',
                    'message': ser.data
                }
            )
        
        except:
            print('exception occured in recieve')
            pass        
        # send message to WebSocket
    
    def chat_message_one_to_one(self, event):
        print('inside chat msg one to one')
        print(event)
        self.send(json.dumps(event))