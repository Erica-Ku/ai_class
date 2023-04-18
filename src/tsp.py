import random
import math

# 인접행렬 - 그래프 만들고 다시 적용
def create_problem(filename):
    f = open(filename, 'r')
    num_cities = int(f.readline())
    locations = []
    for line in f.readlines():
        # 튜플로 만들기
        locations.append(eval(line))
    f.close()
    table = create_distance_table(num_cities, locations)
    return num_cities, locations, table

# 인접행렬 만들기
def create_distance_table(num_cities, locations):
    table = []
    for i in range(num_cities):
        line = []
        for k in range(num_cities):
            distance = math.sqrt(((locations[i][0] - locations[k][0])**2 + (locations[i][1] - locations[k][1])**2))
            line.append(distance)
        table.append(line)
    return table

def random_init(p):
    # 결과 - shuffle!
    n = p[0]
    init = list(range(n))
    random.shuffle(init)
    return init

def evaluate(current, p):
    cost = 0
    num_cities, locations, table = p
    for i in range(num_cities):
        cost += table[current[i]][current[i-1]]
    return cost

def describe_problem(p):
    print()
    n = p[0]
    print(f"Number of cities : {n}")
    locations = p[1]
    for i in range(n):
        print(f"{locations[i]}")
        if i % 5 == 4:
            print()

def display_result():
    pass

def coordinate():
    pass

if __name__ == "__main__":
    p = create_problem("./data/tsp30.txt")
    # describe_problem(p)
    init = random_init(p)
    print(evaluate(init, p))