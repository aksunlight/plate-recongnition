import os
import sys
from tkinter import E
from cv2 import equalizeHist
from matplotlib.cbook import contiguous_regions
import numpy as np
import cv2
import tensorflow as tf

def img_transform(car_rect,image):
    img_h,img_w = image.shape[:2]
    rect_w,rect_h = car_rect[1][0],car_rect[1][1]
    angle = car_rect[2]

    return_flag = False
    if car_rect[2]==0:
        return_flag = True
    if car_rect[2]==-90 and rect_w<rect_h:
        rect_w, rect_h = rect_h, rect_w
        return_flag = True
    if return_flag:
        car_img = image[int(car_rect[0][1]-rect_h/2):int(car_rect[0][1]+rect_h/2),
                  int(car_rect[0][0]-rect_w/2):int(car_rect[0][0]+rect_w/2)]
        return car_img

    car_rect = (car_rect[0],(rect_w,rect_h),angle)
    box = cv2.boxPoints(car_rect)

    heigth_point = right_point = [0,0]
    left_point = low_point = [car_rect[0][0], car_rect[0][1]]
    for point in box:
        if left_point[0] > point[0]:
            left_point = point
        if low_point[1] > point[1]:
            low_point = point
        if heigth_point[1] < point[1]:
            heigth_point = point
        if right_point[0] < point[0]:
            right_point = point

    if left_point[1] <= right_point[1]:  # 正角度
        new_right_point = [right_point[0], heigth_point[1]]
        pts1 = np.float32([left_point, heigth_point, right_point])
        pts2 = np.float32([left_point, heigth_point, new_right_point])  # 字符只是高度需要改变
        M = cv2.getAffineTransform(pts1, pts2)
        dst = cv2.warpAffine(image, M, (round(img_w*2), round(img_h*2)))
        car_img = dst[int(left_point[1]):int(heigth_point[1]), int(left_point[0]):int(new_right_point[0])]

    elif left_point[1] > right_point[1]:  # 负角度
        new_left_point = [left_point[0], heigth_point[1]]
        pts1 = np.float32([left_point, heigth_point, right_point])
        pts2 = np.float32([new_left_point, heigth_point, right_point])  # 字符只是高度需要改变
        M = cv2.getAffineTransform(pts1, pts2)
        dst = cv2.warpAffine(image, M, (round(img_w*2), round(img_h*2)))
        car_img = dst[int(right_point[1]):int(heigth_point[1]), int(new_left_point[0]):int(right_point[0])]

    return car_img

def verify_scale(rotate_rect):
   error = 0.4  #横纵比误差
   aspect = 4    #横纵比3.142857（440mm/140mm）
   min_area = 14*(14*aspect)
   max_area = 140*(140*aspect)
   min_aspect = aspect*(1-error)
   max_aspect = aspect*(1+error)
   theta = 30   #偏角

   #中心点坐标:(rect[0][0],rect[0][1]) Width:rect[1][0] Height:rect[1][1] 偏角rect[2]
   (x, y), (width, height), angle = rotate_rect
   if width==0 or height==0:
       return False
   r = height/width
   r = max(r, 1/r)
   area = height*width
   if area>min_area and area<max_area and r>min_aspect and r<max_aspect:
       #矩形的倾斜角度在不超过规定偏角
       if ((width > height and angle > 0 and angle < theta) or
           (width < height and angle > (90 - theta) and angle <= 90)):
           return True

   return False

