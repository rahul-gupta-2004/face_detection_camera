# Import necessary libraries
import cv2
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import datetime

# Global variable to toggle face detection on/off
show_face_detection = True

# Function to toggle face detection
def toggleFaceDetection():
    global show_face_detection
    show_face_detection = not show_face_detection

# Function to capture and save a snapshot
def takePic():
    # Convert OpenCV image to PIL format
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # Generate a unique filename using the current timestamp
    time = str(datetime.datetime.now().today()).replace(":", " ")
    file_name = time + ".jpg"
    # Save the image
    image.save(file_name)
    print("Image Saved", file_name)

# Function for face detection
def faceDetection(frame):
    # Check if face detection is enabled
    if show_face_detection:
        # Convert frame to grayscale for face detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            color = (0, 223, 255)
            alpha = 0.5
            overlay = frame.copy()
            cv2.rectangle(overlay, (x, y), (x+w, y+h), color, 2)
            cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
    return frame

# Set the width and height for the video window
width, height = 700, 640

# Open a connection to the camera (camera index 0 represents the default camera)
vid = cv2.VideoCapture(0)

# Load the pre-trained face cascade classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Set up the main Tkinter window
root = tk.Tk()
root.title("Tkinter Photo Booth")
root.iconbitmap("camera_icon.ico")
root.geometry(f"{width}x{height}")
root.configure(bg="#F2F3F2")
root.resizable(True, True)

# Create a label frame for displaying the video feed
f1 = LabelFrame(root)
f1.pack(side=TOP, fill=BOTH, expand=True)
l1 = Label(f1)
l1.pack(side=TOP, fill=tk.BOTH, expand=True)

# Create buttons for toggling face detection and taking snapshots
Button(root, text="Toggle Face Detection", font=("times new roman", 20, "bold"), bg="#F9F9F8", command=toggleFaceDetection).pack(side=BOTTOM, fill=X)
Button(root, text="Click to take snapshot", font=("times new roman", 20, "bold"), bg="#F9F9F8", command=takePic).pack(side=BOTTOM, fill=X)

# Main loop for continuously updating the video feed in the GUI
while True:
    # Read a frame from the video feed
    ret, img = vid.read()
    # Flip the frame horizontally for a mirrored effect
    img = cv2.flip(img, 1)
    
    # Apply face detection to the video frame
    img_with_faces = faceDetection(img)
    
    # Convert the processed frame to RGB format for displaying in Tkinter
    img1 = cv2.cvtColor(img_with_faces, cv2.COLOR_BGR2RGB)
    img_tk = ImageTk.PhotoImage(Image.fromarray(img1))
    l1['image'] = img_tk
    root.update()
    
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
vid.release()
cv2.destroyAllWindows()
