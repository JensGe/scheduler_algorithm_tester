from time import time
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed


def test(frontier_collection):
    start_time = int(round(time() * 1000))
    processes = []
    with ThreadPoolExecutor(max_workers=len(frontier_collection)) as executer:
        for crawling_list in frontier_collection:
            processes.append(executer.submit(crawl_frontier, crawling_list))
    for task in as_completed(processes):
        print(task.result())
    # for crawling_list in frontier_collection:
    #     crawl_frontier(crawling_list)

    return int(round(time() * 1000)) - start_time


def crawl_frontier(crawling_list):
    for item in crawling_list:
        crawl_url(item)
    return True


def crawl_url(url):
    sleep(0.1)
    return
