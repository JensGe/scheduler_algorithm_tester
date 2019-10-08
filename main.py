from util import presentation
from util import constants as cst

from ListGenerator import list_generator
from Scheduler import scheduler
from CrawlerSimulator import simulate


def main():

    super_frontier = []
    frontier_collection = []

    frontier_length = cst.SUPER_FRONTIER_LENGTH
    frontier_parts = cst.SUPER_FRONTIER_PARTS

    menu = True
    while menu:
        print("## Scheduler Test")
        print("## (1) Create Super-Frontier List")
        print("## (2) Split Super-Frontier List")
        print("## (3) Test Super-Frontier Splits")
        print("## ---------------")
        print("## (x) Exit")

        menu_selection = str(input("> "))

        if menu_selection == "1":
            super_frontier = list_generator.create_example_frontier()
            print(super_frontier)

        elif menu_selection == "2":
            frontier_collection = scheduler.simple_split(super_frontier=super_frontier, parts=frontier_parts)
            presentation.present_list(list_=frontier_collection)

        elif menu_selection == "3":
            time_, log_list = simulate.test(frontier_collection)
            print(f'Time taken: {str(time_/1000)} s.')
            presentation.present_list(log_list)

        elif menu_selection == "x":
            menu = False


if __name__ == "__main__":
    main()
