import random
from util import *


class GASolver:
    def __init__(self, cities, given_order=[]):
        self.cities = cities
        self.total = len(cities)
        self.best_order = []
        self.best_distance = float("inf")
        self.population = []
        self.fitness = []
        self.mutation_rate = 0.01
        self.pop_size = 1000
        self.gen_num = 0
        order = []

        if len(given_order) == 0:
            for i in range(self.total):
                order.append(i)
            for i in range(self.pop_size):
                p = order[:]
                random.shuffle(p)
                self.population.append(p)
        else:
            order = given_order
            for i in range(self.pop_size - 1):
                p = order[:]
                indexA = random.randrange(len(p))
                indexB = random.randrange(len(p))
                p[indexA], p[indexB] = p[indexB], p[indexA]
                self.population.append(p)
            self.population.append(given_order)

        if len(given_order) != 0:
            self.population[random.randrange(0, self.pop_size)] = given_order

        for i in range(self.pop_size):
            d = calc_path_distance(self.cities, self.population[i])
            if d < self.best_distance:
                self.best_distance = d
                self.best_order = self.population[i]
            self.fitness.append(1 / (d + 1))

    def mutate(self, order, mutation_rate):
        pass

    def cross_over(self, order_A, order_B):
        pass

    def cross_over2(self, order_A, order_B):
        pass
    
    def calc_fitness(self):
        pass

    def normalize_fitness(self):
        pass

    def make_next_population(self):
        pass

    def find(self):
        pass