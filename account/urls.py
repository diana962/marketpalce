from django.urls import path, include
from rest_framework.routers import SimpleRouter

from account.views import UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = SimpleRouter()
router.register('', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
