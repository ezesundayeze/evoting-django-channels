from django.shortcuts import render
from .models import Party, User, Vote


def index(request):
    parties = Party.objects.all()
    print(request)

    context = {"parties": parties}
    return render(request, "votes/index.html", context)

# Create your views here.
