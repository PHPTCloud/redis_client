from tkinter import *
from tkinter.ttk import Separator
from PIL import Image, ImageTk
from tkinter import font
from src.styles import Styles

class MainWindow:

    def __init__(self, app = None, master = None) -> None:
        self.app = app
        self.master = master
        self.redis_icon = None
        self.styles = Styles()

    def init(self):
        # Main logo
        icon_size_x = 48
        icon_size_y = 48
        global redis_icon
        image = Image.open(self.styles.icon_path)
        image = image.resize((icon_size_x, icon_size_y), Image.ANTIALIAS)
        redis_icon = ImageTk.PhotoImage(image)
        image_sprite = Label(self.master, width=icon_size_x, height=icon_size_y, image=redis_icon, background=self.styles.main_bg)
        image_sprite.grid(column=0, row=0, padx=5, pady=20)
        
        # Main title
        title_font = font.Font(size=16, weight='bold')
        title = Label(self.master, text="Redis client", fg="#fff", bg=self.styles.main_bg, font=title_font)
        title.grid(column=1, row=0, sticky=(N, S, W))
        
        functions_buttons_frame = Frame(self.master, bg=self.styles.main_bg, pady=20, padx=20)
        functions_buttons_frame.grid(column=0, row=1)
        # Create connections button
        self.create_connection_button = Button(functions_buttons_frame, text="Create connection", command=self.create_connection_click)
        self.create_connection_button.grid(column=0, row=1)
        
    def create_connection_click(self):
        window = Toplevel(self.master)
        

