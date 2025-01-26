import tkinter as tk


root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")


tasks = []


def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_task_list()
    task_entry.delete(0, tk.END)


def delete_task():
    try:
        selected_task_index = task_list.curselection()[0]
        tasks.pop(selected_task_index)
        update_task_list()
    except IndexError:
        pass


def complete_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task = tasks[selected_task_index]
        tasks[selected_task_index] = f"{task} (Completada)"
        update_task_list()
    except IndexError:
        pass


def update_task_list():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)


task_entry = tk.Entry(root, width=30)
add_button = tk.Button(root, text="Agregar tarea", command=add_task)
delete_button = tk.Button(root, text="Eliminar tarea", command=delete_task)
complete_button = tk.Button(root, text="Marcar como completada", command=complete_task)

task_list = tk.Listbox(root, width=40, height=10)


task_entry.pack(pady=10)
add_button.pack(pady=5)
task_list.pack(pady=10)
delete_button.pack(pady=5)
complete_button.pack(pady=5)


root.mainloop()
