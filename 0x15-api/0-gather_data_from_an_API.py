#!/usr/bin/python3
# Python script that, returns information about his/her TODO list progress
import requests
import sys


def get_employee_todo_progress(employee_id)
    """
    Fetch and display the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee 

    Returns:
        None
    """
    # Define the base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch employee details
    user_url = f'{base_url}/users/{employee_id}'
    user_response = requests.get(user_url)

    # Check if the employee exists
    if user_response.status_code != 200:
        print(f'Employee with ID {employee_id} not found.')
        return

    user_data = user_response.json()
    employee_name = user_data['name']

    # Fetch TODO list for the employee
    todos_url = f'{base_url}/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Filter completed tasks
    completed_tasks = [todo for todo in todos_data if todo['completed']]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos_data)

    # Print the progress
    print(
        f'Employee {employee_name} is done with tasks('
        f'{number_of_done_tasks}/{total_number_of_tasks}):'
    )
    for task in completed_tasks:
        print(f'\t {task["title"]}')


def main():
    """
    Function to handle command-line arguments and initiate fetching TODO list progress.

    Args:
        None

    Returns:
        None
    """
    # Ensure an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print('Usage: python script.py <employee_id>')
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print('Employee ID must be an integer.')
        sys.exit(1)

    # Get and display the employee TODO list progress
    get_employee_todo_progress(employee_id)


if __name__ == "__main__":
    """
    This block ensures script can be used as a module and as a standalone script.

    Args:
        None

    Returns:
        None
    """
    main()
