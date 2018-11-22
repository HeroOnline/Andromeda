#!/usr/bin/python3
# coding=utf-8


"""
UI 操作窗口
"""


__author__ = 'LCD'

import os
import tkinter as tk
# from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from rx.subjects import Subject


info = '''
因为打包为App时默认索引路径与测试时有所出入
SO 是否 .workspace 和 是否 Release 对应选择所选文件的目标路径，参照作用，不可单独修改。

编译生成的 .xcarchive 文件将默认存放在项目路径下新建 archives 文件夹内
打包生成的 ipa 文件将默认存放在项目路径下的 ipas 文件夹内
单独选择输出文件夹(暂不支持,考虑后续添加)

指定 Archive 的 Xcode版本(暂不支持，目前使用Applications内默认版本)
版本控制工具自动化尚未配置

还有更多功能，后续看情况扩展
'''

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

    def __init__(self,
                 width,
                 height,
                 path,
                 plist,
                 target,
                 is_workspace,
                 is_release,
                 is_http,
                 fir='',
                 store_name='',
                 store_pwd=''):
        """
        此窗口 固定宽高 ，不可变动
        :param width: 窗口宽度
        :param height: 窗口高度
        公开属性：
        window， 主窗体
        source， Rx 信号体 通过 source.subscribe(... 获得回调信号
        """
        TkBase.__init__(self, width, height)
        self.project_path = tk.StringVar()
        self.plist_path = tk.StringVar()
        self.target = tk.StringVar()
        self.project_path.set(os.path.abspath('..'))  # 默认父级目录
        self.plist_path.set(os.path.abspath('.') + '/ipaAppStore.plist')  # 默认当前目录
        self.record_info = tk.StringVar()
        self.record_info.set('AutomationIpaInfo')

        self.is_workspace = tk.BooleanVar()
        self.is_workspace.set(True)
        self.is_release = tk.BooleanVar()
        self.is_release.set(True)
        self.is_git = tk.BooleanVar()
        self.is_git.set(True)

        self.is_http = tk.BooleanVar()
        self.is_http.set(False)

        self.fir_token = tk.StringVar()
        self.fir_token.set('')
        self.is_fir = tk.BooleanVar()
        self.is_fir.set(True)

        self.store_name = tk.StringVar()
        self.store_name.set('')
        self.store_pwd = tk.StringVar()
        self.store_pwd.set('')
        self.is_store = tk.BooleanVar()
        self.is_store.set(True)

        self.__make_var()
        self.__make_widgets()
        self.source = Subject()

        self.project_path.set(path)

        self.plist_path.set(plist)

        self.target.set(target)

        self.is_workspace.set(is_workspace)

        self.is_release.set(is_release)
        self.is_fir.set(not is_release)
        self.is_store.set(is_release)

        self.is_http.set(is_http)

        self.fir_token.set(fir)
        self.store_name.set(store_name)
        self.store_pwd.set(store_pwd)


    def __make_var(self):
        path = os.path.abspath('..')  # 获取当前父级目录
        self.project_path.set(path)  # 默认父级目录
        # 获取父级目录下所有文件
        for name in os.listdir(path):
            if name.endswith('.xcodeproj'):
                self.target.set(name.split('.')[0])
                self.is_workspace.set(False)

            if name.endswith('.xcworkspace'):
                self.target.set(name.split('.')[0])
                self.is_workspace.set(True)

    def run(self):
        self.window.mainloop()

    def quit(self):
        self.window.quit()
        self.window.destroy()

    def __make_widgets(self):
        # 底部容器
        frame0 = tk.Frame(self.window)
        frame0.grid(row=0, column=0)

        frame1 = tk.Frame(self.window)
        frame1.grid(row=1, column=0)

        frame2 = tk.Frame(self.window)
        frame2.grid(row=2, column=0)

        # frame0 容器
        self.__make_title_empty(frame0, 0, 0)
        f1 = tk.Frame(frame0)
        f1.grid(row=1, column=0)

        f2 = tk.Frame(frame0)
        f2.grid(row=1, column=1)

        # frame1 容器
        self.__make_title_empty(frame1, 0, 0)
        self.__make_select_confirm(frame1, 1, 0)

        # frame2 容器
        self.__make_title_info(frame2, 0, 0)

        # f1 容器
        self.__make_title_empty(f1, 0, 0)
        self.__make_title(f1, 0, 1, '项目目录：(选择.xcworkspace or .xcodeproj文件)')
        self.__make_title_empty(f1, 1, 0)
        self.__make_select_text(f1, 1, 1, 1, self.project_path)

        self.__make_title_empty(f1, 2, 0)
        self.__make_title(f1, 2, 1, '配置.plist 路径：(对应是否Release，不可单独修改)')
        self.__make_title_empty(f1, 3, 0)
        self.__make_select_text(f1, 3, 1, 2, self.plist_path)

        self.__make_title_empty(f1, 4, 0)
        self.__make_title(f1, 4, 1, '项目 Target：')
        self.__make_title_empty(f1, 5, 0)
        self.__make_select_text(f1, 5, 1, 2, self.target, False)

        """
        self.__make_title_empty(f1, 6, 0)
        self.__make_title(f1, 6, 1, '配置存储文件名')
        self.__make_title_empty(f1, 7, 0)
        self.__make_select_text(f1, 7, 1, 2, self.record_info, False)
        """

        self.__make_title_empty(f1, 8, 0)
        self.__make_title(f1, 8, 1, 'Fir Token：')
        self.__make_title_empty(f1, 9, 0)
        self.__make_select_text(f1, 9, 1, 2, self.fir_token, False)

        self.__make_title_empty(f1, 10, 0)
        self.__make_title(f1, 10, 1, 'App Store 账号：')
        self.__make_title_empty(f1, 11, 0)
        self.__make_select_text(f1, 11, 1, 2, self.store_name, False)

        self.__make_title_empty(f1, 12, 0)
        self.__make_title(f1, 12, 1, 'App Store 密码：')
        self.__make_title_empty(f1, 13, 0)
        self.__make_select_text(f1, 13, 1, 2, self.store_pwd, False)

        # f2 容器
        self.__make_title(f2, 0, 0, '是否.workspace：', 15, 'e')
        self.__make_radio_button(f2, 0, 1, '是', True, self.is_workspace)
        self.__make_radio_button(f2, 0, 2, '否', False, self.is_workspace)
        self.__make_title_empty(f2, 1, 0)

        self.__make_title(f2, 2, 0, '是否 Release：', 15, 'e')
        self.__make_radio_button(f2, 2, 1, '是', True, self.is_release)
        self.__make_radio_button(f2, 2, 2, '否', False, self.is_release)
        self.__make_title_empty(f2, 3, 0)

        self.__make_title(f2, 4, 0, 'Git or SVN：', 15, 'e')
        self.__make_radio_button(f2, 4, 1, 'Git', True, self.is_git)
        self.__make_radio_button(f2, 4, 2, 'SVN', False, self.is_git)
        self.__make_title_empty(f2, 5, 0)

        self.__make_title(f2, 6, 0, '开启http服务：', 15, 'e')
        self.__make_radio_button(f2, 6, 1, '开', True, self.is_http)
        self.__make_radio_button(f2, 6, 2, '关', False, self.is_http)
        self.__make_title_empty(f2, 7, 0)

        self.__make_title(f2, 8, 0, '上传到fir.im：', 15, 'e')
        self.__make_radio_button(f2, 8, 1, '是', True, self.is_fir)
        self.__make_radio_button(f2, 8, 2, '否', False, self.is_fir)
        self.__make_title_empty(f2, 9, 0)

        self.__make_title(f2, 10, 0, '上传到App Store：', 15, 'e')
        self.__make_radio_button(f2, 10, 1, '是', True, self.is_store)
        self.__make_radio_button(f2, 10, 2, '否', False, self.is_store)
        self.__make_title_empty(f2, 11, 0)


    def __make_title_empty(self, frame, row, column):
        tk.Label(frame, text='', width=1, anchor='w').grid(row=row, column=column)

    def __make_title_info(self, frame, row, column):
        tk.Label(frame, text=info,
                 font=('Arial', 10), fg='gray',
                 width=90,
                 justify='left',  anchor='w').grid(row=row, column=column)

    def __make_title(self, frame, row, column, title='  ', width=35, anchor='w'):
        tk.Label(frame, text=title, width=width, anchor=anchor).grid(row=row, column=column)

    def __make_select_text(self, frame, row, column, tag, text, sele=True):
        entry = tk.Entry(frame, width=35, textvariable=text)
        entry.grid(row=row, column=column)
        if sele:
            button = tk.Button(frame, text='选择')
            button.grid(row=row, column=column + 1)
            button['command'] = (lambda:
                                 self.__click_select(entry, tag))

    def __make_radio_button(self,frame, row, column, text, val, var):
        tk.Radiobutton(frame, text=text, width=5,
                       variable=var, value=val).grid(row=row, column=column)


    def __print_selection(self, tag):
        pass

    def __click_select(self, entry, tag):

        if tag == 1:
            path = filedialog.askopenfilename()
            if len(path) > 0:
                t = '/'
                list = path.split('/')
                pro = list.pop()
                path = t.join(list)
                self.is_workspace.set('.xcworkspace' in pro)
                tag = pro.split('.')[0]
                self.project_path.set(path)
                self.target.set(tag)
        else:
            path = filedialog.askopenfilename()
            if len(path) > 0:
                t = '/'
                self.plist_path.set(path)
                list = path.split('/')
                pro = list.pop()
                self.is_release.set('AppStore' in pro)

    def __select_excel_input(self, entry_box):
        path = filedialog.askopenfilename()
        entry_box.delete(0, len(entry_box.get()))
        entry_box.insert(0, path)
        self.project_path = path

    # 如果 函数内部没有使用到 self. 会提示 Method 'select_excel_input' may be 'static' less... (⌘F1)
    # 会建议你 要么 加上@staticmethod ，要么放到class外面去
    def __select_excel_output(self, entry_box):
        path = askdirectory()
        entry_box.delete(0, len(entry_box.get()))
        entry_box.insert(0, path)
        return path

    def __make_select_confirm(self, frame, row, column):
        button = tk.Button(frame, width=15, text='开启自动打包')
        button.grid(row=row, column=column)
        button['command'] = (lambda:
                             self.__click_browser())

    def __click_browser(self):
        if len(self.project_path.get()) > 0 and len(self.plist_path.get()) > 0 and len(self.target.get()) > 0:
            self.quit()

            # 去除了 plist 文件输入框 这里根据 选择重新配置
            """
            if self.is_release.get():
                self.plist_path.set(os.path.abspath('.') + '/ipaAppStore.plist')
            else:
                self.plist_path.set(os.path.abspath('.') + '/ipaAdHoc.plist')
                
            """

            self.source.on_next((self.project_path.get(),
                                 self.plist_path.get(),
                                 self.target.get(),
                                 self.is_workspace.get(),
                                 self.is_release.get(),
                                 self.is_http.get(),
                                 self.fir_token.get(),
                                 self.store_name.get(),
                                 self.store_pwd.get()))
