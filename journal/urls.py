from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

#Creating router for the viewsets
router = DefaultRouter()
router.register(r'entries', views.EntryViewSet)
router.register(r'user-profiles', views.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]