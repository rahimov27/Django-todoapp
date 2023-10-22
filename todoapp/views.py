from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .models import MessageModel
from .forms import MessageForm


def todo_view(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MessageForm

    tasks = MessageModel.objects.all()

    return render(request, "index.html", {"form": form, "tasks": tasks})


def delete_view(request, id):
    context = {}

    obj = get_object_or_404(MessageModel, id=id)

    if request.method == "POST":
        obj.delete()

        return HttpResponseRedirect("/")

    return render(request, "index.html", context)
