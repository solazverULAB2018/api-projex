# mysite/routing.py
from channels.routing import ProtocolTypeRouter
from django.urls import path

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from .consumers import NotificationConsumer


websockets = URLRouter([
    path(
        "ws/notifications/projects/<int:project-id>",
        NotificationConsumer,
        name="ws_notifications_project",
    ),
    path(
        "ws/notifications/tasks/<int:task-id>",
        NotificationConsumer,
        name="ws_notifications_tasks",
    )
])


application = ProtocolTypeRouter({
    # (http->django views is added by default)
    "websocket": AuthMiddlewareStack(websockets),
})