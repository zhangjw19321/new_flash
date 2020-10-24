import cv2
def resize_user_contour(frame):
    # frame = cv2.imread("thresh.png")
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray,20,255,cv2.THRESH_BINARY_INV)
    contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    board = 10
    max_contour_x,max_contour_y,max_contour_w,max_contour_h = 0,0,0,0
    for cidx,cnt in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(cnt)
        if w * h > max_contour_w * max_contour_h:
            max_contour_x,max_contour_y,max_contour_w,max_contour_h = (x, y, w, h) 
    ori = frame[max_contour_y-board:max_contour_y+max_contour_h+2*board,max_contour_x-board:max_contour_x+max_contour_w+2*board]
    user_contour_frame = cv2.resize(ori,(512,512))
    # cv2.imwrite("usr.png",user_contour_frame)
    return user_contour_frame
if __name__ == "__main__":
    frame = cv2.imread("thresh.png")
    user_size_frame = resize_user_contour(frame)
    cv2.imwrite("user.png",user_size_frame)
