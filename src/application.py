from tkinter import *
import tkinter as tk
from src.windows import MainWindow
from src.styles import Styles
from tkinter import font

class Application:
    
    def __init__(self) -> None:
        self.styles = Styles()
   
    def run(self, master=None):
        self.master = master

        icon_path = self.styles.icon_path
        main_bg = self.styles.main_bg
        
        start_window_size_x = self.styles.start_window_size_x
        start_window_size_y = self.styles.start_window_size_y
        
        # get the screen dimension
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - start_window_size_x / 2)
        center_y = int(screen_height / 2 - start_window_size_y / 2)
        start_window_size = f"{start_window_size_x}x{start_window_size_y}+{center_x}+{center_y}"
        
        # Min size for window
        self.master.minsize(600, 300)
        # Initialize window icon
        self.master.tk.call("wm", "iconphoto", self.master._w, tk.PhotoImage(file=icon_path))
        # Initialize window title
        self.master.title("Redis client")
        # Initialize frame settings
        self.master['bg'] = main_bg
        self.master.geometry(start_window_size)
        
        main_window = MainWindow(master=self.master, app=self)
        main_window.init()