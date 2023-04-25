from django.urls import path
from . import views


app_name = 'ads'
urlpatterns = [
    path('list/', views.AdListView.as_view()),
    path('create/', views.AdCreateView.as_view()),
]