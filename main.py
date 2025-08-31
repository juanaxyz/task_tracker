'''
time used to take current time
'''
import time

data = [
    {
        "id": 1,
        "description": "take a bath",
        "status": "todo",
        "createdAt": "Sun Aug 15 14:18:29 2025",
        "updatedAt": "Sun Aug 15 14:18:29 2025",
    },
    {
        "id": 2,
        "description": "take a bom",
        "status": "todo",
        "createdAt": "Sun Aug 1 13:18:29 2025",
        "updatedAt": "Sun Aug 1 13:18:29 2025",
    }
]


def add_task(description: str) -> None:
    '''
    function to add task to the list
    Args :
    description (str): description of the task
    Returns : None
    '''
    last_id = data[-1]["id"]

    data.append(
        {
            "id": last_id + 1,
            "description": description,
            "status": "todo",
            "createdAt": time.ctime(),
            "updatedAt": time.ctime(),
        }
    )


def get_all_tasks() -> list:
    '''
    function to print all task based on each status
    Args : None
    Returns : list of all tasks
    '''
    if data:
        for element in data:
            match element["status"]:
                case "todo":
                    print(element)
                case "in-progress":
                    print(element)
                case "done":
                    print(element)
        return data
    return []


def get_id_task(description: str):
    '''
    function to get task by id
    Args :
    description (str): description of the task
    Returns : task if found else None
    '''
    for element in data:
        if element["description"] == description:
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
        print("task succesfully updated ....")
        time.sleep(1.5)
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
        print(f"task : {task["description"]} succesfully deleted ....")
        time.sleep(1.5)
        return True
    print("task not found....")
    return False


if __name__ == "__main__":
    # print(data[-1]["id"])
    # add_task("do homework")
    # get_all_tasks()
    # print(data[-1])
    # update_task("take a ")
    get_all_tasks()
    delete_task("take a bom")
    get_all_tasks()
