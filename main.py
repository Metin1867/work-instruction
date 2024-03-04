from functools import partial
import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from PIL import Image, ImageTk
import pyglet
# pip install pyglet

import ArbeitsAnweisungen as data

BG_COLOR = "#3d6466"
HEADINGFONT = "TkHeadingFont"
try:
    pyglet.font.add_file("./TkinterRecipes/fonts/Ubuntu-Bold.ttf")      # replace Heading Font
    HEADINGFONT = "Ubuntu"
except:
    pass
MENUFONT = "TkMenuFont"
try:
    pyglet.font.add_file("./TkinterRecipes/fonts/Shanti-Regular.ttf")   # replace Menu Font
    MENUFONT = "Shanti"
except:
    pass

COLUMN_PER_ROW = 4

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
    """
    base_width= 300
img = Image.open('somepic.jpg')
wpercent = (base_width / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.Resampling.LANCZOS)
img.save('somepic.jpg')
"""
    #image = Image.open("./assets/"+name).resize((100,200))
    #return ImageTk.PhotoImage(image)
    image=Image.open("./assets/"+name)
    # Resize the image in the given (width, height)
    #img=image.resize((150, 150))
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
        button_img[anweisung[0]]=get_image(anweisung[1][1])           # PhotoImage(file="./assets/"+anweisung[1][1])
        #button= tk.Button(frame, image=button_img[anweisung[0]],borderwidth=0)
        #button.pack(pady=30)
        button = tk.Button(buttonframe, text=anweisung[1][0], image=button_img[anweisung[0]], font=(HEADINGFONT, 20),
            bg="#28393a", fg='white', 
            cursor="hand2", 
            activebackground="#badee2", activeforeground="black",
            #command=lambda:load_detail_frame(anweisung[0])
            command=partial(load_detail_frame, anweisung[0]),
            width=150, height=150
            ) #.pack(pady=20)
        button.grid(row=row, column=col, padx=5, pady=5)
        button.grid_rowconfigure(col, weight=1)
        count += 1
        col += 1
        if count%COLUMN_PER_ROW == 0:
            row += 1
            col = 0
        """
        tk.Button(frame, text=anweisung[1][0], image=btn_image, font=(HEADINGFONT, 20),
            bg="#28393a", fg='white', cursor="hand2", 
            activebackground="#badee2", activeforeground="black",
            #command=lambda:load_detail_frame(anweisung[0])
            command=partial(load_detail_frame, anweisung[0])
            ).pack(pady=20)

        ttk.Button(frame, text=anweisung[1][0], image=get_image(anweisung[1][1]),
            cursor="hand2", 
            #command=lambda:load_detail_frame(anweisung[0])
            command=partial(load_detail_frame, anweisung[0])
            ).pack(pady=20)"""

    tk.Button(frame, text="EXIT", font=(HEADINGFONT, 20), 
            bg="#28393a", fg='white', cursor="hand2", 
            activebackground="#badee2", activeforeground="black",
            command=lambda:exit()).pack(pady=20)

def load_detail_frame(id):
    frame=init_frame(detail_frame)

    tk.Label(frame, text="Details for "+str(id),
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
#root.minsize(width=250, height=250)
#root.maxsize(width=1000, height=800)
root.resizable(width=False, height=False)
#root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
#root.eval("tk::PlaceWindow . center")

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
"""
root.withdraw()
root.update_idletasks()  # Update "requested size" from geometry manager
print("Screen WxH+w+h:",root.winfo_screenwidth(),"x",root.winfo_screenheight(),"+",root.winfo_reqwidth(),"+",root.winfo_reqheight())
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))
root.deiconify()
"""
root.eval("tk::PlaceWindow . center")
print("Screen WxH+w+h:",root.winfo_screenwidth(),"x",root.winfo_screenheight(),"+",root.winfo_reqwidth(),"+",root.winfo_reqheight())

# Pun app
root.mainloop()