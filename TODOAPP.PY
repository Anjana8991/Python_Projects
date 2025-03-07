import os 
TASKS_FILE= "tasks.txt"
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE,"r") as file:
            return [line.strip() for line in file.readlines()]
    return []
def save_tasks(tasks):
    with open(TASKS_FILE,"w") as file:
        for task in tasks:
            file.write(task + "\n")
            
def display_tasks(tasks):
    if not tasks:
        print("No tasks available")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks,1):
            task_details = task.split(",")
            print(f"{i}.{task_details[0]} (priority: {task_details[1]})" )
            
#Main function
def todo_list():
    #print("Starting To-Do List App...")
    tasks = load_tasks()
    while True:
        print("\nTo-Do List App")
        print("1. Add Task") 
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Save & Exit")
        choice = input("Enter your choice:")  
        if choice =="1":
            task = input("Enter task:")
            priority = input("Enter priority (High/Medium/Low): ").capitalize()
            if priority not in["High","Medium","Low"]:
                print("Invalid priority! Defaulting to 'Medium' .")
                priority = "Medium"
            tasks.append(f" {task},{priority}")
            print(f"'{task}'(priority: {priority} )added to the list.")
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            display_tasks(tasks)
            try:
                task_num = int(input("Enter the task number to remove:")) - 1
                if 0 <= task_num<len(tasks):
                    removed_task = tasks.pop(task_num)
                    print(f"Removed:{removed_task}")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Exiting.....")
            break
        else:
            print("Invalid choice !Please enter  a number from 1 to 4.")
            #Run the To-Do List App
todo_list()
                        