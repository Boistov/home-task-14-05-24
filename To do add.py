from datetime import datetime

tasks = []

def add():
    task = {
        "user": input("username:"),
        "task": input("task name:"),
        "due_date": input("due_date:"),
        "is_completed": False,
        "created_st": datetime.now(),
    }
    tasks.append(task)

add()
print("__________________________")
add()
print(tasks)

def get(username):
    for task in tasks:
        if task["user"] == username:
            return task

users = input()
num = get(users)
if num:
    print("Error")
    print(num)


def delete(username):
    for task in tasks:
        if task["user"] == username:
            tasks.remove(task)
            print(f"Task for user '{username}' deleted successfully.")
            return
    print(f"No task found for user '{username}'.")

# Example usage:
username_to_delete = input("Enter the username to delete the task: ")
delete(username_to_delete)
print(tasks)  # Print the updated tasks list
