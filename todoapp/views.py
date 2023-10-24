from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .models import MessageModel
from .forms import MessageForm
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


def todo_view(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MessageForm
    tasks = MessageModel.objects.all()

    return render(request, "index.html", {"form": form, "tasks": tasks})
