#!/usr/bin/env python3

import requests
import json
import threading
import time

def getgithublink(id):
        url = 'https://hacker-news.firebaseio.com/v0/item/' + str(id) + '.json'
        json_result = json.loads(requests.get(url).text)
        print(url)

        if json_result is None:
            return

        if 'url' in json_result:
            with open('apispider.txt', 'a', ) as gfile:
                gfile.write(json.dumps(json_result, indent=2, sort_keys=True) + '\n')
                gfile.flush()

def main():
    # Technically it's 10 but with the sleep we are saving a little time with one thread
    max_threads = 11
    maxid = int(requests.get('https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty').text)

    with open('apispider.txt', 'w') as gfile:
        pass

    while True:
        if len(threading.enumerate()) > max_threads:
            time.sleep(0.5)
            continue

        while max_threads >= len(threading.enumerate()):
            t = threading.Thread(target=getgithublink,args=(maxid,))
            t.setDaemon(True)
            t.start()
            maxid -= 1


main()
