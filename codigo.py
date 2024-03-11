# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
#pip install pyautogui

import pyautogui
import time

pyautogui.PAUSE = 2
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas


# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link 
#pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#dar uma pausa um pouco maior
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=745, y=520)
pyautogui.write("jeniffer_maximo@gmail.com")
# selecionar o campo de email

#escrever a senha
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("12345")#sua senha

#botao de logar
pyautogui.click(x=935, y=706)
time.sleep(3)


# Passo 3: Importar a base de produtos pra cadastrar
#chrome
import pandas as pd
tabela = pd.read_csv("produtos.csv")
print(tabela)


# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no 1° campo de código
    pyautogui.click(x=704, y=369)
    codigo = tabela.loc[linha, "codigo"] 
# codio do produto
    pyautogui.write(str(codigo))
    pyautogui.press("tab")# passar para o proximo campo

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")# passar para o proximo campo

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")# passar para o proximo campo

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")# passar para o proximo campo

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")# passar para o proximo campo

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")# passar para o proximo campo

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
# passar para o proximo campo
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)

# Passo 5: Repetir o processo de cadastro até o fim