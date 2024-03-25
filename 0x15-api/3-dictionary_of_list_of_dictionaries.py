#!/usr/bin/python3
"""For a given employee ID
returns information about his/her TODO list progress
export data in the JSON format."""
import requests
import sys
import json

if __name__ == "__main__":
    # userid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    # todos = requests.get(url + "todos", params={"UserId": userid}).json()

    with open("todo_all_employees.json", 'w') as json_file:
        for u in users:
            todos = requests.get(url + "todos",
                                 params={"UserId": u.get("id")}).json()
            for t in todos:
                json.dump(
                    {
                        u.get("id"): [
                            {
                                "task": t.get("title"),
                                "completed": t.get("completed"),
                                "username": u.get("username")
                            }
                        ]
                    },
                    json_file)
