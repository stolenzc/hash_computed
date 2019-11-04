import tkinter
from tkinter import ttk
# import os


class MainView(tkinter.Frame):

    def __init__(self, master=None):
        super(MainView, self).__init__(master)

        # 整体框架
        self.body = tkinter.Frame(self.master)
        self.file = tkinter.Frame(self.body)
        self.result = tkinter.Frame(self.body)
        self.computed = tkinter.Frame(self.body)

        self.s = ttk.Style()
        self.s.configure('my.TButton', font=('黑体', 12))

        # 文件区
        self.file_label = tkinter.Label(
            self.file,
            text='path: ',
            font=('黑体', 20)
        )
        self.path = tkinter.Variable()
        self.path_entry = ttk.Entry(
            self.file,
            textvariable=self.path,
            # font=20,
            font=('黑体', 20),
            # width=40,
        )
        self.open_file = ttk.Button(
            self.file,
            text='打开文件',
            width=15,
            # height=1,
            command=lambda: print('hello'),
            style='my.TButton',
            # font=('黑体', 14),
        )

        # hash显示区域
        self.my_hash_label = tkinter.Label(
            self.result,
            font=('黑体', 14),
            text='HASH值'
        )
        self.my_hash = tkinter.Text(
            self.result,
            height=4,
            width=100,
            font=('黑体', 14),
        )
        self.other_hash = tkinter.Text(
            self.result,
            height=4,
            width=100,
            font=('黑体', 14),
        )

        # 结果控制区域
        self.way = tkinter.StringVar()
        self.computed_way = ttk.Combobox(
            self.computed,
            textvariable=self.way,
            font=('黑体', 14),
        )
        self.computed_button = tkinter.Button(
            self.computed,
            text='计算结果',
            width=50,
            height=20,
            font=('黑体', 14),
        )

        self.window_init()

    def window_init(self):
        # 主窗口设置
        self.master.title('Hash值计算')
        self.master.geometry('600x400+400+100')
        self.master.resizable(0, 0)

        # 文件区设置
        tkinter.Label(self.body, text='').pack(side=tkinter.TOP, fill=tkinter.X)
        self.file_label.pack(
            fill=tkinter.Y,
            side=tkinter.LEFT,
        )
        self.open_file.pack(
            fill=tkinter.Y,
            side=tkinter.RIGHT,
        )
        self.path_entry.pack(
            fill=tkinter.BOTH,

            # side=tkinter.LEFT,
        )
        self.file.pack(
            fill=tkinter.X,
            side=tkinter.TOP,
        )

        # 显示区域设置
        self.my_hash_label.pack(
            fill=tkinter.Y,
            side=tkinter.LEFT
        )
        self.my_hash.pack(
            fill=tkinter.BOTH,
            side=tkinter.TOP,
        )
        self.other_hash.pack(
            fill=tkinter.X,
            side=tkinter.TOP,
        )
        self.result.pack(
            fill=tkinter.X,
            side=tkinter.TOP,
        )

        # 结果控制区域设置
        self.computed_way.pack(
            fill=tkinter.Y,
            side=tkinter.LEFT,
        )
        self.computed_button.pack(
            fill=tkinter.Y,
            side=tkinter.RIGHT,
        )
        self.computed.pack(
            fill=tkinter.X,
            side=tkinter.TOP,
        )

        self.body.pack(
            fill=tkinter.BOTH,
        )

    def select_file(self):
        pass


if __name__ == '__main__':
    app = MainView()
    app.mainloop()
