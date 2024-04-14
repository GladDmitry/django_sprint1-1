from django.urls import path
from .views import about


app_name = 'pages'

urlpatterns = [
    path('about/', about, name='about'),     
]