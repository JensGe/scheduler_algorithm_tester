from time import time
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

from util import constants as cst

start_time = 0
log_list = []


def test(frontier_collection):
    global start_time
    start_time = int(round(time() * 1000))
    log_list.append([time(), 'Start'])
    scheduler_processes = []
    with ThreadPoolExecutor(max_workers=len(frontier_collection)) as scheduler:
        for i in range(len(frontier_collection)):
            scheduler_processes.append(scheduler.submit(crawl_frontier, frontier_collection[i], i))
            log_list.append([time(), f'Crawllist {i} started'])
            # print(f'{int(round(time() * 1000)) - start_time}: Crawllist {i} started')
    for task in as_completed(scheduler_processes):
        log_list.append([time(), task.result()])
        # print(f'{task.result()}')

    return int(round(time() * 1000)) - start_time, sorted(log_list)


def crawl_frontier(crawling_list, part):
    crawler_processes = []
    with ThreadPoolExecutor(max_workers=5) as crawler:
        log_list.append([time(), f'Crawling: {crawling_list[0]}'])
        crawler_processes.append(crawler.submit(crawl_url, crawling_list[0], cst.standard_crawl_duration))
        for i in range(1, len(crawling_list)):
            log_list.append([time(), f'Crawling: {crawling_list[i]}'])
            if str(crawling_list[i])[0] == str(crawling_list[i-1])[0]:
                log_list.append([time(), f'Domain Penalty 10s at: {crawling_list[i]}'])
                # print(f'{int(round(time() * 1000)) - start_time}: Domain Penalty 10s before: {crawling_list[i]}')
            crawler_processes.append(crawler.submit(crawl_url, crawling_list[i], cst.same_domain_penalty))

    for task in as_completed(crawler_processes):
        log_list.append([time(), task.result()])
        # print(f'{int(round(time() * 1000)) - start_time}: {task.result()}')
    return f'Finished {part}'


def crawl_url(url, time_):
    sleep(time_)
    return f'{url} crawled'


# def calculate_time(frontier_collection):
#     calc_time = 0
#     for crawler_list in frontier_collection:
#         separated_crawler_list = [[item[0], item[1]] for item in crawler_list]
#         for i in range(1, len(separated_crawler_list)):
#             if separated_crawler_list[i][0] == separated_crawler_list[i-1][0]:
#                 calc_time += cst.same_domain_penalty
#             calc_time += cst.standard_crawl_duration
