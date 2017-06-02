"""
problem: 
    based on the diabetes data, generate a population of height and weight data that gives the BMI value of 23
"""
from random import randint, random
from operator import add

def individual():
    '''Create a member of the population.'''
    individual = []
        # first element is the weight in kgs
    x = randint(1,500)
    individual.append(x)
    # next we create a random weight
    y = randint(500, 2500)
    individual.append(y)

    return individual

def population(count):
    """
    Create a number of individuals (i.e. a population).
        count: the number of individuals in the population
    """
    return [ individual() for x in xrange(count) ]

def fitness(individual, target):
    """
    Determine the fitness of an individual. Higher is better.

    individual: the individual to evaluate
    target: the target number individuals are aiming for
    """

    weight = individual[0]
    height = individual[1]/100 # convert to centimeters
    bmi = weight/(height)**2
    fitness = abs(target-bmi)

    print "individual: {}\n bmi: {}\n fitness: {}\n".format(individual, bmi, fitness)

    return fitness

def grade(pop, target):
    'Find average fitness for a population.'
    summed = reduce(add, (fitness(x, target) for x in pop))
    grade = summed / (len(pop) * 1.0)

    print "Averaging fitness for population: {}\n grade: {}".format(pop, grade)
    return grade

def evolve(pop, target, retain=0.2, random_select=0.05, mutate=0.01):
    graded = [(fitness(x, target), x) for x in pop]
    graded = [x[1] for x in sorted(graded)]
    retain_length = int(len(graded)*retain)
    parents = graded[:retain_length]
    # randomly add other individuals to
    # promote genetic diversity
    for individual in graded[retain_length:]:
        if random_select > random():
            parents.append(individual)
    # mutate some individuals
    for individual in parents:
        if mutate > random():
            pos_to_mutate = randint(0, len(individual)-1)
            # this mutation is not ideal, because it
            # restricts the range of possible values,
            # but the function is unaware of the min/max
            # values used to create the individuals,
            individual[pos_to_mutate] = randint(
                min(individual), max(individual))
    # crossover parents to create children
    parents_length = len(parents)
    desired_length = len(pop) - parents_length
    children = []
    while len(children) < desired_length:
        male = randint(0, parents_length-1)
        female = randint(0, parents_length-1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = len(male) / 2
            child = male[:half] + female[half:]
            children.append(child)        
    parents.extend(children)
    print "Current population: {}".format(parents)
    return parents

def main():
    target = 23
    p_count = 10

    p = population(p_count)
    fitness_history = [grade(p, target)]
    for i in xrange(100):
        p = evolve(p, target)
        fitness_history.append(grade(p, target))

    print "Fitness history: "
    print fitness_history


if __name__ == '__main__':
    main()
