from tkinter import ttk
from tkinter import *
from thongso import *
from setup_window import manhinh
import os
import tkinter as tk
from PIL import ImageTk , Image
import time
from tkinter import messagebox

scrn = tk.Tk( )
app1=manhinh(scrn)
scrn.withdraw( )
scr = Toplevel(scrn)
app2= manhinh(scr)
scr.tk_setPalette('white')
bg = PhotoImage(file = os.path.join(PATH_IMAGES, "bgi.gif"))
#grid option
scr.grid_rowconfigure(0,weight=1)
scr.grid_rowconfigure(1,weight=1)
scr.grid_rowconfigure(2,weight=1)
scr.grid_columnconfigure(0,weight=1)
scr.grid_columnconfigure(1,weight=1)
scr.grid_columnconfigure(2,weight=1)

scrn.grid_rowconfigure(0,weight=1)
scrn.grid_rowconfigure(1,weight=1)
scrn.grid_rowconfigure(2,weight=1)
scrn.grid_rowconfigure(3,weight=1)
scrn.grid_columnconfigure(0,weight=1)
scrn.grid_columnconfigure(1,weight=1)
scrn.grid_columnconfigure(2,weight=1)
scrn.grid_columnconfigure(3,weight=1)

def save_clicked_flag(value):
    with open('clicked_flag.txt', 'w',encoding='utf-8') as file:
        file.write(str(value))

def load_clicked_flag():
    try:
        with open('clicked_flag.txt', 'r') as file:
            value = file.read().strip()
            return value.lower() == 'true'
    except FileNotFoundError:
        return False
clicked_flag = load_clicked_flag()

def read_username():
    with open('user_name.txt', 'r') as file:
        NAME_USER = file.read().strip()

def childwindow():
    global clicked_flag
    if not clicked_flag:
        def clicked( ):
            NAME_USER = txt.get("1.0", "end-1c")
            with open('user_name.txt', 'w', encoding='utf-8') as file:
                file.write(NAME_USER)
            limg= Label(scr, image= bg)
            limg.place(x=0,y=0)
            #label
            lbl= Label(scr,text="Welcome to my app, "+NAME_USER+" !!!", font=("Comic Sans MS",30))
            lbl.grid(row=1, column=1)
            def nextscr( ):
                limg= Label(scr, image= bg)
                limg.place(x=0,y=0)
                scr.destroy( )
                scrn.deiconify( )

            btn_frame1= Frame(scr)
            canvas = Canvas(btn_frame1, height=125, width=125)
            canvas.grid(row=1, column=1)
            btn_frame1.grid(row=2, column=1,sticky=N)
            btn1= Button(scr, text="Next", font=("Comic Sans MS",14),bg=COLOR_NUT1  ,fg= 'white', bd=0,width=8, height=1, activebackground=COLOR_NUT1, command=nextscr )
            btn1.place(x=490,y=500)
            round_rectangle(canvas, 1, 50, 125, 100, r=50, fill = COLOR_NUT1)
            
        #background image
        limg= Label(scr, image= bg)
        limg.place(x=0,y=0)
        #label
        lbl= Label(scr,text="Please enter your name:", font=("Comic Sans MS",15))
        lbl.grid(row=0, column=1,sticky=S)
        def round_rectangle(obj, x1, y1, x2, y2, r=25, **kwargs):
            points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2,
                x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r,x1, y1+r, x1, y1+r, x1, y1)
            return obj.create_polygon(points, **kwargs, smooth = True)
        #button
        btn_frame= Frame(scr)
        canvas = Canvas(btn_frame, height=125, width=125)
        canvas.grid(row=1, column=1)
        btn_frame.grid(row=2, column=1,sticky=N)
        btn= Button(scr, text="Ok", font=("Comic Sans MS",14),bg=COLOR_NUT1  ,fg= 'white', bd=0,width=8, height=1, activebackground=COLOR_NUT1, command=clicked)
        btn.place(x=490,y=500)
        round_rectangle(canvas, 1, 50, 125, 100, r=50, fill = COLOR_NUT1)
        #textbox
        txt = Text(scr, width= 10, font=('Comic Sans MS',20), borderwidth=0, height= 3)
        txt.tag_configure("center", justify=CENTER)
        txt.tag_add("center", "1.0", "end")
        txt.insert(END, "")
        txt.grid(row=1, column=1)
        txt.focus( )
        clicked_flag = True
        save_clicked_flag(clicked_flag)
    else:
        scr.withdraw( )
        scrn.deiconify( )
        read_username( )
