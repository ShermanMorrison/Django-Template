from django.shortcuts import render, get_object_or_404

from .models import ChatRoom

def index(request):
  chat_rooms = ChatRoom.objects.order_by('name')[:5]
  context = {
    'chat_list': chat_rooms,
  }
  return render(request,'chatapp/index.html', context)

def chat_room(request, pk):
  chat = get_object_or_404(ChatRoom, pk=pk)
  return render(request, 'chatapp/chat_room.html', {'chat': chat})
