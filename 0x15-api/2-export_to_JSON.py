#!/usr/bin/python3
"""Given an employee ID, this script returns info about his/her
   TODO list progress.
"""
import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]

    user = requests.get(base_url + "users/{}".format(userId)).json()
    todos = requests.get(base_url + "todos", params={'userId': userId}).json()

    filename = "{}.json".format(userId)
    with open(filename, 'w') as f:
        json.dump({userId: [{
                 "task": todo.get('title'),
                 "completed": todo.get('completed'),
                 "username": user.get('username')} for todo in todos]}, f)
