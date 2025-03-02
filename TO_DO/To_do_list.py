import os

def show_menu():
    os.system('cls')
    print("To-Do List Menu:")
    print("1. Add a Task")
    print("2. Remove a Task")
    print("3. View Tasks")
    print("4. Mark Task as Completed")
    print("5. Exit")

def add_task(tasks):
    t=input("Enter name of the task to add: ")
    tasks[t]='Incomplete'
    print(f"Task {t} added to list.")

def view_task(tasks):
    if not tasks:
        print("Your To-Do list empty")
    else:
        print("\nYour To-Do List:")
        for i,task in enumerate(tasks):
            print(f"{i+1}.  {task}: " + tasks[task])

def mark_comlete(tasks):
    if not tasks:
        print("Your To-Do list empty")
    else:
        t=input("Please enter the name of the task: ")
        if t not in tasks:
            print("Invalid task name")
        else:
            tasks[t]="Complete"
            print(f"Task {t} marked as complete")


def remove_task(tasks):
    t=input("Enter name of the task: ")
    if t not in tasks:
        print(f"Task {t} not present")
    else:
        tasks.pop(t)
        print(f"Task {t} removed from To-Do list" ) 

def main():
    tasks={}    #Initializing dicts for task
    while True:
        show_menu()
        option=int(input("Enter options for tasks: "))
        match option:
            case 1:
                os.system('cls')
                add_task(tasks)
                e=input("\n\nPlese enter to continue...")
            case 2:
                os.system('cls')
                remove_task(tasks)
                e=input("\n\nPlese enter to continue...")
            case 3:
                os.system('cls')
                view_task(tasks)
                e=input("\n\nPlese enter to continue...")
            case 4:
                os.system('cls')
                mark_comlete(tasks)
                e=input("\n\nPlese enter to continue...")
            case 5:
                break

if __name__=="__main__":
    main()