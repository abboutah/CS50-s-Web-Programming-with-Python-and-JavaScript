from django.urls import path 
from . import views #import views file to acces index function
#list of available urls that can be accessed for this particular app
urlpatterns = [
    path("", views.index, name="index"), #index function from views file url/hello
    path("Abdelkhalek", views.Abdelkhalek, name="Abdelkhalek"), #url/hello/Abdelkhalek
    path("Boutahri", views.Boutahri, name="Boutahri"), #url/hello/Boutahri
    path("<str:name>", views.greet, name="greet"), #it can be any string url/hello/<any string>
    path("templates", views.templates, name="templates")
    #path("templates_greet", views.templates_greet, name="templates_greet")
]