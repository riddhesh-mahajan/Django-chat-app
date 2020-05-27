from django.urls import path
from . import views

urlpatterns = [
    # Views
    path('chat/',
         views.chat_page, name="chat-page"),
]
