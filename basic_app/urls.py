from django.urls import path
from basic_app.views import details

urlpatterns = [
    path('',details, name= 'info')
]
