import numpy as np
from body_part_angle import BodyPartAngle
from utils import *


class TypeOfExercise(BodyPartAngle):
    def __init__(self, landmarks):
        super().__init__(landmarks)

    def push_up(self, counter, status):
        left_shoulder = detection_body_part(self.landmarks, "LEFT_SHOULDER") # 11
        left_elbow = detection_body_part(self.landmarks, "LEFT_ELBOW") # 13
        left_wrist = detection_body_part(self.landmarks, "LEFT_WRIST") # 15
        left_hip = detection_body_part(self.landmarks, "LEFT_HIP") # 23
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE") # 25
        
        elbow_angle = calculate_angle(left_shoulder, left_elbow, left_wrist)
        shoulder_angle = calculate_angle(left_elbow, left_shoulder, left_hip)
        hip_angle = calculate_angle(left_shoulder, left_hip, left_knee)
        
        # Percentage of success of pushup
        per = np.interp(elbow_angle, (90, 160), (0, 100))
        
        # Check to ensure right form before starting the program
        print(elbow_angle, shoulder_angle, hip_angle, counter, per)
            
        if per == 0:
            if elbow_angle <= 90 and hip_angle > 160:
                if not status:
                    counter += 0.5
                    status = True
                
        elif per == 100:
            if elbow_angle > 160 and shoulder_angle > 40 and hip_angle > 160:
                if status:
                    counter += 0.5
                    status = False

        return [counter, status]

    def pull_up(self, counter, status):
        nose = detection_body_part(self.landmarks, "NOSE")
        left_elbow = detection_body_part(self.landmarks, "LEFT_ELBOW")
        right_elbow = detection_body_part(self.landmarks, "RIGHT_ELBOW")
        avg_shoulder_y = (left_elbow[1] + right_elbow[1]) / 2

        if status:
            if nose[1] > avg_shoulder_y:
                counter += 1
                status = False
        else:
            if nose[1] < avg_shoulder_y:
                status = True
        return [counter, status]

    def squat(self, counter, status):
        hip = detection_body_part(self.landmarks, "LEFT_HIP")
        knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        ankle = detection_body_part(self.landmarks, "LEFT_ANKLE")
        
        knee_angle = calculate_angle(hip, knee, ankle)
        
        if knee_angle > 169:
            status = "UP"
        if knee_angle <= 110 and status =='UP': # the knee angle is fine-tuned
            status="DOWN"
            counter +=1
        return [counter, status]

    def walk(self, counter, status):
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")

        if status:
            if left_knee[0] > right_knee[0]:
                counter += 1
                status = False
        else:
            if left_knee[0] < right_knee[0]:
                counter += 1
                status = True
        return [counter, status]

    def sit_up(self, counter, status):
        angle = self.angle_of_the_abdomen()
        if status:
            if angle < 55:
                counter += 1
                status = False
        else:
            if angle > 105:
                status = True
        return [counter, status]
    
    def Skipping(self, counter, status):
        right_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE")

        if status:
            if left_knee[0] > right_knee[0]:
                counter += 1
                status = False
        else:
            if left_knee[0] < right_knee[0]:
                counter += 1
                status = True
        return [counter, status]

    def calculate_exercise(self, exercise_type, counter, status):
        if exercise_type == "push-up":
            counter, status = TypeOfExercise(self.landmarks).push_up(counter, status)
        elif exercise_type == "pull-up":
            counter, status = TypeOfExercise(self.landmarks).pull_up(counter, status)
        elif exercise_type == "squat":
            counter, status = TypeOfExercise(self.landmarks).squat(counter, status)
        elif exercise_type == "walk":
            counter, status = TypeOfExercise(self.landmarks).walk(counter, status)
        elif exercise_type == "sit-up":
            counter, status = TypeOfExercise(self.landmarks).sit_up(counter, status)
        elif exercise_type == "Skipping":
            counter, status = TypeOfExercise(self.landmarks).Skipping(counter, status)
        return [counter, status]
