# import tkinter as tk
# import subprocess

# def run_program_1():
#     subprocess.run(["python", "main.py", '-t', 'squat'])

# def run_program_2():
#     subprocess.run(["python", "main.py", '-t', 'push-up'])

# root = tk.Tk()

# button1 = tk.Button(root, text="Count Squat", command=run_program_1,width=60, height=12, font=("Helvetica", 24), 
#                    foreground="white", background="black", 
#                    borderwidth=2, relief="groove")
# button1.pack()

# button2 = tk.Button(root, text="Count Push-Up", command=run_program_2,width=60, height=12, font=("Helvetica", 24), 
#                    foreground="white", background="black", 
#                    borderwidth=2, relief="groove")
# button2.pack()

# root.mainloop()







# import tkinter as tk
# import subprocess

# def run_program_1():
#     subprocess.run(["python", "main.py", '-t', 'squat'])

# def run_program_2():
#     subprocess.run(["python", "main.py", '-t', 'push-up'])

# def display_popup_window(title, content):
#     popup = tk.Toplevel(root)
#     popup.title(title)
#     popup.geometry("300x200")

#     label = tk.Label(popup, text=content)
#     label.pack(pady=10, padx=10)

#     close_button = tk.Button(popup, text="Close", command=popup.destroy)
#     close_button.pack(pady=10, padx=10)

# def on_button1_click():
#     run_program_1()
#     display_popup_window("Count Squat", "Counting Squats...")

# def on_button2_click():
#     run_program_2()
#     display_popup_window("Count Push-Up", "Counting Push-Ups...")

# root = tk.Tk()

# button1 = tk.Button(root, text="Count Squat", command=on_button1_click, width=60, height=12, font=("Helvetica", 24),
#                    foreground="white", background="black",
#                    borderwidth=2, relief="groove")
# button1.pack()

# button2 = tk.Button(root, text="Count Push-Up", command=on_button2_click, width=60, height=12, font=("Helvetica", 24),
#                    foreground="white", background="black",
#                    borderwidth=2, relief="groove")
# button2.pack()

# root.mainloop()







import tkinter as tk
import subprocess
import cv2
import argparse
from utils import *
import mediapipe as mp
from types_of_exercise import TypeOfExercise

def start_workout(exercise_type, video_source=None):
    ## setting the video source
    if video_source is not None:
        cap = cv2.VideoCapture(video_source)
    else:
        cap = cv2.VideoCapture(0)  # webcam


    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    cap.set(3, 800)  # width
    cap.set(4, 480)  # height

    ## setup mediapipe
    with mp_pose.Pose(min_detection_confidence=0.5,
                    min_tracking_confidence=0.5) as pose:

        counter = 0  # movement of exercise
        status = True  # state of move
        while cap.isOpened():
            ret, frame = cap.read()

            frame = cv2.resize(frame, (800, 480), interpolation=cv2.INTER_AREA)
            ## recolor frame to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame.flags.writeable = False
            ## make detection
            results = pose.process(frame)
            ## recolor back to BGR
            frame.flags.writeable = True
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark
                counter, status = TypeOfExercise(landmarks).calculate_exercise(
                    exercise_type, counter, status)
            except:
                pass

            # Create white rectangle at top left of image
            cv2.rectangle(frame, (0, 0), (200, 40), (255, 255, 255), cv2.FILLED)

            # Add text on top of white rectangle
            cv2.putText(frame, "Activity: " + exercise_type.replace("-", " "),
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
            
            # Create white rectangle at bottom left of image
            cv2.rectangle(frame, (0, 350), (80, 480), (255, 255, 255), cv2.FILLED)
            
            # Add text on top of white rectangle
            cv2.putText(frame, str(counter), (10, 450),
                        cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 3, cv2.LINE_AA)

            ## render detections (for landmarks)
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(255, 255, 255),
                                    thickness=2,
                                    circle_radius=2),
                mp_drawing.DrawingSpec(color=(174, 139, 45),
                                    thickness=2,
                                    circle_radius=2),
            )

            cv2.imshow('Gym Robot Trainer', frame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

def run_program_1():
    start_workout("squat")

def run_program_2():
    start_workout("push-up")


root = tk.Tk()

button1 = tk.Button(root, text="Count Squat", command=run_program_1, width=60, height=12, font=("Helvetica", 24),
                   foreground="white", background="black",
                   borderwidth=2, relief="groove")
button1.pack()

button2 = tk.Button(root, text="Count Push-Up", command=run_program_2, width=60, height=12, font=("Helvetica", 24),
                   foreground="white", background="black",
                   borderwidth=2, relief="groove")
button2.pack()

root.mainloop()
