import sys,random,os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps








# def combine_bg_fg(bg_str, fg_str):
#     bg_list = []
#     fg_list = []
#     # 以字典列表存储背景及其对应的色彩组
#     if bg_str is not None:
#         bgs = bg_str.strip(';').splite(';')
#         for item in bgs:
#             # bg第一元素为背景文件命名，后面的元素都是为色彩组名称
#             bg = item.strip().splite('|')
#             bg_list.append(bg)
#     if fg_str is not None:
#         fgs = fg_str.strip(';').splite(';')
#         for item in fgs:
#             # fg第一元素为前景文件命名，后面的元素都是为色彩组名称
#             fg = item.strip().splite('|')
#             fg_list.append(fg)
#     bg=None
#     fg=None
#     #组合产生可能的色彩结果
#     if(len(bg_list) >= len(fg_list)):  # 背景图比前景图多
#         bg_temp = bg_list
#         for i in range(len(bg_temp)):
#             k1 = random.randint(0,len(bg_temp)-1)
#             bg = bg_temp[k1][0]
#             fg_temp = fg_list
#             for j in range(len(fg_temp)):
#                 k2 = random.randint(0,len(fg_temp)-1)
#                 fg = fg_temp[k2][0]
#                 # 两个列表取交集,若有交集则return
#                 colors = list(set(bg_temp[k1]).intersection(set(fg_temp[k2])))
#                 # 若找到合适的匹配项，就返回
#                 if len(colors)>0:
#                     index = random.randint(0,len(colors)-1)
#                     return bg,fg,colors[index]
#                 fg_temp.remove(fg_temp[k2])
#         #特殊处理遍历了一遍还是找不到背景前景都匹配的色彩组，那就只取背景
#         k1 = random.randint(0, len(bg_list) - 1)
#         bg = bg_list[k1][0]
#         fg = None
#         color = bg_list[k1][random.randint(1,len(bg_list[k1])-1)]
#     else: # 背景图比前景图少
#         fg_temp = fg_list
#         for i in range(len(fg_temp)):
#             k1 = random.randint(0, len(fg_temp) - 1)
#             fg = fg_temp[k1][0]
#             bg_temp = bg_list
#             for j in range(len(bg_temp)):
#                 k2 = random.randint(0, len(bg_temp) - 1)
#                 bg = bg_temp[k2][0]
#                 # 两个列表取交集,若有交集则return
#                 colors = list(set(fg_temp[k1]).intersection(set(bg_temp[k2])))
#                 # 若找到合适的匹配项，就返回
#                 if len(colors) > 0:
#                     index = random.randint(0, len(colors) - 1)
#                     return bg, fg, colors[index]
#                 bg_temp.remove(bg_temp[k2])
#         # 特殊处理遍历了一遍还是找不到背景前景都匹配的色彩组，那就只取背景
#         k1 = random.randint(0, len(fg_list) - 1)
#         bg = None
#         fg = fg_list[k1][0]
#         color = fg_list[k1][random.randint(1, len(fg_list[k1]) - 1)]
#     return bg,fg,color
#
#
# bg="bg003.png|R001|R002|R004|R005;bg004.png|R002|R003|R005;bg006.png|R005"
# fg="fg003.png|R002|R003|R005;fg005.png|R002|R003|R004|R005;fg006.png|R002|R003|R004|R005;fg007.png|R001|R002|R003|R004|R005"
# for i in range(20):
#     b,f,c = combine_bg_fg(bg,fg)






def draw_img_in_circle(url):
    ima = Image.open(url).convert("RGBA")
    size = ima.size
    # 因为是要圆形，所以需要正方形的图片
    r2 = min(size[0], size[1])
    if size[0] != size[1]:
        ima = ima.resize((r2, r2), Image.ANTIALIAS)
    imb = Image.new('RGBA', (r2, r2),(255,255,255,0))
    pima = ima.load()
    pimb = imb.load()
    r = float(r2/2) #圆心横坐标
    for i in range(r2):
        for j in range(r2):
            lx = abs(i-r+0.5)#到圆心距离的横坐标
            ly = abs(j-r+0.5)#到圆心距离的纵坐标
            l  = pow(lx,2) + pow(ly,2)
            if l <= pow(r, 2):
                pimb[i,j] = pima[i,j]
    imb.save("t1.png")




def circle_corder_image(url):
    im = Image.open(url).convert("RGBA")
    rad = 500  # 设置半径
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h-rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    im.save('t2.png')



def circle_new(url):
    ima = Image.open(url).convert("RGBA")
    size = ima.size
    r2 = min(size[0], size[1])
    if size[0] != size[1]:
        ima = ima.resize((r2, r2), Image.ANTIALIAS)
    circle = Image.new('L', (r2, r2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, r2, r2), fill=255)
    alpha = Image.new('L', (r2, r2), 255)
    alpha.paste(circle, (0, 0))
    ima.putalpha(alpha)
    ima.save('t3.png')



if __name__ == '__main__':
    draw_img_in_circle('测试图.png')
    circle_corder_image('测试图.png')
    circle_new('测试图.png')









