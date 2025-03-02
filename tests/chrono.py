from time import time_ns
import gc
from alternatives import message_loop_generator, message_loop, message_loop_comprehension, message_loop_enumerate, message_loop_combo, message_loop_generator

def test_message_loop_performance():
    # Number of iterations for timing
    number = 100
    
    # Time the original implementation
    print("Timing message_loop() performance...")
    gc.collect()
    start = time_ns()
    for _ in range(number):
        message_loop()
    end = time_ns()
    time_original = (end - start) / 1e9

    # Time the comprehension implementation
    print("Timing message_loop_comprehension() performance...")
    gc.collect()
    start = time_ns()
    for _ in range(number):
        message_loop_comprehension()
    end = time_ns()
    time_comprehension = (end - start) / 1e9

    # Time the enumeration implementation
    print("Timing message_loop_enumerate() performance...")
    gc.collect()
    start = time_ns()
    for _ in range(number):
        message_loop_enumerate()
    end = time_ns()
    time_enumerate = (end - start) / 1e9

    # time combo
    print("Timing message_loop_combo() performance...")
    gc.collect()
    start = time_ns()
    for _ in range(number):
        message_loop_combo()
    end = time_ns()
    time_combo = (end - start) / 1e9

    # time generator
    print("Timing message_loop_generator() performance...")
    gc.collect()
    start = time_ns()
    for _ in range(number):
        message_loop_generator()
    end = time_ns()
    time_generator = (end - start) / 1e9

    print(f"Original implementation: {time_original}")
    print(f"Optimised with list comprehension: {time_comprehension}")
    print(f"Optimised with enumerate: {time_enumerate}")
    print(f"Optimised with combo: {time_combo}")
    print(f"Optimised with generator: {time_generator}")


if __name__ == '__main__':
    test_message_loop_performance()