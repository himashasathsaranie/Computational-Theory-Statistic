import random

def simulate_dice_throws(num_simulations, num_dice, target_sum):
    count_sum_32 = 0
    
    for _ in range(num_simulations):
        throws = [random.randint(1, 6) for _ in range(num_dice)]
        if sum(throws) == target_sum:
            count_sum_32 += 1
    
    probability_simulated = count_sum_32 / num_simulations
    return probability_simulated

# User Input
num_simulations = int(input("Enter the number of simulations: "))
num_dice = int(input("Enter the number of dice throws: "))
target_sum = int(input("Enter the target sum: "))

# Simulate and Calculate Simulated Probability
probability_simulated = simulate_dice_throws(num_simulations, num_dice, target_sum)

print(f"Simulated Probability: {probability_simulated}")
