#单线程
#%%
import time
import tkinter
import tkinter.messagebox

def download():
    time.sleep(10)
    tkinter.messagebox('提示','ok')

def show_about():
    tkinter.messagebox.showinfo('关于','author:OneKing')

def main():
    top=tkinter.Tk()
    top.title("单线程")
    top.geometry('200x150')
    top.wm_attributes('-topmost',True)

    panel=tkinter.Frame(top)
    button1=tkinter.Button(panel,text='download',command=download)
    button2=tkinter.Button(panel,text='about',command=show_about)
    button1.pack(side='left')
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()

if __name__ == "__main__":
    main()

#%%
#多线程
import time
import tkinter
import tkinter.messagebox
from threading import Thread

def main():

    class DownTask(Thread):
        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('reminder','download ok')

            button1.config(state=tkinter.NORMAL)

    def download():
        button1.config(state=tkinter.DISABLED)
        DownTask(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于', 'author:OneKINg')

    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', 1)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()
    

#%%
from multiprocessing import Process, Queue
from random import randint
from time import time


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target=task_handler,
                    args=(number_list[index:index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    # 开始记录所有进程执行完成花费的时间
    start = time()
    for p in processes:
        p.join()
    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time: ', (end - start), 's', sep='')


if __name__ == '__main__':
    main()