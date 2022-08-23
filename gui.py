'''
Screen Recorder GUI
by Donya Ghavami
'''

import pyscreenrec
import pyautogui
from pathlib import Path
from tkinter import StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage , messagebox , filedialog


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



window = Tk()
window.title("Screen Recorder")
window.geometry("400x210")
window.configure(bg = "#FFFFFF")
window.iconbitmap("Screen_Recorder.ico")

def start_the_recording(): 

    files = file_name.get()
    recording.start_recording(str(files + ".mp4") , 5)

    messagebox.showinfo("Information" , "You start the recording ! ")


def pause_the_recording():

    recording.pause_recording()

    messagebox.showinfo("Information" , "You pause the recording ! ")


def resume_the_recording():

    recording.resume_recording()

    messagebox.showinfo("Information" , "You resume the recording ! ")


def stop_the_recording(): 

    recording.stop_recording()

    messagebox.askquestion("Information" ,  "Do you want to finish the recording ? ")


recording = pyscreenrec.ScreenRecorder()
file_name = StringVar()
file_name.set("")


def screen_shot():

    shot = pyautogui.screenshot()

    file_path = filedialog.asksaveasfilename(defaultextension='.png')
    shot.save(file_path)


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 210,
    width = 400,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=screen_shot,
    relief="flat"
)
button_1.place(
    x=15.0,
    y=120.0,
    width=68.0,
    height=55.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=resume_the_recording,
    relief="flat"
)
button_2.place(
    x=90.0,
    y=120.0,
    width=68.0,
    height=57.739585876464844
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=stop_the_recording,
    relief="flat"
)
button_3.place(
    x=167.0,
    y=120.0,
    width=68.0,
    height=55.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=pause_the_recording,
    relief="flat"
)
button_4.place(
    x=244.0,
    y=120.0,
    width=68.0,
    height=55.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=start_the_recording,
    relief="flat"
)
button_5.place(
    x=320.0,
    y=123.0,
    width=68.0,
    height=55.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    257.5,
    82.0,
    image=entry_image_1
)
entry_1 = Entry(
    textvariable = file_name,
    bd=0,
    bg="#C1D5E3",
    highlightthickness=0
)
entry_1.place(
    x=194.0,
    y=59.0,
    width=127.0,
    height=44.0
)

canvas.create_text(
    41.0,
    72.0,
    anchor="nw",
    text="Record Name : ",
    fill="#3B2D63",
    font=("Inter Medium", 16 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    186.0,
    39.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#1625AB",
    highlightthickness=0
)
entry_2.place(
    x=65.5,
    y=38.0,
    width=241.0,
    height=1.0
)

canvas.create_text(
    109.0,
    11.0,
    anchor="nw",
    text="Screen Recorder ",
    fill="#121B67",
    font=("Inter", 20 * -1)
)

window.resizable(False, False)
window.mainloop()
