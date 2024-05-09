from . import models
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pet
        fields = '__all__'


class PetSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PetSize
        fields = '__all__'


class PetGenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PetGender
        fields = '__all__'


class SpecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specie
        fields = '__all__'


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Breed
        fields = '__all__'


class Services_NamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Services_Names
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Services
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Appointment
        fields = '__all__'
