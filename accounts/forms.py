from django import forms


class signup_form(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()


class login_form(forms.Form):
    email = forms.CharField()
    password = forms.CharField()
