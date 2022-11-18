from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('coffees/', views.coffees_index, name='index'),
    path('coffees/<int:coffee_id>/', views.coffees_detail, name='detail'),
    path('coffees/create/', views.CoffeeCreate.as_view(), name='coffees_create'),
    path('coffees/<int:pk>/update/', views.CoffeeUpdate.as_view(), name='coffees_update'),
    path('coffees/<int:pk>/delete/', views.CoffeeDelete.as_view(), name='coffees_delete'),
    path('coffees/<int:coffee_id>/add_location/', views.add_location, name='add_location'),
    path('ratings/', views.RatingList.as_view(), name='ratings_index'),
    path('ratings/<int:pk>/', views.RatingDetail.as_view(), name='ratings_detail'),
    path('ratings/create/', views.RatingCreate.as_view(), name='ratings_create'),
    path('ratings/<int:pk>/update/', views.RatingUpdate.as_view(), name='ratings_update'),
    path('ratings/<int:pk>/delete/', views.RatingDelete.as_view(), name='ratings_delete'),
    path('coffees/<int:coffee_id>/assoc_rating/<int:rating_id>/', views.assoc_rating, name='assoc_rating'),
    path('accounts/signup/', views.signup, name='signup'),


]