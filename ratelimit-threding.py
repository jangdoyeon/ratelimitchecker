# -*- coding: utf-8 -*-

__author__ = "dyjang"


import concurrent.futures
import datetime
import requests
import json
import sys
import time

setting_dict = json.load(open("setting.json"))


def url_req(c):
    # Post Request Data
    data = setting_dict["data"]
    # Header
    hd = setting_dict["header"]
    test_url = setting_dict["url"]
    # URL

    print(f'[{c+1}] Request at {datetime.datetime.now()}')
    try:
        # POST Request
        f = requests.post(test_url, data=data, headers=hd)
        # status_code, text
        print(f'[{c+1}] Response status code : {f.status_code}')
    except urllib.error.HTTPError as e:
        print(f'[{c+1}] Error : {e}')


def thread_req():

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(url_req, range(5))

        for result in results:
            print(result)


def main():

    # get argv
    # if len(sys.argv) < 2:
    #     print("""
    #     Please Input thread count in argv.

    #     Usage : ratelimit.py <thread count>
    #     """)
    # else:
    # cnt = sys.argv[1]
    thread_req()


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"time : {round(end-start,2)}")
