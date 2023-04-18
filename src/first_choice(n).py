import numeric
import random

LIMITS = 100

def first_choice(p):
    current = numeric.random_init(p)
    value_distance = numeric.evaluate(current, p)
    i = 0
    while i < LIMITS:
        pass
    return current, value_distance

def random_mutant(current, p):
    DELTA = 0.01
    delta = [-DELTA, DELTA]
    d = random.choice(delta)
    return d

def inversion(current, i, j):
    pass

if __name__ == "__main__":
    p = tsp.create_problem("./data/Convex.txt")
    solution, minimum = first_choice(p)
    print(solution)
    print(minimum)