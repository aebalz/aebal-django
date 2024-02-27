from api.v1 import item
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'item', item.ItemModelViewSet, basename='item')

urlpatterns = [
    path('', include(router.urls)),
]