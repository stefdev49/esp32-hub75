BLUE_VALUE = 1
GREEN_VALUE = 2
RED_VALUE = 4

class MatrixData:
    '''
    RGB LED matrix data object for HUB75 LED displays.
    3-Bit Color Mapping:
        Color   Binary Value  Decimal Value
        Black   0b000         0
        Blue    0b001         1
        Green   0b010         2
        Cyan    0b011         3
        Red     0b100         4
        Magenta 0b101         5
        Yellow  0b110         6
        White   0b111         7
    '''
    def __init__(self, row_size, col_size, buffer_size):
        self.row_size = row_size
        self.col_size = col_size
        self.col_bytes = col_size // 8
        self.buffer_size = buffer_size
        self.buffer_bytes = buffer_size // 8

        self.red_matrix_data = [bytearray(self.buffer_bytes) for _ in range(self.row_size)]
        self.green_matrix_data = [bytearray(self.buffer_bytes) for _ in range(self.row_size)]
        self.blue_matrix_data = [bytearray(self.buffer_bytes) for _ in range(self.row_size)]

    def set_pixels(self, row, col, array):
        '''
        Set an array of pixels (i.e. an image).

        Parameters
        ----------
        row : int
            Top row (y position) of image.
        col : int
            Left column (x position) of image.
        array : 2D list of bitmapped values [[int,...],[...],...]
            Decimal color representations of the image.

        Returns
        -------
        None.
        '''
        for r in range(len(array)):
            for c in range(len(array[0])):
                if array[r][c]:
                    self.set_pixel_value(row + r, col + c, array[r][c])

    def set_pixel_value(self, row, col, val):
        '''
        Set an individual pixel.

        Parameters
        ----------
        row : int
            Row value of pixel (y value).
        col : int
            Column value of pixel (x value).
        val : int
            Decimal color representation.

        Returns
        -------
        None.
        '''
        if (row < 0 or row >= self.row_size or col < 0 or col >= self.buffer_size):
            return

        # One row is divided into col_size // 8 = 8 bytes.
        # => Compute the column index (i.e. byte) of the pixel.
        col_byte_index = col >> 3
        # => Compute the bit index of the pixel within the byte.
        bit_mask = 1 << (7 - (col % 8))

        if val & RED_VALUE:
            self.red_matrix_data[row][col_byte_index] |= bit_mask
        else:
            self.red_matrix_data[row][col_byte_index] &= ~bit_mask
        if val & GREEN_VALUE:
            self.green_matrix_data[row][col_byte_index] |= bit_mask
        else:
            self.green_matrix_data[row][col_byte_index] &= ~bit_mask
        if val & BLUE_VALUE:
            self.blue_matrix_data[row][col_byte_index] |= bit_mask
        else:
            self.blue_matrix_data[row][col_byte_index] &= ~bit_mask


    def clear_all_bytes(self):
        '''
        Reset all pixels.

        Returns
        -------
        None.
        '''
        self.red_matrix_data = [bytearray(self.buffer_bytes) for _ in range(self.row_size)]
        self.green_matrix_data = [bytearray(self.buffer_bytes) for _ in range(self.row_size)]
        self.blue_matrix_data = [bytearray(self.buffer_bytes) for _ in range(self.row_size)]
