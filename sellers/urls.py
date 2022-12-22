from django.urls import path
from . import views

sellers_path = '<int:pk>/'

app_name = 'sellers'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path(sellers_path, views.DetailView.as_view(), name = 'detail'),
    path(sellers_path + 'results/', views.ResultsView.as_view(), name = 'results'),
    path('<int:seller_id>/add/', views.add, name = 'add'),
]