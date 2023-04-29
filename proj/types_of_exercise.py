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
        """Check whether a push-up is done and count the number of push-ups

        Args:
            counter (int): #push-ups
            status (int): whether the push-up is finished

        Returns:
            list: [counter, status]
        """
        self.check_body_position()
        elbow_angle = self.angle_of_elbow()
        shoulder_angle = self.angle_of_shoulder()
        hip_angle = self.angle_of_hip()
        
        # Percentage of success of pushup
        per = np.interp(elbow_angle, (90, 160), (0, 100))
        
        # print(per, elbow_angle, shoulder_angle, hip_angle)
        # print(self.l_shoulder[1], self.l_hip[1], self.l_knee[1], self.l_ankle[1])
        
        # You cannot do push-up while standing up
        if self.l_hip[1] - self.l_shoulder[1] > 0.1:
            return [counter, status]
        
        if per == 0:
            if 10 < elbow_angle <= 90 and 10 < shoulder_angle <= 40 and hip_angle > 150:
                if not status:
                    counter += 1
                    status = True
        else:
            if elbow_angle > 90 and shoulder_angle > 40 and hip_angle > 150:
                if status:
                    status = False
        return [counter, status]

    def squat(self, counter: int, status: int) -> list:
        """Check whether a squat is done and count the number of squats

        Args:
            counter (int): #squats
            status (int): whether the squat is finished

        Returns:
            list: [counter, status]
        """
        knee_angle = self.angle_of_knee()
        
        if knee_angle > 169:
            status = False
        if knee_angle <= 110 and status == False: # the knee angle is fine-tuned
            status = True
            counter += 1
        return [counter, status]

    def calculate_exercise(self, exercise_type: str, counter: int, status: int) -> list:
        """Call the corresponding function for the exercise type specified in args

        Args:
            exercise_type (str): "push-up" or "squat"
            counter (int): #push-up/squat done
            status (int): whether the push-up/squat is finished

        Returns:
            list: [counter, status]
        """
        if exercise_type == "push-up":
            counter, status = TypeOfExercise(self.landmarks).push_up(counter, status)
        elif exercise_type == "squat":
            counter, status = TypeOfExercise(self.landmarks).squat(counter, status)
        return [counter, status]
    
    def check_body_position(self):
        """Check whether all body parts can be seen
        """
        for joint in self.body_parts:
            if self.body_parts[joint][2] < 0.7:
                print(f"Cannot see your {joint}!")
