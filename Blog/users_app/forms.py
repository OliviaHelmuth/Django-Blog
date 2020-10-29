from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from cloudinary.forms import CloudinaryFileField


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']

class AvatarUploadForm(forms.ModelForm):
    image = CloudinaryFileField(
        options = {
            'width': 300,
            'height': 300,
            'folder': 'profile_pictures'
       }
    )
    class Meta:
        model = Profile
        fields = ('image',)
