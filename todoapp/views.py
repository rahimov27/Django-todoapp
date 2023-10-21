from django.shortcuts import render
from .models import MessageModel
from .forms import MessageForm


def todo_view(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MessageForm

    tasks = MessageModel.objects.all().order_by()

    return render(request, "index.html", {"form": form, "tasks": tasks})
