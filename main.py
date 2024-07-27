from tkinter import *

tasks = []
def add_task():
  task_description = entry_task.get()
  if task_description:
    tasks.append(task_description)
    update_task_list()
    entry_task.delete(0, END)  # Clear the entry field after adding
def list_tasks():
  task_list.delete(0, END)  # Clear existing tasks
  for task in tasks:
    task_list.insert(END, task)
def delete_task():
  selected_task_index = task_list.curselection()
  if selected_task_index:
    task_index = selected_task_index[0]  # Get the index of the selected item
    del tasks[task_index]
    update_task_list()
def update_task_list():
  list_tasks()
root = Tk()
root.title('ToDo_App')
entry_frame = Frame(root)
entry_frame.pack(pady=10)
label_task = Label(entry_frame, text="Enter Task:")
label_task.pack(side=LEFT)
entry_task = Entry(entry_frame, width=50)
entry_task.pack(side=LEFT, padx=5)
add_button = Button(entry_frame, text="Add Task", command=add_task)
add_button.pack(side=RIGHT)
task_list_frame = Frame(root)
task_list_frame.pack(pady=10)
label_tasks = Label(task_list_frame, text="Tasks:")
label_tasks.pack()
task_list = Listbox(task_list_frame, width=50)
task_list.pack()
delete_button = Button(task_list_frame, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)
update_task_list()
root.mainloop()
