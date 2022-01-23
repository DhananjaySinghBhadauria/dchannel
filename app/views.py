from django.shortcuts import render
from django.views import View

# Create your views here.

def home(request):
    return render(request, 'app/index.html')


class ChatView(View):
    def get(self, request):
        return render(request, 'app/chat.html')