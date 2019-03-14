from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from vote.consumers import EchoConsumer

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    "websocket": URLRouter([
        path("home/", EchoConsumer),
    ])

})
