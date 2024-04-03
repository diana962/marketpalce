from comment import views
from django.urls import path


urlpatterns = [
    path('', views.CommenCreateView.as_view()),
    path('<int:pk>/', views.CommentDetailView.as_view()),
]