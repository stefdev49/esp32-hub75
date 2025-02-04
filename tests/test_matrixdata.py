import unittest
import timeit

class MatrixData:
    def __init__(self, row_size, col_size):
        self.row_size = row_size
        self.col_size = col_size
        self.col_bytes = col_size // 8

        self.red_matrix_data = [bytearray(self.col_bytes) for _ in range(self.row_size)]
        self.green_matrix_data = [bytearray(self.col_bytes) for _ in range(self.row_size)]
        self.blue_matrix_data = [bytearray(self.col_bytes) for _ in range(self.row_size)]

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

        # One row is divided into col_size // 8 = 8 bytes.
        # => Compute the column index (i.e. byte) of the pixel.
        col_byte_index = col >> 3
        # => Compute the bit index of the pixel within the byte.
        bit_index = 7 - (col % 8)

        mask : int = 1 << bit_index
        
        if val & 4:
            self.red_matrix_data[row][col_byte_index] |= mask
        else:
            self.red_matrix_data[row][col_byte_index] &= ~mask
        if val & 2:
            self.green_matrix_data[row][col_byte_index] |= mask
        else:
            self.green_matrix_data[row][col_byte_index] &= ~mask
        if val & 1:
            self.blue_matrix_data[row][col_byte_index] |= mask
        else:
            self.blue_matrix_data[row][col_byte_index] &= ~mask
    
    def is_out_of_bounds(self, row, col):
        '''
        Check if a pixel is out of LED matrix bounds.

        Parameters
        ----------
        row : int
            Row value of pixel (y value).
        col : int
            Column value of pixel (x value).

        Returns
        -------
        bool
            Pixel is out of bounds?
        '''
        return (row < 0 or row >= self.row_size or col < 0 or col >= self.col_size)
    
    def set_pixel_value_with_match(self, row, col, val):
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

        # One row is divided into col_size // 8 = 8 bytes.
        # => Compute the column index (i.e. byte) of the pixel.
        col_byte_index = col >> 3
        # => Compute the bit index of the pixel within the byte.
        bit_index = 7 - (col % 8)

        mask : int = 1 << bit_index
        
        match val:
            case 0:
                self.red_matrix_data[row][col_byte_index] &= ~mask
                self.green_matrix_data[row][col_byte_index] &= ~mask
                self.blue_matrix_data[row][col_byte_index] &= ~mask
            case 1:
                self.red_matrix_data[row][col_byte_index] &= ~mask
                self.blue_matrix_data[row][col_byte_index] |= mask
                self.green_matrix_data[row][col_byte_index] &= ~mask
            case 2:
                self.red_matrix_data[row][col_byte_index] &= ~mask
                self.green_matrix_data[row][col_byte_index] |= mask
                self.blue_matrix_data[row][col_byte_index] &= ~mask
            case 3:
                self.red_matrix_data[row][col_byte_index] |= mask
                self.green_matrix_data[row][col_byte_index] |= mask
                self.blue_matrix_data[row][col_byte_index] &= ~mask
            case 4:
                self.red_matrix_data[row][col_byte_index] |= mask
                self.green_matrix_data[row][col_byte_index] &= ~mask
                self.blue_matrix_data[row][col_byte_index] &= ~mask
            case 5:
                self.red_matrix_data[row][col_byte_index] |= mask
                self.blue_matrix_data[row][col_byte_index] |= mask
                self.green_matrix_data[row][col_byte_index] &= ~mask
            case 6:
                self.red_matrix_data[row][col_byte_index] &= ~mask
                self.green_matrix_data[row][col_byte_index] |= mask
                self.blue_matrix_data[row][col_byte_index] |= mask
            case 7:
                self.red_matrix_data[row][col_byte_index] |= mask
                self.green_matrix_data[row][col_byte_index] |= mask
                self.blue_matrix_data[row][col_byte_index] |= mask


class TestMatrixData(unittest.TestCase):

    def setUp(self):
        self.matrix = MatrixData(32, 32)  # Initialize with a 32x32 matrix

    def test_set_pixel_value_benchmark(self):
        row, col, val = 15, 15, 7  # Example pixel position and value

        # Benchmark the set_pixel_value method
        times = 1_000_000
        execution_time = timeit.timeit(lambda: self.matrix.set_pixel_value(row, col, val), number=times) / times
        
        self.assertFalse(execution_time >= 0, f"Execution time for set_pixel_value: {execution_time*1_000_000} *s")

    def test_set_pixel_value_benchmark_match(self):
        row, col, val = 15, 15, 7  # Example pixel position and value

        # Benchmark the set_pixel_value method
        times = 1_000_000
        execution_time = timeit.timeit(lambda: self.matrix.set_pixel_value_with_match(row, col, val), number=times) / times
        
        self.assertFalse(execution_time >= 0, f"Execution time for set_pixel_value: {execution_time*1_000_000} *s")

if __name__ == '__main__':
    unittest.main()