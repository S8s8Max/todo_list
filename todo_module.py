#!/usr/bin/env/python3
import re
import sys

class TodoApp:
    task_list = {}

    def __init__(self):
        #use regex for that the user can type their name either in upper case or lower case.
        self.user = "Kippei" 


    def check_name(self):
        name = str(input("Name: "))

        if name != self.user:
            return False
        return True
    
    
    # wondering if the all functions below have to be in Task class.
    # Because these are the method of Tasks.
    def add_task(self):
        print("Add your task. Line is devided by '|' into Task, Date and Tag.\n: ", end="")
        
        line = sys.stdin.readline().split("|")
        todo = Task(line[0], line[1], line[2])

        self.task_list[todo.task] = [todo.date, todo.tag]

        print("Task added !")
        #todo._status()


    def delete_task(self):
        print("Which task do you wanna delete? ")
        
        while True:
            dlt_task = str(input("-Type task name(Press 'q' to quit) : "))

            if dlt_task in self.task_list.keys():
                del self.task_list[dlt_task]
                print("Task deleted.")
            elif dlt_task == "q":
                break
            else:
                print("There are no such a task.")
    

    def edit_task(self):
        print("Which task do you wanna edit?")

        while True:
            edt_task = str(input("-Type task name(Press 'q' to quit) : "))

            if edt_task in self.task_list.keys():
                print("How do you wanna edit?")
                edit_commands = {1:"Change name", 2:"Change date", 3:"Change tag", 4:"quit"}

                while True:
                    edt_cmd_keys = list(edit_commands.keys())
                    edt_cmd_values = list(edit_commands.values())
                    for i in range(len(edit_commands)):
                        print(f"{edt_cmd_keys[i]}. {edt_cmd_values[i]}")

                    edit_number = int(input("-Type a number : "))
                    
                    if edit_number == 1:
                        new_name = str(input("-Type a new name : "))
                        self.task_list[new_name] = self.task_list.pop(edt_task)

                    elif edit_number == 2:
                        new_date = str(input("-Type a new date : "))
                        original_value = list(self.task_list[edt_task])
                        original_tag = original_value[1]
                        self.task_list[edt_task] = [new_date, original_tag]

                    elif edit_number == 3:
                        new_tag = str(input("-Type a new tag : "))
                        original_value = list(self.task_list[edt_task])
                        original_date = original_value[0]
                        self.task_list[edt_task] = [original_date, new_tag]

                    elif edit_number == 4:
                        break
                    else:
                        print("Invalid number")

            elif edt_task == "q":
                break
            else:
                print("There are no such a task.")
    

    def show_task_list(self):
        task_names = list(self.task_list.keys())
        task_info = list(self.task_list.values())
        print("-----------[Task List]-----------")
        for i in range(len(task_names)):
            print(f"{i+1} | Name : {task_names[i]} | Date : {task_info[i][0]} | Tag : {task_info[i][1]}")


    def get_command(self):
        while True:
            print("----.-----.-----.-----.-----.----")
            print("Commands - \n"
                + "1. Add Task, "
                + "2. Delete Task\n"
                + "3. Edit Task, "
                + "4. Exit")
            print("----.-----.-----.-----.-----.----")
            command = int(input("-Type a number : "))
            print("")

            if command == 1:
                self.add_task()
            elif command == 2:
                if len(self.task_list) == 0:
                    print("There are no tasks.")
                else:
                    self.show_task_list()
                    self.delete_task()
            elif command == 3:
                if len(self.task_list) == 0:
                    print("There are no tasks.")
                else:
                    self.show_task_list()
                    self.edit_task()
            else:
                print("See you later!")
                break
        
class Task():
    def __init__(self, task, date="-", tag="-"):
        self.task = task
        self.date = date
        self.tag = tag
        self._status = True
    

    # set status to make sure that the task is done or not.
    #def change_status(self):
    #    if self._status:
    #        self._status = False
    #    else:
    #        self._status = True
    

