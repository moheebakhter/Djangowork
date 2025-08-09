

from django.urls import path,include
from . import views

urlpatterns = {
    path("", views.Index, name="index"),
    path("a", views.About_page, name="about"),
    path("c", views.Contact_page, name="con")
}