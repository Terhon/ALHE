import random


class Algorithm:
    VALUES = [1, 2, 5, 10]
    POP_SIZE = 100
    MUTATION_CHANCE = 0.2
    MUTATION_SIZE = 2

    def __init__(self, c):
        self.C = c
        self.population = []
        self.generate_population()

    def generate_population(self):
        for _ in range(self.POP_SIZE):
            elem = []
            for _ in range(len(self.VALUES)):
                elem.append(random.randint(0, 10))
            self.population.append(elem)
        self.evaluate()

    def run(self, iterations):
        for _ in range(iterations):
            self.reproduce()
            self.evaluate()
            self.population = self.population[:-int(self.POP_SIZE/2)]
            print(self.population)

    def evaluate(self):
        self.population.sort(key=sum)
        self.population.sort(key=lambda e: self.fitness(e))

    def fitness(self, pop_list):
        sum = 0
        for i in range(len(self.VALUES)):
            sum += pop_list[i]*self.VALUES[i]
        return abs(sum/self.C - 1)

    def reproduce(self):
        for _ in range(int(self.POP_SIZE/2)):
            p1 = self.population[self.POP_SIZE - int(random.triangular(0,self.POP_SIZE - 1,self.POP_SIZE/2))]
            p2 = self.population[self.POP_SIZE - int(random.triangular(0,self.POP_SIZE - 1,self.POP_SIZE/2))]
            new = []
            for i in range(len(self.VALUES)):
                elem = p1[i] if random.randint(0,1) == 1 else p2[i]
                new.append(elem)
            self.population.append(self.mutate(new))

    def mutate(self, speciemen):
        if random.random() < self.MUTATION_CHANCE:
            mutation = random.randint(1, self.MUTATION_SIZE)
            mutation *= -random.randint(0,1)
            mutation_idx = random.randint(0, len(self.VALUES) - 1)
            speciemen[mutation_idx] += mutation
            if speciemen[mutation_idx] < 0:
                speciemen[mutation_idx] = 0
        return speciemen

a = Algorithm(50)
a.run(500)