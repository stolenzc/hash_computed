"""
此模块作用为hash计算的显示和功能实现
"""

import hashlib
import tkinter
from tkinter import ttk
import tkinter.filedialog
# import os


class MainView(tkinter.Frame):
    """此类为显示类"""

    def __init__(self, master=None):
        super(MainView, self).__init__(master)

        # 整体框架
        self.body = tkinter.Frame(self.master)
        self.file = tkinter.Frame(self.body)
        self.my_result = tkinter.Frame(self.body)
        self.other_result = tkinter.Frame(self.body)
        self.computed = tkinter.Frame(self.body)

        self.style = ttk.Style()
        self.style.configure('my.TButton', font=('黑体', 14))
        self.style.configure('my2.TButton', font=('黑体', 20))

        # 文件区
        self.file_label = tkinter.Label(
            self.file,
            text='path: ',
            font=('黑体', 20)
        )
        self.path = tkinter.Variable()
        self.path_entry = tkinter.Text(
            self.file,
            # textvariable=self.path,
            # font=20,
            font=('', 14),
            height=3

            # width=40,
        )
        self.open_file = ttk.Button(
            self.file,
            text='打开文件',
            width=10,
            # height=1,
            command=self.select_file,
            style='my.TButton',
            # font=('黑体', 14),
        )

        # hash显示区域
        self.my_hash_label = tkinter.Label(
            self.my_result,
            font=('黑体', 20),
            text='计算值'
        )
        self.my_hash = tkinter.Text(
            self.my_result,
            height=3,
            width=100,
            state='disable',
            font=('黑体', 18),
        )
        self.other_hash_label = tkinter.Label(
            self.other_result,
            font=('黑体', 20),
            text='对比值'
        )
        self.other_hash = tkinter.Text(
            self.other_result,
            height=3,
            width=100,
            font=('黑体', 18),
        )

        # 显示对比结果区域
        self.compare_v = tkinter.Variable()
        self.compare = tkinter.Label(
            self.body,
            font=('黑体', 20),
            textvariable=self.compare_v,
        )

        # 结果控制区域
        self.way = tkinter.StringVar()
        self.computed_way = ttk.Combobox(
            self.computed,
            textvariable=self.way,
            # 设置为只可选择，不可输入
            state='readonly',
            font=('黑体', 14),
        )
        self.computed_button = ttk.Button(
            self.computed,
            text='计算',
            width=10,
            # height=1,
            command=self.get_result,
            # style='my.TButton2',
            style='my2.TButton',
        )

        self.window_init()
        self.insert_hash_way()

    def window_init(self):
        """此函数为窗口显示函数"""
        # 主窗口设置
        self.master.title('Hash计算器')
        self.master.geometry('600x400+400+100')
        self.master.resizable(0, 0)

        # 文件区设置
        # 放一行空白行
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
        tkinter.Label(self.body, text='').pack(side=tkinter.TOP, fill=tkinter.X)
        self.my_hash_label.pack(
            fill=tkinter.Y,
            side=tkinter.LEFT,
        )
        self.my_hash.pack(
            fill=tkinter.BOTH,
            # side=tkinter.RIGHT,
        )
        self.my_result.pack(
            fill=tkinter.X,
            side=tkinter.TOP,
        )
        tkinter.Label(self.body, text='').pack(side=tkinter.TOP, fill=tkinter.X)
        self.other_hash_label.pack(
            fill=tkinter.Y,
            side=tkinter.LEFT,
        )
        self.other_hash.pack(
            fill=tkinter.BOTH,
            # side=tkinter.RIGHT,
        )
        self.other_result.pack(
            fill=tkinter.X,
            side=tkinter.TOP,
        )

        # 对比结果显示区域
        tkinter.Label(self.body, text='').pack(side=tkinter.TOP, fill=tkinter.X)
        self.compare.pack()

        # 结果控制区域设置
        tkinter.Label(self.body, text='').pack(side=tkinter.TOP, fill=tkinter.X)
        self.computed_way.pack(
            fill=tkinter.Y,
            side=tkinter.LEFT,
        )
        self.computed_button.pack(
            fill=tkinter.Y,
            side=tkinter.RIGHT,
        )
        self.computed.pack(
            # fill=tkinter.X,
            # side=tkinter.TOP,
        )

        self.body.pack(
            fill=tkinter.BOTH,
        )

    def insert_hash_way(self):
        """此函数为下拉框数据插入函数"""
        way = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
        self.computed_way['value'] = way
        self.computed_way.current(1)

    def select_file(self):
        """此函数为文件路径选择函数"""
        filename = tkinter.filedialog.askopenfilename(initialdir=r'C:\Users\陈倔强\Desktop')
        self.path_entry.delete('1.0', 'end')
        self.path_entry.insert('insert', filename)

    def get_result(self):
        """此函数为hash值校验函数"""
        way = self.computed_way.get()
        # 将字符串转换为命令执行
        hasher = eval('hashlib.' + way + '()')
        self.compare_v.set('正在计算')
        count = 0

        with open(self.path_entry.get('1.0', 'end')[:-1], 'rb') as file:
            for data in iter(lambda: file.read(2048), b''):
                hasher.update(data)
                count += 1
            # for data in file.read(2048):
            #     if data:
            #         hasher.update(data.encode('utf-8'))
            #         count += 1
            #     else:
            #         break
        result = hasher.hexdigest()
        print(count)

        self.my_hash['state'] = 'normal'
        self.my_hash.delete('1.0', 'end')
        self.my_hash.insert('insert', result)
        self.my_hash['state'] = 'disable'

        if self.other_hash.get('1.0', 'end') != '\n':
            if self.other_hash.get('1.0', 'end')[:-1].lower() == result:
                self.compare_v.set('校验成功')
            else:
                self.compare_v.set('校验失败')
        else:
            self.compare_v.set('计算完毕')

    def hash_test(self):
        """此函数为测试hashlib函数"""
        hashlib.md5(self.path_entry)


if __name__ == '__main__':
    APP = MainView()
    APP.mainloop()
