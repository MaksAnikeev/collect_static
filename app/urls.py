from django.urls import path

from .views import add_statistic, get_statistic, clear_statistic

app_name = "app"

urlpatterns = [
    path('statistic_day/add', add_statistic),
    path('statistics/get', get_statistic),
    path('statistics/clear', clear_statistic)
]
