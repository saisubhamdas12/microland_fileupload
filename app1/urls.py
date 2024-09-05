from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_page'),
    path('upload/', views.upload_view, name='upload_page'),
    path('summary/', views.summary_view, name='summary_page'),
]
