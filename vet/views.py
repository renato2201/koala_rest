from rest_framework import viewsets
from . import models
from . import serializers


class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = models.Pet.objects.all()
    serializer_class = serializers.PetSerializer


class PetSizeViewSet(viewsets.ModelViewSet):
    queryset = models.PetSize.objects.all()
    serializer_class = serializers.PetSizeSerializer


class PetGenderViewSet(viewsets.ModelViewSet):
    queryset = models.PetGender.objects.all()
    serializer_class = serializers.PetGenderSerializer


class SpecieViewSet(viewsets.ModelViewSet):
    queryset = models.Specie.objects.all()
    serializer_class = serializers.SpecieSerializer


class BreedViewSet(viewsets.ModelViewSet):
    queryset = models.Breed.objects.all()
    serializer_class = serializers.BreedSerializer


class Services_NamesViewSet(viewsets.ModelViewSet):
    queryset = models.Services_Names.objects.all()
    serializer_class = serializers.Services_NamesSerializer


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = models.Services.objects.all()
    serializer_class = serializers.ServicesSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer
