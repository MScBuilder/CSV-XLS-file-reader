import tkinter as tk
import Dataframe.dataframe as df



def new_button(frame, text, command):
    '''creates new button with specific description and command'''
    button = tk.Button(frame, text=text, command=command)
    return button

def new_text_field(frame, width, height ):
    '''creates new text field with given dimensions'''
    text_field = tk.Text(frame, width=width, height=height )
    return text_field


#def choose_datset_button(frame):
    '''creates button with function of chooseing dataset'''
    datset_button = tk.Button(frame, text='Choose Dataset', command=df.Dataframe().choose_dataset)
    return datset_button

#def quit_frame_button(frame):
    '''creates button that close current frame'''
    quit_button = tk.Button(frame, text='Quit', command=frame.destroy)
    return quit_button

