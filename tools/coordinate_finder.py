import time
import pyautogui

# Aguarda 5 segundos para o usuário posicionar o mouse
time.sleep(5)

# Imprime a posição atual do mouse (coordenadas x e y)
print(pyautogui.position())