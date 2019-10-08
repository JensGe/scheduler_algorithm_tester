from util import constants as cst


def simple_split(super_frontier, parts):
    frontier_collection = []
    part_size = int(len(super_frontier) / parts)

    for i in range(0, len(super_frontier), part_size):
        frontier_collection.append(super_frontier[i:i + part_size])

    return frontier_collection


def split_group_domain():
    frontier_collection = [[] for _ in range(cst.SUPER_FRONTIER_PARTS)]

