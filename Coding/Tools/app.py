import random


def objective_function(individual):
    """
    The function to be optimized. Here, we aim to maximize the sum of elements
    in a binary string, representing a simple 'knapsack' problem or similar.
    """
    return sum(individual)


def create_individual(length):
    """Creates a random binary individual (a list of 0s and 1s)."""
    return [random.randint(0, 1) for _ in range(length)]


def create_population(size, individual_length):
    """Creates a population of individuals."""
    return [create_individual(individual_length) for _ in range(size)]


def select_parents(population, num_parents):
    """Selects the best individuals as parents using a simple ranking."""
    population.sort(key=objective_function, reverse=True)
    return population[:num_parents]


def crossover(parent1, parent2):
    """Performs single-point crossover between two parents."""
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


def mutate(individual, mutation_rate):
    """Mutates an individual by flipping bits with a given probability."""
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]  # Flip the bit
    return individual


def genetic_algorithm(population_size, individual_length, generations, num_parents, mutation_rate):
    """Main genetic algorithm loop."""
    population = create_population(population_size, individual_length)

    for generation in range(generations):
        # Evaluate fitness
        fitness_scores = [objective_function(ind) for ind in population]

        # Select parents
        parents = select_parents(population, num_parents)

        # Create next generation
        next_population = []
        # Keep the best parents directly
        next_population.extend(parents)

        # Fill the rest of the population with offspring
        while len(next_population) < population_size:
            p1, p2 = random.sample(parents, 2)  # Randomly pick two parents
            child1, child2 = crossover(p1, p2)
            next_population.append(mutate(child1, mutation_rate))
            if len(next_population) < population_size:
                next_population.append(mutate(child2, mutation_rate))

        population = next_population

        # Optional: Print best individual of the current generation
        best_individual = max(population, key=objective_function)
        print(
            f"Generation {generation + 1}: Best individual = {best_individual}, Fitness = {objective_function(best_individual)}")

    return max(population, key=objective_function)


if __name__ == "__main__":
    # Parameters for the genetic algorithm
    POPULATION_SIZE = 50
    INDIVIDUAL_LENGTH = 10
    GENERATIONS = 100
    NUM_PARENTS = 10
    MUTATION_RATE = 0.05

    print("Starting Genetic Algorithm...")
    best_solution = genetic_algorithm(
        POPULATION_SIZE,
        INDIVIDUAL_LENGTH,
        GENERATIONS,
        NUM_PARENTS,
        MUTATION_RATE
    )
    print("\nGenetic Algorithm Finished.")
    print(f"Optimal solution found: {best_solution}, Fitness: {objective_function(best_solution)}")