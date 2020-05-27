from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
# from channels.security.websocket import OriginValidator

from chat.consumers import ChatConsumer


application = ProtocolTypeRouter({

    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    url(
                        "messages-tcp/(?P<employee_jwt_token>[^/ ]+)", ChatConsumer),
                ]
            )
        )
    )
})
