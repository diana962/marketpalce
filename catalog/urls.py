from django.urls import path, include
# from category.views import category_list, category_create
from catalog import views

urlpatterns = [
    path('', views.CatalogCreateListView.as_view()),
    path('<int:pk>/', views.CatalogDetailView.as_view())
]