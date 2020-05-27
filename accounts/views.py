from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import signup_form, login_form
from django.urls import reverse
from django.db import IntegrityError


def login_page(request):
    template_name = 'accounts/login.html'

    context = {
        "login_api_url": reverse('login_api'),
        "chat_page_url": reverse('chat-page')
    }

    return render(request, template_name, context)


def signup_page(request):
    template_name = 'accounts/signup.html'

    context = {
        "signup_api_url": reverse('signup_api')
    }

    return render(request, template_name, context)


class login_api(APIView):
    def post(self, request):
        # Form
        form = login_form(
            request.POST)

        # Validate form
        if form.is_valid() is False:
            return Response({
                'msg': '',
                'error_flag': 1,
                'error': 'invalid parameters',
                'data': '',
            })

        # Get cleaned data
        username = form.cleaned_data["email"]
        password = form.cleaned_data["password"]

        # Create user
        try:
            User.objects.get(username=username, password=password)
        except:
            return Response({
                'msg': '',
                'error_flag': 1,
                'error': 'login failed',
                'data': '',
            })

        # Response
        return Response({
            'msg': 'log in successful',
            'error_flag': 0,
            'error': '',
            'data': '',
        })


class signup_api(APIView):
    def post(self, request):
        # Form
        form = signup_form(
            request.POST)

        # Validate form
        if form.is_valid() is False:
            return Response({
                'msg': '',
                'error_flag': 1,
                'error': 'invalid parameters',
                'data': '',
            })

        # Get cleaned data
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]

        # Create user
        try:
            User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                username=email,
            ).save()
        except IntegrityError:
            return Response({
                'msg': '',
                'error_flag': 1,
                'error': 'account already exist',
                'data': '',
            })

        # Response
        return Response({
            'msg': 'account created successfully',
            'error_flag': 0,
            'error': '',
            'data': '',
        })
