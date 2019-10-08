import random


def create_ordered_frontier(length):
    return [i for i in range(length)]


def create_random_frontier(length):
    return [random.randint(10, 99) for i in range(length)]
