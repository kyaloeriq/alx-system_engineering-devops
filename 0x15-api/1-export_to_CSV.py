#!/usr/bin/python3
"""
Python script to export data in CSV format.
"""

import csv
import requests
import sys

BASE_URL = 'https://jsonplaceholder.typicode.com'

def fetch_user_data(employee_id):
    """
    Fetch the user details for a given employee ID
    """
    try:
        response = requests.get(f'{BASE_URL}/users/{employee_id}')
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f'Error fetching user data: {e}')
        return None

def fetch_todo_data(employee_id):
    """
    Fetch the TODO list for a given employee ID
    """
    try:
        response = requests.get(f'{BASE_URL}/todos?userId={employee_id}')
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f'Error fetching TODO data: {e}')
        return []

def export_to_csv(employee_id, employee_name, todos):
    """
    Export TODO data to a CSV file
    """
    csv_filename = f'{employee_id}.csv'
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = [
                'USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'
                ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for todo in todos:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': todo['completed'],
                'TASK_TITLE': todo['title']
            })

    print(f'TODO list data exported to {csv_filename}')

def get_employee_todo_progress(employee_id):
    """
    Fetch and display the TODO list progress for a given ID.
    """
    user_data = fetch_user_data(employee_id)
    if not user_data:
        print(f'Employee with ID {employee_id} not found.')
        return

    employee_name = user_data['name']
    todos = fetch_todo_data(employee_id)

    completed_tasks = [todo for todo in todos if todo['completed']]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos)

    print(f'Employee {employee_name} is done with tasks (
            {number_of_done_tasks}/{total_number_of_tasks}
            ):')
    for task in completed_tasks:
        print(f'\t {task["title"]}')

    export_to_csv(employee_id, employee_name, todos)

def main():
    """
    Handle command-line arguments and initiate the process
    """
    if len(sys.argv) != 2:
        print('Usage: python script.py <employee_id>')
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print('Employee ID must be an integer.')
        sys.exit(1)

    get_employee_todo_progress(employee_id)

if __name__ == "__main__":
    main()
