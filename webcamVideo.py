import cv2

vid = cv2.VideoCapture(0)

width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)


height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)

fps = int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

if vid.isOpened() == False:
    print('Unable to read the feed.')

size=(width, height)

out = cv2.VideoWriter('readVideoC105.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

while True:
    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    out.write(frame)

    if cv2.waitKey(25) == 32:
        break

vid.release()
out.release()

cv2.destroyAllWindows()