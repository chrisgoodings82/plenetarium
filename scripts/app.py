# app.py
from scripts.chat import chat
from tkinter import *
import customtkinter as ctk
from PIL import ImageTk, Image
import os
import utilities.utils as utils

# If a Windows machine, import the system accessors
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

class app:

    _instance = None

    def __new__(cls):
        """Creates a singleton instance of the app class
        
        :return: An instance of the class.
        :rtype: app
        """
        if cls._instance is None:
            cls._instance = super(app, cls).__new__(cls)
            cls._instance.init_app()
        return cls._instance
    
    def setup(self, parent):
        """Sets up the application instance and initializes the chat.

        .. impl::
            :id: APP_SETUP

        """
        # Menu
        menubar = Menu(parent)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=parent.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        settingsmenu = Menu(menubar, tearoff=0)
        settingsmenu.add_command(label="Settings")
        menubar.add_cascade(label="Settings", menu=settingsmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About")
        menubar.add_cascade(label="Help", menu=helpmenu)

        parent.config(menu=menubar)

        # Configure the grid
        parent.columnconfigure(0, weight = 1)
        parent.columnconfigure(1, weight = 1)
        parent.columnconfigure(2, weight = 4)
        parent.columnconfigure(3, weight = 6)
        parent.rowconfigure(0, weight = 1)
        parent.rowconfigure(1, weight = 1)

        # Left Output Display
        text_main_display = Text(parent, height=20, width=50, padx=5, pady=5)
        text_main_display.grid(column=0, row=0, columnspan=3)

        # Right Output Display




        pass
    
    def init_app(self):
        """Initialises the app instance and sets up the chat.

        .. impl::
            :id: APP_INIT_APP

        """
        self.chat_instance = chat()
        self.window = ctk.CTk(fg_color='#EAE8ED')
        self.window.title("Planetarium Chatbot")
        self.window.geometry("1000x600")

        # https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
        # https://www.youtube.com/watch?v=36PpT4Z22Os&t=43s
        # A Windows specific feature that allows the title bar, window border, and title bar font colours to be set
        # For Mac and Linux, they will use default colours and styles as they won't have access to windll, reuslting in 
        # an exception being raised.
        try:
            HWND = windll.user32.GetParent(self.window.winfo_id())
            windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(utils.ORANGE)), sizeof(c_int))                    # Title Bar
            windll.dwmapi.DwmSetWindowAttribute(HWND, 34, byref(c_int(utils.ORANGE)), sizeof(c_int))                    # Window Border
            windll.dwmapi.DwmSetWindowAttribute(HWND, 36, byref(c_int(utils.BLACK)), sizeof(c_int))                     # Title Bar Text Colour
        except:
            pass

        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        ROOT_DIR = ROOT_DIR.replace('scripts', 'data')
        self.window.iconbitmap(utils.get_absolute_path('/data/images/icons/favicon.ico'))

        self.setup(self.window)
        self.window.mainloop()

    