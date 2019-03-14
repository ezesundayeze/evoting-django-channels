from channels.consumer import AsyncConsumer


class EchoConsumer(AsyncConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("notify_voters", self.channel_name)

    async def disconnect(self):
        await self.channel_layer.group_discard("notify_voters", self.channel_name)

    async def user_vote(self, event):
        await self.send_json(event)
