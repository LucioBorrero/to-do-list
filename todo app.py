import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App 2.0")

        self.tasks = []
        self.selected_task = None  # Almacena la tarea seleccionada

        # Crear la caja de entrada y el botón para agregar tareas
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        add_button = tk.Button(root, text="Agregar tarea", command=lambda: self.handle_button_click(self.add_task))
        add_button.pack()

        # Crear la lista con barra de desplazamiento
        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
        scrollbar.config(command=self.task_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=scrollbar.set)

        # Etiqueta para mostrar la tarea seleccionada
        self.selected_task_label = tk.Label(root, text="Tarea seleccionada:")
        self.selected_task_label.pack()

        # Botón para eliminar tareas seleccionadas
        remove_button = tk.Button(root, text="Eliminar tarea seleccionada", command=lambda: self.handle_button_click(self.remove_task))
        remove_button.pack()

        # Configurar el evento de doble clic en la lista para marcar la tarea como completada
        self.task_listbox.bind("<Double-Button-1>", lambda event: self.handle_button_click(self.complete_task))

    def handle_button_click(self, func):
        # Manejar clics en botones
        func()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)  # Limpiar la caja de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea válida.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            # Almacenar la tarea seleccionada antes de eliminarla
            self.selected_task = self.tasks[selected_task_index[0]]

            removed_task = self.tasks.pop(selected_task_index[0])
            self.update_task_list()
            messagebox.showinfo("Tarea eliminada", f"{removed_task} ha sido eliminada.")

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.selected_task = self.tasks[selected_task_index[0]]
            task = self.selected_task
            messagebox.showinfo("Tarea completada", f"{task} ha sido marcada como completada.")
            self.remove_task()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

        # Actualizar la etiqueta de la tarea seleccionada
        self.selected_task_label.config(text=f"Tarea seleccionada: {self.selected_task}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
