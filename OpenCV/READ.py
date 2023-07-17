import cv2 as cv


# img = cv.imread('opencv-course-master/Resources/Photos/cat.jpg')

# cv.imshow('Cat', img)



# img = cv.imread('opencv-course-master/Resources/Photos/cat_large.jpg')

# cv.imshow('Big-Cat', img)
# cv.waitKey(0)



# READING VIDEOS
# capture = cv.VideoCapture('opencv-course-master/Resources/Videos/dog.mp4')

# while True:
#     # Means the video is stored frame by frame using capture.read() fuction
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)

#     # Means the video will stop when letter d is pressed. 
#     if cv.waitKey(20) & 0xff==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()    



def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions =(width, height)

    return cv.resize(frame, dimensions,interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('opencv-course-master/Resources/Videos/dog.mp4')

while True:
    # Means the video is stored frame by frame using capture.read() fuction
    isTrue, frame = capture.read()
    frame_resized= rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized',frame)

    # Means the video will stop when letter d is pressed. 
    if cv.waitKey(20) & 0xff==ord('d'):
        break

capture.release()
cv.destroyAllWindows() 

cv.waitKey(0)