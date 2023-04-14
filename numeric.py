# 간단한 언덕 등반 알고리즘
## Convex.txt를 사용해서 계산
import random

def create_problem(filename):
    ini_file = open(filename, 'r')
    expression = ini_file.readline().strip()
    var_names = []
    low = []
    up = []
    for line in ini_file.readlines():
        # n, l, u = tuple(line.split(","))
        var_names.append(line.split(",")[0])
        low.append(float(line.split(",")[1]))
        up.append(float(line.split(",")[2]))
    ini_file.close()
    domain = [var_names, low, up]
    return (expression, domain)

def random_init(p):
    expression, domain = p
    init = []
    for i in range(0, len(domain[0])):
        init.append(random.uniform(domain[1][i], domain[2][i]))
    return init

def evaluate(state, p):
    num_eval = 0
    expression = p[0]
    var_name = p[1][0]
    for i in range(len(var_name)):
        assignment = var_name[i] + '=' + str(state[i])
        exec(assignment)
    return num_eval

if __name__ == "__main__":
    pass