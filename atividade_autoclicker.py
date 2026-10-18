import time
import threading
from pynput import mouse, keyboard

HOTKEY = keyboard.KeyCode.from_char('c')
EXIT_KEY = keyboard.Key.esc
CLICK_DELAY = 0

mouse_controller = mouse.Controller()
clicando = False

def auto_click():
    global clicando

    while clicando:
        mouse_controller.click(mouse.Button.left, 1)
        time.sleep(CLICK_DELAY)

def on_press(key):
    global clicando
    if key == HOTKEY:
        clicando = not clicando

        if clicando:
            print("[AUTOCLICK] Ativado")
            threading.Thread(target=auto_click).start()
        else:
            print("[AUTOCLICK] Desativado")
    elif key == EXIT_KEY:
        print("[INFO] Encerramento script")
        return False

print("Auto Click iniciado")
print("pressione 'c' para ligar/desligar")
print("pressione 'esc' para encerrar")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
