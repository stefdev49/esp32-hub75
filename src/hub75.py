from machine import SoftSPI, freq, Pin
from micropython import const
import micropython

#freq(160000000)  # default NodeMCU ESP-32S v1.1
freq(240000000)

class Hub75SpiConfiguration:
    '''
    SoftSPI pin configuration for HUB75 RGB LED matrix.
    Defaults are for Hub75 Blaster PCB from Hackerbox 0065
    (https://hackerboxes.com/collections/past-hackerboxes/products/hackerbox-0065-realtime).
    '''
    def __init__(self):
        self.spi_baud_rate = const(2500000)

        self.illumination_time_microseconds = const(10)

        # Row select pins
        self.line_select_a_pin_number = const(5)
        self.line_select_b_pin_number = const(18)
        self.line_select_c_pin_number = const(19)
        self.line_select_d_pin_number = const(21)
        self.line_select_e_pin_number = const(12)

        # Hub75 RGB data pins
        self.red1_pin_number = const(2)
        self.blue1_pin_number = const(15)
        self.green1_pin_number = const(4)
        self.red2_pin_number = const(16)
        self.blue2_pin_number = const(27)
        self.green2_pin_number = const(17)

        self.clock_pin_number = const(22)
        self.latch_pin_number = const(26)
        self.output_enable_pin_number = const(25)  # active low

        self.spi_miso_pin_number = const(13)  # not connected


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
        self.half_row_size = const(matrix_data.row_size // 2)

        self.latch_pin = Pin(config.latch_pin_number, Pin.OUT)
        self.output_enable_pin = Pin(config.output_enable_pin_number, Pin.OUT)
        self.line_select_a_pin = Pin(config.line_select_a_pin_number, Pin.OUT)
        self.line_select_b_pin = Pin(config.line_select_b_pin_number, Pin.OUT)
        self.line_select_c_pin = Pin(config.line_select_c_pin_number, Pin.OUT)
        self.line_select_d_pin = Pin(config.line_select_d_pin_number, Pin.OUT)
        self.line_select_e_pin = Pin(config.line_select_e_pin_number, Pin.OUT)

        self.line_select_a_pin.off()
        self.line_select_b_pin.off()
        self.line_select_c_pin.off()
        self.line_select_d_pin.off()
        self.line_select_e_pin.off()

        self.red1_mosi_pin = Pin(config.red1_pin_number)
        self.red2_mosi_pin = Pin(config.red2_pin_number)
        self.green1_mosi_pin = Pin(config.green1_pin_number)
        self.green2_mosi_pin = Pin(config.green2_pin_number)
        self.blue1_mosi_pin = Pin(config.blue1_pin_number)
        self.blue2_mosi_pin = Pin(config.blue2_pin_number)

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
        # self.line_select_e_pin.value(row & 16)

    def display_top_half(self):
        '''
        Write top half of display, see display_data().

        Returns
        -------
        None.
        '''
        red_matrix_data = self.matrix_data.red_matrix_data
        green_matrix_data = self.matrix_data.green_matrix_data
        blue_matrix_data = self.matrix_data.blue_matrix_data

        output_enable_pin = self.output_enable_pin
        latch_pin = self.latch_pin

        red1_spi = self.red1_spi
        red1_mosi_pin = self.red1_mosi_pin
        green1_spi = self.green1_spi
        green1_mosi_pin = self.green1_mosi_pin
        blue1_spi = self.blue1_spi
        blue1_mosi_pin = self.blue1_mosi_pin

        for row in range(self.half_row_size):
            row_data_red1 = red_matrix_data[row]
            row_data_green1 = green_matrix_data[row]
            row_data_blue1 = blue_matrix_data[row]

            output_enable_pin.on() # disable
            self.set_row_select(row)
            
            # shift in data
            red1_spi.write(row_data_red1)
            red1_mosi_pin.off()


            latch_pin.on()
            latch_pin.off()
            output_enable_pin.off() # enable

            # shift in data
            green1_spi.write(row_data_green1)
            green1_mosi_pin.off()
            output_enable_pin.on() # disable
            latch_pin.on()
            latch_pin.off()
            output_enable_pin.off() # enable

            # shift in data
            blue1_spi.write(row_data_blue1)
            blue1_mosi_pin.off()
            output_enable_pin.on() # disable
            latch_pin.on()
            latch_pin.off()
            output_enable_pin.off() # enable

    def display_bottom_half(self):
        '''
        Write bottom half of display, see display_data().

        Returns
        -------
        None.
        '''
        red_matrix_data = self.matrix_data.red_matrix_data
        green_matrix_data = self.matrix_data.green_matrix_data
        blue_matrix_data = self.matrix_data.blue_matrix_data
        
        output_enable_pin = self.output_enable_pin
        latch_pin = self.latch_pin

        red2_spi = self.red2_spi
        red2_mosi_pin = self.red2_mosi_pin
        green2_spi = self.green2_spi
        green2_mosi_pin = self.green2_mosi_pin
        blue2_spi = self.blue2_spi
        blue2_mosi_pin = self.blue2_mosi_pin

        for row in range(self.half_row_size, self.matrix_data.row_size):
            row_data_red2 = red_matrix_data[row]
            row_data_green2 = green_matrix_data[row]
            row_data_blue2 = blue_matrix_data[row]

            # shift in data
            red2_spi.write(row_data_red2)
            red2_mosi_pin.off()
            output_enable_pin.on() # disable

            self.set_row_select(row % self.half_row_size)

            latch_pin.on()
            latch_pin.off()
            output_enable_pin.off() # enable

            green2_spi.write(row_data_green2)
            green2_mosi_pin.off()
            output_enable_pin.on() # disable
            latch_pin.on()
            latch_pin.off()
            output_enable_pin.off() # enable

            blue2_spi.write(row_data_blue2)
            blue2_mosi_pin.off()
            output_enable_pin.on() # disable
            latch_pin.on()
            latch_pin.off()
            output_enable_pin.off() # enable

        # flush out last blue line
        blue2_spi.write(bytearray(self.matrix_data.col_bytes))
        output_enable_pin.on()
        latch_pin.on()
        latch_pin.off()
        output_enable_pin.off() # enable

    @micropython.native
    def display_data(self):
        '''
        Write pixel data to LED matrix.

        Returns
        -------
        None.
        '''
        red1_matrix_data = self.matrix_data.red_matrix_data
        green1_matrix_data = self.matrix_data.green_matrix_data
        blue1_matrix_data = self.matrix_data.blue_matrix_data
        red2_matrix_data = self.matrix_data.red_matrix_data[16:]
        green2_matrix_data = self.matrix_data.green_matrix_data[16:]
        blue2_matrix_data = self.matrix_data.blue_matrix_data[16:]

        output_enable_pin = self.output_enable_pin
        latch_pin = self.latch_pin

        red1_spi = self.red1_spi
        red1_mosi_pin = self.red1_mosi_pin
        green1_spi = self.green1_spi
        green1_mosi_pin = self.green1_mosi_pin
        blue1_spi = self.blue1_spi
        blue1_mosi_pin = self.blue1_mosi_pin
        
        red2_spi = self.red2_spi
        red2_mosi_pin = self.red2_mosi_pin
        green2_spi = self.green2_spi
        green2_mosi_pin = self.green2_mosi_pin
        blue2_spi = self.blue2_spi
        blue2_mosi_pin = self.blue2_mosi_pin

        for row in range(self.half_row_size):
            # shift in data
            row_data = red1_matrix_data[row]
            red1_spi.write(row_data)
            red1_mosi_pin.off()
            output_enable_pin.on() # disable
            self.set_row_select(row)
            latch_pin.on()
            latch_pin.off()
            output_enable_pin.off() # enable

            # shift in data
            row_data = green1_matrix_data[row]
            green1_spi.write(row_data)
            green1_mosi_pin.off()
            output_enable_pin.on() # disable
            latch_pin.on()
            latch_pin.off()
            output_enable_pin.off() # enable

            # shift in data
            row_data = blue1_matrix_data[row]
            blue1_spi.write(row_data)
            blue1_mosi_pin.off()
            output_enable_pin.on() # disable
            latch_pin.on()
            latch_pin.off()
            output_enable_pin.off() # enable

            # shift in data
            row_data = red2_matrix_data[row]
            red2_spi.write(row_data)
            red2_mosi_pin.off()
            output_enable_pin.on() # disable
            latch_pin.on()
            latch_pin.off()
            output_enable_pin.off() # enable

            row_data = green2_matrix_data[row]
            green2_spi.write(row_data)
            green2_mosi_pin.off()
            output_enable_pin.on() # disable
            latch_pin.on()
            latch_pin.off()
            output_enable_pin.off() # enable

            row_data = blue2_matrix_data[row]
            blue2_spi.write(row_data)
            blue2_mosi_pin.off()
            output_enable_pin.on() # disable
            latch_pin.on()
            latch_pin.off()
            output_enable_pin.off() # enable
        
        # flush out last blue line
        blue2_spi.write(bytearray(self.matrix_data.col_bytes))
        output_enable_pin.on()
        latch_pin.on()
        latch_pin.off()
        output_enable_pin.off() # enable