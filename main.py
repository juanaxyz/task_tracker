'''
time used to take current time
os used to check if file exist
json used to read and write data in json format
'''
import json
import os
import time

FILENAME = "data.json"
data = []

# check if file exist


def open_file():
    '''
    function to open file if exist else create it
    '''
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    else:
        # create file data.json if it's not exist
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump([], file)
        return []


# init data variable with data from json file
data = open_file()


def save_json():
    '''
    function to save data in json file
    Returns : bool : True if data saved else False
    '''
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
            return True
    except Exception as e:
        print(f"error : {e}")
        return False


def add_task(description: str) -> None:
    '''
    function to add task to the list
    Args :
    description (str): description of the task
    Returns : None
    '''
    try:
        last_id = data[-1]["id"]
    except IndexError:
        last_id = 0

    data.append(
        {
            "id": last_id + 1,
            "description": description,
            "status": "todo",
            "createdAt": time.ctime(),
            "updatedAt": time.ctime(),
        }
    )
    save_json()
    print("task succesfully added ....")
    return None


def get_all_tasks() -> list:
    '''
    function to print all task based on each status
    Args : None
    Returns : list of all tasks
    '''
    if data:
        for element in data:
            print(element)
        return data
    print("it's a bit empty here add some tasks....")
    return []


def get_id_task(description: str):
    '''
    function to get task by id
    Args :
    description (str): description of the task
    Returns : task if found else None
    '''
    for element in data:
        if element["description"] == description or str(element["id"]) == description:
            return element
    return None


def update_task(description: str) -> bool:
    '''
    function to update a status of task
    Args :
    description (str) : string of a task that become a query
    Return : bool : True if task updated else False
    '''
    status = ["todo", "in-progress", "done"]
    task = get_id_task(description)
    if task is not None:
        new_status = input("Enter new status (todo, in-progress, done): ")
        while new_status not in status:
            new_status = input(
                "error please enter valid status (todo, in-progress, done): ")

        task["status"] = new_status
        task["updatedAt"] = time.ctime()
        save_json()
        print("task succesfully updated ....")
        return True
    print("task not found....")
    return False


def delete_task(description: str) -> bool:
    '''
    function to delete a task
    Args :
    description (str) : string of a task that become a query
    Return : bool : True if task deleted else False
    '''
    task = get_id_task(description)
    if task is not None:
        data.remove(task)
        save_json()
        print(f"task : {task["description"]} succesfully deleted ....")
        time.sleep(1.5)
        return True
    print("task not found....")
    return False


def menu():
    '''
    function to show menu
    '''
    print(f"\n{'='*20}Task Tracker Menu{'='*20}")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Exit \n")


if __name__ == "__main__":
    open_file()
    # show CLI menu
    menu()
    user_input = input("Enter your choice (1-5): ")
    while user_input != "5":
        match user_input:
            case "1":
                desc = input("Enter task description: ")
                add_task(desc)

            case "2":
                get_all_tasks()
            case "3":
                desc = input("Enter task description / task id to update: ")
                update_task(desc)
            case "4":
                desc = input("Enter task description / task id to delete: ")
                delete_task(desc)
            case _:
                print("Invalid choice. Please enter a number between 1 and 5.")
        time.sleep(1)
        menu()
        user_input = input("Enter your choice (1-5): ")

    print(f"\n{'='*20}thanks for using Task Tracker...{'='*20}\n")
