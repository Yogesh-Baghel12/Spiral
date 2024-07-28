from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path("",views.INDEX,name='home'),
    path("add",views.ADD,name="add"),
    path("update/<str:id>",views.update,name='update'),
    path("delete/<str:id>",views.delete,name='delete'),
]