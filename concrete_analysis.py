import tkinter as tk
from tkinter import ttk
import numpy

from Dataframe.dataframe import Dataframe

def open_file():
    file = Dataframe.open_dataset(Dataframe)
    file_name = file[0]
    data_frame = file[1]
    inf_label.config(text=file_name)
    clear_tree()
    tree_view["columns"] = list(data_frame)
    tree_view["show"] = "headings"

    for column in tree_view["columns"]:
        tree_view.heading(column, text=column)
        
    df_rows = data_frame.to_numpy().tolist()
    for row in df_rows:
        tree_view.insert("", "end", values=row)
    tree_view.pack()
    
def clear_tree():
    tree_view.delete(*tree_view.get_children())

root = tk.Tk()
root.geometry('600x600')
root.title('Dataset')

#Creating main frame
frame_1 = tk.Frame(root)
frame_1.pack(pady=5)

#Creating TreeView
tree_view = ttk.Treeview(frame_1)

#Add menu
menu_1 = tk.Menu(root)
root.config(menu=menu_1)

#Add menu dropdown
file_menu = tk.Menu(menu_1, tearoff=False)
menu_1.add_cascade(label="Spreadsheets", menu=file_menu)
file_menu.add_command(label='Open', command=open_file)

#Adding information label
inf_label = tk.Label(root, text='File path and name')
inf_label.pack(pady=30)

root.mainloop()