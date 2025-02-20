import unittest
import timeit
from comprehension import message_loop, message_loop_comprehension, matrix

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
        
        print(f"\nPerformance test results ({number} iterations):")
        print(f"Original loop: {time_original:.4f} seconds")
        print(f"List comprehension: {time_comprehension:.4f} seconds")
        print(f"Difference: {abs(time_original - time_comprehension):.4f} seconds")
        print(f"Ratio: {(time_original/time_comprehension):.2f}x")

        # Verify both implementations produce same output
        matrix.clear_all_bytes()
        message_loop()
        result1 = matrix.get_all_bytes()
        
        matrix.clear_all_bytes()
        message_loop_comprehension()
        result2 = matrix.get_all_bytes()
        
        self.assertEqual(result1, result2, "Both implementations should produce identical output")

if __name__ == '__main__':
    unittest.main()