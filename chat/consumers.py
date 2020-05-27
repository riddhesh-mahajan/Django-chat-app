# import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        chat_room = f'chat_room'
        self.chat_room = chat_room

        await self.channel_layer.group_add(
            chat_room,
            self.channel_name,
        )

        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        json_data = json.loads(event['text'])

        msg = json_data['msg']
        email = json_data['email']

        # Broadcast message
        broadcast_msg = {
            'msg': msg,
            'email': email,
        }

        await self.channel_layer.group_send(
            f"chat_room",
            {
                "type": "chat_message",
                "message": json.dumps(broadcast_msg),
            }
        )

    async def chat_message(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event['message']
        })

    async def websocket_disconnect(self, event):
        pass
