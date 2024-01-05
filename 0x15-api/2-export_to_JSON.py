#!/usr/bin/python3
"""
This script fetches user information and their corresponding tasks from the 
JSONPlaceholder API and stores the data in a JSON file named
'todo_all_employees.json'.
"""

import json
import requests as r

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"

    # Get a list of users
    users = r.get(url + "users").json()

    all_user_tasks = {}

    # Iterate through each user
    for user in users:
        user_id = user.get("id")
        user_tasks = r.get(url + f"todos?userId={user_id}").json()

        # Collect tasks for the user
        tasks_info = [
            {
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in user_tasks
        ]

        # Store tasks for the user in the dictionary
        all_user_tasks[user_id] = tasks_info

    # Dump all tasks for all users into a JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_user_tasks, jsonfile, indent=4)
