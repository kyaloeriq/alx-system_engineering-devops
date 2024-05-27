#!/usr/bin/python3
"""
Python script to export data in the JSON format
"""
import requests
import sys
import json


def get_all_employees_todo_progress():
    """
    Fetch, export the TODO list progress for all employees in JSON format
    """
    # Define the base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch all employee details
    users_url = f'{base_url}/users'
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Dictionary to hold all tasks for all employees
    all_tasks = {}

    # Iterate over each user to fetch their TODO list
    for user in users_data:
        employee_id = user['id']
        employee_name = user['name']

        # Fetch TODO list for the current employee
        todos_url = f'{base_url}/todos?userId={employee_id}'
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Prepare the list of tasks for the current employee
        tasks = [
            {
                "username": employee_name,
                "task": todo['title'],
                "completed": todo['completed']
            }
            for todo in todos_data
        ]

        # Add the tasks to the dictionary with the employee ID as the key
        all_tasks[str(employee_id)] = tasks

    # Export data to JSON
    json_filename = 'todo_all_employees.json'
    with open(json_filename, mode='w') as json_file:
        json.dump(all_tasks, json_file, indent=4)

    print(f'TODO list data for all employees exported to {json_filename}')

def main():
    """
    Function to initiate fetching TODO list progress for all employees.
    """
    # Get and display the employee TODO list progress for all employees
    get_all_employees_todo_progress()

if __name__ == "__main__":
    """
    This block ensures script can be used as a module and as a standalone script.

    Args:
        None

    Returns:
        None
    """
    main()
