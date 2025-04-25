from rest_framework import generics
from .serializers import PoliticaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Politica, Analise
from django.conf import settings
import requests

class PoliticaCreateView(generics.CreateAPIView):
    queryset = Politica.objects.all()
    serializer_class = PoliticaSerializer

class PoliticaListView(generics.ListAPIView):
    queryset = Politica.objects.all()
    serializer_class = PoliticaSerializer

class PoliticaDetailView(generics.RetrieveAPIView):
    queryset = Politica.objects.all()
    serializer_class = PoliticaSerializer

class PoliticaAnaliseAPIView(APIView):
    def post(self, request, pk):
        politica = Politica.objects.get(pk=pk)
        headers = {
          "Authorization": f"Bearer {settings.MISTRAL_API_KEY}",
          "Content-Type": "application/json"
        }
        data = {
          "model": "mistral-tiny",
          "messages": [
            {"role":"user","content":f"Simplifique:\n\n{politica.conteudo}"}
          ]
        }
        r = requests.post("https://api.mistral.ai/v1/chat/completions",
                          headers=headers, json=data, timeout=15)
        try:
            texto = r.json()['choices'][0]['message']['content']
        except Exception:
            texto = "Erro na análise."
        analise, _ = Analise.objects.update_or_create(
            politica=politica, defaults={'resultado': texto}
        )
        return Response({'resultado': texto}, status=status.HTTP_200_OK)