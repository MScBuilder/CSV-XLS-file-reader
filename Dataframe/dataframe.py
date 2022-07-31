from asyncio.windows_events import NULL
from tkinter import filedialog
import pandas as pd
# from sklearn import datasets

class Dataframe():
    '''dataframe class'''
    def __init__(self):
        pass  
        
    def open_dataset(self):
        '''choose dataset module'''
        filetypes = (
            ('comma separated values', '*.csv'),
            ('spreadsheet files', '*.xls'),
            ('All files', '*.*'))
        file_name = filedialog.askopenfilename(title='Open a file', initialdir='.', filetype=filetypes)
        print(file_name)
        if file_name:
            try:
                file_type = file_name[-4:]
                if file_type == '.csv':
                   df = pd.read_csv(file_name)
                   print("It's CSV file")
                elif file_type == '.xls':
                  df = pd.read_excel(file_name)
                  print("It's EXCEL file")
                elif file_type == 'xlsx':
                  df = pd.read_excel(file_name)
                  print("It's EXCEL file")
                else:
                    print("Can't do")
                    
                print(file_type)
                return file_name, df
            
            except ValueError:
                print('Somethings go wrong')
                return NULL
