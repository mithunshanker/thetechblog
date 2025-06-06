from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name="Home"),
    path("details/<str:id>",views.details,name="Details")
]