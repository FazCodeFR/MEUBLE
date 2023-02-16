from myApp1.models import *
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class RealisateurSerializer(ModelSerializer):
    class Meta:
        model = Realisateur
        fields = '__all__'
        # depth = 1


class ScenarioSerializer(ModelSerializer):
    class Meta:
        model = Scenario
        fields = '__all__'
        # depth = 1


class FilmSerializer(ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'
        # depth = 1


class ActeurSerializer(ModelSerializer):
    class Meta:
        model = Acteur
        fields = '__all__'
        # depth = 1


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        # depth = 1


class EmprunterSerializer(ModelSerializer):
    class Meta:
        model = Emprunter
        fields = '__all__'
        # depth = 1
