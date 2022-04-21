from tkinter import StringVar


class Styles:
    
    main_bg = None
    second_bg = None
    white_color = None
    icon_path = None
    start_window_size_x = None
    start_window_size_y = None
    
    def __init__(self) -> None:
        self.main_bg = "#010409"
        self.second_bg = "#161b22"
        self.white_color = "#c9d1d9"
        self.icon_path = "assets/images/redis_icon.png"
        self.connection_icon_path = "assets/images/connection_icon.png"
        self.start_window_size_x = 720
        self.start_window_size_y = 480