from django.urls import path 

from . import views 

app_name='core'

urlpatterns = [
    path("", views.index, name="index" ),
    path("contact", views.contact, name="contact"),
    path("<int:pk>", views.get_item, name = "details"),
    path("signup", views.signup, name="signup"),
]






