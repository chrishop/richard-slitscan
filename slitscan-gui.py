#!/usr/bin/env python3

from tkinter import Tk, Label, Button, filedialog, scrolledtext
import os
import argparse
from moviepy.editor import VideoFileClip
import numpy as np
from PIL import Image

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        self.src_file = None
        self.target_file = None
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="select source file", command=self.select_source_file)
        self.greet_button.pack()

        self.greet_button = Button(master, text="select target file", command=self.set_target_location)
        self.greet_button.pack()
        
        self.greet_button = Button(master, text="apply slitscan", command=self.create_slitscan_image)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
        
        self.log = scrolledtext.ScrolledText(master, width=30, height=8, font = ("Courier", 15))
        
    def select_source_file(self):
        print("select_source_file")
        self.src_file = filedialog.askopenfilename()
        
        
    def set_target_location(self):
        print("select_target_location")
        self.target_file = filedialog.asksaveasfile(mode='w', defaultextension='.jpg').name
        if self.target_file is None:
            return
        
    def create_slitscan_image(self):
        clip = VideoFileClip(self.src_file)
        img = np.zeros((clip.size[1], clip.size[0], 3), dtype='uint8')
        currentX = 0
        slitwidth = 1
        slitpoint = clip.size[0] // 2

        # generate our target fps with width / duration
        target_fps = clip.size[0] / clip.duration

        for i in clip.iter_frames(fps=target_fps, dtype='uint8'):
            if currentX < (clip.size[0] - slitwidth):
                img[:,currentX:currentX + slitwidth,:] = i[:,slitpoint:slitpoint+slitwidth,:]
            currentX += slitwidth

        output = Image.fromarray(img)
        output.save(self.target_file)
        
        
        

root = Tk()
root.geometry('500x300')
my_gui = MyFirstGUI(root)
root.mainloop()