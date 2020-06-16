from django.contrib.auth import get_user_model
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = get_user_model()
        fields = '__all__'

class ChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = get_user_model()
        fields = '__all__'