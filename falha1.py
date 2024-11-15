import unittest
from cadastro import cadastrar_usuario

class TestCadastroFalha(unittest.TestCase):
    def test_nome_vazio(self):
        resultado = cadastrar_usuario("", "1234")
        self.assertEqual(resultado, "Erro: Por favor, insira um nome.")  # Deve falhar

    def test_senha_curta(self):
        resultado = cadastrar_usuario("usuario1", "123")
        self.assertEqual(resultado, "Erro: A senha deve ter pelo menos 4 caracteres.")  # Deve falhar

    def test_nome_duplicado(self):
        resultado = cadastrar_usuario("usuario1", "1234")
        self.assertEqual(resultado, "Erro: Esse nome já está cadastrado.")  # Deve falhar

if __name__ == "__main__":
    unittest.main()
