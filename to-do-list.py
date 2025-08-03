import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append({"task": task, "done": False})
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task():
    selected = listbox.curselection()
    if selected:
        idx = selected[0]
        tasks.pop(idx)
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

def update_task():
    selected = listbox.curselection()
    new_task = entry.get()
    if selected and new_task:
        idx = selected[0]
        tasks[idx]["task"] = new_task
        update_listbox()
        entry.delete(0, tk.END)
    elif not selected:
        messagebox.showwarning("Selection Error", "Please select a task to update.")
    else:
        messagebox.showwarning("Input Error", "Please enter the new task.")

def mark_done():
    selected = listbox.curselection()
    if selected:
        idx = selected[0]
        tasks[idx]["done"] = not tasks[idx]["done"]
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

def update_listbox():
    listbox.delete(0, tk.END)
    for t in tasks:
        status = " [Done] " if t["done"] else " [To do] "
        listbox.insert(tk.END, t["task"] + status)

root = tk.Tk()
root.title("To-Do-List")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

listbox = tk.Listbox(frame, width=20, height=10, font=("Display", 14))
listbox.pack(side=tk.TOP, pady=5)

entry = tk.Entry(frame, width=10, font=("Display", 12))
entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(frame, text="Add Task", width=10, command=add_task)
update_button = tk.Button(root, text="Update Selected Task", width=20, command=update_task)
done_button = tk.Button(root, text="Mark/Unmark as Done", width=20, command=mark_done)
remove_button = tk.Button(root, text="Remove Selected Task", width=20, command=remove_task)

add_button.pack(side=tk.LEFT, padx=20)
update_button.pack(pady=2)
done_button.pack(pady=2)
remove_button.pack(pady=2)

root.mainloop()