#close child_windows
def on_closing():
    scrn.destroy( )
scr.protocol("WM_DELETE_WINDOW", on_closing)

childwindow()

bg2 = PhotoImage(file= os.path.join(PATH_IMAGES,"scr.png"))
background2= Label(scrn,i=bg2)
background2.place(x=0,y=0)

frame2 = tk.Frame(scrn)
frame2.place(x=0,y=0)
frame2.pack_propagate(False)
frame2.configure(width= 1080, height=652)
#tabs option
tabcontrol = ttk.Notebook(frame2)
tabcontrol.pack(fill ='both',expand=True)
tab_clock = ttk.Frame(tabcontrol)
tabcontrol.add(tab_clock, text = "clock")
tab_chbx = ttk.Frame(frame2)
tabcontrol.add(tab_chbx, text = "checkbox")
tab_sch = ttk.Frame(frame2)
tabcontrol.add(tab_sch, text = "schedule")
tab_cht = ttk.Frame(frame2)
tabcontrol.add(tab_cht, text = "chart")
style = ttk.Style()
style.layout('TNotebook.Tab', [])

#change tabs
def ch2clk( ):
    tabcontrol.select(tab_clock)
def ch2sch( ):
    tabcontrol.select(tab_sch)
def ch2cht( ):
    tabcontrol.select(tab_cht)
def ch2chbx( ):
    tabcontrol.select(tab_chbx)


fclck_image=tk.PhotoImage(file= os.path.join(PATH_IMAGES, "bgclock.png"))
fclck_label = tk.Label(tab_clock, image=fclck_image)
fclck_label.place(x=0,y=0)
tab_clock.tk_setPalette('white')
#countdown clock
f = ("Comic Sans MS",100)
hour = StringVar()
minute = StringVar()
second = StringVar()
hour.set("00")
minute.set("00")
second.set("00")
#dấu ":"
hour_tf = Entry(tab_clock, width=3, font=f, textvariable=hour,borderwidth=0,bg= 'white')
hour_tf.place(x=168,y=180)
mins_tf = Entry(tab_clock, width=3, font=f, textvariable=minute,borderwidth=0, bg= 'white')
mins_tf.place(x=451,y=180)
sec_tf = Entry(tab_clock, width=3, font=f, textvariable=second,borderwidth=0,bg='white')
sec_tf.place(x=742,y=180)
paused = False
def update():
    global userinput
    global paused
    if not paused:
        if userinput > -1:
            mins, secs = divmod(userinput, 60)
            hours = 0
        if mins > 59:
            hours, mins = divmod(mins, 60)
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        tab_clock.update()
        #imgpl.config(state='disabled')
        imgps.place(x=360,y=500)
        imgpl.place_forget( )
        hour_tf.bind("<Key>", lambda a: "break")
        mins_tf.bind("<Key>", lambda a: "break")
        sec_tf.bind("<Key>", lambda a: "break")
        hour_tf.config(state="readonly")
        mins_tf.config(state="readonly")
        sec_tf.config(state="readonly")
        if userinput == 0:
            messagebox.showinfo("", "Time's Up")
            hour_tf.unbind("<Key>")
            mins_tf.unbind("<Key>")
            sec_tf.unbind("<Key>")
            hour_tf.config(state="normal")
            mins_tf.config(state="normal")
            sec_tf.config(state="normal")
            hour.set("00")
            minute.set("00")
            second.set("00")
            imgpl.config(state="normal")
            imgpl.place(x=360,y=500)
            imgps.place_forget()
        userinput -= 1
        tab_clock.after(1000, update)
def startcd():
    global userinput   
    global paused
    paused = False
    try:
        userinput = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        messagebox.showwarning('Invalid Input!')
    tab_clock.update()
    update( )
def enable_btnrs():
    imgrs.config(state="normal")
def enable_btnps():
    imgps.config(state="normal")
def pause_resume( ):
        global paused
        paused = not paused
        def enable_btnrs():
            imgrs.config(state="normal")
        def enable_btnps():
            imgps.config(state="normal")
        def dis_btnrs():
            imgrs.config(state="disabled")
            tab_clock.after(1000, enable_btnrs)
        def dis_btnps():
            imgps.config(state="disabled")
            tab_clock.after(1000, enable_btnps)
        imgps.place_forget()
        imgrs.place(x=360,y=500)
        if not paused:
            update()
        if paused == False:
            imgrs.place_forget()
            imgps.place(x=360,y=500)
            dis_btnps()
        if paused == True:
            imgps.place_forget()
            imgrs.place(x=360,y=500)
            dis_btnrs()
