# app.py
from scripts.chat import chat
from tkinter import *
import customtkinter as ctk
from PIL import ImageTk, Image
import os
import utilities.utils as utils
import scripts.response as response

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
    
    def submit_chat(self):
        # Get user input
        user_input = self.chat_entry.get()

        # Get bot response
        bot_response = response.get_response(user_input=user_input)
        self.text_main_display.delete('1.0', END)
        self.text_main_display.insert(END, bot_response)

        # Set image
        self.img_main_display = Image.open(utils.get_absolute_path(utils.PLANET_IMAGE)).resize((480, 475))
        self.img_main_display = ImageTk.PhotoImage(self.img_main_display)
        self.lbl_image_holder.config(image=self.img_main_display)
        self.lbl_image_holder.image = self.img_main_display 
        self.window.mainloop()

        # Update chat history
        self.chat_instance.update_chat_history({'user': user_input, 'bot': bot_response})
    
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
        parent.rowconfigure(0, weight = 1)
        parent.rowconfigure(1, weight = 1)
        parent.rowconfigure(2, weight = 1)

        # Left Output Display
        self.text_main_display = Text(parent, height=29, width=60, padx=5, pady=5)
        self.text_main_display.grid(column=0, row=0,sticky='new')

        # Right Output Display
        self.img_main_display = Image.open(utils.get_absolute_path(utils.PLANET_IMAGE)).resize((480, 475))
        self.img_main_display = ImageTk.PhotoImage(self.img_main_display)

        self.lbl_image_holder = Label(parent, image=self.img_main_display, width=480, bg='#EDE8EA')
        self.lbl_image_holder.image = self.img_main_display  # Keep a reference to avoid garbage collection
        self.lbl_image_holder.grid(column=1, row=0, sticky='new')

        # Chat entry
        self.chat_entry = ctk.CTkEntry(parent, placeholder_text="Type your question here...", width=400)
        self.chat_entry.grid(column=0, row=1, columnspan=2, padx=5, pady=5)

        # Chat entry button
        self.chat_button = ctk.CTkButton(parent, text="Send", command=self.submit_chat)
        self.chat_button.grid(column=0, row=2, padx=5, pady=5, sticky='e')

        # Chat clear button
        self.chat_clear_button = ctk.CTkButton(parent, text="Clear")
        self.chat_clear_button.grid(column=1, row=2, padx=5, pady=5, sticky='w')



        pass
    
    def init_app(self):
        """Initialises the app instance and sets up the chat.

        .. impl::
            :id: APP_INIT_APP

        """
        self.chat_instance = chat()
        self.image = utils.PLANET_IMAGE
        self.window = ctk.CTk(fg_color='#EAE8ED')
        self.window.title("Planetarium Chatbot")
        self.window.geometry("960x600")

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

    