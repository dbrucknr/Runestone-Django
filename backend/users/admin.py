from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import ChangeForm, CreationForm

User = get_user_model()
class Admin(UserAdmin):
    add_form = CreationForm
    form = ChangeForm
    model = User
    
admin.site.register(User)
