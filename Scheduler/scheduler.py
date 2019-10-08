def simple_split(super_frontier, parts):
    frontier_collection = []
    part_size = int(len(super_frontier) / parts)
    for i in range(0, len(super_frontier), part_size):
        frontier_collection.append(super_frontier[i:i + part_size])

    return frontier_collection
