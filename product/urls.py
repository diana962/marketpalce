from django.urls import path, include
from product import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.ProductViewSet)

urlpatterns = [
    # path('', views.PosstListCreate.as_view()),
    # path('<int:pk>/', views.PostDetailView.as_view()),
    path('', include(router.urls)),
]

