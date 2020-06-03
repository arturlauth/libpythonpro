from unittest.mock import Mock

import pytest

from libpythonpro_arturlauth.spam.enviador_de_email import Enviador
from libpythonpro_arturlauth.spam.main import EnviadorDeSpam
from libpythonpro_arturlauth.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Artur', email='arturlauth@gmail.com'),
            Usuario(nome='Luciano', email='luciano@python.pro.br')
        ],
        [
            Usuario(nome='Artur', email='arturlauth@gmail.com')
        ]
    ]
)


def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()# enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'arturlauth@gmail.com',
        'Curso Python Pro',
        'Confira os módulos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Artur', email='arturlauth@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@gmail.com',
        'Curso Python Pro',
        'Confira os módulos'
    )
    enviador.enviar.assert_called_once_with(# assert enviador.parametros_de_envio == (
        'luciano@gmail.com',
        'arturlauth@gmail.com',
        'Curso Python Pro',
        'Confira os módulos'
    )