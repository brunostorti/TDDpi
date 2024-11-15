import unittest
from cadastro import cadastrar_usuario, usuarios

class TestCadastroSucesso(unittest.TestCase):
    def setUp(self):
        usuarios.clear()

    def test_cadastro_valido(self):
        resultado = cadastrar_usuario("usuario2", "1234")
        self.assertEqual(resultado, "Cadastro realizado com sucesso!")
        self.assertIn("usuario2", usuarios)
        self.assertEqual(usuarios["usuario2"], "1234")  # Verifica o registro correto

if __name__ == "__main__":
    unittest.main()