# from flask import Flask,request
# import json
#
#
# if __name__ == '__main__':
#     app = Flask(__name__)
#
#     @app.route('/smartposter',methods=['GET','POST'])  # app.route装饰器映射URL和执行的函数，这个设置将根URL映射到了hello_world函数上
#     def smart_poster():
#         if request.method == 'POST':
#             data = request.get_data()
#             print(data)
#             json_data = json.loads(data.decode("utf-8"))
#             print(json_data)
#             style = json_data.get('layers')
#             return '海报制作中!'
#
#     @app.route('/hello/',methods=['GET','POST'])    #route装饰器直接指定了URL，
#     def SmartPoster():
#         # #data = Flask.request.data  # 方法一：获取字符串
#         # data = Flask.request.get_data()  # 方法二：获取字符串
#         # j_data = json.loads(data)
#         # print(j_data)
#         return 'Hello Flask!'
#
#     app.run(host='0.0.0.0')





# src = cv.imread("background/happy1.jpg")
# size=src.shape
# width=size[0]/2
# height=size[1]/2
# print ("%d  %d  %d"%(width,height,size[2]))
# cv.namedWindow("name window",cv.WINDOW_AUTOSIZE)
# new_src=cv.resize(src,(int(height),int(width)),cv.INTER_CUBIC)#变换图像尺寸
#
# #定义文字类型
# # font=ImageFont.truetype("Fonts/mygdmc.otf",90)
# # draw=ImageDraw.Draw(new_src)
# # draw.text((100,100),u"春节有优惠",(133,21,213),font)
# cv.putText(new_src,u"what the",(100,100),cv.FONT_HERSHEY_COMPLEX,1,(233,255,255),1)
#
# cv.imshow("name window",new_src)
# cv.imwrite("outputPosters/xjw.jpg",new_src)
# cv.waitKey(0)#等待下一个操作，才会消失，释放内存
# cv.destroyAllWindows()




# import cv2
# import numpy as np
#
# img1 = cv2.imread('background/happy1.jpg') #原始图像
# img2 = cv2.imread('haarcascade/weicheche2.png')   #logo图像，要往原始图像上添加
#
# rows,cols,channels = img2.shape  #得到logo的尺寸
# roi  = img1[0:rows,0:cols ]   #在原始图像中截取logo图像大小的部分
#
# # img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)#将logo图像灰度化
# # ret,mask =cv2.threshold(img2gray,200,255,cv2.THRESH_BINARY)#将logo灰度图二值化，将得到的图像赋值给mask，logo部分的值为255，白色
# # mask_inv = cv2.bitwise_not(mask)  #将mask按位取反，即白变黑，黑变白
# #
# # img1_bg = cv2.bitwise_and(roi,roi,mask = mask)#将原始图像中截取的部分做处理，mask中黑色部分按位与运算，即保留黑色部分，保留除logo位置外的部分
# # img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)#将logo图像中，mask_inv部分按位与运算，即保留黑色部分，保留logo
#
#
#
#
# dst = cv2.add(img1,img2) #图像相加
# img1[0:rows,0:cols] = dst       #图像替换
# det =cv2.calc
#
# cv2.Cas
#
# cv2.imshow('res',img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()








# import requests
# from PIL import Image
# from io import BytesIO
# import time
# import jieba
# #import mmseg
#
# if __name__ == '__main__':
#     try:  # 获取网络地址
#         URL = 'https://mp.zhihuiyouzhan.com/img/ic_home_logo.png'
#         response = requests.get(URL)
#         photo = Image.open(BytesIO(response.content))
#         photo = photo.convert('RGBA')
#     except Exception as e:  # 网络地址获取失败的话获取本地图片
#         photo = Image.open(URL)
#
#     # 计算海报制作时间，在 Unix 系统中，建议使用 time.time()，在 Windows 系统中，建议使用 time.clock()
#     start_linux = time.time()  # time.time()为1970.1.1到当前时间的毫秒数
#     # 方式一：获取json数据
#
#     do_start = time.time()
#     photo.save('jb.png')
#     temp_photo = photo.resize((200, 50))
#     do_end = time.time()
#
#     # 结束时间
#     end_linux = time.time()
#     print("runing time : %d s "%(end_linux - start_linux))
#     print("do poster runing time : %d s "%(do_end - do_start))
#
#
#     # 中文分词测试——jieba
#     seg_list = jieba.cut(u"这个老汉奸杀了我两个兄弟", cut_all=False)
#     print("Full mode: " + ",".join(seg_list))  # 默认精确模式
#
#
#     # 中文分词测试——jieba
#     seg_list = jieba.cut(u"我从小学计算机", cut_all=False)
#     print("Full mode: " + ",".join(seg_list))  # 默认精确模式
#
#     # mmseg.dict_load_defaults()
#     # text = u"这个老汉奸杀了我两个兄弟"
#     # algor = mmseg.Algorithm(text)
#     # for tok in algor:
#     #     print(tok.text)
#
#     dictionary = {"asd":None}
#     print(dictionary)







