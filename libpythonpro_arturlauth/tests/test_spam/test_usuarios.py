import pytest

from libpythonpro_arturlauth.spam.db import Conexao
from libpythonpro_arturlauth.spam.modelos import Usuario


@pytest.fixture
def conexao():

    # Setup
    conexao_obj = Conexao()
    yield conexao_obj
    # Tear Down
    conexao_obj.fechar()

@pytest.fixture
def sessao(conexao):

    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()

def test_salvar_usuario(sessao):

    # conexao = conexao()
    # sessao = sessao(conexao)
    usuario = Usuario(nome='Artur')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    # sessao.roll_back()
    # sessao.fechar()
    # conexao.fechar()



def test_listar_usuario(sessao):

    usuarios = [Usuario(nome='Artur'), Usuario(nome='Luciano')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

