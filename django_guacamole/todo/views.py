from django.shortcuts import render
from .forms import task_form
from django.http import HttpResponseRedirect
from django.urls import reverse

def show(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "todo/list.html",{
        "tasks": request.session["tasks"]
    })

def new(request):
    if request.method == "POST":
        form = task_form(request.POST)
        if form.is_valid():
            request.session["tasks"] += [form]
            return HttpResponseRedirect(reverse("todo:index"))
        else:
            render(request, "todo/new.html", {
                "form": form
            }) 
    else:
        return render(request, "todo/new.html",{
            "form": task_form()
        })
