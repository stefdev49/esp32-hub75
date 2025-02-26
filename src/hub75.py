from machine import SoftSPI, freq, Pin
from time import sleep_us

#freq(160000000)  # default NodeMCU ESP-32S v1.1
freq(240000000)

class Hub75SpiConfiguration:
    '''
    SoftSPI pin configuration for HUB75 RGB LED matrix.
    Defaults are for Hub75 Blaster PCB from Hackerbox 0065
    (https://hackerboxes.com/collections/past-hackerboxes/products/hackerbox-0065-realtime).
    '''
    def __init__(self):
        self.spi_baud_rate = 5000000

        self.illumination_time_microseconds = 10

        # Row select GPIO pins
        self.line_select_a_pin_number = 5
        self.line_select_b_pin_number = 18
        self.line_select_c_pin_number = 19
        self.line_select_d_pin_number = 21
        self.line_select_e_pin_number = 12

        # Hub75 RGB data GPIO pins
        self.red1_pin_number = 2
        self.blue1_pin_number = 15
        self.green1_pin_number = 4
        self.red2_pin_number = 16
        self.blue2_pin_number = 27
        self.green2_pin_number = 17

        self.clock_pin_number = 22
        self.latch_pin_number = 26
        self.output_disable_pin_number = 25

        self.spi_miso_pin_number = 13  # not connected


