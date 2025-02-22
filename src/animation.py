import matrixdata
import math
import random

import matrixdata
import math
import random

def create_firework_animation():
    """
    Generate a firework animation sequence.
    Returns a list of MatrixData objects representing each frame.
    
    Colors used:
    - 1 (Blue) for the initial rocket
    - 4 (Red), 2 (Green), 1 (Blue), 6 (Yellow), 7 (White) for explosion particles
    Particles are drawn as 2x2 pixel squares for better visibility
    """
    animation = []
    matrix_width = 64
    matrix_height = 32
    
    # Launch phase (frames 0-7)
    rocket_y = [28, 25, 22, 19, 16, 13, 10, 8]
    for y in rocket_y:
        matrix = matrixdata.MatrixData(matrix_height, matrix_width, matrix_width)
        matrix.set_pixel_value(y, 16 + 16, 1)  # Blue rocket, centered
        animation.append(matrix)
    
    # Explosion phase (frames 8-19)
    particles = []
    colors = [1, 2, 4, 6, 7]  # Blue, Green, Red, Yellow, White
    
    # Initialize 20 particles
    for _ in range(20):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(0.5, 2.0)
        color = random.choice(colors)
        particles.append({
            'x': 16.0,  # Center x
            'y': 8.0,   # Explosion point y
            'dx': math.cos(angle) * speed,
            'dy': math.sin(angle) * speed,
            'color': color
        })
    
    # Generate explosion frames
    for _ in range(12):
        matrix = matrixdata.MatrixData(matrix_height, matrix_width, matrix_width)
        
        # Update and draw particles
        for p in particles:
            # Update position
            p['x'] += p['dx']
            p['y'] += p['dy']
            p['dy'] += 0.1  # Gravity effect
            
            # Draw particle as 2x2 square if in bounds
            base_x, base_y = int(p['x']) + 16, int(p['y'])  # Add 16 to center horizontally
            
            # Draw 2x2 pixel square for each particle
            for offset_y in range(2):
                for offset_x in range(2):
                    x = base_x + offset_x
                    y = base_y + offset_y
                    if 0 <= x < matrix_width and 0 <= y < matrix_height:
                        matrix.set_pixel_value(y, x, p['color'])
        
        animation.append(matrix)
    
    return animation