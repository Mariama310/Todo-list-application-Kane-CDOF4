from tasks import TaskList

def print_menu():
    print("\nTodo List Application\n")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Mark Task as Completed")
    print("4. View Tasks")
    print("5. Exit\n")

def main():
    task_list = TaskList()
    
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            task_list.add_task(description)
            print("Task added successfully!")
        elif choice == '2':
            index = int(input("Enter task index to delete: "))
            task_list.delete_task(index)
            print("Task deleted successfully!")
        elif choice == '3':
            index = int(input("Enter task index to mark as completed: "))
            task_list.complete_task(index)
            print("Task marked as completed!")
        elif choice == '4':
            tasks = task_list.get_task_list()
            if not tasks:
                print("No tasks yet!")
            else:
                print("Task List:")
                for i, task in enumerate(tasks):
                    status = "Completed" if task.completed else "Pending"
                    print(f"{i}. {task.description} - {status}")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
