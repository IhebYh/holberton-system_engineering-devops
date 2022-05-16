#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == '__main__':

    id = sys.argv[1]
    title = []
    com = 0
    total = 0
    url = "https://jsonplaceholder.typicode.com/users/" + id
    result = requests.get(url).json()
    name = res.get('name')
    url = "https://jsonplaceholder.typicode.com/todos/"
    result2 = requests.get(url).json()
    for r in result2:
        if r.get('userId) == int(id):
            if r.get('completed') is True:
                title.append(i['title'])
                complete += 1
            total += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, com, total))
    for s in title:
        print("\t {}".format(s))
