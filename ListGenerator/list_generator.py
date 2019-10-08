from util import constants as cst
import random


def create_ordered_frontier(length):
    return [i for i in range(10, length+10)]


def create_random_frontier():
    rv = [i for i in range(10, 99)]
    random.shuffle(rv)
    return rv


def create_example_frontier():
    super_frontier = [i for i in range(cst.SUPER_FRONTIER_LENGTH)]
    repeat_domain_indices = random.sample(range(1, cst.SUPER_FRONTIER_LENGTH), cst.SUPER_FRONTIER_DOMAIN_REPEATS)
    for i in range(len(repeat_domain_indices)):
        super_frontier[repeat_domain_indices[i]] = super_frontier[repeat_domain_indices[i]-1]
    return super_frontier
