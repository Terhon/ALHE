import random
import matplotlib.pyplot as plt


class OtherAlgorithm:

    def __init__(self, change, denominations):
            self.C = change
            self.VALUES = denominations

    def run(self):
        self.VALUES = sorted(self.VALUES, reverse=True)
        elem = []
        for x in self.VALUES:
            count = int(self.C / x)
            self.C -= x * count
            elem.append(count)
        elem.reverse()
        return elem


class Algorithm:
    POP_SIZE = 200
    MUTATION_CHANCE = 0.2
    MUTATION_SIZE = 2

    def __init__(self, change, denominations, pop_size, mutation_chance, mutation_size):
        self.C = change
        self.VALUES = denominations
        self.POP_SIZE = pop_size
        self.MUTATION_CHANCE = mutation_chance
        self.MUTATION_SIZE = mutation_size
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
        return self.population[0]

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
            p1 = self.population[self.POP_SIZE - int(random.triangular(0, self.POP_SIZE - 1, self.POP_SIZE/2)) - 1]
            p2 = self.population[self.POP_SIZE - int(random.triangular(0, self.POP_SIZE - 1, self.POP_SIZE/2)) - 1]
            new = []
            for i in range(len(self.VALUES)):
                elem = p1[i] if random.randint(0,1) == 1 else p2[i]
                new.append(elem)
            self.population.append(self.mutate(new))

    def mutate(self, specimen):
        if random.random() < self.MUTATION_CHANCE:
            mutation = random.randint(1, self.MUTATION_SIZE)
            mutation *= random.choice([1, -1])
            mutation_idx = random.randint(0, len(self.VALUES) - 1)
            specimen[mutation_idx] += mutation
            if specimen[mutation_idx] < 0:
                specimen[mutation_idx] = 0
        return specimen


class Test:
    axisX = []
    axisY = []

    def __init__(self):
        self.TEST = 1

    def test_all(self, iterations):
        self.test_case_population(iterations)
        self.test_case_mutation_chance(iterations)
        self.test_case_mutation_size(iterations)

    def test_case_population(self, iterations):
        for pop_size in range(50, 500, 50):
            correct = 0
            for _ in range(iterations):
                change = 50
                a = OtherAlgorithm(change, [1, 2, 5, 10])
                correct_solution = a.run()
                b = Algorithm(change, [1, 2, 5, 10], pop_size, 0.2, 2)
                solution = b.run(50)
                if solution == correct_solution:
                    correct += 1
            self.axisX.append(pop_size)
            self.axisY.append(correct/iterations)
        self.show_plot("population_size", "correct")

    def test_case_mutation_chance(self, iterations):
        for mutation_chance in range(1, 10, 1):
            correct = 0
            for _ in range(iterations):
                change = 50
                a = OtherAlgorithm(change, [1, 2, 5, 10])
                correct_solution = a.run()
                b = Algorithm(change, [1, 2, 5, 10], 100, mutation_chance, 2)
                solution = b.run(50)
                if solution == correct_solution:
                    correct += 1
            self.axisX.append(mutation_chance)
            self.axisY.append(correct/iterations)
        self.show_plot("mutation_chance", "correct")

    def test_case_mutation_size(self, iterations):
        for mutation_size in range(1, 4, 1):
            correct = 0
            for _ in range(iterations):
                change = 50
                a = OtherAlgorithm(change, [1, 2, 5, 10])
                correct_solution = a.run()
                b = Algorithm(change, [1, 2, 5, 10], 100, 0.2, mutation_size)
                solution = b.run(50)
                if solution == correct_solution:
                    correct += 1
            self.axisX.append(mutation_size)
            self.axisY.append(correct/iterations)
        self.show_plot("mutation_size", "correct")

    def show_plot(self, label_x, label_y):
        plt.xlabel(label_x)
        plt.ylabel(label_y)
        plt.plot(self.axisX, self.axisY)
        plt.show()
        self.axisX = []
        self.axisY = []
        
        
class Interface:
    change = 50
    denominations = []
    pop_size = 200
    mutation_chance = 0.2
    mutation_size = 2
    iterations = 50

    def __init__(self):
        self.prompt()

    def prompt(self):
        self.change = int(input("Enter change: "))
        self.denominations = [int(x) for x in input("Enter list of denominations (separated by space): ").split()]
        self.pop_size = int(input("Enter initial population: "))
        self.mutation_chance = float(input("Enter mutation chance: "))
        self.mutation_size = int(input("Enter mutation size: "))
        self.iterations = int(input("Enter number of iterations: "))

    def run(self):
        algorithm = Algorithm(self.change, self.denominations, self.pop_size, self.mutation_chance, self.mutation_size)
        other_algorithm = OtherAlgorithm(self.change, self.denominations)
        print("Evolutionary output: ", algorithm.run(self.iterations))
        print("Optimal output: ", other_algorithm.run())


interface = Interface()
interface.run()


# test = Test()
# test.test_all(100)
