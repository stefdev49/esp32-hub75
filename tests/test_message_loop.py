import unittest
import timeit
from comprehension import message_loop, message_loop_comprehension, matrix, message_loop_opt

class TestMessageLoop(unittest.TestCase):
    def setUp(self):
        matrix.clear_all_bytes()

    def test_message_loop_performance(self):
        # Number of iterations for timing
        number = 100
        
        # Time the original implementation
        time_original = timeit.timeit(
            lambda: message_loop(), 
            number=number
        )
        
        # Time the comprehension implementation
        time_comprehension = timeit.timeit(
            lambda: message_loop_comprehension(), 
            number=number
        )

        # Time the optimised implementation
        time_opt = timeit.timeit(
            lambda: message_loop_opt(), 
            number=number
        )
        
        print(f"\nPerformance test results ({number} iterations):")
        print(f"Original loop: {time_original:.4f} seconds")
        print(f"List comprehension: {time_comprehension:.4f} seconds")
        print(f"Difference: {abs(time_original - time_comprehension):.4f} seconds")
        print(f"Ratio: {(time_original/time_comprehension):.3f}x")
        print(f"Optimised loop: {time_opt:.4f} seconds")
        print(f"Difference: {abs(time_original - time_opt):.4f} seconds")
        print(f"Ratio: {(time_original/time_opt):.3f}x")
        print(f"Optimised vs Comprehension: {(time_opt/time_comprehension):.3f}x")
        print(f"Optimised vs Original: {(time_opt/time_original):.3f}x")

if __name__ == '__main__':
    unittest.main()