from chat.serializers import MessageSerializer
from users.models import profile
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from .models import Message

from django.db.models import Q

class chatConsumer(WebsocketConsumer):
    def connect(self):
        self.sender_id = int(self.scope['url_route']['kwargs']['sender_id'])
        a = profile.objects.values_list('id')
        self.roomnames=[]
        for i in a:
            id = int(i[0])
            if id==self.sender_id:
                continue
            mi = min(self.sender_id, id)
            ma = max(self.sender_id, id)
            roomName = f'chat_{mi}_{ma}'
            async_to_sync(self.channel_layer.group_add)(
                roomName,
                self.channel_name,
            )
            self.roomnames.append(roomName)
            print(f'sucessfully added ------------$m{mi}-${ma}')
        self.accept()
        
    
    def disconnect(self, code):
        a = profile.objects.values_list('id')
        for i in a:
            id = int(i[0])
            if id==self.sender_id:
                continue
            mi = min(self.sender_id, id)
            ma = max(self.sender_id, id)
            roomName = f'chat_{mi}_{ma}'
            async_to_sync(self.channel_layer.group_discard)(
                roomName,
                self.channel_name,
            )
            self.roomnames.append(roomName)
            print(f'sucessfully closed ------------$m{mi}-${ma}')
    
    
    def receive(self, text_data):
        print("yoyo")
        message_data = json.loads(text_data)
        message = message_data['message']
        reciever_id = message_data['reciever_id']
        text = message_data['message']
        mi = min(self.sender_id, reciever_id)
        ma = max(self.sender_id, reciever_id)
        roomName = f'chat_{mi}_{ma}'
        print(message)
        try:
            msgobj = Message.objects.create(
                sender = profile.objects.get(id = self.sender_id),
                reciever = profile.objects.get(id = reciever_id),
                text = text,
                room = roomName, 
            )
            msgobj.save()
            ser = MessageSerializer(msgobj, many=False)
            print(message)
            async_to_sync(self.channel_layer.group_send)(
                roomName,
                {
                    'type': 'chat_message_one_to_one',
                    'message': ser.data
                }
            )
        
        except:
            print('exception occured in recieve')
            pass
    
    def chat_message_one_to_one(self, event):
        print('inside chat msg one to one')
        sent = event['message']
        self.send(json.dumps(sent))