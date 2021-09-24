from django.shortcuts import render

# Create your views here.
from .models import Compiti


def index(request):
    return render(request, "sito/index.html", {
        "compiti": Compiti.objects.all()
    })
