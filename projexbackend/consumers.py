from channels.generic.websocket import AsyncJsonWebsocketConsumer
from rest_framework import serializers
from api.serializers import *
import json


class NotificationConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        # We're always going to accept the connection, though we may
        # close it later based on other factors.
        user = self.scope.get('user')
        group_name = user.get_group_name

        print("Hola mundo:  " + group_name)

        await self.channel_layer.group_add(
            group_name,
            self.channel_name,
        )
        await self.accept()

    async def notify(self, event):
        """
        This handles calls elsewhere in this codebase that look
        like:

            channel_layer.group_send(group_name, {
                'type': 'notify',  # This routes it to this handler.
                'content': json_message,
            })

        Don't try to directly use send_json or anything; this
        decoupling will help you as things grow.
        """

        await self.send_json(event["payload"])

    async def receive_json(self, content, **kwargs):
        """
        This handles data sent over the wire from the client.

        We need to validate that the received data is of the correct
        form. You can do this with a simple DRF serializer.

        We then need to use that validated data to confirm that the
        requesting user (available in self.scope["user"] because of
        the use of channels.auth.AuthMiddlewareStack in routing) is
        allowed to subscribe to the requested object.
        """

        # serializer = self.get_serializer(data=content)
        # if not serializer.is_valid():
        #     return
        # # Define this method on your serializer:
        # group_name = serializer.get_group_name()
        # # The AsyncJsonWebsocketConsumer parent class has a
        # # self.groups list already. It uses it in cleanup.
        # self.groups.append(group_name)
        # # This actually subscribes the requesting socket to the
        # # named group:
        # await self.channel_layer.group_add(
        #     group_name,
        #     self.channel_name,
        # )

        self.send(text_data=json.dumps({
            'message': 'Hello, World!'
        }))

    async def websocket_disconnect(self):
        super(self)
