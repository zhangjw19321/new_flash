import numpy as np
import cv2 as cv
import cv2
from add_pic import *
from extract_contour_by_tools import *
from generate_flash import *
import sys

################## step one: get a picutre #############
# gril student boy mogu bear sheep
# may need to convert to ＲGB
image_file = "src/input/gril.jpeg"
# image_file = "user.png"
raw_frame = cv2.imread(image_file)

################# step two: auto paint ################
from AttentionedDeepPaint.colorize import *
colored_frame = paint_color(raw_frame)
save_colored_name = "src/temp/colored_frame.png"
cv2.imwrite(save_colored_name,colored_frame)


################ step three: extract contour #########
transparent_coloed_frame = koutu(save_colored_name)
cv2.imwrite("src/temp/transparent_colored.png",transparent_coloed_frame)

############### step four: generate animate ##########
from Animate.animate_api import *
image = "src/temp/transparent_colored.png"
video_index = random.randint(1,4)
driving_video = "src/driving_video/dance_use" + str(video_index) + ".mp4"
model = "taichi"
animate(image,driving_video,model,"src/temp/test_flash/result_test.mp4")
sys.exit(0)
# animate(image,self.driving_video,model,save_video_name,save_video_name)
'''
############# step five: generate flash ############
background_image = "src/backgroud/backgroud.jpeg"
cloud_image = "src/backgroud/cloud_contour.png"
animation_video = "result.mp4"
flow_picture(background_image,cloud_image,animation_video)
'''



if __name__ == "__main__":
    pass 
    # flow_picture()
    # frame = cv.imread("cloud_contour.png")
    # fangshe(frame)
