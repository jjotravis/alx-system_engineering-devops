#!/usr/bin/python3
"""For a given employee ID
returns information about his/her TODO list progress
export data in the JSON format."""
import requests
import sys
import json

if __name__ == "__main__":
    userid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(userid)).json()
    todos = requests.get(url + "todos", params={"userId": userid}).json()

    with open(f"{userid}.json", 'w') as json_file:
        for t in todos:
            json.dump({userid: [
                {
                    "task": t.get("title"),
                    "completed": t.get("completed"),
                    "username": user.get("username")
                }
            ]}, json_file)
