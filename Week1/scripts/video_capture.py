import cv2
import os
import numpy as np

# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Move up one directory level to the project directory
project_directory = os.path.join(current_directory, "..")

# Create the path to the image
image_path = os.path.join(project_directory, "data/videos", "chaplin.mp4")

cap = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'X264')
out = cv2.VideoWriter("output.mp4", fourcc, 30.0, (int(cap.get(3)),
                                                   int(cap.get(4))))

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print("cap ", width)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        out.write(frame)
        # grey = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow("frame ", frame)
        # cv2.imshow("grey", grey)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("break ")
        break

cap.release()
out.release()
cv2.destroyAllWindows()
