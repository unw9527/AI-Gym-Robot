#################################################################################
#
# tab:4
#
# types_of_exercise.py: define the counting rules for each exercise
# 
# Author:          Kunle Li
# Creation Date:   2023-03-29
#
#################################################################################

from body_part_angle import BodyPartAngle
from utils import *


class TypeOfExercise(BodyPartAngle):
    def __init__(self, landmarks):
        super().__init__(landmarks)

    def push_up(self, counter: int, status: int) -> list:
        elbow_angle = self.angle_of_elbow()
        shoulder_angle = self.angle_of_shoulder()
        hip_angle = self.angle_of_hip()
        
        # Percentage of success of pushup
        per = np.interp(elbow_angle, (90, 160), (0, 100))
        
        # Check to ensure right form before starting the program
        # print(elbow_angle, shoulder_angle, hip_angle, counter, per)
        if per == 0:
            if elbow_angle <= 90 and hip_angle > 160:
                if not status:
                    counter += 1
                    status = True
        elif per == 100:
            if elbow_angle > 160 and shoulder_angle > 40 and hip_angle > 160:
                if status:
                    status = False
        return [counter, status]

    def squat(self, counter: int, status: int) -> list:
        knee_angle = self.angle_of_knee()
        
        if knee_angle > 169:
            status = False
        if knee_angle <= 110 and status == False: # the knee angle is fine-tuned
            status = True
            counter += 1
        return [counter, status]


    def calculate_exercise(self, exercise_type: str, counter: int, status: int):
        if exercise_type == "push-up":
            counter, status = TypeOfExercise(self.landmarks).push_up(counter, status)
        elif exercise_type == "squat":
            counter, status = TypeOfExercise(self.landmarks).squat(counter, status)
        return [counter, status]
