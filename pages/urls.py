from django.urls import path

from .views import (HomeView, IndexView,
                    PortfolioView, AboutView)

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('index', IndexView.as_view(), name="index"),
    path("portfolio", PortfolioView.as_view(), name="portfolio"),
    path("about", AboutView.as_view(), name="about"),
]
