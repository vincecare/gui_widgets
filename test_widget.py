import tkinter as tk
import widget as wg

def func_A():
    print("Here")
    print(entry1.get())

if __name__=="__main__":

    window=tk.Tk()
    window.title("My window")

    wg1=wg.widget()
    label1=wg1.label_create(window,"This is my label1\nline 2",wg1.RELIEF_GROOVE,0,0,10,30)
    wg1.grid(label1,0,0)
    wg1.justify(label1,wg1.JUSTIFY_LEFT)
    label2 = wg1.label_create(window, "This is my label2", wg1.RELIEF_RAISED, 1,0,30, 30)
    wg1.place(label2, 10, 30,100,200)

    button1=wg1.button_create(window,"button",command=func_A,relief=wg1.RELIEF_RAISED,gridrow=2,gridcol=1)
    button1.state=tk.DISABLED
    wg1.grid(button1,3,1)
    wg1.font_color(button1,'RED',None)

    entry1,ans=wg1.entry_create(window, default_text="default_text",relief=wg1.RELIEF_RAISED,gridrow=4,gridcol=2, borderwidth=5)

    wg1.display_message_timeout("shut itself off in 10 second","title", timeout_second=10)
    print (wg1.messagebox_askquestion(msg="This is dispplay message",title=None))
    print(wg1.messagebox_askquestion(msg=ans, title="entry1 text"))
    #label1.pack()

    window.mainloop()
    print ("done")
