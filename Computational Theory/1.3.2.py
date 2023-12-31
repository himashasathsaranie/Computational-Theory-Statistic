import random
import math
import pandas as pd
import matplotlib.pyplot as plt

def simulate_dart_throw():
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    distance = math.sqrt(x**2 + y**2)
    
    return distance <= 1  # True if within the circle, False otherwise

def run_experiment(num_simulations, num_experiments):
    pi_values = []

    for _ in range(num_experiments):
        hits = sum(simulate_dart_throw() for _ in range(num_simulations))
        pi_estimate = 4 * (hits / num_simulations)
        pi_values.append(pi_estimate)

    mean_pi = sum(pi_values) / num_experiments
    mode_pi = max(set(pi_values), key=pi_values.count)

    return pi_values, mean_pi, mode_pi

def save_to_excel(data, file_path):
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)

def plot_pi_values(N_values, pi_values):
    plt.plot(N_values, pi_values, marker='o')
    plt.xscale('log')  # Use a logarithmic scale for better visualization
    plt.xlabel('Number of Simulations (N)')
    plt.ylabel('Estimated Value of pi')
    plt.title('Estimation of pi through Dart Simulation')
    plt.grid(True)
    plt.show()

# Get user input for the number of experiments
num_experiments = int(input("Enter the number of experiments: "))

# Define the list of N values
num_simulations_list = [1000, 10000, 100000, 1000000]

# Predefined Excel file path
excel_file_path = 'pi_estimationnew.xlsx'

# Run experiments and collect data
data = {'Num Simulations': [], 'Pi Values': [], 'Mean Pi': [], 'Mode Pi': []}

for num_simulations in num_simulations_list:
    pi_values, mean_pi, mode_pi = run_experiment(num_simulations, num_experiments)
    data['Num Simulations'].extend([num_simulations] * num_experiments)
    data['Pi Values'].extend(pi_values)
    data['Mean Pi'].extend([mean_pi] * num_experiments)
    data['Mode Pi'].extend([mode_pi] * num_experiments)

# Save data to Excel file
save_to_excel(data, excel_file_path)
print(f'Data saved to {excel_file_path}')

# Plot the pi values
plot_pi_values(num_simulations_list, [data['Pi Values'][i:i+num_experiments] for i in range(0, len(data['Pi Values']), num_experiments)])