def verify_color(rotate_rect,src_image):
    img_h,img_w = src_image.shape[:2]
    mask = np.zeros(shape=[img_h+2,img_w+2],dtype=np.uint8)
    connectivity = 4 #种子点上下左右4邻域与种子颜色值在[loDiff,upDiff]的被涂成new_value，也可设置8邻域
    loDiff,upDiff = 30,30
    new_value = 255
    flags = connectivity
    flags |= cv2.FLOODFILL_FIXED_RANGE  #考虑当前像素与种子象素之间的差，不设置的话则和邻域像素比较
    flags |= new_value << 8
    flags |= cv2.FLOODFILL_MASK_ONLY #设置这个标识符则不会去填充改变原始图像，而是去填充掩模图像（mask）

    rand_seed_num = 5000 #生成多个随机种子
    valid_seed_num = 200 #从rand_seed_num中随机挑选valid_seed_num个有效种子
    adjust_param = 0.1
    box_points = cv2.boxPoints(rotate_rect)
    box_points_x = [n[0] for n in box_points]
    box_points_x.sort(reverse=False)
    adjust_x = int((box_points_x[2]-box_points_x[1])*adjust_param)
    col_range = [box_points_x[1]+adjust_x,box_points_x[2]-adjust_x]
    box_points_y = [n[1] for n in box_points]
    box_points_y.sort(reverse=False)
    adjust_y = int((box_points_y[2]-box_points_y[1])*adjust_param)
    row_range = [box_points_y[1]+adjust_y, box_points_y[2]-adjust_y]
    # 如果以上方法种子点在水平或垂直方向可移动的范围很小，则采用旋转矩阵对角线来设置随机种子点
    if (col_range[1]-col_range[0])/(box_points_x[3]-box_points_x[0])<0.4\
        or (row_range[1]-row_range[0])/(box_points_y[3]-box_points_y[0])<0.4:
        points_row = []
        points_col = []
        for i in range(2):
            pt1,pt2 = box_points[i],box_points[i+2]
            x_adjust,y_adjust = int(adjust_param*(abs(pt1[0]-pt2[0]))),int(adjust_param*(abs(pt1[1]-pt2[1])))
            if (pt1[0] <= pt2[0]):
                pt1[0], pt2[0] = pt1[0] + x_adjust, pt2[0] - x_adjust
            else:
                pt1[0], pt2[0] = pt1[0] - x_adjust, pt2[0] + x_adjust
            if (pt1[1] <= pt2[1]):
                pt1[1], pt2[1] = pt1[1] + adjust_y, pt2[1] - adjust_y
            else:
                pt1[1], pt2[1] = pt1[1] - y_adjust, pt2[1] + y_adjust
            temp_list_x = [int(x) for x in np.linspace(pt1[0],pt2[0],int(rand_seed_num /2))]
            temp_list_y = [int(y) for y in np.linspace(pt1[1],pt2[1],int(rand_seed_num /2))]
            points_col.extend(temp_list_x)
            points_row.extend(temp_list_y)
    else:
        points_row = np.random.randint(row_range[0],row_range[1],size=rand_seed_num)
        points_col = np.linspace(col_range[0],col_range[1],num=rand_seed_num).astype(np.int)

    points_row = np.array(points_row)
    points_col = np.array(points_col)
    hsv_img = cv2.cvtColor(src_image, cv2.COLOR_BGR2HSV)
    h,s,v = hsv_img[:,:,0],hsv_img[:,:,1],hsv_img[:,:,2]
    # 将随机生成的多个种子依次做漫水填充,理想情况是整个车牌被填充
    flood_img = src_image.copy()
    seed_cnt = 0
    for i in range(rand_seed_num):
        rand_index = np.random.choice(rand_seed_num,1,replace=False)
        row,col = points_row[rand_index],points_col[rand_index]
        # 限制随机种子必须是车牌背景色
        if (((h[row,col]>26)&(h[row,col]<34))|((h[row,col]>100)&(h[row,col]<124)))&(s[row,col]>70)&(v[row,col]>70):
            cv2.floodFill(src_image, mask, (col,row), (255, 255, 255), (loDiff,) * 3, (upDiff,) * 3, flags)
            cv2.circle(flood_img,center=(col,row),radius=2,color=(0,0,255),thickness=2)
            seed_cnt += 1
            if seed_cnt >= valid_seed_num:
                break
    #======================调试用======================#
    show_seed = np.random.uniform(1,100,1).astype(np.uint16)
    cv2.imshow('floodfill'+str(show_seed),flood_img)
    cv2.imshow('flood_mask'+str(show_seed),mask)
    #======================调试用======================#
    # 获取掩模上被填充点的像素点，并求点集的最小外接矩形
    mask_points = []
    for row in range(1,img_h+1):
        for col in range(1,img_w+1):
            if mask[row,col] != 0:
                mask_points.append((col-1,row-1))
    mask_rotateRect = cv2.minAreaRect(np.array(mask_points))
    if verify_scale(mask_rotateRect):
        return True,mask_rotateRect
    else:
        return False,mask_rotateRect

