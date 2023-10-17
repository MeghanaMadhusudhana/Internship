def display_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Add Task Function
def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Added: {task}")

# Remove Task Function
def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Removed: {removed_task}")
    else:
        print("Invalid task index. No task removed.")

# Step 2: Implement the Main Function

def main():
    todo_list = []
    while True:
        print("\nMenu:")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_list(todo_list)
        elif choice == "2":
            task = input("Enter a new task: ")
            add_task(todo_list, task)
        elif choice == "3":
            task_index = int(input("Enter the task index to remove: "))
            remove_task(todo_list, task_index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

# Step 3: Testing (optional, but highly recommended)

# Display To-Do List
# Test the display_list function by calling it with a sample list of tasks.
# add_task(["Task 1", "Task 2", "Task 3"])

# Add Task
# Test the add_task function by calling it with a sample task and check if it gets added to the list.
# add_task([], "Sample Task")

# Remove Task
# Test the remove_task function by calling it with a sample task index and check if the task is removed correctly.
# remove_task(["Task 1", "Task 2", "Task 3"], 2)

# Step 4: Run and Debug (Test Various Scenarios and Handle Errors and Edge Cases)
# Run the program and test it with different scenarios to ensure it works as expected and handles errors gracefully.
