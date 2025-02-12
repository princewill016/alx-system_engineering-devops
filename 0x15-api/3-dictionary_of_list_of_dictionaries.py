#!/usr/bin/python3
"""Script to export all employees' TODO list data to JSON format"""
import json
import requests


def export_all_employees_tasks():
    """Exports all employees' TODO list data to JSON file"""
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get all users
    users_response = requests.get(f"{base_url}/users")
    if users_response.status_code != 200:
        print("Error: Could not fetch users")
        return
    
    users = users_response.json()
    
    # Get all todos
    todos_response = requests.get(f"{base_url}/todos")
    if todos_response.status_code != 200:
        print("Error: Could not fetch TODO list")
        return
    
    todos = todos_response.json()
    
    # Format data
    all_tasks = {}
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        user_todos = [todo for todo in todos 
                     if todo.get("userId") == int(user_id)]
        
        all_tasks[user_id] = [
            {
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }
            for todo in user_todos
        ]
    
    # Write to JSON
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    export_all_employees_tasks()
