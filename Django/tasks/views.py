from django.shortcuts import render

tasks = ["HTML/CSS", "GIT", "PYTHON", "DJANGO", "SQL", "JS", "UI", "TESTING", "CI/CD", "SCALABILITY", "SECURITY"]
# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
