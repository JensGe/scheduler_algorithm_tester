from util import presentation
from ListGenerator import list_generator
from Scheduler import scheduler
from CrawlerSimulator import simulate


def main():

    super_frontier = []
    frontier_collection = []

    frontier_length = 100
    frontier_parts = 5

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
            super_frontier = list_generator.create_random_frontier(length=frontier_length)
            presentation.present_list(list_=super_frontier)

        elif menu_selection == "2":
            frontier_collection = scheduler.simple_split(super_frontier=super_frontier, parts=frontier_parts)
            presentation.present_list(list_=frontier_collection)

        elif menu_selection == "3":

            time_ = simulate.test(frontier_collection)
            print("Time taken: " + str(time_) + " ms.")

        elif menu_selection == "x":
            menu = False


if __name__ == "__main__":
    main()
