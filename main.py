from functools import partial
import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from PIL import Image, ImageTk

from constants import BG_COLOR, HEADINGFONT, MENUFONT, COLUMN_PER_ROW
from utils import flatten_list
import ArbeitsAnweisungen as data

button_img = {}

def exit():
    root.destroy()

def clear_widgets(current_frame):
    for frame in frames:
        if current_frame!=frame:
            frame.grid(row=0, column=0, sticky="news")
            for widget in frame.winfo_children():
                widget.destroy()

def get_image(name, base_width=150):
    image=Image.open("./assets/"+name)
    # Resize the image in the given (width, height)
    wpercent = (base_width / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(wpercent)))
    image = image.resize((base_width, hsize), Image.Resampling.LANCZOS)
    # Conver the image in TkImage
    my_img=ImageTk.PhotoImage(image)
    return my_img

def append_logo(frame):
    try:
        image = Image.open("./assets/logo.png").resize((300,200))
        logo_image = ImageTk.PhotoImage(image)
        logo_widget = tk.Label(frame,image=logo_image, bg=BG_COLOR)
        logo_widget.image = logo_image
        logo_widget.pack()
    except:
        print("WARNING:", "Logo doesn't exists!")

def init_frame(frame, logo=None):
    clear_widgets(frame)
    frame.tkraise()
    frame.pack_propagate(False)

    if logo!=None:
        append_logo(frame)

    return frame
    
def load_main_frame():
    frame=init_frame(main_frame, "Logo")
        
    tk.Label(frame, text="Ready for development",
                bg=BG_COLOR, fg='white', font=(MENUFONT, 14)).pack()

    buttonframe = tk.Frame(frame, background=BG_COLOR)
    buttonframe.pack()
    count=row=col=0
    for anweisung in data.anweisungen:
        print(anweisung, anweisung[0], anweisung[1][0],anweisung[1][1])
        print("Row/Column:", row, "/", col)
        button_img[anweisung[0]]=get_image(anweisung[1][1])
        button = tk.Button(buttonframe, text=anweisung[1][0], image=button_img[anweisung[0]], font=(HEADINGFONT, 20),
            bg="#28393a", fg='white', 
            cursor="hand2", 
            activebackground="#badee2", activeforeground="black",
            command=partial(load_detail_frame, anweisung[0]),
            width=150, height=150
            )
        button.grid(row=row, column=col, padx=5, pady=5)
        button.grid_rowconfigure(col, weight=1)
        count += 1
        col += 1
        if count%COLUMN_PER_ROW == 0:
            row += 1
            col = 0

    tk.Button(frame, text="EXIT", font=(HEADINGFONT, 20), 
            bg="#28393a", fg='white', cursor="hand2", 
            activebackground="#badee2", activeforeground="black",
            command=lambda:exit()).pack(pady=20)

def load_detail_frame(id):
    frame=init_frame(detail_frame)

    anweisung=None
    for item in data.anweisungen:
        if item[0]==id:
            anweisung=item[1]

    datatext = ""
    for info in (flatten_list(anweisung)):
        if info==None:
            datatext += "\n"
        else:
            datatext += str(info) + "\n"

    print(datatext)
    tk.Label(frame, text=datatext,
                bg=BG_COLOR, fg='white', font=(MENUFONT, 14)).pack()

    tk.Button(frame, text="BACK", font=(HEADINGFONT, 20), 
            bg="#28393a", fg='white', cursor="hand2", 
            activebackground="#badee2", activeforeground="black",
            command=lambda:load_main_frame()).pack(pady=20)

def load_config_frame():
    pass

def load_config_main_frame():
    pass

def load_config_detail_frame():
    pass

# initiallize app
root = tk.Tk()
root.title("Arbeits Anweisungen")
root.geometry("1024x768")
root.resizable(width=False, height=False)

frames=[]
main_frame = tk.Frame(root, width=1024, height=768, bg=BG_COLOR)
frames.append(main_frame)
detail_frame = tk.Frame(root, bg=BG_COLOR)
frames.append(detail_frame)
config_frame = tk.Frame(root, bg=BG_COLOR)
frames.append(config_frame)
config_main_frame = tk.Frame(root, bg=BG_COLOR)
frames.append(config_main_frame)
config_detail_frame = tk.Frame(root, bg=BG_COLOR)
frames.append(config_detail_frame)

for frame in frames:
    frame.grid(row=0, column=0, sticky="news")

load_main_frame()
root.eval("tk::PlaceWindow . center")
print("Screen WxH+w+h:",root.winfo_screenwidth(),"x",root.winfo_screenheight(),"+",root.winfo_reqwidth(),"+",root.winfo_reqheight())

# Run app
root.mainloop()