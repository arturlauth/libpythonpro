from libpythonpro_arturlauth.spam.modelos import Usuario


def test_salvar_usuario(sessao):

    # conexao = conexao()
    # sessao = sessao(conexao)
    usuario = Usuario(nome='Artur', email='arturlauth@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    # sessao.roll_back()
    # sessao.fechar()
    # conexao.fechar()



def test_listar_usuario(sessao):

    usuarios = [Usuario(nome='Artur', email='arturlauth@gmail.com'),
                Usuario(nome='Luciano', email='luciano@python.pro.br')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

