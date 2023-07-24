from django.urls import path
from results import views

app_name='election_result'

urlpatterns = [
    path('', views.result, name='result')
]
