from tkinter import *
frame = Tk()
frame.geometry('400x550')
txt1 = Entry(frame, width=35)
txt1.place(relx=0.1, rely=0.2, anchor=W)
txt2 = Text(frame, width=40, height=10)
txt2.place(relx=0.09, rely=0.6, anchor=W)


def clk():
    txt2.delete('1.0', END)
    fn = txt1.get()
    filename = str("D:/" + fn + ".txt")
    tf = open(filename, "a+")
    tf.close()
    tf = open(filename, 'r')
    b = tf.read()
    txt2.insert(INSERT, b)


def sav():
    fc = txt2.get('1.0', END)
    fn = txt1.get()
    tf = open("D:/" + fn + ".txt", "w")
    tf.write(fc)


btn1 = Button(frame, text='Find', command=clk)
btn1.place(relx=0.8, rely=0.2, anchor=CENTER)
btn2 = Button(frame, text='Save', command=sav)
btn2.place(relx=0.6, rely=0.9, anchor=CENTER)

frame.mainloop()
