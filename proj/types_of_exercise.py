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
import logging

logger = logging.getLogger(__name__)

class TypeOfExercise(BodyPartAngle):
    def __init__(self, landmarks):
        super().__init__(landmarks)

    def push_up(self, counter: int, status: bool) -> list:
        """Check whether a push-up is done and count the number of push-ups

        Args:
            counter (int): #push-ups
            status (bool): whether the push-up is finished

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
            if not status:
                if 10 < elbow_angle <= 90 and 10 < shoulder_angle <= 40 and hip_angle > 150:
                    counter += 1
                    logger.info(f"Push-up {counter} done")
                    status = True
                else:
                    if elbow_angle > 90 and 10 < shoulder_angle <= 40 and hip_angle > 150:
                        logger.warning(f"Push-up {counter + 1}: Your elbow angle is too large")
                    if 10 < elbow_angle <= 90 and shoulder_angle > 40 and hip_angle > 150:
                        logger.warning(f"Push-up {counter + 1}: Your shoulder angle is too large")
                    if 10 < elbow_angle <= 90 and 10 < shoulder_angle <= 40 and hip_angle <= 150:
                        logger.warning(f"Push-up {counter + 1}: Your hip angle is too small")
        else:
            if elbow_angle > 90 and shoulder_angle > 40 and hip_angle > 150:
                if status:
                    status = False
        return [counter, status]

    def squat(self, counter: int, status: bool) -> list:
        """Check whether a squat is done and count the number of squats

        Args:
            counter (int): #squats
            status (bool): whether the squat is finished

        Returns:
            list: [counter, status]
        """
        # print(self.l_ankle[1], self.r_ankle[1])
        # You are not doing squat if one of your feet is up
        if abs(self.l_ankle[1] - self.r_ankle[1]) > 0.1:
            return [counter, status]
        
        knee_angle = self.angle_of_knee()
        hip_angle = self.angle_of_hip()
        # print(knee_angle, hip_angle)
        
        if knee_angle > 169 and hip_angle > 160:
            status = False
        if 0 < knee_angle <= 120 and 0 < hip_angle <= 120 and status == False: # the knee angle is fine-tuned
            status = True
            counter += 1
        return [counter, status]

    def calculate_exercise(self, exercise_type: str, counter: int, status: bool) -> list:
        """Call the corresponding function for the exercise type specified in args

        Args:
            exercise_type (str): "push-up" or "squat"
            counter (int): #push-up/squat done
            status (bool): whether the push-up/squat is finished

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
        # for joint in self.body_parts:
        #     if self.body_parts[joint][2] < 0.7:
        #         print(f"Cannot see your {joint}!") # TODO add warning sound
        pass
