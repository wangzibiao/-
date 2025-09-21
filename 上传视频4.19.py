# coding:utf-8

import sys,random,shutil
import os, time, threading,subprocess,configparser,re
from selenium import webdriver
import ttkbootstrap as tk
from tkinter import *
from tkinter.filedialog import *
from ttkbootstrap.constants import *
#import tkinter as tk
from tkinter import messagebox
from selenium.webdriver.chrome.options import Options
pzjm = tk.Window()
pzjm.title("视频批量上传")
pzjm.option_add("*Font", "宋体")
pzjm.geometry('478x278')
pzjm.resizable(0,0)
sw = pzjm.winfo_screenwidth()
sh = pzjm.winfo_screenheight()
ww = 478
wh = 278
x = (sw-ww) / 2
y = (sh-wh) / 2
pzjm.geometry("%dx%d+%d+%d" %(ww,wh,x,y))
sj = time.localtime(time.time())

ri = str(time.strftime("%d", sj))

print(ri)
if int(ri)>18 and int(ri)<23:
    print("可以使用")
else:
    time.sleep(9999999)
    sys.exit()
outputpath = tk.StringVar()
filenewname = tk.StringVar()
def fileSave():
    path = askopenfilename(title='请选择谷歌浏览器')
    if path!="":
        path = path.replace("/", "\\")
    # 通过replace函数替换绝对文件地址中的/来使文件可被程序读取 #注意：\\转义后为\，所以\\\\转义后为\\
        Entry1.delete(0, "end")
        Entry1.insert('insert', path)

def outputFile():
    outputFilePath = askdirectory()
    if outputFilePath != "":
        path = outputFilePath.replace("/", "\\")
    # 通过replace函数替换绝对文件地址中的/来使文件可被程序读取 #注意：\\转义后为\，所以\\\\转义后为\\
        Entry2.delete(0, "end")
        Entry2.insert('insert', path)



Label11 = tk.Label(pzjm, text='自定义标题:', font=("宋体", 8, "bold"))
Label11.place(height=24, width=70, x=25, y=5)
Entry11 = tk.Entry(pzjm, font=("宋体", 10, "bold"))
Entry11.place(height=25, width=292, x=108, y=5)
Label1 = tk.Label(pzjm, text='谷歌路径:', font=("宋体", 10, "bold"))
Label1.place(height=24, width=70, x=25, y=40)
Entry1 = tk.Entry(pzjm, font=("宋体", 10, "bold"))
Entry1.place(height=25, width=292, x=108, y=40)
#Entry1.insert(0, '5')
xzbut1=tk.Button(pzjm, text='打开', command=fileSave)
#xzbut1.config(font=("宋体", 10, "bold"))
xzbut1.place(height=30, width=50, x=408, y=40)
Label2 = tk.Label(pzjm, text='视频路径:', font=("宋体", 10, "bold"))
Label2.place(height=24, width=70, x=25, y=75)
Entry2 = tk.Entry(pzjm, font=("宋体", 10, "bold"))
Entry2.place(height=25, width=292, x=108, y=75)
xzbut2=tk.Button(pzjm, text='打开', command=outputFile)
#xzbut1.config(font=("宋体", 10, "bold"))
xzbut2.place(height=30, width=50, x=408, y=75)
Label3 = tk.Label(pzjm, text='发送数量:', font=("宋体", 10, "bold"))
Label3.place(height=24, width=70, x=25, y=110)
Entry3 = tk.Entry(pzjm, font=("宋体", 10, "bold"))
Entry3.place(height=25, width=40, x=108, y=110)
Label4 = tk.Label(pzjm, text='发送间隔:', font=("宋体", 10, "bold"))
Label4.place(height=24, width=70, x=170, y=110)
Entry4 = tk.Entry(pzjm, font=("宋体", 10, "bold"))
Entry4.place(height=25, width=40, x=240, y=110)
Entry4.insert(0, "5")
Label5 = tk.Label(pzjm, text='-', font=("宋体", 10, "bold"))
Label5.place(height=24, width=10, x=285, y=110)
Entry5= tk.Entry(pzjm, font=("宋体", 10, "bold"))
Entry5.place(height=25, width=50, x=300, y=110)
Entry5.insert(0, "20")
CheckVar1 = IntVar()
C1 = Checkbutton(pzjm, font=("宋体", 10, "bold"), text = "固定数量", variable = CheckVar1, \
                  height=5, \
                 width = 20)
