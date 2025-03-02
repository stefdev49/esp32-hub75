import timeit
from comprehension import message_loop, message_loop_comprehension, message_loop_enumerate, message_loop_combo

def test_message_loop_performance():
    # Number of iterations for timing
    number = 100
    
    # Time the original implementation
    print("Timing message_loop() performance...")
    time_original = timeit.timeit(
        lambda: message_loop(), 
        number=number
    )
    
    # Time the comprehension implementation
    print("Timing message_loop_comprehension() performance...")
    time_comprehension = timeit.timeit(
        lambda: message_loop_comprehension(), 
        number=number
    )

    # Time the enumerate implementation
    print("Timing message_loop_enumerate() performance...")
    time_enumerate = timeit.timeit(
        lambda: message_loop_enumerate(), 
        number=number
    )

    # Time the combo implementation
    print("Timing message_loop_combo() performance...")
    time_combo = timeit.timeit(
        lambda: message_loop_combo(), 
        number=number
    )

    print(f"Original implementation: {time_original}")
    print(f"Optimised with list comprehension: {time_comprehension}")
    print(f"Optimised with enumerate: {time_enumerate}")
    print(f"Optimised with combo: {time_combo}")


if __name__ == '__main__':
    test_message_loop_performance()