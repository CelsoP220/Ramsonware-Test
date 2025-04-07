import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os

def carregar_arquivo(caminho):
    with open(caminho, "rb") as f:
        return f.read()

def salvar_arquivo(caminho, dados):
    with open(caminho, "wb") as f:
        f.write(dados)

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as f:
        f.write(chave)
    return chave

def criptografar_arquivo():
    caminho = filedialog.askopenfilename(title="Selecione o arquivo para criptografar")
    if not caminho:
        return

    try:
        chave = gerar_chave()
        f = Fernet(chave)
        dados = carregar_arquivo(caminho)
        dados_criptografados = f.encrypt(dados)
        salvar_arquivo(caminho, dados_criptografados)

        messagebox.showinfo("Sucesso", "Arquivo criptografado com sucesso!\nChave salva como 'chave.key'.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao criptografar o arquivo:\n{e}")

# Interface Tkinter
janela = tk.Tk()
janela.title("Criptografador de Arquivo")
janela.geometry("400x200")

titulo = tk.Label(janela, text="Criptografar Arquivo com Fernet", font=("Arial", 14))
titulo.pack(pady=20)

botao_criptografar = tk.Button(janela, text="Selecionar Arquivo e Criptografar", command=criptografar_arquivo)
botao_criptografar.pack(pady=10)

janela.mainloop()
