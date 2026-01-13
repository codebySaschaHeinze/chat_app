from django.urls import path
from .views import chat_view, delete_chat

urlpatterns = [
    path("chat/", chat_view, name="chat"),
    path("chat/<int:chat_id>/", delete_chat),
]
