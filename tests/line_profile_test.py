from line_profiler import LineProfiler
from comprehension import message_loop, message_loop_comprehension, message_loop_opt, printat

def run_line_profiler():
    profiler = LineProfiler()
    # Profile specific functions
    profiler.add_function(printat)
    profiler.add_function(message_loop)
    profiler.add_function(message_loop_comprehension)
    profiler.add_function(message_loop_opt)
    
    # Run the code
    profiler.run('message_loop()')
    profiler.run('message_loop_comprehension()')
    profiler.run('message_loop_opt()')
    
    # Print results
    profiler.print_stats()

if __name__ == "__main__":
    run_line_profiler()