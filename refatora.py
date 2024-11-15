usuarios = {}

# Centralizando mensagens
MENSAGENS = {
    "sucesso": "Cadastro realizado com sucesso!",
    "nome_vazio": "Erro: Por favor, insira um nome.",
    "senha_curta": "Erro: A senha deve ter pelo menos 4 caracteres.",
    "nome_duplicado": "Erro: Esse nome já está cadastrado."
}

# Funções auxiliares para validação
def validar_nome(nome):
    if not nome.strip():
        return MENSAGENS["nome_vazio"]
    if nome in usuarios:
        return MENSAGENS["nome_duplicado"]
    return None

def validar_senha(senha):
    if len(senha) < 4:
        return MENSAGENS["senha_curta"]
    return None

# Função principal
def cadastrar_usuario(nome, senha):
    erro_nome = validar_nome(nome)
    if erro_nome:
        return erro_nome

    erro_senha = validar_senha(senha)
    if erro_senha:
        return erro_senha

    usuarios[nome] = senha  # Cadastro
    return MENSAGENS["sucesso"]
