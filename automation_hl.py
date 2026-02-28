import keyboard
import time

verses_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print("Pressione 'right' para iniciar...")
keyboard.wait('right')

def verse(timer):
    time.sleep(timer)
    keyboard.press('right')
    keyboard.release('right')
    print(f"Espera de {timer}s concluída e 'right' enviado.")

for wait_time in verses_sequence:
    verse(wait_time)

print("automação finalizada")
