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
            list: [counter, status, msg]
        """
        elbow_angle = self.angle_of_elbow()
        shoulder_angle = self.angle_of_shoulder()
        hip_angle = self.angle_of_hip()
        msg = ''
        
        # Percentage of success of pushup
        per = np.interp(elbow_angle, (90, 160), (0, 100))
        
        # print(per, elbow_angle, shoulder_angle, hip_angle)
        # print(self.l_shoulder[1], self.l_hip[1], self.l_knee[1], self.l_ankle[1])
        
        # You cannot do push-up while standing up
        if self.l_hip[1] - self.l_shoulder[1] > 0.2:
            # print(self.l_hip[1] - self.l_shoulder[1])
            return [counter, status, msg]
        
        if per < 30:
            if not status:
                if 10 < elbow_angle <= 90 and 10 < shoulder_angle <= 45 and hip_angle > 150:
                    counter += 1
                    logger.info(f"Push-up {counter} done")
                    status = True
                else:
                    if elbow_angle > 100 and 10 < shoulder_angle <= 45 and hip_angle > 140:
                        logger.warning(f"Push-up {counter + 1}: Your elbow angle is too large")
                        msg += "Elbow angle too large. "
                    if 10 < elbow_angle <= 100 and shoulder_angle > 45 and hip_angle > 140:
                        logger.warning(f"Push-up {counter + 1}: Your shoulder angle is too large")
                        msg += "Shoulder angle too large. "
                    if 10 < elbow_angle <= 100 and 10 < shoulder_angle <= 45 and hip_angle <= 140:
                        logger.warning(f"Push-up {counter + 1}: Your hip angle is too small")
                        msg += "Hip angle is too small. "
        elif elbow_angle > 90 and shoulder_angle > 40 and hip_angle > 150 and status:
            status = False
        return [counter, status, msg]

    def squat(self, counter: int, status: bool) -> list:
        """Check whether a squat is done and count the number of squats

        Args:
            counter (int): #squats
            status (bool): whether the squat is finished

        Returns:
            list: [counter, status, msg]
        """
        # You are not doing squat if one of your feet is up
        if abs(self.l_ankle[1] - self.r_ankle[1]) > 0.1:
            return [counter, status]
        
        knee_angle = self.angle_of_knee()
        hip_angle = self.angle_of_hip()
        msg = ''
        
        if knee_angle > 169 and hip_angle > 160:
            status = False
        if not status:
            if 120 < knee_angle <= 169 and 0 < hip_angle <= 120:
                logger.warning(f"Squat {counter + 1}: Your knee angle is too large")
                msg += "Knee angle too large. "
            if 0 < knee_angle <= 120 and hip_angle > 120:
                logger.warning(f"Squat {counter + 1}: Your hip angle is too large")
                msg += "Hip angle too large. "
            if 0 < knee_angle <= 120 and 0 < hip_angle <= 120: # the knee angle is fine-tuned
                status = True
                logger.info(f"Squat {counter + 1} done")
                counter += 1
        return [counter, status, msg]

    def calculate_exercise(self, exercise_type: str, counter: int, status: bool) -> list:
        """Call the corresponding function for the exercise type specified in args

        Args:
            exercise_type (str): "push-up" or "squat"
            counter (int): #push-up/squat done
            status (bool): whether the push-up/squat is finished

        Returns:
            list: [counter, status, msg]
        """
        if exercise_type == "push-up":
            counter, status, msg = TypeOfExercise(self.landmarks).push_up(counter, status)
        elif exercise_type == "squat":
            counter, status, msg = TypeOfExercise(self.landmarks).squat(counter, status)
        return [counter, status, msg]
    
