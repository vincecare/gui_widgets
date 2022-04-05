### widget.py
### Written by Vince Du
###

import tkinter as tk
from tkinter import messagebox
#from tkinter import File

import sys

class widget():


    RELIEF_RAISED=tk.RAISED
    RELIEF_SUNKEN=tk.SUNKEN
    RELIEF_RIDGE=tk.RIDGE
    RELIEF_GROOVE=tk.GROOVE
    RELIEF_FLAT=tk.FLAT
    JUSTIFY_LEFT=tk.LEFT
    JUSTIFY_RIGHT=tk.RIGHT
    JUSTIFY_CENTER=tk.CENTER
    PACK_SIDE_TOP=tk.TOP
    PACK_SIDE_BOTTOM = tk.BOTTOM
    PACK_SIDE_LEFT = tk.LEFT
    PACK_SIDE_RIGHT = tk.RIGHT
    PACK_FILL_X=tk.X
    PACK_FILL_Y=tk.Y
    PACK_FILL_BOTH=tk.BOTH
    RAISED=tk.RAISED

#####  Label  #####
    def label_create(self,window,text,relief,gridrow, gridcol,padx=None, pady=None):
        label1=tk.Label(window,text=text,relief=relief,padx=padx,pady=pady)
        label1.grid(row=gridrow,column=gridcol)
        return label1


###  button  ######
    def button_create(self,window, text, command, relief, gridrow, gridcol):
       button1=tk.Button(window,text=text,command=command,relief=relief)
       button1.grid(row=gridrow,column=gridcol)
       return button1

### Entry  #########
    def entry_create(self, window, default_text, relief, gridrow,gridcol,borderwidth=5):
        entry1=tk.Entry(window, text=default_text,relief=relief, bd=borderwidth)
        entry1.grid(row=gridrow,column=gridcol)
        ans=entry1.get()
        return entry1,ans

    def frame_border(self, frame_obj, borderwidth, bordercolor='black'):
         frame_obj.config(highlightthickness=borderwidth,highlightbackground=bordercolor )

    def menubutton_create(self):
        pass

    def radiobutton_create(self):
        pass

##########################################################################################

    def place(self, widget_obj, x, y, width, height , anchor=None):
        widget_obj.place(x=x, y=y, width=width, height=height, anchor=anchor)

    def pack(self, widget_obj,fill, expand, side):
        # fill: 'both', 'x', 'y'
        # side= 'top','bottom', 'left', 'right'
        # expand=1
        widget_obj.pack(fill=fill, expand=expand, side=side)

    def geometry(self,widget_obj,x_width,y_height,x_coordinate,y_coordinate ):
        ## Frame has no geometry attribute'
        widget_obj.geometry("{}x{}+{}+{}".format(x_width,y_height,x_coordinate,y_coordinate))

    def grid(self, widget_obj, row, col):
        widget_obj.grid(row=row, column=col)

    def justify(self, widget_obj, justify):
        widget_obj.justify = justify

    def font_color(self, widget_obj, forecolor, backcolor):
        if not forecolor == None: widget_obj.fg = forecolor
        if not backcolor == None: widget_obj.bg = backcolor

    #######################################################################################################

    def display_message_timeout_old(self,msg, title, timeout_second=0, msg_width=200, fg='BLUE', font="Verdana 12 bold"):
        try:
            root1=tk.Tk()
            root1.title(title)
            root1.resizable(True,True)
            label1=tk.Label(root1,text=msg,fg=fg, font=font, width=msg_width)
            label1.pack(side='top', fill="both", expand=1, padx=0,pady=0)
            button1=tk.Button(root1,text="OK",command=lambda: root1.destroy())
            button1.pack(side='bottom', fill="none",expand=True)
            if timeout_second > 0:
                root1.after(timeout_second * 1000, root1.destroy())

            window_height=root1.winfo_height()
            window_width=root1.winfo_width()
            screen_width=root1.winfo_screenwidth()
            screen_height=root1.winfo_screenheight()
            window_width=int(screen_width/10)
            window_height=int(screen_height/8)
            #print ("screenwidth={} height={}  windowwidth={} height={}".format(screen_width,screen_height,window_width,window_height))
            x_cordinate=int((screen_width / 2 ) - (window_width / 2 ))
            y_cordinate = int((screen_height / 2) - (window_height / 2))
            #print ("{}x{}+{}+{}".format(window_width,window_height,x_cordinate,y_cordinate))
            root1.geometry( "{}x{}+{}+{}".format(window_width,window_height,x_cordinate,y_cordinate))
            root1.mainloop()
        except Exception as e:
            print("display_message() Exception: " + str(e))
        finally:
            print(".")

    def display_message_timeout(self,msg, title, timeout_second=0, msg_width=200, fg='BLUE', font="Verdana 12 bold"):
        try:
            root=tk.Tk()
            frame1=tk.Frame(root)
            frame1.title(title)
            frame1.resizable(True,True)
            label1=tk.Label(frame1,text=msg,fg=fg, font=font, width=msg_width)
            label1.pack(side='top', fill="both", expand=1, padx=0,pady=0)
            button1=tk.Button(frame1,text="OK",command=lambda: frame1.destroy())
            button1.pack(side='bottom', fill="none",expand=True)
            if timeout_second > 0:
                frame1.after(timeout_second * 1000, frame1.destroy())

            window_height=frame1.winfo_height()
            window_width=frame1.winfo_width()
            screen_width=frame1.winfo_screenwidth()
            screen_height=frame1.winfo_screenheight()
            window_width=int(screen_width/10)
            window_height=int(screen_height/8)
            #print ("screenwidth={} height={}  windowwidth={} height={}".format(screen_width,screen_height,window_width,window_height))
            x_cordinate=int((screen_width / 2 ) - (window_width / 2 ))
            y_cordinate = int((screen_height / 2) - (window_height / 2))
            #print ("{}x{}+{}+{}".format(window_width,window_height,x_cordinate,y_cordinate))
            frame1.geometry( "{}x{}+{}+{}".format(window_width,window_height,x_cordinate,y_cordinate))
            frame1.mainloop()
        except Exception as e:
            print("display_message() Exception: " + str(e))
        finally:
            print(".")

    def messagebox_showinfo(self,msg,title):
        messagebox.showinfo(title, msg)
    def messagebox_showerror(self,msg, title):
        messagebox.showerror(title, msg)
    def messagebox_showwarning(self,msg, title):
        messagebox.showwarning(title, msg)
    def messagebox_askquestion(self,msg, title):
        return messagebox.askquestion(title, msg)
    def messagebox_askyesnocancel(self, msg,title):
        return messagebox.askyesnocancel(title,msg)
    def messagebox_askokcancel(self, msg,title):
        return messagebox.askokcancel(title,msg)
    def messagebox_askretrycancel(self, msg,title):
        return messagebox.askretrycancel(title,msg)
    def messagebox_askyesno(self, msg,title):
        return messagebox.askyesno(title,msg)



if __name__=="__main__":
    pass
