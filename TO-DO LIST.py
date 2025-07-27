import tkinter as tk
import json
import os

FILE_NAME = "task_data.json" 

def read_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def write_tasks(task_data):
    with open(FILE_NAME, "w") as f:
        json.dump(task_data, f, indent=4)

def refresh_tasks():
    task_listbox.delete(0, tk.END)
    for task in task_items:
        symbol = "✔" if task["completed"] else "✘"
        task_listbox.insert(tk.END, f"{symbol} {task['title']}")

def add_new_task():
    task_text = task_input.get().strip()
    if task_text:
        task_items.append({"title": task_text, "completed": False})
        write_tasks(task_items)
        task_input.delete(0, tk.END)
        refresh_tasks()

def mark_done():
    selected = task_listbox.curselection()
    if selected:
        task_items[selected[0]]["completed"] = True
        write_tasks(task_items)
        refresh_tasks()

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_items.pop(selected[0])
        write_tasks(task_items)
        refresh_tasks()

task_items = read_tasks()

root = tk.Tk()
root.title("TO-DO LIST")

task_input = tk.Entry(root, width=44)
task_input.pack(pady=8)

btn_add = tk.Button(root, text="Add Task", command=add_new_task)
btn_add.pack()

task_listbox = tk.Listbox(root, width=54)
task_listbox.pack(pady=10)

btn_complete = tk.Button(root, text="Mark as Done", command=mark_done)
btn_complete.pack()

btn_delete = tk.Button(root, text="Delete Task", command=delete_task)
btn_delete.pack()

refresh_tasks()
root.mainloop()
