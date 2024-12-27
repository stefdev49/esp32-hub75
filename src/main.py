import hub75
import matrixdata
from time import time_ns

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
          [0, 1, 1, 1, 1, 1, 0, 0],
          [1, 1, 0, 0, 0, 1, 1, 0],
          [1, 1, 0, 0, 0, 1, 1, 0],
          [1, 1, 0, 0, 0, 1, 1, 0],
          [1, 1, 0, 0, 0, 1, 1, 0],
          [1, 1, 0, 0, 0, 1, 1, 0],
          [1, 1, 0, 0, 0, 1, 1, 0],
          [1, 1, 0, 0, 0, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 0, 0],
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

def printat(row, col, char, color):
    for i in range(12):
        for j in range(8):
            matrix.set_pixel_value(row+i, col+j, char[i][j] * color)

matrix.clear_all_bytes()
printat(0, 0, char_b, 7)
printat(0, 7, char_o, 7)
printat(0, 14, char_n, 7)
printat(0, 21, char_n, 7)
printat(0, 28, char_e, 7)
printat(0, 36, char_ex, 7)

printat(12, 0, char_a, 7)
printat(12, 7, char_n, 7)
printat(12, 14, char_n, 7)
printat(12, 21, char_e, 7)
printat(12, 28, char_ea, 7)

printat(12, 36, char_2, 7)
printat(12, 43, char_0, 7)
printat(12, 51, char_2, 7)
printat(12, 58, char_5, 7)

for col in range(0, 64):
    matrix.set_pixel_value(30, col, 7)
    matrix.set_pixel_value(31, col, col % 8)

counter = 1
start = time_ns()
while True:
    hub75spi.display_data()
    counter = counter + 1
    if counter == 100:
        hub75spi.display_data()
        end = time_ns()
        print(f"durée = {(end - start)/(1000000*counter)} ms")
        counter = 1
        start = time_ns()