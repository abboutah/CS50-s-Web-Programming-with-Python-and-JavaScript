from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
tasks = ["HTML/CSS", "GIT", "PYTHON", "DJANGO", "SQL", "JS", "UI", "TESTING", "CI/CD", "SCALABILITY", "SECURITY"]
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
def add(request):
    if request.method == "POST": 
        form = NewTaskForm(request.POST) #figure out all data submitted
        if form.is_valid():
            task = form.cleaned_data["task"] #add to task variable
            tasks.append(task)
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
             return render(request, "tasks/add.html", {
             "form": form
                })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
