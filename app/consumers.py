from channels.consumer import SyncConsumer, AsyncConsumer
import time
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
class MyChatConsumer(AsyncConsumer):
    
    async def websocket_connect(self, event):
        print('websocket connect method', event)
        #adding a channel to nex or existing group
        await self.channel_layer.group_add('programmers', self.channel_name)
        await self.send({'type':'websocket.accept'})
        
    async def websocket_receive(self, event):
        print('message received', event)
        
        await self.channel_layer.group_send(
            'programmers', {'type':'chat.message', 'text':event['text']}
        )
        
    async def chat_message(self, event):
            await self.send({
                'type':'websocket.send', 'text':event['text']
            })
        
       
        
    async def websocket_disconnect(self, event):
        print('connection disconnected', event)
        raise StopConsumer()


#consumers for simple understanding of channels
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('my sync consumer connected', event)
        self.send({
            'type':'websocket.accept'
        })
    def websocket_receive(self, event):
        print('mysync consumer data received', event)
        for i in range(50):
            self.send({
                'type':'websocket.send',
                'text':str(i)
            })
            time.sleep(1)    
    def websocket_disconnect(self, event):
        print('mysync consumer disconnect')



class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('my sync consumer connected', event)
        await self.send({'type':'websocket.accept'})
    
    async def websocket_receive(self, event):
        print('mysync consumer data received')
    
    async def websocket_disconnect(self, event):
        print('mysync consumer disconnect')