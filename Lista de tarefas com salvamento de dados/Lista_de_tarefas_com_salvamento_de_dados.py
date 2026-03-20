import os
import json
from time import sleep

def menu():
    print("""1. Add task
2. Remove task
3. Finish task
4. List tasks
5. Edit task
6. Exit""")
    
tasks = [{"name": "study python", "status":False}]

def save_data():
    with open("tasks.json", "w") as archive:
        json.dump(tasks, archive, indent=4)

def load_data():
    global tasks
    try:
        with open("tasks.json", "r") as archive:
            tasks = json.load(archive)
    except FileNotFoundError:
        tasks = []

def add_task():
    task_to_add = input("Type your task: ").lower()
    data = {"name":task_to_add, "status":False}
    tasks.append(data)
    save_data()
    print("Task added successfully!")
    sleep(2)
    os.system("cls")
    main()

def remove_task():
    task_to_remove = input("Type the name of the task you want to remove: ").lower()
    found = False
    for t in tasks:
        if t["name"] == task_to_remove:
            found = True
            tasks.remove(t)
            save_data()
            print("Task removed successfully!")
            input("Type any key to return to the menu: ")
            break
    if not found:
        print("Task not found!")
        sleep(2)
    os.system("cls")
    main()   
            
def finish_task():
    task_to_finish = input("Type the name of the task you finished: ").lower()
    found = False
    for t in tasks:
        if t["name"] == task_to_finish:
            found = True
            t["status"] = True
            save_data()
            print("Task finished!")
            sleep(2)
            break
    if not found:
        print("Task not found!")
        sleep(2)
    os.system("cls")
    main()

def list_tasks():
    print(f"{'Task'.ljust(20)} | {'Status'}")
    for t in tasks:
        status = "Done" if t["status"] else "Pending"
        print(f"{t['name'].ljust(20).title()} | {status.title()}")
    input("Type any key to return to the menu: ")
    os.system("cls")
    main()

def edit_task():
    task_to_edit = input("Type the name of the task you want to edit: ").lower()
    found = False
    for t in tasks:
        if t["name"] == task_to_edit:
            found = True
            new_name = input("Type the new name").lower()
            index = tasks.index(t)
            tasks.insert(index, {"name": new_name, "status": False})
            tasks.remove(t)
            save_data()
            print("Task edited successfully!")
            sleep(2)
            break
    if not found:
        print("Task not found!")
        sleep(2)
    os.system("cls")
    main()
            
def options():
    option = int(input("Choose an option: "))
    match option:
        case 1:
            add_task()
        case 2:
            remove_task()
        case 3:
            finish_task()
        case 4:
            list_tasks()
        case 5:
            edit_task()
        case 6:
            exit()


def main():
    load_data()
    os.system("cls")
    menu()
    options()

if __name__ == "__main__":
    main()