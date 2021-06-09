# import required library
from tkinter import *
from PyDictionary import PyDictionary
# create objects
dictionary = PyDictionary()
root = Tk()
# set geometry
root.geometry("400x400")
def dict():
    meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get()))
# add lael, button, and frames
Label(root,text="Dictionary",font=("Helvetica 20 bold"),fg="green").pack(pady=10)
# frame 1
frame = Frame(root)
Label(frame,text="Type Word",font=("Helvetica 15 bold")).pack(side=LEFT)
word = Entry(frame,font=("Helvetica 15 bold"))
word.pack()
frame.pack(pady=10)
# frame 2
frame1 = Frame(root)
Label(frame1,text="Meaning:- ",font=("Helvetica 10 bold")).pack(side=LEFT)
meaning = Label(frame1,text="",font=("Helvetica 10"))
meaning.pack()
frame1.pack(pady=10)
# frame 3
frame2 = Frame(root)
Label(frame2,text="Synonyme:- ",font=("Helvetica 10 bold")).pack(side=LEFT)
synonym = Label(frame2,text="",font=("Helvetica 10"))
synonym.pack()
frame2.pack(pady=10)
# frame 4
frame3 = Frame(root)
Label(frame3,text="Antonym:- ",font=("Helvetica 10 bold")).pack(side=LEFT)
antonym = Label(frame3,text="",font=("Helvetica 10"))
antonym.pack()
frame3.pack(pady=10)
Button(root,text="Submit",font=("Helvetica 15 bold"),command=dict).pack()
# execute tkinter
root.mainloop()