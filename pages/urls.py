from django.urls import path
from view import HomPageView, AboutPageView

urlspatterns = [
    path("", HomePagesView.as_view(),name= "home"),
    path("home/", HomePageView.as_view(), name= "home_two"),
    patr("sbout/", AboutPageView.as_view(), name="about"),

]