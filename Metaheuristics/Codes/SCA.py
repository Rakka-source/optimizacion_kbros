import math
import random
import numpy as np


# Sine Cosine Algorithm SCA
def iterarSCA(maxIter, t, dimension, population, bestSolution):
    a = 2
    r1 = a - t * (a / maxIter)
    for i in range(population.len()):
        for j in range(dimension):
            r2 = (2*np.pi)*random.uniform(0.0)
            r3 = 2*random.uniform(0.0)
            r4 = random.uniform(0.0)

        if r4 < 0.5:
            population[i][j] = population[i][j] + ( r1 * math.sin(r2) * abs(r3 * bestSolution[j] - population[i][j]))
        else:
            population[i][j] = population[i][j] + ( r1 * math.cos(r2) * abs(r3 * bestSolution[j] - population[i][j]))
    return np.array(population)