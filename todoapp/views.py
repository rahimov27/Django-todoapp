from django.shortcuts import render, HttpResponse
from .models import MessageModel
from .forms import MessageForm


# Create your views here.
def index(request):
    return render(request, "index.html")


def create_view(request):
    context = {}

    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()

    context["form"] = form
    return render(request, "index.html", context)


def list_view(request):
    context = {}

    context["dataset"] = MessageModel.objects.all()

    return render(request, "index.html", context)
