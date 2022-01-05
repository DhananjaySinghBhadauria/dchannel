from channels.consumer import SyncConsumer, AsyncConsumer
import time

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