def resetcd():
    global userinput
    global paused
    userinput = 0
    paused = True
    hour_tf.unbind("<Key>")
    mins_tf.unbind("<Key>")
    sec_tf.unbind("<Key>")
    hour_tf.config(state="normal")
    mins_tf.config(state="normal")
    sec_tf.config(state="normal")
    imgps.place_forget()
    imgrs.place_forget()
    imgpl.place(x=360,y=500)
    hour.set("00")
    minute.set("00")
    second.set("00")
    tab_clock.update()
    
clccdlbl1 = Label(tab_clock, text=":",font=f,fg='black')
clccdlbl1.place(x=404,y=167)
clccdlbl2 = Label(tab_clock, text=":",font=f,fg='black')
clccdlbl2.place(x=696,y=167)

play = Image.open(os.path.join(PATH_IMAGES, "playbtn.png"))
render01 = ImageTk.PhotoImage(play)
imgpl = tk.Button(tab_clock, image=render01, borderwidth=0,command= startcd)
imgpl.image = render01
imgpl.place(x=360,y=500)
pause = Image.open(os.path.join(PATH_IMAGES, "pausebtn.png"))
render02 = ImageTk.PhotoImage(pause)
imgps = tk.Button(tab_clock, image=render02, borderwidth=0,command= pause_resume)
imgps.image = render02
#imgps.place(x=360,y=500) #x=485
imgps.place_forget()
reset = Image.open(os.path.join(PATH_IMAGES, "resetbtn.png"))
render03 = ImageTk.PhotoImage(reset)
imgrs = tk.Button(tab_clock, image=render03, borderwidth=0,command=resetcd)
imgrs.image = render03
imgrs.place(x=610,y=500)
resume = Image.open(os.path.join(PATH_IMAGES, "playbtn.png"))
render04 = ImageTk.PhotoImage(resume)
imgrs = tk.Button(tab_clock, image=render04, borderwidth=0,command= pause_resume)
imgrs.image = render04
#imgps.place(x=360,y=500) #x=485
imgrs.place_forget()


#button app
clock = Image.open(os.path.join(PATH_IMAGES, "clock-remaining.png"))
render1 = ImageTk.PhotoImage(clock)
imgclk = tk.Button(scrn, image=render1, borderwidth=0,command=ch2clk, highlightcolor='#E8DBD0',highlightthickness=0,highlightbackground='#E8DBD0',activebackground='#DFD0C2')
imgclk.image = render1
imgclk.grid(row = 3, column=2, sticky= S, pady=5)

chbx = Image.open(os.path.join(PATH_IMAGES, "chbx.png"))
render2 = ImageTk.PhotoImage(chbx)
imgchb = tk.Button(scrn, image=render2, borderwidth=0,command=ch2chbx, highlightcolor='#E8DBD0',highlightthickness=0,highlightbackground='#E8DBD0',activebackground='#DFD0C2')
imgchb.image = render2
imgchb.grid(row = 3, column=1, sticky= S,pady=5)

sch = Image.open(os.path.join(PATH_IMAGES, "schedule.png"))
render3 = ImageTk.PhotoImage(sch)
imgsch = tk.Button(scrn, image=render3, borderwidth=0,command=ch2sch, highlightcolor='#E8DBD0',highlightthickness=0,highlightbackground='#E8DBD0',activebackground='#DFD0C2')
imgsch.image = render3
imgsch.grid(row = 3, column=0, sticky= S,pady=5)

cht = Image.open(os.path.join(PATH_IMAGES, "fan-chart.png"))
render4 = ImageTk.PhotoImage(cht)
imgcht = tk.Button(scrn, image=render4, borderwidth=0,command=ch2cht, highlightcolor='#E8DBD0',highlightthickness=0,highlightbackground='#E8DBD0',activebackground='#DFD0C2')
imgcht.image = render4
imgcht.grid(row = 3, column=3, sticky= S,pady=5)



#tab-chbx

frame3 = tk.Frame(tab_chbx, bg = 'white', width=1080, height= 653)
frame3.place(x=0,y=0)
frame3.pack_propagate(False)

bgchbx = PhotoImage(file= os.path.join(PATH_IMAGES,"bgchbx.png"))
backgroundchbx= Label(tab_chbx,i=bgchbx)
backgroundchbx.propagate(False)
backgroundchbx.place(x=0,y=0)

