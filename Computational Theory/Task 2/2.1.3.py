from itertools import product

def count_ways_to_make_sum(target_sum, num_dice, dice_faces):
    count = 0
    dice_combinations = product(range(1, dice_faces + 1), repeat=num_dice)
    
    for combination in dice_combinations:
        if sum(combination) == target_sum:
            count += 1
    
    return count

def calculate_exact_probability(target_sum, num_dice, dice_faces):
    ways_to_make_sum = count_ways_to_make_sum(target_sum, num_dice, dice_faces)
    total_possible_combinations = dice_faces ** num_dice
    probability_exact = ways_to_make_sum / total_possible_combinations
    return probability_exact

# User Input
target_sum = int(input("Enter the target sum: "))
num_dice = int(input("Enter the number of dice throws: "))
dice_faces = int(input("Enter the number of faces on each die: "))

# Calculate Exact Probability
probability_exact = calculate_exact_probability(target_sum, num_dice, dice_faces)

print(f"Exact Probability: {probability_exact}")
