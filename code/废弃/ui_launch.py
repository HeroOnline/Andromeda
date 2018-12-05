#!/usr/bin/python3
# coding=utf-8


"""
UI 操作窗口 基类
"""


__author__ = 'LCD'

import tkinter as tk
from tkinter import filedialog
import os



info_launch = """
1、将Andromeda.app  拖到 Application，AndromedaPlist 拖到 Application
2、将 Xcode 内的 Applications 文件夹拷贝一份到 AndromedaPlist文件夹，
    并将 Application Loader.app 重命名：ApplicationLoader.app
3、按说明格式正确配置 Andromeda.plist 
4、点击启动
"""


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


class TkSelect(TkBase):
    def __init__(self, width=500, height=300):
        TkBase.__init__(self, width, height)
        self.plist_path = tk.StringVar()
        self.plist_path.set(os.path.abspath('.'))

        frame0 = tk.Frame(self.window)
        frame0.pack()

        frame1 = tk.Frame(self.window)
        frame1.pack()

        frame2 = tk.Frame(self.window)
        frame2.pack()

        self.__make_title_info(frame0, 0, 0)
        self.__make_title(frame1, 0, 1, 'Andromeda.plist 文件目录')
        self.__make_title_empty(frame1, 1, 0)
        self.__make_select_text(frame1, 1, 1, 1, self.plist_path)

        self.__make_title_empty(frame2, 0, 0)
        self.__make_select_confirm(frame2, 1, 0)

        self.window.mainloop()


    def __make_title_empty(self, frame, row, column):
        tk.Label(frame, text='', width=1, anchor='w').grid(row=row, column=column)

    def __make_title_info(self, frame, row, column):
        tk.Label(frame, text=info_launch,
                 font=('Arial', 12), fg='gray',
                 justify='left',  anchor='w').grid(row=row, column=column)

    def __make_title(self, frame, row, column, title='  ', width=35, anchor='w'):
        tk.Label(frame, text=title, width=width, anchor=anchor).grid(row=row, column=column)

    def __make_select_text(self, frame, row, column, tag, text, sele=True):
        entry = tk.Entry(frame, width=35, textvariable=text)
        entry.grid(row=row, column=column)
        if sele:
            button = tk.Button(frame, text='选择', width=10,)
            button.grid(row=row, column=column + 1)
            button['command'] = (lambda:
                                 self.__click_select(entry, tag))

    def __click_select(self, entry, tag):
        if tag == 1:
            path = filedialog.askopenfilename()
            if len(path) > 0:
                self.plist_path.set(path)
        else:
            pass

    def __make_select_confirm(self, frame, row, column):
        button = tk.Button(frame, width=15, text='开启自动打包')
        button.grid(row=row, column=column)
        button['command'] = (lambda:
                             self.__click_browser())

    def __click_browser(self):
        self.window.quit()
        self.window.destroy()
        pass




t = TkSelect()