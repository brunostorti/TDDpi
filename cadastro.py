usuarios = {}

def cadastrar_usuario(nome, senha):
    erros = {
        "nome_vazio": "Erro: Por favor, insira um nome.",
        "senha_curta": "Erro: A senha deve ter pelo menos 4 caracteres.",
        "nome_duplicado": "Erro: Esse nome já está cadastrado."
    }

    if not nome.strip():  # Nome vazio ou apenas espaços
        return erros["nome_vazio"]
    if len(senha) < 4:  # Senha muito curta
        return erros["senha_curta"]
    if nome in usuarios:  # Nome já existente
        return erros["nome_duplicado"]

    # Caso de sucesso
    usuarios[nome] = senha
    return "Cadastro realizado com sucesso!"