frame4 = tk.Frame(tab_chbx, bg= 'white', height=345, width=775)
frame4.place(x=155,y=145)
frame4.pack_propagate(False)

addtkslbl = Label(tab_chbx, text= "Please enter your tasks: ", font=('Comic Sans MS',14))
addtkslbl.place(x=10,y=548)
addtasks_box = Entry(tab_chbx, font=("Arial",20),width=56, borderwidth=0,bg='white', highlightthickness=0.5,highlightcolor='white',highlightbackground='white')
addtasks_box.place(x=25,y=595)

tasks = []

#tạo theme cho checkbox hình trònnn....(bing AI)
style = ttk.Style()
image_on = Image.open( os.path.join(PATH_IMAGES,"chbxon.png"))
image_off = Image.open(os.path.join(PATH_IMAGES,"chbxoff.png"))
image_on = ImageTk.PhotoImage(image_on)
image_off = ImageTk.PhotoImage(image_off)
style.element_create("custom.Checkbutton.indicator", "image", image_off,
                     ("selected", image_on), ("active", image_on),
                     width=image_on.width(), sticky="w")
style.layout("CustomCheckbutton",
             [("custom.Checkbutton.padding",
               {"sticky": "nswe",
                "children": [("custom.Checkbutton.indicator", {"side": "left", "sticky": ""}),
                             ("custom.Checkbutton.label", {"sticky": "nswe"})]})])
style.configure("CustomCheckbutton", background="white")
style.configure("CustomCheckbutton", font=("Arial", 14))

def update_checkboxes():
    for widget in frame4.winfo_children():
        widget.destroy()
    
    canvas = tk.Canvas(frame4)
    scrollbar = tk.Scrollbar(frame4, orient="vertical", command=canvas.yview, width=7)
    if canvas.winfo_exists():
        canvas.configure(highlightthickness=0, highlightbackground="white")
    scrollable_frame = tk.Frame(canvas)
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
        if scrollable_frame.winfo_height() > canvas.winfo_height():
            scrollbar.pack(side="right", fill="y")
            canvas.bind("<MouseWheel>", on_mousewheel)
        else:
            scrollbar.pack_forget()
            canvas.unbind("<MouseWheel>")

    scrollable_frame.bind("<Configure>", on_configure)

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    def on_checkbutton_select(task):
        tasks.remove(task)
        with open("tasks.txt", "w", encoding = "utf-8") as f:
            for task in tasks:
                f.write(task + "\n")
        update_checkboxes()
        if canvas.winfo_exists():
            canvas.configure(highlightthickness=0, highlightbackground="white")

    for task in tasks:
        var = tk.IntVar()
        frame = tk.Frame(scrollable_frame)
        c = ttk.Checkbutton(frame, variable=var, style="CustomCheckbutton", command=lambda task=task: on_checkbutton_select(task))
        c.pack(side=tk.LEFT)
        l = tk.Label(frame, text=task, wraplength=725, font=('Arial',14))
        l.pack(side=tk.LEFT)
        frame.pack(side=tk.TOP, anchor=tk.W, pady=(10,0))

    def on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    scrn.bind("<MouseWheel>", on_mousewheel)

    canvas.pack(side="left", fill="both", expand=True)

def save_tasks(event = None):
    task = addtasks_box.get()
    if task != "":
        tasks.append(task)
        update_checkboxes()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")
    addtasks_box.delete(0, tk.END)
    with open("tasks.txt", "w", encoding = "utf-8") as f:
        for task in tasks:
            f.write(task + "\n")
def load_tasks():
    try:
        with open("tasks.txt", "r", encoding = "utf-8") as f:
            lines = f.readlines()
            for line in lines:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass

addtask_btn = Image.open(os.path.join(PATH_IMAGES, "addtasks.png"))
render5 = ImageTk.PhotoImage(addtask_btn)
imgadtk = tk.Button(backgroundchbx, image=render5, borderwidth=0, command= save_tasks)
imgadtk.image = render5
imgadtk.place(x=940,y=525)

addtasks_box.bind('<Return>', save_tasks)

gdutks = Label(backgroundchbx, text="Your tasks", font=("Comic Sans MS", 30))
gdutks.place(x=315,y=15)

load_tasks()
update_checkboxes()


































scr.resizable(False,False )
scrn.resizable(False,False )
scr.mainloop( )
scrn.mainloop( )
