#!/usr/bin/python3
"""Script to fetch and display TODO list progress for a given employee ID"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays TODO list progress for given employee ID
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
    
    # Calculate progress
    total_tasks = len(todos)
    done_tasks = len([todo for todo in todos if todo.get("completed")])
    
    # Display progress
    print(f"Employee {employee.get('name')} is done with tasks"
          f"({done_tasks}/{total_tasks}):")
    
    # Display completed tasks
    for todo in todos:
        if todo.get("completed"):
            print(f"\t {todo.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
    
    get_employee_todo_progress(employee_id)
