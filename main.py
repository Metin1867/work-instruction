from functools import partial
import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
from PIL import Image, ImageTk

from constants import BG_COLOR, HEADINGFONT, MENUFONT, COLUMN_PER_ROW
from utils import log, flatten_list, list_to_string
import ArbeitsAnweisungen as data

button_img = {}
imgages = {}

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
        log("WARNING:", "Logo doesn't exists!")

def init_frame(frame, logo=None):
    clear_widgets(frame)
    frame.tkraise()
    frame.pack_propagate(False)

    if logo!=None:
        append_logo(frame)

    return frame
    
def load_main_frame():
    frame=init_frame(main_frame, "Logo")
        
    tk.Label(frame, text="Eine Anweisung auswählen ...",
                bg=BG_COLOR, fg='white', font=(MENUFONT, 14)).pack()

    buttonframe = tk.Frame(frame, background=BG_COLOR)
    buttonframe.pack()
    count=row=col=0
    for anweisung in data.anweisungen:
        log(anweisung, anweisung[0], anweisung[1][0],anweisung[1][1])
        log("Row/Column:", row, "/", col)
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

    anweisung=data.get_anweisung(id)

    datavalue = list_to_string(flatten_list(anweisung))
    
    dataframe = tk.Frame(frame)
    datascrollabletext = scrolledtext.ScrolledText(dataframe, state=tk.DISABLED,
                    bg=BG_COLOR, fg='white', font=(MENUFONT, 14))
    datascrollabletext.config(height=10)
    datascrollabletext.config(state=tk.NORMAL)
    datascrollabletext.insert(tk.END, datavalue)
    datascrollabletext.config(state=tk.DISABLED)
    datascrollabletext.pack(expand=True, fill='both')
    dataframe.pack(padx=5, pady=10)

    anweisungsframe=tk.Frame(frame, bg=BG_COLOR)
    anweisungsframe.pack()
    indx=2
    for el in ("Kurzbeschreibung", "Erstellung", "Letzte Änderung"):
        log(el, ".grid(row={}, column={})".format(indx-2, 0))
        label = tk.Label(anweisungsframe, text=el,
                bg=BG_COLOR, fg='white', font=(MENUFONT, 14)).grid(row=indx-2, column=0, sticky=tk.E)
        log(anweisung[indx], ".grid(row={}, column={})".format(indx-2, 1))
        label = tk.Label(anweisungsframe, text=anweisung[indx],
                bg=BG_COLOR, fg='white', font=(MENUFONT, 14)).grid(row=indx-2, column=1, sticky=tk.W)
        indx +=1
    schritte = anweisung[indx:]
    for s in schritte:
        print("Schritt:", s)
        label = tk.Label(anweisungsframe, text="Schritt "+str(s[0]),
                bg=BG_COLOR, fg='white', font=(MENUFONT, 14)).grid(row=indx-2, column=0, sticky=tk.E)
        label = tk.Label(anweisungsframe, text=s[1],
                bg=BG_COLOR, fg='white', font=(MENUFONT, 14)).grid(row=indx-2, column=1, sticky=tk.W)
        indx +=1
        if s[2] == None:
            notizen = s[3:]
            print("Notizen:", notizen)
            for n in notizen:
                print("Notiz:", n)
                label = tk.Label(anweisungsframe, text="Notiz "+str(n[0]),
                        bg=BG_COLOR, fg='white', font=(MENUFONT, 14)).grid(row=indx-2, column=0, sticky=tk.E)
                label = tk.Label(anweisungsframe, text=n[1],
                        bg=BG_COLOR, fg='white', font=(MENUFONT, 14)).grid(row=indx-2, column=1, sticky=tk.W)
        else:
                print("Image:", s[2])
                label = tk.Label(anweisungsframe, text="Image", 
                        bg=BG_COLOR, fg='white', font=(MENUFONT, 14)).grid(row=indx-2, column=0, sticky=tk.E)
                imgages[s[2]]=get_image(s[2], 500)
                label = tk.Label(anweisungsframe, image=imgages[s[2]],
                        bg=BG_COLOR, fg='white').grid(row=indx-2, column=1, sticky=tk.W)
        indx +=1

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
log("Screen WxH+w+h:",root.winfo_screenwidth(),"x",root.winfo_screenheight(),"+",root.winfo_reqwidth(),"+",root.winfo_reqheight())

# Run app
root.mainloop()