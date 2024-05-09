from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('clients', views.ClientViewSet)
router.register('pets', views.PetViewSet)
router.register('species', views.SpecieViewSet)
router.register('breeds', views.BreedViewSet)
router.register('pet_sizes', views.PetSizeViewSet)
router.register('pet_gender', views.PetGenderViewSet)
router.register('services_names', views.Services_NamesViewSet)
router.register('services', views.ServicesViewSet)
router.register('appointments', views.AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
