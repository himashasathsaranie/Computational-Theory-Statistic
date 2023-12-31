import random
import math

def simulate_dart_throw():
    # Generate random coordinates within the square (-1, 1) x (-1, 1)
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    # Calculate distance from the center (0, 0)
    distance = math.sqrt(x**2 + y**2)
    
    # Check if the generated point is within the unit circle (dartboard)
    return distance <= 1

def compute_probability(num_simulations):
    hits = 0
    for _ in range(num_simulations):
        if simulate_dart_throw():
            hits += 1
    
    probability = hits / num_simulations
    return probability

# Example usage
num_simulations = 10000
probability = compute_probability(num_simulations)

print(f"Probability of hitting the dartboard: {probability:.4f}")
