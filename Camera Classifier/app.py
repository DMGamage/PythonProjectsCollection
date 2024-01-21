import tkinter as tk
from tkinter import simpledialog

import cv2 as cv
import os
import PIL.Image , PIL.ImageTk
import camera

class App:
    def __init__(self, window=tk.Tk(),window_title="camera classifier"):
        self.window = window
        self.window_title = window_title
        self.counters = [1,1]

        self.auto_predict= False
        self.camera = camera.Camera
        self.delay =15
        self.window .attributes
        self.init_gui()

    def init_gui(self):

        self.canvas = tk.Canvas(self.window, width=self.camera.width, height=self.camera.height)
        self.canvas.pack()

        self.btn_toggleauto = tk.Button(self.window, text="Auto Prediction", width=50, command=self.auto_predict_toggle)
        self.btn_toggleauto.pack(anchor=tk.CENTER, expand=True)

        self.classname_one = simpledialog.askstring("Classname One", "Enter the name of the first class:", parent=self.window)
        self.classname_two = simpledialog.askstring("Classname Two", "Enter the name of the second class:", parent=self.window)

        self.btn_class_one = tk.Button(self.window, text=self.classname_one, width=50, command=lambda: self.save_for_class(1))
        self.btn_class_one.pack(anchor=tk.CENTER, expand=True)

        self.btn_class_two = tk.Button(self.window, text=self.classname_two, width=50, command=lambda: self.save_for_class(2))
        self.btn_class_two.pack(anchor=tk.CENTER, expand=True)

        self.btn_train = tk.Button(self.window, text="Train Model", width=50, command=lambda: self.model.train_model(self.counters))
        self.btn_train.pack(anchor=tk.CENTER, expand=True)

        self.btn_predict = tk.Button(self.window, text="Predcit", width=50, command=self.predict)
        self.btn_predict.pack(anchor=tk.CENTER, expand=True)

        self.btn_reset = tk.Button(self.window, text="Reset", width=50, command=self.reset)
        self.btn_reset.pack(anchor=tk.CENTER, expand=True)

        self.class_label = tk.Label(self.window, text="CLASS")
        self.class_label.config(font=("Arial", 20))
        self.class_label.pack(anchor=tk.CENTER, expand=True)

    def auto_predict_toggle(self):
        self.auto_predict = not self.auto_predict

    def save_for_class(self,class_num):
        ret,frame = self.camera.get_frame()
        if not os.path.exists('1'):
            os.mkdir('1')
        if not os.path.exists('2'):
            os.mkdir('2')
        
        cv.imwrite(f'{class_num}/frame{self.counters[class_num-1]}.jpg',cv.cvtColor(frame,cv.COLOR_RGB2GRAY))
        img = PIL.Image.open(f'{class_num}/frame{self.counters[class_num-1]}.jpg')
        img.thumbnail((150,150),PIL.Image.ANTIALIS)
        img.save(f'{class_num}/frame{self.counters[class_num-1]}.jpg')

        self.counters[class_num-1] +=1

    def reset(self):
        for directory in ['1','2']:
            for file in os.listdir(directory):
                file_path =os.path.join(directory,file)

                if os.path.isfile(file_path):
                    os.unlink(file_path)

        self.counters= [1,1]

        self.class_label.config(text='CLASS')



        