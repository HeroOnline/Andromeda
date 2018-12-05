#!/usr/bin/python3
# coding=utf-8


"""
UI 操作窗口 基类
"""


__author__ = 'LCD'


import tkinter as tk


class TkBase(object):
    def __init__(self, width, height):
        self.window = tk.Tk()
        self.window.geometry(self.center_window(width, height))
        self.window.resizable(False, False)
        self.window.title('基础配置')
        # self.window.attributes("-topmost", 1)

    def get_screen_size(self):
        return self.window.winfo_screenwidth(), self.window.winfo_screenheight()

    def get_window_size(self):
        return self.window.winfo_reqwidth(), self.window.winfo_reqheight()

    def get_default_size(self):
        return self.window.winfo_screenwidth()/3, self.window.winfo_screenheight()/3

    def center_window(self, width, height):
        x = self.get_screen_size()[0]/2 - width/2
        y = self.get_screen_size()[1]/2-height/2
        size = '%dx%d+%d+%d' % (width, height, x, y)
        return size

    def make_widgets(self):
        pass