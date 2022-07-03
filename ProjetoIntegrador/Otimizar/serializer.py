from dataclasses import fields
from rest_framework import serializers
from Otimizar.models import Peca, Sobra, Aproveita

class PecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peca
        fields = '__all__'

class SobraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sobra
        fields = '__all__'

class AproveitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aproveita
        fields = '__all__'

class ListaAproveitaSobraSerializer(serializers.ModelSerializer):
    peca = serializers.ReadOnlyField(source = 'peca.material')

    class Meta:
        model = Aproveita
        fields = '__all__'