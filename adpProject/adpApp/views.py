from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from .models import Politica, Analise
from .forms import PoliticaForm
from django.conf import settings
import requests

def listar_politicas(request):
    politicas = Politica.objects.all()
    return render(request, 'adpApp/listar.html', {'politicas': politicas})


def criar_politica(request):
    if request.method == 'POST':
        form = PoliticaForm(request.POST)
        if form.is_valid():
            politica = form.save()
            return redirect('ver_politica', politica.id)
    else:
        form = PoliticaForm()
    return render(request, 'adpApp/criar.html', {'form': form})


def ver_politica(request, politica_id):
    politica = get_object_or_404(Politica, id=politica_id)
    return render(request, 'adpApp/ver.html', {'politica': politica})


def analisar_politica(request, politica_id):
    politica = get_object_or_404(Politica, id=politica_id)
    if hasattr(politica, 'analise'):
        return redirect('ver_politica', politica.id)

    headers = {
        'Authorization': f"Bearer {settings.MISTRAL_API_KEY}",
        'Content-Type': 'application/json'
    }
    payload = {
        'model': 'mistral-tiny',
        'messages': [
            {'role': 'user',
             'content': f"Simplifique essa política:\n\n{politica.conteudo}"}
        ]
    }

    try:
        resp = requests.post(
            'https://api.mistral.ai/v1/chat/completions',
            headers=headers,
            json=payload,
            timeout=15
        )
        resp.raise_for_status()
        data = resp.json()
        resultado = data['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        resultado = f"Erro de requisição à API Mistral: {e}"
    except (ValueError, KeyError) as e:
        resultado = f"Resposta inesperada da API Mistral: {e}"

    Analise.objects.create(politica=politica, resultado=resultado)
    return redirect('ver_politica', politica.id)
