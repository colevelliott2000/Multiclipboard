import sys
import tkinter as tk
import os

import functions
import gui


if __name__ == '__main__':
    if len(sys.argv) == 2:
        command = sys.argv[1]
        data = functions.load_clipboard_data()

        if command == 'display':
            functions.display_clipboard_data(data)
        elif command == 'save':
            key = input('Enter a key to save your clipboard under: ')
            functions.save_clipboard_data(data, key)
        elif command == 'load':
            key = input('Input key to load from: ')
            functions.load_clipboard(data, key)
        elif command == 'delete':
            key = input('Input a key to delete from: ')
            functions.delete_clipboard_data(data, key)
        else:
            print('Enter a valid command: display, save, load, delete')

    else:
        
        root = tk.Tk()
        gui.App(root).pack(side='top', fill='both', expand=True)

        root.geometry("1920x1080")
        root.configure(bg = "#FFFFFF")
        
        root.mainloop()
