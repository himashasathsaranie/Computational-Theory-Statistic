
import random
import math

def simulate_dart_throw():
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    distance = math.sqrt(x**2 + y**2)
    
    return distance <= 1  # True if within the circle, False otherwise

def estimate_pi(num_simulations):
    hits = 0
    for _ in range(num_simulations):
        if simulate_dart_throw():
            hits += 1
    
    pi_estimate = 4 * (hits / num_simulations)
    return pi_estimate

# Example usage
num_simulations = 10000
estimated_pi = estimate_pi(num_simulations)

print(f"Estimated value of pi: {estimated_pi:.4f}")
