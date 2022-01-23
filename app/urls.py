from django.urls import path
from . import views
from .views import ChatView

app_name="app"

urlpatterns = [
    path('', views.home, name="home"),
    path('chat/', ChatView.as_view())
]