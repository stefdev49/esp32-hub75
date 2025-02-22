import hub75
import matrixdata
from logo import logo
from chars import sequence
from time import time_ns, sleep_ms

ROW_SIZE = 32
COL_SIZE = 64
BUFFER_SIZE = 256

config = hub75.Hub75SpiConfiguration()
config.illumination_time_microseconds = 0
matrix = matrixdata.MatrixData(ROW_SIZE, COL_SIZE, BUFFER_SIZE)
hub75spi = hub75.Hub75Spi(matrix, config)

matrix.clear_all_bytes()

shadow = matrixdata.MatrixData(ROW_SIZE, COL_SIZE, COL_SIZE)
shadow.clear_all_bytes()
shadow.set_pixels(0, 16, logo)

def printat(row, col, char, color):
    for i in range(12):
        for j in range(8):
            matrix.set_pixel_value(row+i, col+j, char[i][j] * color)

def prepare_buffers(matrixes):
    CHAR_WIDTH = 7
    BYTE_WIDTH = BUFFER_SIZE // 8
    for i in range(len(sequence)):
        printat(8, COL_SIZE + i * CHAR_WIDTH, sequence[i], 255)

    matrix.set_pixels(0, 16, logo)
    matrix.set_pixels(0, 256-32-16, logo)

    matrixes.append(matrix)

    for i in range(1, 8):
        new_matrix = matrixdata.MatrixData(ROW_SIZE, COL_SIZE, BUFFER_SIZE)
        for row in range(ROW_SIZE):
            for col in range(BYTE_WIDTH-1):
                value = matrixes[i-1].red_matrix_data[row][col] << 1
                if col < BYTE_WIDTH-1:
                    if matrixes[i-1].red_matrix_data[row][col+1] & 128:
                        value |= 1
                new_matrix.red_matrix_data[row][col] = value
                value = matrixes[i-1].green_matrix_data[row][col] << 1
                if col < BYTE_WIDTH-1:
                    if matrixes[i-1].green_matrix_data[row][col+1] & 128:
                        value |= 1
                new_matrix.green_matrix_data[row][col] = value
                value = matrixes[i-1].blue_matrix_data[row][col] << 1
                if col < BYTE_WIDTH-1:
                    if matrixes[i-1].blue_matrix_data[row][col+1] & 128:
                        value |= 1
                new_matrix.blue_matrix_data[row][col] = value
            new_matrix.red_matrix_data[row][BYTE_WIDTH-1] = matrixes[i-1].red_matrix_data[row][BYTE_WIDTH-1] << 1
            new_matrix.green_matrix_data[row][BYTE_WIDTH-1] = matrixes[i-1].green_matrix_data[row][BYTE_WIDTH-1] << 1
            new_matrix.blue_matrix_data[row][BYTE_WIDTH-1] = matrixes[i-1].blue_matrix_data[row][BYTE_WIDTH-1] << 1
        matrixes.append(new_matrix)

if __name__ == "__main__":
    matrixes = []
    prepare_buffers(matrixes)

    while True:
        offset = 0
        prog_start = time_ns()
        while offset < BUFFER_SIZE - COL_SIZE:
            hub75spi.display_data(offset, matrixes [offset % 8])
            hub75spi.display_data(offset, matrixes [offset % 8])
            hub75spi.matrix_data = shadow
            hub75spi.display_data(0, shadow)
            sleep_ms(10)
            offset += 1
        prog_end = time_ns()
        print(f"durée totale = {(prog_end - prog_start)/(1_000_000)} ms")
