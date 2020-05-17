import canvasapi
from canvasapi import Canvas
import collections
from view_courses import view_Courses
import viewClass
from methodtools import lru_cache
import tkinter
from tkinter import ttk

class peerReviewer:
    def __init__(self, canvas : Canvas, user: canvasapi.user):
        self.user = user
        self.root = tkinter.Tk()
        self.canvas = canvas
        self.viewStack = collections.deque([view_Courses(canvas,user,self.root)])
        self.run()

    @lru_cache()
    def run(self):
        # self.root.geometry("600x600")
        #
        # w = self.root.winfo_screenwidth()
        # h = self.root.winfo_screenheight()
        # x = w / 2 - 600 / 2
        # y = h / 2 - 600 / 2
        # self.root.geometry("+%d+%d" % (x, y))
        # self.root.title("Peer Reviewer")
        #
        # tkinter.Label(self.root, text="Peer Reviewer", bg="#0fccf7", height=3).pack(fill='x', side="top")

        # frame = tkinter.Frame(self.root)
        # frame.pack(fill="both", expand=True)

        # tkinter.Label (frame, text = "Welcome To The Peer-Reviewer ").pack(side = "top", expand = False, pady = 10)
        # tkinter.Button(frame, text = "Click Here To Continue", command = self.root.quit,relief= "flat", highlightthickness= 0).pack(side = "top")
        # self.root.mainloop()
        # frame.destroy()
        while self.viewStack:
            action = self.viewStack[-1].run()
            action.do(self.viewStack)

        # frame = tkinter.Frame(self.root)
        # frame.pack(fill="both", expand=True)
        # ttk.Label(frame, text = "Bye!").pack(side = "top", expand = False, pady = 10)
        # self.root.mainloop()






