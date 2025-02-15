import hub75
import matrixdata
import logo
from time import time_ns
from time import time_ns
import asyncio

ROW_SIZE = 32
COL_SIZE = 64

config = hub75.Hub75SpiConfiguration()
config.illumination_time_microseconds = 0
matrix = matrixdata.MatrixData(ROW_SIZE, COL_SIZE)
hub75spi = hub75.Hub75Spi(matrix, config)

matrix.clear_all_bytes()

char_b = [[0, 0, 0, 0, 0, 0, 0, 0], 
          [1, 1, 1, 1, 1, 1, 0, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 0, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]
          ]

char_o = [[0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 1, 1, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 0],
          [0, 0, 1, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]
          ]

char_e = [[0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 1, 1, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 0],
          [0, 0, 1, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]
          ]

char_ea = [[0, 0, 0, 0, 1, 0, 0, 0], 
          [0, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 1, 1, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 0],
          [0, 0, 1, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]
          ]

char_n = [[0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 1, 1, 0, 0, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]
          ]

char_a = [[0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 1, 1, 0, 0],
          [0, 1, 1, 1, 1, 1, 0, 0],
          [1, 1, 0, 0, 1, 1, 0, 0],
          [1, 1, 0, 0, 1, 1, 0, 0],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [0, 1, 1, 1, 0, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]
          ]

char_0 = [[0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 0, 0, 0],
          [1, 1, 0, 0, 1, 1, 0, 0],
          [1, 1, 0, 0, 1, 1, 0, 0],
          [1, 1, 0, 0, 1, 1, 0, 0],
          [1, 1, 0, 0, 1, 1, 0, 0],
          [1, 1, 0, 0, 1, 1, 0, 0],
          [1, 1, 0, 0, 1, 1, 0, 0],
          [1, 1, 0, 0, 1, 1, 0, 0],
          [0, 1, 1, 1, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]
          ]

char_2 = [[0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 0, 0, 0],
          [1, 1, 0, 0, 1, 1, 0, 0],
          [1, 1, 0, 0, 1, 1, 0, 0],
          [0, 0, 0, 0, 1, 1, 0, 0],
          [0, 0, 0, 1, 1, 0, 0, 0],
          [0, 0, 1, 1, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 0, 0, 0],
          [1, 1, 0, 0, 1, 1, 0, 0],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]
          ]

char_6 = [[0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 0, 0, 0],
          [1, 1, 0, 0, 1, 1, 0, 0],
          [1, 1, 0, 0, 1, 1, 0, 0],
          [1, 1, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 0, 0, 0],
          [1, 1, 0, 0, 1, 1, 0, 0],
          [1, 1, 0, 0, 1, 1, 0, 0],
          [1, 1, 0, 0, 1, 1, 0, 0],
          [0, 1, 1, 1, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]
          ]

char_5 = [[0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [1, 1, 0, 0, 0, 0, 0, 0],
          [1, 1, 0, 0, 0, 0, 0, 0],
          [1, 1, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 0, 0, 0],
          [0, 0, 0, 0, 1, 1, 0, 0],
          [0, 0, 0, 0, 1, 1, 0, 0],
          [1, 1, 0, 0, 1, 1, 0, 0],
          [0, 1, 1, 1, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]
          ]


char_ex = [[0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 1, 1, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]
          ]

char_space = [[0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]
          ]

def printat(row, col, char, color):
    for i in range(12):
        for j in range(8):
            matrix.set_pixel_value(row+i, col+j, char[i][j] * color)

sequence = [char_b, char_o, char_n, char_n, char_e, char_space, char_a, char_n, char_n, char_ea, char_e, char_space, char_2, char_0, char_2, char_5, char_ex]

async def message_loop():
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
                await asyncio.sleep(0.01)
        scroll -= 1
        end = time_ns()
        # Mesure le temps de rendu en millisecondes
        print(f"durée = {(end - start)/(1_000_000)} ms")

async def refresh_display():
    # Boucle infinie de rafraîchissement
    # asyncio permet son exécution en parallèle avec message_loop
    while True:
        # Attend que l'affichage soit mis à jour
        # await permet de céder le contrôle à d'autres coroutines pendant l'attente
        hub75spi.display_data()
        await asyncio.sleep(0.01)

async def main():
    # Initialisation de l'affichage
    matrix.clear_all_bytes()
    # Dessine une ligne horizontale
    for col in range(0, 63):
        matrix.set_pixel_value(31, col, 7)
    
    # Crée deux tâches asynchrones qui s'exécuteront en parallèle
    # create_task permet de démarrer une coroutine sans bloquer l'exécution
    refresh = asyncio.create_task(refresh_display())
    loop = asyncio.create_task(message_loop())
    
    # Attend que les deux tâches soient terminées
    await refresh
    await loop

# Point d'entrée du programme
# asyncio.run crée une nouvelle boucle d'événements et exécute la coroutine main
asyncio.run(main())