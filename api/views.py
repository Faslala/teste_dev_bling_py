# cspell:disable
'''TBD'''
from django.shortcuts import redirect, HttpResponse
from decouple import config
import requests
from .models import Venda

def bling_auth(request):
    '''TBD'''
    client_id = config('BLING_CLIENT_ID')
    state = request.GET.get('state')
    auth_url = (
    f"https://bling.com.br/Api/v3/oauth/authorize?response_type=code"
    f"&client_id={client_id}&state={state}"
)

    return redirect(auth_url)

def bling_callback(request):
    '''TBD'''
    code = request.GET.get('code')
    # state = request.GET.get('state')

    # Faça a requisição do access_token usando o code
    token_url = "https://bling.com.br/Api/v3/oauth/token"
    auth = requests.auth.HTTPBasicAuth(config('BLING_CLIENT_ID'), config('BLING_CLIENT_SECRET'))
    data = {
        'grant_type': 'authorization_code',
        'code': code
    }
    response = requests.post(token_url, auth=auth, data=data, timeout=10)

    # Processar o access_token retornado
    return response.json()

def import_data():
    '''TBD'''
    access_token = "access_token_obtido"  # Salve e reutilize o access_token em sessões
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    vendas_url = "https://api.bling.com.br/Api/v3/vendas"
    response = requests.get(vendas_url, headers=headers, timeout=10)

    if response.status_code == 200:
        vendas = response.json()
        for venda in vendas['retorno']['vendas']:
            # Salvar no banco de dados
            Venda.objects.create(
                id_venda=venda['numero'],
                cliente=venda['cliente']['nome'],
                total=venda['totalvenda'],
                data_venda=venda['data']
            )
    return HttpResponse("Importação realizada com sucesso")
