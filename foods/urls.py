from django.urls import path
from . import views

app_name = 'foods'
urlpatterns = [
    path('', views.index),
    path('foods/', views.FoodView.as_view()),
    path('menu/', views.menu),
    # path('test/', views.food),
    path('<int:pk>', views.FoodDetailView.as_view())

]
