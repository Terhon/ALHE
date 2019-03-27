import random
import sys


class OtherAlgorithm:

    def __init__(self):
        if len(sys.argv) > 1:
            self.C = int(sys.argv[1])
            self.VALUES = [int(x) for x in sys.argv[2:]]

    def run(self):
        self.VALUES = sorted(self.VALUES, reverse=True)
        elem = []
        for x in self.VALUES:
            count = int(self.C / x)
            self.C -= x * count
            elem.append(count)
        elem.reverse()
        print(elem)


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
            print(self.population[0])

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
            p1 = self.population[self.POP_SIZE - int(random.triangular(0,self.POP_SIZE - 1, self.POP_SIZE/2)) - 1]
            p2 = self.population[self.POP_SIZE - int(random.triangular(0,self.POP_SIZE - 1, self.POP_SIZE/2)) - 1]
            new = []
            for i in range(len(self.VALUES)):
                elem = p1[i] if random.randint(0,1) == 1 else p2[i]
                new.append(elem)
            self.population.append(self.mutate(new))

    def mutate(self, specimen):
        if random.random() < self.MUTATION_CHANCE:
            mutation = random.randint(1, self.MUTATION_SIZE)
            mutation *= -random.randint(0,1)
            mutation_idx = random.randint(0, len(self.VALUES) - 1)
            specimen[mutation_idx] += mutation
            if specimen[mutation_idx] < 0:
                specimen[mutation_idx] = 0
        return specimen


a = Algorithm(53)
a.run(500)
b = OtherAlgorithm()
b.run()
