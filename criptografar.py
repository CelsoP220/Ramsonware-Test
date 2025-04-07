from cryptography.fernet import Fernet

def carregar_arquivo(caminho):
    with open(caminho, "rb") as f:
        return f.read()

def salvar_arquivo(caminho, dados):
    with open(caminho, "wb") as f:
        f.write(dados)

chave = Fernet.generate_key()
with open("chave.key", "wb") as f:
    f.write(chave)

f = Fernet(chave)
dados = carregar_arquivo("arquivo_teste/teste.txt")
dados_criptografados = f.encrypt(dados)
salvar_arquivo("arquivo_teste/teste.txt", dados_criptografados)

print("Arquivo criptografado com sucesso.")