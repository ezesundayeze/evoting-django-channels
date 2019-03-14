from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "template_name", context)

# Create your views here.
