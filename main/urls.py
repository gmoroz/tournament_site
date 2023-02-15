from django.urls import path

from .views import GamesView

urlpatterns = [
    path("games/", GamesView.as_view(), name="games"),
]