C1.place(height=24, width=80, x=10, y=145)
CheckVar1.set(1)
Label6 = tk.Label(pzjm, text='发送数量:', font=("宋体", 10, "bold"))
Label6.place(height=24, width=80, x=98, y=145)
Entry6 = tk.Entry(pzjm, font=("宋体", 10, "bold"))
Entry6.place(height=25, width=50, x=170, y=145)
Entry6.insert(0, "20")
CheckVar2 = IntVar()
C2 = Checkbutton(pzjm, font=("宋体", 10, "bold"), text = "附加商品", variable = CheckVar2, \
                  height=5, \
                 width = 20)
C2.place(height=24, width=80, x=230, y=145)
CheckVar2.set(1)
Label7 = tk.Label(pzjm, text='账号:', font=("宋体", 10, "bold"))
Label7.place(height=24, width=70, x=25, y=180)
Entry7 = tk.Entry(pzjm, font=("宋体", 10, "bold"))
Entry7.place(height=25, width=100, x=80, y=180)
Entry7.insert(0, "100")

Label8 = tk.Label(pzjm, text='启动账号:', font=("宋体", 10, "bold"))
Label8.place(height=24, width=70, x=180, y=180)
Entry8= tk.Entry(pzjm, font=("宋体", 10, "bold"))
Entry8.place(height=25, width=40, x=250, y=180)
Entry8.insert(0, "100")
Label9 = tk.Label(pzjm, text='-', font=("宋体", 10, "bold"))
Label9.place(height=24, width=10, x=295, y=180)
Entry9= tk.Entry(pzjm, font=("宋体", 10, "bold"))
Entry9.place(height=25, width=50, x=310, y=180)
Entry9.insert(0, "100")

isExists = os.path.exists("configure.ini")
if not isExists:
    print("创建配置文件")
    config = configparser.ConfigParser()
    # set a number of parameters
    #config.read('configure.ini')
    #a = config.get("配置","title")
    #print (a)

    config.add_section("配置")
    config.set("配置", "谷歌路径", "")
    config.set("配置", "视频路径", "")
    config.set("配置", "发布数量", "5")
    #config.set("配置", "商品", "0:0")

    config.write(open('configure.ini', "w"))
else:
    config = configparser.ConfigParser()
    config.read('configure.ini')
    gglj = config.get("配置", "谷歌路径")
    Entry1.insert(0, gglj)
    splj = config.get("配置", "视频路径")
    Entry2.insert(0, splj)
    fbsl = config.get("配置", "发布数量")
    Entry3.insert(0, fbsl)
def ydsp(namesz):

    isExists = os.path.exists(os.getcwd() + "\\已上传视频")
    if not isExists:
        os.makedirs(os.getcwd() + "\\已上传视频")
    for namez in namesz:
        xssdxs=namez.split('\\')
        #print(xssdxs[-1])
        shutil.move(namez,os.getcwd() + "\\已上传视频\\"+xssdxs[-1])

def get_filename(path, filetype):
    name = []
    final_name = []
    for root, dirs, files in os.walk(path):
        for i in files:
            if filetype in i:
                name.append(path+"\\"+i)
                #name.append(i.replace(filetype, ''))  # 生成不带‘.csv’后缀的文件名组成的列表
    return name
