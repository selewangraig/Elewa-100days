import json
import time
from datetime import datetime

class Task:
    def __init__(self, name, description, estimated_time, priority=0):
        self.name = name
        self.description = description
        self.estimated_time = estimated_time
        self.completed = False
        self.start_time = None
        self.end_time = None
        self.priority = priority

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        self.end_time = time.time()

    def get_elapsed_time(self):
        if self.start_time and self.end_time:
            return round(self.end_time - self.start_time, 2)
        else:
            return 0

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "estimated_time": self.estimated_time,
            "completed": self.completed,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "priority": self.priority
        }

    @classmethod
    def from_dict(cls, task_dict):
        task = cls(task_dict["name"], task_dict["description"], task_dict["estimated_time"])
        task.completed = task_dict["completed"]
        task.start_time = task_dict["start_time"]
        task.end_time = task_dict["end_time"]
        task.priority = task_dict["priority"]
        return task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                task.stop_timer()
                return True
        return False

    def display_tasks(self):
        for task in self.tasks:
            print(f"{task.name} - {task.description} - Estimated Time: {task.estimated_time} - Completed: {task.completed} - Priority: {task.priority}")

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]

    def get_total_time_spent(self):
        return sum(task.get_elapsed_time() for task in self.get_completed_tasks())

    def suggest_task(self):
        incomplete_tasks = [task for task in self.tasks if not task.completed]
        if incomplete_tasks:
            sorted_tasks = sorted(incomplete_tasks, key=lambda x: x.priority, reverse=True)
            return sorted_tasks[0]
        else:
            return None

    def save_tasks_to_file(self, filename):
        with open(filename, "w") as file:
            tasks_data = [task.to_dict() for task in self.tasks]
            json.dump(tasks_data, file)

    def load_tasks_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                tasks_data = json.load(file)
                self.tasks = [Task.from_dict(task_data) for task_data in tasks_data]
        except FileNotFoundError:
            pass

def display_menu():
    print("\n1. Add Task\n2. Start Task Timer\n3. Stop Task Timer\n4. Mark Task as Completed\n5. Display Tasks\n6. Display Reports\n7. Suggest Task\n8. Save and Exit")

def main():
    task_manager = TaskManager()
    task_manager.load_tasks_from_file("tasks.json")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            estimated_time = input("Enter estimated time for the task: ")
            priority = int(input("Enter task priority (1 for highest, 0 for default): "))
            new_task = Task(name, description, estimated_time, priority)
            task_manager.add_task(new_task)
            print("Task added successfully!")

        elif choice == '2':
            task_name = input("Enter the name of the task to start the timer: ")
            for task in task_manager.tasks:
                if task.name == task_name and not task.completed:
                    task.start_timer()
                    print(f"Timer started for task: {task_name}")
                    break
            else:
                print(f"Task not found or already completed: {task_name}")

        elif choice == '3':
            task_name = input("Enter the name of the task to stop the timer: ")
            for task in task_manager.tasks:
                if task.name == task_name and not task.completed and task.start_time:
                    task.stop_timer()
                    print(f"Timer stopped for task: {task_name}")
                    break
            else:
                print(f"Task not found, already completed, or timer not started: {task_name}")

        elif choice == '4':
            task_name = input("Enter the name of the task to mark as completed: ")
            if task_manager.mark_task_completed(task_name):
                print(f"{task_name} marked as completed!")
            else:
                print(f"Task not found or already completed: {task_name}")

        elif choice == '5':
            task_manager.display_tasks()

        elif choice == '6':
            completed_tasks = task_manager.get_completed_tasks()
            total_time_spent = task_manager.get_total_time_spent()

            print(f"\nCompleted Tasks:")
            task_manager.display_tasks()

            print(f"\nTotal Time Spent on Completed Tasks: {total_time_spent} seconds")

        elif choice == '7':
            suggested_task = task_manager.suggest_task()
            if suggested_task:
                print(f"Suggested Task: {suggested_task.name} - Priority: {suggested_task.priority}")
            else:
                print("No tasks to suggest.")

        elif choice == '8':
            task_manager.save_tasks_to_file("tasks.json")
            print("Tasks saved. Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()