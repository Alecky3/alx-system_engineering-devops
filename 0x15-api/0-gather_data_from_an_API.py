#!/usr/bin/python3
"""Given an employee ID, this script returns info about his/her
   TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]

    user = requests.get(base_url + "users/{}".format(userId)).json()
    todos = requests.get(base_url + "todos", params={'userId': userId}).json()

    completed_todos = [todo.get('title') for todo in todos
                       if todo.get('completed') is True]
    print("Employee {} is done with tasks({}/{})"
          .format(user.get('name'), len(completed_todos), len(todos)))
    for todo in completed_todos:
        print("\t {}".format(todo))
