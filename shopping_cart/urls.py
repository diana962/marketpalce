from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddToCartView.as_view()),
    path('remove/', views.RemoveFromCartView.as_view()),
    path('view/', views.ViewCartView.as_view())
]
