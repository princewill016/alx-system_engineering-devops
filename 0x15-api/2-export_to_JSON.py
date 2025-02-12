#!/usr/bin/python3
"""Script to export TODO list data to JSON format"""
import json
import requests
import sys


def export_to_json(employee_id):
    """
    Exports employee TODO list data to JSON file
    Args:
        employee_id: Integer ID of the employee
    """
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get employee info
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print(f"Error: Employee with ID {employee_id} not found")
        sys.exit(1)
    
    employee = user_response.json()
    
    # Get todos for employee
    todos_response = requests.get(f"{base_url}/todos", 
                                params={"userId": employee_id})
    if todos_response.status_code != 200:
        print("Error: Could not fetch TODO list")
        sys.exit(1)
    
    todos = todos_response.json()
    
    # Format data
    tasks_list = []
    for todo in todos:
        tasks_list.append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": employee.get("username")
        })
    
    # Write to JSON
    json_filename = f"{employee_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump({str(employee_id): tasks_list}, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
    
    export_to_json(employee_id)
