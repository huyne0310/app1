from tkinter import ttk
from tkinter import *
from thongso import *
from setup_window import manhinh
import os
import tkinter as tk
from PIL import ImageTk , Image

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

def clicked( ):
    NAME_USER = txt.get(1.0, "end-1c")
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
    points = (
        x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2,
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
#close child_windows
def on_closing():
    scrn.destroy( )
scr.protocol("WM_DELETE_WINDOW", on_closing)

bg2 = PhotoImage(file= os.path.join(PATH_IMAGES,"scr.png"))
background2= Label(scrn,i=bg2)
background2.place(x=0,y=0)

frame2 = tk.Frame(scrn)
frame2.place(x=0,y=0)
frame2.pack_propagate(False)
frame2.configure(width= 1080, height=652)


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

#style = ttk.Style()
#style.layout('TNotebook.Tab', [])

def ch2clk( ):
    tabcontrol.select(tab_clock)
def ch2sch( ):
    tabcontrol.select(tab_sch)
def ch2cht( ):
    tabcontrol.select(tab_cht)
def ch2chbx( ):
    tabcontrol.select(tab_chbx)





clock = Image.open(os.path.join(PATH_IMAGES, "clock-remaining.png"))
render1 = ImageTk.PhotoImage(clock)
imgclk = tk.Button(scrn, image=render1, borderwidth=0,command=ch2clk)
imgclk.image = render1
imgclk.grid(row = 3, column=2, sticky= S)

chbx = Image.open(os.path.join(PATH_IMAGES, "chbx.png"))
render2 = ImageTk.PhotoImage(chbx)
imgchb = tk.Button(scrn, image=render2, borderwidth=0,command=ch2chbx)
imgchb.image = render2
imgchb.grid(row = 3, column=1, sticky= S)

sch = Image.open(os.path.join(PATH_IMAGES, "schedule.png"))
render3 = ImageTk.PhotoImage(sch)
imgsch = tk.Button(scrn, image=render3, borderwidth=0,command=ch2sch)
imgsch.image = render3
imgsch.grid(row = 3, column=0, sticky= S)

cht = Image.open(os.path.join(PATH_IMAGES, "fan-chart.png"))
render4 = ImageTk.PhotoImage(cht)
imgcht = tk.Button(scrn, image=render4, borderwidth=0,command=ch2cht)
imgcht.image = render4
imgcht.grid(row = 3, column=3, sticky= S)




























scr.resizable(False,False )
scrn.resizable(False,False )
scr.mainloop( )
scrn.mainloop( )