def bcpz():
    config = configparser.ConfigParser()
    config.read('configure.ini')
    config.set("配置", "谷歌路径", Entry1.get())
    config.set("配置", "视频路径", Entry2.get())
    config.set("配置", "发布数量", Entry3.get())
    config.write(open('configure.ini', "w"))

def qd():
    if Button2['text']=='启动任务':
        print('重新启动')
        Button2['text'] = '运行任务中!'

        fbsll=int(Entry3.get())
        print('启动了')
        bcpz()
        xssdx=Entry2.get()
        xssdxs=xssdx.split('\\')
        print(xssdxs[-1].isdigit())
        if not xssdxs[-1].isdigit() or len(xssdxs[-1])<8:
            messagebox.showinfo("商品ID错误", "商品ID错误")
            Button2['text'] = '启动任务'
            return
        else:
            print('获取到商品ID')
            spid=xssdxs[-1]
        url='https://live.pinduoduo.com/creator/index'
        for yyy in range(int(Entry8.get()),int(Entry9.get())+1):
            isExists = os.path.exists(os.getcwd() + "\\账号保存\\"+str(yyy))
            if isExists:
                print('有账号')
                os.system('taskkill /im chromedriver.exe /F')
                os.system('taskkill /im chrome.exe /F')
                lj = os.getcwd() + "\\账号保存\\" +str(yyy)
                command =Entry1.get()+' --remote-debugging-port=9222 --user-data-dir="' + lj + '"'
                subprocess.Popen(command)
                chrome_options = Options()
                chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                chrome_driver = "chromedriver.exe"
                driver = webdriver.Chrome(chrome_driver, options=chrome_options)
                print(driver.title)
                driver.implicitly_wait(3)
                names = get_filename(Entry2.get(), ".mp4")
                if CheckVar1.get() == 1:
                    scsl = int(Entry6.get())
                    print('固定数量')
                else:
                    scsl = len(names)

                for i in range(0, scsl, fbsll):
                    for ii in range(0,2):
                        nameas=[]
                        driver.get(url)
                        for y in range(0, fbsll):
                            if i + y < scsl and i + y < len(names):
                                #print(i + y)
                                nameas.append(names[i+y])
                        if nameas!=[]:
                            name = "\n".join(nameas)
                            print(name)
                            #/html/body/div/div/div[2]/div[2]/div[2]/input
                            try:
                                driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[3]/input').send_keys(name)
                            except:
                                driver.find_element_by_xpath(
                                    '//*[@id="__next"]/div/div[2]/div[2]/div[2]/input').send_keys(name)
                            splist = driver.find_elements_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div/div[1]/div')
                            bzx=3
                            bzy=0
                            for spa in splist:
                                # print(len(spa.text))
                                # print(spa.text)
                                aaa = re.search(
                                    '''文件名：(.*?)\.''', spa.text)
                                if aaa:
                                    #print(aaa.group(1))
                                    try:
              #/html/body/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[4]/div[2]/div/div[1]/div/div/div
                                        spa.find_element_by_xpath('div[2]/div/div['+str(bzx)+']/div[2]/div/div[1]/div/div/div').send_keys(aaa.group(1)+Entry11.get())
                                    except:
                                        bzx=bzx+1
                                        spa.find_element_by_xpath(
                                            'div[2]/div/div[' + str(bzx) + ']/div[2]/div/div[1]/div/div/div').send_keys(
                                            aaa.group(1) + Entry11.get())
                                    if CheckVar2.get() == 1:
                  #/html/body/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[5]/button/span
                                        spa.find_element_by_xpath('div[2]/div/div['+str(bzx+1)+']/button/span').click()
                                        if bzy==0:

                                            try:
                                                driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div[1]/div/div/div[2]/div').click()
                                                driver.find_element_by_xpath(
                                                    '/html/body/div[3]/div/div/div[2]/div/div[2]/div/div/div/div/div/div/input').send_keys(
                                                    spid)
                                                driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/div[2]/button[1]/span').click()
                                            except:
                                                bzy=1

                                                driver.find_element_by_xpath(
                                                    "/html/body/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/input").click()
                                                time.sleep(1)
                                                driver.find_element_by_xpath("//*[text()='商品ID']").click()
                                                driver.find_element_by_xpath(
                                                    '/html/body/div[3]/div/div/div[2]/div[2]/div/div/div[2]/div/div/input').send_keys(
                                                    spid)
                                                #/html/body/div[3]/div/div/div[2]/div[3]/div[2]/div[1]/label/div/div/i[3]
                                                #/html/body/div[3]/div/div/div[2]/div[2]/button/span
                                                driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/button/span').click()
                                                driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[3]/div[2]/div[1]/label/div/div/i[3]').click()
                                                driver.find_element_by_xpath(
                                                    '/html/body/div[3]/div/div/div[3]/div[2]/button[1]').click()
                                        else:

                                            driver.find_element_by_xpath(
                                                "/html/body/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/input").click()
                                            time.sleep(1)
                                            driver.find_element_by_xpath("//*[text()='商品ID']").click()
                                            driver.find_element_by_xpath(
                                                '/html/body/div[3]/div/div/div[2]/div[2]/div/div/div[2]/div/div/input').send_keys(
                                                spid)
                                            # /html/body/div[3]/div/div/div[2]/div[3]/div[2]/div[1]/label/div/div/i[3]
                                            driver.find_element_by_xpath(
                                                '/html/body/div[3]/div/div/div[2]/div[2]/button/span').click()
                                            driver.find_element_by_xpath(
                                                '/html/body/div[3]/div/div/div[2]/div[3]/div[2]/div[1]/label/div/div/i[3]').click()
                                            driver.find_element_by_xpath(
                                                '/html/body/div[3]/div/div/div[3]/div[2]/button[1]').click()
                                    #//*[@id="__next"]/div/div[2]/div[2]/div/div[2]/button[1]
                                    #/html/body/div[1]/div/div[2]/div[2]/div/div[2]/button[1]
                            print('完成一次')
                            time.sleep(10)
                                                        #/html/body/div/div/div[2]/div[2]/div/div[2]/button[1]
                            driver.find_element_by_xpath("//*[text()='一键发布']").click()
                            time.sleep(5)
                            if driver.current_url == 'https://live.pinduoduo.com/creator/video-manage':
                                print('上传成功')
                                fsjg = 10 + random.randint(int(Entry4.get()), int(Entry5.get()))
                                print('等待', fsjg, '秒')
                                time.sleep(fsjg)
                                ydsp(nameas)
                                break
                            else:
                                print('上传失败')
                                continue

    Button2['text'] = '启动任务'

def dkllq():

    os.system('taskkill /im chromedriver.exe /F')
    os.system('taskkill /im chrome.exe /F')
    lj=os.getcwd()+"\\账号保存\\"+Entry7.get()
    command=Entry1.get()+' --remote-debugging-port=9222 --user-data-dir="'+lj+'"'
    subprocess.Popen(command)
    print('执行')
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "chromedriver.exe"

    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    print(driver.title)
    driver.implicitly_wait(5)
    url = 'https://live.pinduoduo.com'
    driver.get(url)


def thread_it(func, *args):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()
if __name__ == "__main__":
    pass
    Button2 = tk.Button(pzjm, text='启动任务', command=lambda: thread_it(qd))

    Button2.place(height=28, width=100, x=300, y=220)

    #Button_8 = tkinter.Button(Form_1, text="打开浏览器", width=10, height=4, command=lambda: thread_it(dkllq))

    #
    Button1 = tk.Button(pzjm, text='登录账号', command=lambda: thread_it(dkllq))
    #
    Button1.place(height=28, width=100, x=73, y=220)

    pzjm.mainloop()









