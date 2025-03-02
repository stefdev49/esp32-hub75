import matrixdata

ROW_SIZE = 32
COL_SIZE = 64

matrix = matrixdata.MatrixData(ROW_SIZE, COL_SIZE, COL_SIZE)

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

# version originale
def message_loop():
    pixels = len(sequence)*7
    scroll = 0
    matrix.clear_all_bytes()
    while scroll != - pixels:
        for i in range(0, len(sequence)):
            if scroll+i*7 < COL_SIZE or scroll+i*7 > 0:
                printat(8, scroll+i*7, sequence[i], 255)
        scroll -= 1

# optimisé avec list_comprehension
def message_loop_comprehension():
    pixels = len(sequence)*7
    scroll = 0
    matrix.clear_all_bytes()
    while scroll != -pixels:
        [printat(8, scroll+i*7, sequence[i], 255) 
         for i in range(len(sequence)) 
         if scroll+i*7 < COL_SIZE or scroll+i*7 > 0]
        scroll -= 1

# optimisé avec enumerate
def message_loop_enumerate():
    pixels = len(sequence)*7
    scroll = 0
    matrix.clear_all_bytes()
    while scroll != - pixels:
        for i, char in enumerate(sequence):
            if scroll+i*7 < COL_SIZE or scroll+i*7 > 0:
                printat(8, scroll+i*7, char, 255)
        scroll -= 1    

# optimisation calculs
def message_loop_opt():
    seq_len = len(sequence)
    pixels = seq_len*7
    scroll = 0
    matrix.clear_all_bytes()
    while scroll != - pixels:
        for i in range(0, len(sequence)):
            if val := scroll+i*7 < COL_SIZE or val > 0:
                printat(8, val, sequence[i], 255)
        scroll -= 1

# combinaisons des optimisations
def message_loop_combo():
    pixels = len(sequence)*7
    scroll = 0
    matrix.clear_all_bytes()
    while scroll != - pixels:
        [printat(8, scroll+i*7, char, 255) 
         for i, char in enumerate(sequence) 
         if (val := scroll+i*7) < COL_SIZE or val > 0]
        scroll -= 1

def scroll_sequence(scroll, sequence):
    """Generator that yields (position, char) tuples for valid scroll positions"""
    for i, char in enumerate(sequence):
        pos = scroll + i*7
        if pos < COL_SIZE or pos > 0:
            yield (pos, char)

def message_loop_generator():
    seq_len = len(sequence)
    pixels = seq_len*7
    scroll = 0
    matrix.clear_all_bytes()
    while scroll != -pixels:
        for pos, char in scroll_sequence(scroll, sequence):
            printat(8, pos, char, 255)
        scroll -= 1