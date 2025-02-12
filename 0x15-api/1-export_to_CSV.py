#!/usr/bin/python3
"""Script to export TODO list data to CSV format"""
import csv
import requests
import sys


def export_to_csv(employee_id):
    """
    Exports employee TODO list data to CSV file
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
    
    # Write to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([
                employee_id,
                employee.get('username'),
                str(todo.get('completed')),
                todo.get('title')
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
    
    export_to_csv(employee_id)
