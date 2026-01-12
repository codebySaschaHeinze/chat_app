from django.shortcuts import render

# Create your views here.

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Chat

@csrf_exempt
@require_http_methods(["GET", "POST"])
def chat_view(request):
    if request.method == "GET":
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
    
    payload = json.loads(request.body)

    name = (payload.get("name") or "").strip()
    message = (payload.get("message") or "").strip()

    if not name:
        return JsonResponse({"error": "name ist required"}, status=400)
    if not message:
        return JsonResponse({"error": "message ist required"}, status=400)

    chat = Chat.objects.create(
        name=name, 
        message=message,
    )
    
    return JsonResponse(
        {
            "id": chat.id, 
            "name": chat.name,
            "message": chat.message,
            "created_at": chat.created_at.isoformat(),
        },
        status=201,
    )