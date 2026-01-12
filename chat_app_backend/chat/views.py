from django.shortcuts import render

# Create your views here.

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Chat

@csrf_exempt
@require_http_methods(["GET"])
def chat_view(request):
    chats = Chat.objects.order_by("created_at")
    data = [
        {
            "id": chat.id,
            "name": chat.name,
            "message": chat.message,
            "created_at": chat.created_at.isoformat(),
        }

        for chat in chats
    ]
    return JsonResponse(data, safe=False)