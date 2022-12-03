from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

__author__ = 'BENZNANA Mohamed : benznana.med@gmail.com'


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
