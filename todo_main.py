from todo_module import TodoApp
from todo_module import Task

if __name__ == "__main__":
    app = TodoApp()
    
    while True:
        if app.check_name():
            app.show_task_list
            app.get_command()
            break
        else:
            print("Invalid User")

    

