# ============================================================
# AUTOMAÇÃO DE CADASTRO DE PRODUTOS
# ============================================================

# ------------------------------------------------------------
# BIBLIOTECAS
# ------------------------------------------------------------
# pyautogui → Automação de mouse e teclado
# time → Controle de tempo

import pyautogui
import time

pyautogui.PAUSE = 0.5  # Intervalo padrão entre comandos

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# ------------------------------------------------------------
# ETAPA 1 — ACESSO AO SISTEMA
# ------------------------------------------------------------
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

# ------------------------------------------------------------
# ETAPA 2 — LOGIN
# ------------------------------------------------------------
pyautogui.click(x=595, y=546)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(4)

# ------------------------------------------------------------
# ETAPA 3 — LEITURA DA BASE DE DADOS
# ------------------------------------------------------------
# pandas → Manipulação da planilha CSV
import pandas

tabela = pandas.read_csv("products.csv")
print(tabela)

# ------------------------------------------------------------
# ETAPA 4 — CADASTRO DOS PRODUTOS (LOOP)
# ------------------------------------------------------------
for linha in tabela.index:

    pyautogui.click(x=664, y=371)

    # Código do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    # Marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    # Tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    # Categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    # Preço unitário
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    # Custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    # Observação (se existir)
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# ------------------------------------------------------------
# ETAPA 5 — REPETIÇÃO AUTOMÁTICA ATÉ FINAL DA LISTA
# ------------------------------------------------------------
