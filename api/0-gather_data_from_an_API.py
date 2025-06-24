import requests
import sys

"""
    This module downloads from an api (jsonplaceholder api) and prints the data.
"""

if __name__ == "__main__":
    employer_number = sys.argv[1]
    raw_user_data = requests.get(
        f"https://jsonplaceholder.typicode.com/users?id={employer_number}")
    raw_todo_data = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employer_number}")
    user_json = raw_user_data.json()
    todo_json = raw_todo_data.json()

    user_name = user_json[0]["name"]
    todo_done = [x for x in todo_json if x['completed'] == True]
    print(
        f"Employee {user_name} is done with tasks({len(todo_done)}/{len(todo_json)}):")
    for todo in todo_done:
        print(f"\t {todo["title"]}")
