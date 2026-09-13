import pytest

from app import app, veiculos


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_pagina_inicial(client):
    resposta = client.get("/")

    assert resposta.status_code == 200
    assert b"Sistema de Controle de Manuten\xc3\xa7\xc3\xa3o" in resposta.data


def test_cadastro_de_veiculo(client):
    resposta = client.post(
        "/veiculos",
        data={
            "placa": "TEST123",
            "marca": "Volvo",
            "modelo": "FH 540"
        }
    )

    assert resposta.status_code == 302
    assert any(
        veiculo["placa"] == "TEST123"
        for veiculo in veiculos
    )


def test_nao_permite_placa_duplicada(client):
    client.post(
        "/veiculos",
        data={
            "placa": "DUP1234",
            "marca": "Scania",
            "modelo": "R 450"
        }
    )

    resposta = client.post(
        "/veiculos",
        data={
            "placa": "DUP1234",
            "marca": "DAF",
            "modelo": "XF 530"
        }
    )

    assert resposta.status_code == 302


def test_campos_obrigatorios(client):
    resposta = client.post(
        "/veiculos",
        data={
            "placa": "",
            "marca": "",
            "modelo": ""
        }
    )

    assert resposta.status_code == 302