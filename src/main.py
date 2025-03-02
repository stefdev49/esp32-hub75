import hub75
import matrixdata
from time import time_ns
from letters import *
from machine import Timer

ROW_SIZE = 32
COL_SIZE = 64

config = hub75.Hub75SpiConfiguration()
config.illumination_time_microseconds = 0
matrix = matrixdata.MatrixData(ROW_SIZE, COL_SIZE)
hub75spi = hub75.Hub75Spi(matrix, config)

matrix.clear_all_bytes()


def printat(row, col, char, color):
    for i in range(12):
        for j in range(8):
            matrix.set_pixel_value(row+i, col+j, char[i][j] * color)

sequence = [char_b, char_o, char_n, char_n, char_e, char_space, char_a, char_n, char_n, char_ea, char_e, char_space, char_2, char_0, char_2, char_5, char_ex]

matrix.clear_all_bytes()


def message_loop():
    # Calcule la largeur totale du message en pixels
    pixels = len(sequence)*7
    scroll = COL_SIZE
    matrix.clear_all_bytes()
    # Boucle d'animation jusqu'à ce que le message soit sorti de l'écran
    while scroll != - pixels:
        start = time_ns()
        # Pour chaque caractère de la séquence
        for i in range(0, len(sequence)):
            # Vérifie si le caractère est visible à l'écran
            if scroll+i*7 < COL_SIZE or scroll+i*7 > 0:
                # Affiche le caractère à la position calculée
                printat(8, scroll+i*7, sequence[i], 255)
        scroll -= 1
        end = time_ns()
        # Mesure le temps de rendu en millisecondes
        print(f"durée = {(end - start)/(1_000_000)} ms")

if __name__ == "__main__":
    timer = Timer(0)
    timer.init(period=20, mode=Timer.PERIODIC, callback=hub75spi.display_data)
    message_loop()