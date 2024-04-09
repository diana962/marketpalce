from django.urls import path, include
from payment import views

urlpatterns = [
    path('', views.PaymentCreateView.as_view()),
    path('', views.PaymentSuccessView.as_view())
]
