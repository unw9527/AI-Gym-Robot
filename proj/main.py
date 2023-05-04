#################################################################################
#
# tab:4
#
# main.py: main function for all pose-recognition
#
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose, without fee, and without written agreement is
# hereby granted, provided that the above copyright notice and the following
# two paragraphs appear in all copies of this software.
#
# IN NO EVENT SHALL THE AUTHOR OR THE UNIVERSITY OF ILLINOIS BE LIABLE TO 
# ANY PARTY FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL 
# DAMAGES ARISING OUT  OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, 
# EVEN IF THE AUTHOR AND/OR THE UNIVERSITY OF ILLINOIS HAS BEEN ADVISED 
# OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# THE AUTHOR AND THE UNIVERSITY OF ILLINOIS SPECIFICALLY DISCLAIM ANY 
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF 
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE SOFTWARE 
# PROVIDED HEREUNDER IS ON AN "AS IS" BASIS, AND NEITHER THE AUTHOR NOR
# THE UNIVERSITY OF ILLINOIS HAS ANY OBLIGATION TO PROVIDE MAINTENANCE, 
# SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS."
#
# Author:          Kunle Li
# Creation Date:   2023-03-29
# Credits:         https://github.com/M-A-D-A-R-A/Sports_py
#
#################################################################################

import cv2
import argparse
from utils import *
import mediapipe as mp
from types_of_exercise import TypeOfExercise
import logging
from datetime import datetime
import os

def mouse_callback(event: int, x: int, y: int, flags, param):
    """Halt the program if the button is clicked.

    Args:
        event: event type 
        x (int): x coordinate
        y (int): y coordinate
    """
    if event == cv2.EVENT_LBUTTONDOWN and 700 <= x <= 800 and 0 <= y <= 40:
        cv2.waitKey(10)
        cap.release()
        cv2.destroyAllWindows()

def main(mp_drawing, mp_pose, cap, screenshots):
    with mp_pose.Pose(min_detection_confidence=0.5,
                    min_tracking_confidence=0.5) as pose:
        counter = 0 
        status = True  # State of move
        start_time = datetime.now()
        
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                logger.warning("Empty frame")
                break
            
            frame = cv2.resize(frame, (800, 480), interpolation=cv2.INTER_AREA)
            # Recolor frame to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame.flags.writeable = False
            # Make detection
            results = pose.process(frame)
            # Recolor back to BGR
            frame.flags.writeable = True
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark
                counter, status, msg = TypeOfExercise(landmarks).calculate_exercise(
                    args["exercise_type"], counter, status)
                if msg:
                    cv2.rectangle(frame, (50, 50), (750, 150), (0, 255, 255), cv2.FILLED)
                    cv2.putText(frame, msg, (60, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2, cv2.LINE_AA)
                    cv2.imwrite(os.path.join(screenshots, f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.jpg"), frame)
            except:
                pass
            
            # Draw the stop button on the top right of the image
            button_color = (92, 98, 254)
            button_text_color = (0, 0, 0)
            cv2.rectangle(frame, (700, 0), (800, 40), button_color, -1, cv2.LINE_AA)
            cv2.putText(frame, "Exit", (720, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, button_text_color, 2, cv2.LINE_AA)

            # Top left of image
            cv2.rectangle(frame, (0, 0), (200, 40), (255, 255, 255), cv2.FILLED)
            cv2.putText(frame, "Activity: " + args["exercise_type"].replace("-", " "),
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
            
            # Bottom left of image
            if counter < 10:
                cv2.rectangle(frame, (0, 350), (80, 480), (255, 255, 255), cv2.FILLED)
            else:
                cv2.rectangle(frame, (0, 350), (160, 480), (255, 255, 255), cv2.FILLED)
            cv2.putText(frame, str(counter), (10, 450),
                        cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 3, cv2.LINE_AA)

            # Render detections (for landmarks)
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
            cv2.setMouseCallback('Gym Robot Trainer', mouse_callback)
            
            # Press q to exit
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        
        logger.info(f"Total number of repetitions: {counter}")
        logger.info(f"Used time: {datetime.now() - start_time}")
        logger.info("Finish exercising. Thanks for using Gym Robot Trainer!")
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-t",
                    "--exercise_type",
                    type=str,
                    help='Type of activity to do',
                    required=True)
    ap.add_argument("-vs",
                    "--video_source",
                    type=str,
                    help='Source of video',
                    required=False)
    args = vars(ap.parse_args())
    
    # Initialize logger
    log_folder = 'logs'
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
        
    screenshots = "screenshots"
    if not os.path.exists(screenshots):
        os.makedirs(screenshots)
        
    now = datetime.now()
    log_file = os.path.join(log_folder, f'feedback-{now.strftime("%Y-%m-%d-%H-%M-%S")}.log')
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')
    logger = logging.getLogger(__name__)
    
    logger.info(f"Starting to do {args['exercise_type']}")

    # Drawing body
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    if args["video_source"] is not None:
        cap = cv2.VideoCapture(args["video_source"])
        logger.info(f"Video source: {args['video_source']}")
    else:
        cap = cv2.VideoCapture(0)  # webcam
        logger.info("Video source: webcam")
    
    cap.set(3, 800)  # width
    cap.set(4, 480)  # height
    
    main(mp_drawing, mp_pose, cap, screenshots)
