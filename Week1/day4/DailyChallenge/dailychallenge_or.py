import random

# ======================
# Gene
# ======================

class Gene:
    def __init__(self):
        self.value = random.randint(0, 1)

    def mutate(self):
        # Flip : 0 -> 1 ou 1 -> 0
        self.value = 1 - self.value

    def __str__(self):
        return str(self.value)


# ======================
# Chromosome
# ======================

class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]

    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.5:  # 1 chance sur 2
                gene.mutate()

    def is_all_ones(self):
        return all(gene.value == 1 for gene in self.genes)

    def __str__(self):
        return ''.join(str(gene) for gene in self.genes)


# ======================
# DNA
# ======================

class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]

    def mutate(self):
        for chromosome in self.chromosomes:
            if random.random() < 0.5:
                chromosome.mutate()

    def is_all_ones(self):
        return all(
            chromosome.is_all_ones()
            for chromosome in self.chromosomes
        )

    def fitness(self):
        """
        Nombre de gènes à 1
        Maximum = 100
        """
        return sum(
            gene.value
            for chromosome in self.chromosomes
            for gene in chromosome.genes
        )

    def __str__(self):
        return '\n'.join(
            str(chromosome)
            for chromosome in self.chromosomes
        )


# ======================
# Organism
# ======================

class Organism:
    def __init__(self, dna, environment):
        self.dna = dna
        self.environment = environment

    def mutate(self):
        if random.random() < self.environment:
            self.dna.mutate()

    def is_perfect(self):
        return self.dna.is_all_ones()

    def fitness(self):
        return self.dna.fitness()


# ======================
# Simulation
# ======================

POPULATION_SIZE = 100
ENVIRONMENT = 0.7

population = [
    Organism(DNA(), ENVIRONMENT)
    for _ in range(POPULATION_SIZE)
]

generation = 0
found = False

while not found:

    generation += 1

    for organism in population:

        organism.mutate()

        if organism.is_perfect():
            found = True

            print(f"\nPerfect organism found!")
            print(f"Generation: {generation}")
            print(f"Fitness: {organism.fitness()}/100")

            print("\nDNA:")
            print(organism.dna)

            break

print(f"\nTotal generations: {generation}")