from line_profiler import LineProfiler
from alternatives import message_loop, message_loop_comprehension, message_loop_enumerate, printat, message_loop_opt
from matrixdata import MatrixData

def run_line_profiler():
    matrix = MatrixData(32, 64, 64) 

    profiler = LineProfiler()
    # Profile specific functions
    profiler.add_function(matrix.set_pixel_value)
    profiler.add_function(printat)
    profiler.add_function(message_loop)
    profiler.add_function(message_loop_comprehension)
    profiler.add_function(message_loop_enumerate)
    profiler.add_function(message_loop_opt)
    
    # Run the code
    profiler.run('message_loop()')
    profiler.run('message_loop_comprehension()')
    profiler.run('message_loop_enumerate()')
    profiler.run('message_loop_opt()')
    
    # Print results
    profiler.print_stats()

if __name__ == "__main__":
    run_line_profiler()