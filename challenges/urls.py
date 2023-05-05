from django.urls import path
from . import views

# URL Config
urlpatterns = [
    # path("january", views.january),
    # path("february", views.february),
    path("", views.home, name="home"),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]
