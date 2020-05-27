from django.urls import path
from . import views

urlpatterns = [
    # Views
    path('login/',
         views.login_page, name="login-page"),
    path('signup/',
         views.signup_page, name="signup-page"),

    # APIs
    path('signup_api/', views.signup_api.as_view(), name="signup_api"),
]
