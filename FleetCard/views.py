from django.shortcuts import render

from .veiculos_api import (
    buscar_carros,
    buscar_motos,
    buscar_caminhoes,
    buscar_imagem,
)


def home(request):
    return render(request, 'home.html')


def sobre(request):
    return render(request, 'sobre.html')


def contatos(request):
    return render(request, 'contatos.html')


def pagina_veiculos(request):

    # Busca os veículos
    carros = buscar_carros()[:5]
    motos = buscar_motos()[:5]
    caminhoes = buscar_caminhoes()[:5]

    # Busca imagens dos carros
    for veiculo in carros:
        veiculo["imagem"] = buscar_imagem(
            veiculo["Make_Name"],
            veiculo["Model_Name"],
            "car"
        )

    # Busca imagens das motos
    for veiculo in motos:
        veiculo["imagem"] = buscar_imagem(
            veiculo["Make_Name"],
            veiculo["Model_Name"],
            "moto"
        )

    # Busca imagens dos caminhões
    for veiculo in caminhoes:
        veiculo["imagem"] = buscar_imagem(
            veiculo["Make_Name"],
            veiculo["Model_Name"],
            "caminhao"
        )

    # Envia os veículos para a página
    contexto = {
        "carros": carros,
        "motos": motos,
        "caminhoes": caminhoes,
    }

    return render(
        request,
        "pagina_veiculos.html",
        contexto
    )


def ver_detalhes(request, tipo, marca, modelo):

    # Define o nome do tipo
    nomes_tipos = {
        "car": "Carro",
        "moto": "Moto",
        "caminhao": "Caminhão",
    }

    # Busca a imagem do veículo
    imagem = buscar_imagem(
        marca,
        modelo,
        tipo
    )

    # Monta os dados do veículo
    veiculo = {
        "marca": marca,
        "modelo": modelo,
        "tipo": nomes_tipos.get(tipo, "Veículo"),
        "imagem": imagem,
    }

    # Envia os dados para a página de detalhes
    return render(
        request,
        "ver_detalhes.html",
        {
            "veiculo": veiculo
        }
    )