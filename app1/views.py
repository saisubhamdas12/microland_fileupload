# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import LoginForm, FileUploadForm
from .models import FileUpload

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('upload_page')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def upload_view(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.user = request.user  
            file_instance.save() 
            return redirect('summary_page')
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})

@login_required
def summary_view(request):
    uploads = FileUpload.objects.filter(user=request.user)
    return render(request, 'summary.html', {'uploads': uploads})

