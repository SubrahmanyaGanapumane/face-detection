import cv2,os
import sys

# Get user supplied values
path = './0001'
cascPath = "haarcascade_frontalface_default.xml"
valid_images = (".jpg",".gif",".png",".tga")
image_paths = [os.path.join(path, f) for f in os.listdir(path)if f.lower().endswith(valid_images)]
dir_paths = [os.path.join(path, f) for f in os.listdir(path)if not f.lower().endswith(valid_images)]
# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image one by one
i=0
for path1 in image_paths:
    image = cv2.imread(path1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        #flags = cv2.CV_HAAR_SCALE_IMAGE
    )

    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("In put name?", image)
    cv2.waitKey(0)


    for (x, y, w, h) in faces:
        #cv2.imshow("In put name?", image[y:y+h, x:x+w])
        #cv2.waitKey(0)
        
        name=str(i)
        i=i+1
        cv2.imwrite("dataBase/"+name+".jpg", image[y:y+h, x:x+w])
        cv2.waitKey(100)
    
