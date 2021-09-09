# importing libraries
import cv2
import pafy
import numpy as np
   
def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

# Create a VideoCapture object and read from input file
#cap = cv2.VideoCapture('Sample0.mp4')

url = 'https://www.youtube.com/watch?v=_9OBhtLA9Ig'
print(f'input url:{url}')

video = pafy.new(url)

best = video.getbest(preftype="mp4")
print(f'best url:{best.url}')
cap = cv2.VideoCapture(best.url)
   
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video  file")
   
# Read until video is completed
while(cap.isOpened()):
      
  # Capture frame-by-frame
  ret, frame = cap.read()
  frame = rescale_frame(frame, 50)
  if ret == True:
   
    # Display the resulting frame
    cv2.imshow('Frame', frame)
   
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
   
  # Break the loop
  else: 
    break
   
# When everything done, release 
# the video capture object
cap.release()
   
# Closes all the frames
cv2.destroyAllWindows()