from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import signup_form
from django.urls import reverse
from django.db import IntegrityError


def login_page(request):
    template_name = 'accounts/login.html'

    context = {

    }

    return render(request, template_name, context)


def signup_page(request):
    template_name = 'accounts/signup.html'

    context = {
        "signup_api_url": reverse('signup_api')
    }

    return render(request, template_name, context)


class signup_api(APIView):
    def post(self, request):
        # Form
        form = signup_form(
            request.POST)

        # Validate form
        if form.is_valid() is False:
            return Response('invalid parameters')

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
            ).save()
        except IntegrityError:
            return Response('account already exist')

        # Response
        return Response('Account created successfully')
