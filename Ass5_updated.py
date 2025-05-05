
import random
import numpy as np

def objective(x):
    return np.sum(x**2)

def clonal(antibody , dimension , generation , clone , fclone , fmut):
    antibodies = np.random.uniform(-5 , 5 , size = (antibody , dimension))

    for i in range(generation):
        values = np.array([objective(ant) for ant in antibodies])
        clones = np.repeat(antibodies , np.round(clone * (1 + (1 / fclone * values))).astype(int) , axis = 0)
        mut_mask = np.random.rand(*clones.shape) < fmut
        mut_amount = np.random.uniform(-0.5 , 0.5, size = clones.shape) * (5+5)
        mut_clones = np.clip(clones + mut_mask * mut_amount , -5 , 5)
        combined_ant = np.vstack((antibodies , mut_clones))
        combined_values = np.array([objective(ant) for ant in combined_ant])
        antibodies = combined_ant[np.argsort(combined_values)][:antibody]

    return antibodies[0]


answer = clonal(50 , 3 , 100 , 10 , 0.1 , 0.1)

value = objective(answer)

print(answer , value)


# 1. Start with random guesses
# We create a group of random guesses (called antibodies). Each guess is a list of 3 numbers between -5 and 5.

# Example guess: [3.2, -1.5, 4.9]

# 2. Check how good each guess is
# We use the math function to check how "bad" each guess is. The smaller the answer, the better the guess.

# 3. Make copies (clones)
# We make more copies of the better guesses. Good guesses get more clones, bad guesses get fewer.

 # 4. Change the clones (mutation)
# We slightly change the numbers in the clones to try new guesses. This is like trying similar but new ideas.

# 5. Pick the best guesses
# We now have the old guesses and the new mutated guesses. We keep only the best ones (the ones with the smallest value from the function).

# 6. Repeat
# We do steps 2 to 5 again and again (100 times in this case). Each time, the guesses should get better.


# import numpy as np

# # Define the objective function (fitness function)
# def objective_function(x):
#     return np.sum(x**2)

# # Clonal Selection Algorithm
# def clonal_selection_algorithm(num_antibodies, num_dimensions, search_space, num_generations, num_clones, clone_factor, mutation_rate):
#     antibodies = np.random.uniform(search_space[:, 0], search_space[:, 1], size=(num_antibodies, num_dimensions))

#     for generation in range(num_generations):
#         fitness = np.array([objective_function(antibody) for antibody in antibodies])
#         clones = np.repeat(antibodies, np.round(num_clones * (1 / (1 + fitness * clone_factor))).astype(int), axis=0)
#         mutation_mask = np.random.rand(*clones.shape) < mutation_rate
#         mutation_amounts = np.random.uniform(-0.5, 0.5, size=clones.shape) * (search_space[:, 1] - search_space[:, 0])
#         mutated_clones = np.clip(clones + mutation_mask * mutation_amounts, search_space[:, 0], search_space[:, 1])
#         combined_population = np.vstack((antibodies, mutated_clones))
#         fitness_combined = np.array([objective_function(antibody) for antibody in combined_population])
#         antibodies = combined_population[np.argsort(fitness_combined)][:num_antibodies]

#     return antibodies[0]

# best_solution = clonal_selection_algorithm(50, 3, np.array([[-5,5]]* 3), 100, 10,0.1, 0.1)
# print("Best Solution:", best_solution)
# print("Objective Value:", objective_function(best_solution))






