#!/usr/bin/python3
"""Given an employee ID, this script returns info about his/her
   TODO list progress.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]

    user = requests.get(base_url + "users/{}".format(userId)).json()
    todos = requests.get(base_url + "todos", params={'userId': userId}).json()

    filename = "{}.csv".format(userId)
    with open(filename, 'w', newline='') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        [csv_writer.writerow([userId, user.get('username'), todo.get('completed'),
                             todo.get('title')]) for todo in todos]
