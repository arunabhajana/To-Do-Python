import tkinter as tk
from tkinter import ttk, messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to remove this task?")
        if confirmation:
            listbox.delete(selected_task_index)

root = tk.Tk()
root.title("To-Do List")

icon_path = "to-do.png"
root.iconphoto(True, tk.PhotoImage(file=icon_path))

style = ttk.Style()
style.configure("TEntry", padding=5, relief="flat", borderwidth=4)
entry = ttk.Entry(root, font=('Arial', 14), style="TEntry")
entry.pack(pady=10, padx=10, fill=tk.X)

add_button = tk.Button(root, text="Add Task", command=add_task, font=('Arial', 12))
add_button.pack(pady=5)
remove_button = tk.Button(root, text="Remove Task", command=remove_task, font=('Arial', 12))
remove_button.pack(pady=5)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set, font=('Arial', 12))
listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

scrollbar.config(command=listbox.yview)

listbox.config(borderwidth=4, relief="flat")

root.mainloop()
