import tkinter
from tkinter import *
import main
import sys
from tkinter import messagebox
import webbrowser

root = Tk()
logo_icon = tkinter.PhotoImage(file='GUI/logo_icon.png')
root.iconphoto(False, logo_icon)
root['bg'] = '#2b3136'
root.geometry('600x750+650+150')
root.title('Computer')
root.resizable(False, False)

#HEADER
header = Canvas(root, bg='#282e33', width=600, height=83, highlightthickness=0)
header.create_image(30, 0, anchor=NW, image=logo_icon)
header.create_text(110, 15, anchor=NW, text='Computer', font=('Gotham Narrow Thin', 23), fill='white')
header.create_text(110, 50, anchor=NW, text='v0.9.1', font=('Gotham Narrow Thin', 13), fill='white')
settings_image = tkinter.PhotoImage(file='GUI/setting_button.png')
commands_image = tkinter.PhotoImage(file='GUI/commands_button.png')

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        sys.exit()

root.protocol("WM_DELETE_WINDOW", on_closing)


def command_window():
    webbrowser.open('https://telegra.ph/Komandy-Golosovogo-assistenta-Computer-02-14')

def open_github():
    webbrowser.open('https://github.com/Darvin18/Computer-voice_assistent')


button_settings = tkinter.Button(root, image=settings_image, bg='#2b3136', activebackground='#2b3136', bd=0)
header.create_window(350, 42, window=button_settings)
button_commands = tkinter.Button(root, image=commands_image, bg='#2b3136', activebackground='#2b3136', bd=0, command=command_window)
header.create_window(490, 42, window=button_commands)

header.pack()

#Кнопка включения выключения
global is_on
is_on = True

def switch():
    global is_on
    if is_on:
        microphone_button.config(image=on_button)
        is_on = False
        main.button_clicked()
    else:
        microphone_button.config(image=off_button)
        is_on = True

#MAIN_BUTTON
on_button = tkinter.PhotoImage(file='GUI/on_button.png')
off_button = tkinter.PhotoImage(file='GUI/off_button.png')
microphone_button = tkinter.Button(root, image=off_button, bg='#2b3136', activebackground='#2b3136', bd=0, command=switch)
microphone_button.pack()

#MINI_BUTTON
img_button_settings2 = tkinter.PhotoImage(file='GUI/setting_button2.png')
button_settings2 = tkinter.Button(root, image=img_button_settings2, height=80, width=240, bg='#2b3136', activebackground='#2b3136', bd=0)
button_settings2.pack()
button_settings2.place(relx=0.060, rely=0.765)

img_button_commands2 = tkinter.PhotoImage(file='GUI/commands_button2.png')
commands_settings2 = tkinter.Button(root, image=img_button_commands2, height=80, width=240, bg='#2b3136', activebackground='#2b3136',
                                    bd=0, command=command_window)
commands_settings2.pack()
commands_settings2.place(relx=0.50, rely=0.76)

#BOTTOM
img_github = tkinter.PhotoImage(file='GUI/Github.png')
github_button = tkinter.Button(root, image=img_github, height=30, bg='#2b3136', activebackground='#2b3136', bd=0,
                               command=open_github)
github_button.pack()
github_button.place(relx=0.3, rely=0.92)




root.mainloop()