class Hub75Spi:
    '''
    HUB75 RGB LED matrix communication.
    '''
    def __init__(self, matrix_data, config):
        '''
        Parameters
        ----------
        matrix_data : MatrixData object
        config : Hub75SpiConfiguration
            Pin configuration.
        '''
        self.config = config
        self.matrix_data = matrix_data
        self.half_row_size = matrix_data.row_size // 2
        self.offset = 0

        self.latch_pin = Pin(config.latch_pin_number, Pin.OUT, Pin.PULL_UP)
        self.output_disable_pin = Pin(config.output_disable_pin_number, Pin.OUT, Pin.PULL_UP)
        self.line_select_a_pin = Pin(config.line_select_a_pin_number, Pin.OUT, Pin.PULL_UP)
        self.line_select_b_pin = Pin(config.line_select_b_pin_number, Pin.OUT, Pin.PULL_UP)
        self.line_select_c_pin = Pin(config.line_select_c_pin_number, Pin.OUT, Pin.PULL_UP)
        self.line_select_d_pin = Pin(config.line_select_d_pin_number, Pin.OUT, Pin.PULL_UP)
        self.line_select_e_pin = Pin(config.line_select_e_pin_number, Pin.OUT, Pin.PULL_UP)

        self.line_select_a_pin.off()
        self.line_select_b_pin.off()
        self.line_select_c_pin.off()
        self.line_select_d_pin.off()
        self.line_select_e_pin.off()

        self.red1_mosi_pin = Pin(config.red1_pin_number, Pin.PULL_UP)
        self.red2_mosi_pin = Pin(config.red2_pin_number, Pin.PULL_UP)
        self.green1_mosi_pin = Pin(config.green1_pin_number, Pin.PULL_UP)
        self.green2_mosi_pin = Pin(config.green2_pin_number, Pin.PULL_UP)
        self.blue1_mosi_pin = Pin(config.blue1_pin_number, Pin.PULL_UP)
        self.blue2_mosi_pin = Pin(config.blue2_pin_number, Pin.PULL_UP)

        self.red1_spi = SoftSPI(baudrate=config.spi_baud_rate, polarity=1, phase=0, sck=Pin(config.clock_pin_number), mosi=self.red1_mosi_pin, miso=Pin(config.spi_miso_pin_number))
        self.red2_spi = SoftSPI(baudrate=config.spi_baud_rate, polarity=1, phase=0, sck=Pin(config.clock_pin_number), mosi=self.red2_mosi_pin, miso=Pin(config.spi_miso_pin_number))
        self.green1_spi = SoftSPI(baudrate=config.spi_baud_rate, polarity=1, phase=0, sck=Pin(config.clock_pin_number), mosi=self.green1_mosi_pin, miso=Pin(config.spi_miso_pin_number))
        self.green2_spi = SoftSPI(baudrate=config.spi_baud_rate, polarity=1, phase=0, sck=Pin(config.clock_pin_number), mosi=self.green2_mosi_pin, miso=Pin(config.spi_miso_pin_number))
        self.blue1_spi = SoftSPI(baudrate=config.spi_baud_rate, polarity=1, phase=0, sck=Pin(config.clock_pin_number), mosi=self.blue1_mosi_pin, miso=Pin(config.spi_miso_pin_number))
        self.blue2_spi = SoftSPI(baudrate=config.spi_baud_rate, polarity=1, phase=0, sck=Pin(config.clock_pin_number), mosi=self.blue2_mosi_pin, miso=Pin(config.spi_miso_pin_number))

    def set_row_select(self, row):
        '''
        Set data for row select pins.

        Parameters
        ----------
        row : int
            current row for serial color data.

        Returns
        -------
        None.
        '''
        self.line_select_a_pin.value(row & 1)
        self.line_select_b_pin.value(row & 2)
        self.line_select_c_pin.value(row & 4)
        self.line_select_d_pin.value(row & 8)

    @micropython.native
    def display_data(self, offset, matrix_data):
        '''
        Write pixel data to LED matrix.

        Returns
        -------
        None.
        '''
        start = offset // 8
        end = start + matrix_data.col_bytes
        red_matrix_data = matrix_data.red_matrix_data
        green_matrix_data = matrix_data.green_matrix_data
        blue_matrix_data = matrix_data.blue_matrix_data

        red1_spi = self.red1_spi
        green1_spi = self.green1_spi
        blue1_spi = self.blue1_spi
        red1_mosi_pin = self.red1_mosi_pin
        green1_mosi_pin = self.green1_mosi_pin
        blue1_mosi_pin = self.blue1_mosi_pin

        latch_pin = self.latch_pin
        output_disable_pin = self.output_disable_pin
        line_select_a_pin = self.line_select_a_pin
        line_select_b_pin = self.line_select_b_pin
        line_select_c_pin = self.line_select_c_pin
        line_select_d_pin = self.line_select_d_pin

        red2_spi = self.red2_spi
        green2_spi = self.green2_spi
        blue2_spi = self.blue2_spi
        red2_mosi_pin = self.red2_mosi_pin
        green2_mosi_pin = self.green2_mosi_pin
        blue2_mosi_pin = self.blue2_mosi_pin

        for row in range(16):
            # shift in data
            red1_spi.write(red_matrix_data[row][start:end])
            red1_mosi_pin.off()
            output_disable_pin.on()

            line_select_a_pin.value(row & 1)
            line_select_b_pin.value(row & 2)
            line_select_c_pin.value(row & 4)
            line_select_d_pin.value(row & 8)

            latch_pin.on()
            latch_pin.off()
            output_disable_pin.off()

            # shift in data
            green1_spi.write(green_matrix_data[row][start:end])
            green1_mosi_pin.off()
            output_disable_pin.on()
            latch_pin.on()
            latch_pin.off()
            output_disable_pin.off()

            # shift in data
            blue1_spi.write(blue_matrix_data[row][start:end])
            blue1_mosi_pin.off()
            output_disable_pin.on()
            latch_pin.on()
            latch_pin.off()
            output_disable_pin.off()

            # second half of the display
            row_half = row + 16

            # shift in data
            red2_spi.write(red_matrix_data[row_half][start:end])
            red2_mosi_pin.off()
            output_disable_pin.on()
            latch_pin.on()
            latch_pin.off()
            output_disable_pin.off()

            green2_spi.write(green_matrix_data[row_half][start:end])
            green2_mosi_pin.off()
            output_disable_pin.on()
            latch_pin.on()
            latch_pin.off()
            output_disable_pin.off()

            blue2_spi.write(blue_matrix_data[row_half][start:end])
            blue2_mosi_pin.off()
            output_disable_pin.on()
            latch_pin.on()
            latch_pin.off()
            output_disable_pin.off()
