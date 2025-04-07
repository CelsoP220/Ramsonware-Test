from cryptography.fernet import Fernet

def carregar_arquivo(caminho):
    with open(caminho, "rb") as f:
        return f.read()

def salvar_arquivo(caminho, dados):
    with open(caminho, "wb") as f:
        f.write(dados)

# Carrega a chave
with open("chave.key", "rb") as f:
    chave = f.read()

f = Fernet(chave)

# Carrega o conteúdo criptografado
dados = carregar_arquivo("arquivo_teste/teste.txt")

try:
    # Tenta descriptografar
    dados_descriptografados = f.decrypt(dados)
    salvar_arquivo("arquivo_teste/teste.txt", dados_descriptografados)
    print("Arquivo descriptografado com sucesso.")
except Exception as e:
    print("Erro ao descriptografar:", e)
