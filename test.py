import sys

print(sys.path)




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







