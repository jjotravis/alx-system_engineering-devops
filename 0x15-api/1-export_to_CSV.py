#!/usr/bin/python3
"""For a given employee ID
returns information about his/her TODO list progress
export data in the CSV format."""
import requests
import sys
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    user_id = sys.argv[1]

    with open(f'{user_id}.csv', 'w', newline="") as csv_file:
        writer = csv.writer(csv_file)
        for t in todos:
            writer.writerow(
                [user_id, user.get("username"),
                 t.get("completed"), t.get("title")]
            )
