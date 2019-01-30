from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import re


# 模拟浏览器发送请求
def get_data():
    startUrl = 'http://www.uustv.com/'
    # 获取用户输入的姓名
    name = entry.get()
    # 去空格
    name = name.strip()
    if name == '':
        messagebox.showinfo('提示：', '请输入用户名')
    else:
        date = {
            'word': name,
            'sizes': '60',
            'fonts': 'jfcs.ttf',
            'fontcolor': '#000000'
        }
        result = requests.post(startUrl, data=date)
        result.encoding = 'utf-8'
        # 获取网站的源代码
        html = result.text
        reg = '<div class="tu">.<img src="(.*?)"/></div>'
        # 正则表达  （.*?）全部都需要匹配
        imagePath = re.findall(reg, html)
        # 获取图片的完整路径
        imgUrl = startUrl + imagePath[0]
        print(imgUrl)
        # 获取图片内容
        response = requests.get(imgUrl).content
        f = open('{}.gif'.format(name), 'wb')
        f.write(response)

        # 图片显示到窗口上
        bm = ImageTk.PhotoImage(file='{}.gif'.format(name))

        label2 = Label(root, image=bm)
        label2.bm = bm
        label2.grid(row=2, columnspan=2)


# 创建窗口
root = Tk()
# 标题
root.title('Design-signature')
# 窗口大小     宽 高
root.geometry('800x500')
# 窗口初始位置
root.geometry('-400+200')
# 标签控件
label = Label(root, text='签名', font=('宋体', 20), fg='black')
label.grid()

# 设计输入框
entry = Entry(root, font=('微软雅黑', 25))
entry.grid(row=0, column=1)
# 点击按钮
button = Button(root, text='设计签名', font=('微软雅黑', 22)
                , command=get_data)
button.grid(row=1, column=1,sticky=W)
# 消息循环  显示窗口
root.mainloop()
