from django.urls import path

from chat import views

urlpatterns = [
    path("", views.index, name="index"),
    path("room/<str:room_name>/", views.room, name="room"),
    path(
        "admin_message/<str:room_name>/<str:message>/",
        views.send_admin_message_to_room,
        name="admin_message",
    ),
]
