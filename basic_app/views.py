from django.shortcuts import render
from django.http import JsonResponse
from django.utils.timezone import now

def details(request):
  data = {
    "slack_email": "temidayoejide1@gmail.com",
    "current_datetime": now().isoformat(),
    "git_repo": "https://github.com/TemidayoE/task0"
  }
  
  return JsonResponse(data)