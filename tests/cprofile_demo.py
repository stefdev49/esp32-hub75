import cProfile
import pstats
from comprehension import message_loop, message_loop_comprehension, message_loop_enumerate

def run_profiler():
    # Profile original loop
    profiler = cProfile.Profile()
    print("Profiling message_loop() performance...")
    profiler.enable()
    for _ in range(100):
        message_loop()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumulative')
    print("\nOriginal message_loop() performance:")
    stats.print_stats(10)  # Show top 10 entries

    # Profile comprehension loop
    profiler = cProfile.Profile()
    print("Profiling message_loop_comprehension() performance...")
    profiler.enable()
    for _ in range(100):
        message_loop_comprehension()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumulative')
    print("\nList comprehension message_loop_comprehension() performance:")
    stats.print_stats(10)

    # Profile enumerate loop
    profiler = cProfile.Profile()
    print("Profiling message_loop_enumerate() performance...")
    profiler.enable()
    for _ in range(100):
        message_loop_enumerate()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumulative')
    print("\nOptimized message_loop_enumerate() performance:")
    stats.print_stats(10)

if __name__ == "__main__":
    run_profiler()