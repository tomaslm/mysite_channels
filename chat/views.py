from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})


def send_admin_message_to_room(request, room_name, message):
    layer = get_channel_layer()
    async_to_sync(layer.group_send)(
        f"chat_{room_name}", {"type": "chat_message", "message": message}
    )
    return HttpResponse(f"Message {message} sent to {room_name}")
