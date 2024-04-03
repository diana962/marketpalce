from django.urls import path
from like import views

urlpatterns = [
    path('', views.RatingSerializer.as_view()),
    # path('delete/', views.RatingSerializer.as_view()),
]