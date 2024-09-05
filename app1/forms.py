from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import FileUpload

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['file_name']  
        widgets = {
            'file_name': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

