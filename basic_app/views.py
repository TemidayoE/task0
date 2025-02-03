from django.shortcuts import render
from django.http import JsonResponse
from django.utils.timezone import now

def details(request):
  data = {
    "email": "temidayoejide1@gmail.com",
    "current_datetime": now().isoformat(),
    "github_url": "https://github.com/TemidayoE/task0"
  }
  
  return JsonResponse(data)