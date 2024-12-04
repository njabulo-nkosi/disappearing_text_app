import time
from tkinter import *
from tkinter import filedialog

TIME = 0.15 * 60
# INACTIVITY_LIMIT = 5


class DisappearingText:

    def __init__(self, window):
        self.window = window
        self.time_remaining = TIME
        self.last_typing_time = time.time()
        self.typing_active = False

        self.setup_title()
        self.create_window()
        self.setup_text_box()
        self.setup_buttons()

    def create_window(self):
        self.window.title('Disappearing Text App')
        self.window.config(padx=50, pady=50, bg='black')

    def setup_title(self):
        title = Label(self.window,
                      text='Disappearing Text App',
                      font=('Courier', 30, 'bold'),
                      bg='black',
                      fg='white')
        title.grid(column=1, row=0)  #
        sub_text = Label(self.window,
                         text='The ultimate solution to writer’s block\n Start now.',
                         font=('Courier', 20, 'bold'),
                         bg='black',
                         fg='white')
        sub_text.config(pady=20)
        sub_text.grid(column=1, row=1)  #

    def setup_text_box(self):
        self.text_widget = Text(self.window, font=("Courier", 10), width=50, height=15, state=DISABLED)  # h=20
        self.text_widget.grid(column=1, row=3, pady=20)
        self.text_widget.insert('insert', '')
        self.text_widget.bind('<<Modified>>', self.reset_typing_timer)

    def setup_buttons(self):
        self.start_button = Button(self.window, text='Start Writing', font=('Courier', 10), command=self.start_program)
        self.start_button.grid(column=1, row=4)

        self.save_button = Button(self.window, text='Save file', font=('Courier', 10), command=self.save_text)
        self.save_button.grid(column=1, row=5, pady=20)

    def start_program(self):
        self.text_widget.config(state=NORMAL)
        self.text_widget.delete('1.0', END)
        self.last_typing_time = time.time()
        self.typing_active = True
        self.check_inactivity()

    def reset_typing_timer(self, event=None):
        if self.typing_active:
            self.last_typing_time = time.time()
            self.text_widget.edit_modified(False)
            self.check_inactivity()

    def check_inactivity(self):
        if self.typing_active:
            current_time = time.time()
            if current_time - self.last_typing_time > TIME:
                self.clear_text()
            else:
                self.window.after(1000, self.check_inactivity)

    def clear_text(self):
        self.text_widget.delete('1.0', END)
        self.last_typing_time = time.time()
        # self.typing_active = False

    def save_text(self):
        text_input = self.text_widget.get('1.0', END)

        if text_input:
            file_path = filedialog.asksaveasfilename(defaultextension='.txt',
                                                     filetypes=[("Text files", "*.txt"),
                                                                ("All files", "*.*")])
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(text_input)
                    print(f'File saved to {file_path}')


