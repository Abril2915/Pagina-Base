import pyautogui as pg
import time

pg.hotkey("win", "r")
pg.write("chrome.exe web.whatsapp.com", interval=0.5)
time.sleep(1)
pg.press("enter")
time.sleep(1)

mensajes = int(input("Numero de mensajes: "))
mensaje = "hola"

pg.write(f'{mensaje}')
pg.press('enter')
time.sleep(1)