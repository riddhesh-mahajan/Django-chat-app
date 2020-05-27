from django.shortcuts import render


def chat_page(request):
    template_name = 'chat/chat.html'

    context = {

    }

    return render(request, template_name, context)