def locate_carPlate(orig_img, pred_image, car_plate_w, car_plate_h):
    carPlate_list = []
    contour_img = orig_img.copy()
    contours,heriachy = cv2.findContours(pred_image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    for i,contour in enumerate(contours):
        #画出所有的轮廓
        #cv2.drawContours(contour_img, contours, i, (0, 255, 255), 2)
        #获取每个轮廓最小外接矩形
        min_rect = cv2.minAreaRect(contour)
        #根据矩形面积大小和长宽比判断疑似车牌
        if verify_scale(min_rect):
            #使用漫水法修补疑似车牌
            ret,min_rect = verify_color(min_rect, orig_img)
            if ret == False:
                continue
            #画出疑似车牌轮廓的最小外接矩形
            box = cv2.boxPoints(min_rect)
            box = np.intp(box)
            cv2.drawContours(contour_img, [box], 0, (0, 0, 255), 1)
            #车牌位置矫正
            car_plate = img_transform(min_rect, orig_img)
            #调整尺寸为后面CNN车牌识别做准备
            car_plate = cv2.resize(car_plate, (car_plate_w, car_plate_h))
            carPlate_list.append(car_plate)

    cv2.imshow('contour', contour_img)

    return carPlate_list

orig_img = cv2.imread('./16.jpeg')

blur_img = cv2.GaussianBlur(orig_img, (5, 5), 0)   #高斯模糊，模糊半径为5像素
#cv.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) -> dst
#cv2.imshow('blur img', blur_img)

gray_img = cv2.cvtColor(blur_img, cv2.COLOR_BGR2GRAY)   #灰度化
#cv.cvtColor(src, code[, dst[, dstCn]]) -> dst
#cv2.imshow('gray img', gray_img)

sobel_img = cv2.Sobel(gray_img, cv2.CV_16S, 1, 0, ksize=3)  #Soble算子求取边缘，Sobel核半径为3像素
sobel_img = cv2.convertScaleAbs(sobel_img)
#cv2.imshow('sobel img', sobel_img)

hsv_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2HSV)
h, s, v = hsv_img[:, :, 0], hsv_img[:, :, 1], hsv_img[:, :, 2]
#黄色色调区间[28.8-79.2]，蓝色色调区间[201.6-259.2]，饱和度、亮度[0.35-1]   复杂背景下基于 HSV 空间和模板匹配的车牌识别方法研究 谢永祥， 董兰芳
#黄色色调区间[25-55]，蓝色色调区间[200-255]，饱和度[0.35-1]，亮度[0.3-1]   基于 HSV 色彩空间与数学形态学的车牌定位研究 常巧红， 高满屯
#黄色色调区间[26-34]，蓝色色调区间[100-124]
#blue_img = (h > 100) & (h < 122) & (s > 90) & (v > 90)  #识别蓝牌
#blue_img = (h > 18) & (h < 28) & (s > 90) & (v > 90)  #识别黄牌
blue_img = (((h > 100) & (h < 122)) | ((h > 20) & (h < 28))) & (s > 90) & (v > 90)
blue_img = blue_img.astype('float32')
#cv2.imshow('blue img1', blue_img)
blue_img = cv2.blur(blue_img, (3, 3))
#cv2.imshow('blue img2', blue_img)
mix_img = np.multiply(sobel_img, blue_img)
#cv2.imshow('mix1', mix_img)
mix_img = mix_img.astype(np.uint8)
#cv2.imshow('mix2', mix_img)

#灰度图只有一个通道，他有256个灰度等级，255代表全白，0表示全黑
ret, binary_img = cv2.threshold(mix_img, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY) #二值化操作
#cv2.imshow('binary img', binary_img)                                                   

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (17,3))  #闭操作(21,5)
close_img = cv2.morphologyEx(binary_img, cv2.MORPH_CLOSE, kernel)
cv2.imshow('close img', close_img)

#车牌定位和剪裁
car_plate_w,car_plate_h = 136,36
car_plate_list = locate_carPlate(orig_img, close_img, car_plate_w, car_plate_h)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
blur_img = cv2.blur(gray_img, (3, 3))
#cv2.imshow('blur', blur_img)

sobel_img = cv2.Sobel(blur_img, cv2.CV_16S, 1, 0, ksize=3)
sobel_img = cv2.convertScaleAbs(sobel_img)
#cv2.imshow('sobel', sobel_img)

hsv_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2HSV)

h, s, v = hsv_img[:, :, 0], hsv_img[:, :, 1], hsv_img[:, :, 2]
# 黄色色调区间[26，34],蓝色色调区间:[100,124]
blue_img = (((h > 26) & (h < 34)) | ((h > 100) & (h < 124))) & (s > 70) & (v > 70)
blue_img = blue_img.astype('float32')

mix_img = np.multiply(sobel_img, blue_img)
#cv2.imshow('mix', mix_img)

mix_img = mix_img.astype(np.uint8)

ret, binary_img = cv2.threshold(mix_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#cv2.imshow('binary',binary_img)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(21,5))
close_img = cv2.morphologyEx(binary_img, cv2.MORPH_CLOSE, kernel)
#cv2.imshow('close', close_img)
'''