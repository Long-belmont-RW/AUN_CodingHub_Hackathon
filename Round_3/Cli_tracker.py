from datetime import datetime
from random import randint
import json

task_file = 'data.json'



def create_task(name, description, status, Created_at):
    task_details = dict(name = name, description = description,
                        status = status, Created_at = Created_at, id=randint(1, 100) )
    

    try:
        with open('data.json', 'r') as file:
            Tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        Tasks = []
    
    Tasks.append(task_details)

    
    with open('data.json', 'w') as file:
        json.dump(Tasks, file, indent=4)
    print("Your task has been added successfully")

def update_task():
    
    try: 
        with open('data.json', 'r') as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

    if not tasks:
        print("No data to update, kindly add some tasks")
        return

    id = int(input("Kindly insert a unique id: "))
    status = input("Kindly input current status")
    task_found = False
    
    for task in tasks:

        if task['id'] == id:
            task['status'] = status
            task['updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            task_found = True
            print(f"updated status: ")
            print(f"Name: {task['name']}")
            print(f"Description: {task['description']}")
            print(f"Status: {task['status']}")
            print(f"Created_at: {task['Created_at']}")
            print(f"Unique Id: {task['id']}")
            print(f"Updated_at: {task['updated']}")
            break

           
    if not task_found:
        print(f"Task with the ID {id} not found")

    with open('data.json', 'w') as file:
        json.dump(tasks, file, indent=4)
    print("Your task has been added successfully")



def display_tasks():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    
    if not data:
        print("No tasks found.\n")
        return
    
    for task in data:
        print(f"Name: {task['name']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task['status']}")
        print(f"Created_at: {task['Created_at']}\n")
        print(f"Unique Id: {task['id']}")


def task_done():
    tasks_done = []
    task_status = False
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    
    if not data:
        print("No tasks found")
    
    for task in data:
        if task['status'] == 'done':
            task_status = True
            print(f"Name: {task['name']}")
            print(f"Description: {task['description']}")
            print(f"Status: {task['status']}")
            print(f"Created_at: {task['Created_at']}\n")
            print(f"Unique Id: {task['id']}")

    if not task_status:
        print("no task has been done yet")
        
def task_in_progress():
    tasks_done = []
    task_status = False
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    
    if not data:
        print("No tasks found")
    
    for task in data:
        if task['status'] == 'in-progress':
            task_status = True
            print(f"Name: {task['name']}")
            print(f"Description: {task['description']}")
            print(f"Status: {task['status']}")
            print(f"Created_at: {task['Created_at']}\n")
            print(f"Unique Id: {task['id']}")
    
    if not task_status:
        print("no task in progress yet")



flag = True


while flag:
    indicator = int(input("What do you want to do: \n1.Create Task \n2.Display task \n3.Show task done \n4.show tasks in progress \n5.Update Task \n6.Quit\n"))

    if indicator == 1:
        name = input("Task: ")
        description = input("Description: ")
        status = input("Status (todo, in-progress, done): ")
        Created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        create_task(name, description, status, Created_at)

    
    elif indicator == 2:
        display_tasks()
    
    elif indicator == 3:
        task_done()
    elif indicator == 4:
        task_in_progress()
    
    elif indicator == 5:
        update_task()
    else:
        flag = False
        
