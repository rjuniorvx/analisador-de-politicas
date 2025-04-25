from rest_framework import serializers
from .models import Politica, Analise

class AnaliseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analise
        fields = ['resultado', 'analisado_em']

class PoliticaSerializer(serializers.ModelSerializer):
    analise = AnaliseSerializer(read_only=True)

    class Meta:
        model = Politica
        fields = ['id', 'titulo', 'conteudo', 'criado_em', 'analise']
        read_only_fields = ['id', 'criado_em', 'analise']