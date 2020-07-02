from todo_module import TodoApp
from todo_module import Task

if __name__ == "__main__":
    app = TodoApp()
    
    if app.check_name():
        app.show_task_list
    else:
        print("Invalid User")

    app.get_command()
    

