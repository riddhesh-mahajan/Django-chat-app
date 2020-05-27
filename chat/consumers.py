# import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        pass
        # employee_jwt_token = self.scope['url_route']['kwargs']['employee_jwt_token']
        # jwt_data = jwt_tool.verify(employee_jwt_token)

        # if jwt_data is not False:
        #     employee_id = jwt_data['employee_id']
        #     plan = jwt_data['plan']

        #     # Only allow connection to plan greater than or equal to 2
        #     if plan >= 2:
        #         chat_room = f'chat_room_{employee_id}'
        #         self.chat_room = chat_room

        #         await self.channel_layer.group_add(
        #             chat_room,
        #             self.channel_name,
        #         )

        #         await self.send({
        #             "type": "websocket.accept",
        #         })

    async def websocket_receive(self, event):
        pass
        # json_data = json.loads(event['text'])

        # msg = json_data['msg']
        # jwt_token = json_data['jwt_token']
        # receiver_employee_id = json_data['receiver_employee_id']

        # jwt_data = jwt_tool.verify(jwt_token)

        # if jwt_data is not False:
        #     if jwt_data['employee_id'] != receiver_employee_id:
        #         # Save message in database
        #         await self.save_message(jwt_data['employee_id'],
        #                                 receiver_employee_id, msg)

        #         # Broadcast message
        #         broadcast_msg = {
        #             'msg': msg,
        #             'sender': jwt_data['employee_id'],
        #         }
        #         await self.channel_layer.group_send(
        #             f"chat_room_{receiver_employee_id}",
        #             {
        #                 "type": "chat_message",
        #                 "message": json.dumps(broadcast_msg),
        #             }
        #         )

    async def chat_message(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event['message']
        })

    async def websocket_disconnect(self, event):
        pass

    @database_sync_to_async
    def save_message(self, sender_id, receiver_id, msg):
        msg_obj = messages(
            sender_id=sender_id,
            receiver_id=receiver_id,
            msg=msg,
        )

        msg_obj.save()
