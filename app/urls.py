from django.urls import include, path

from rest_framework import routers

from app.views import UserRegisterView, TeamViewSet, PlayerViewSet, login

router = routers.DefaultRouter()
router.register(r'team', TeamViewSet)
router.register(r'player', PlayerViewSet)


urlpatterns = [
   path('', include(router.urls)),
   path('login/', login, name='login'),
   path('register/', UserRegisterView.as_view(), name='register'),
]