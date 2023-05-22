#################################################################################
#
# tab:4
#
# body_part_angle.py: calculate the angle of body parts
# 
# Author:          Kunle Li
# Creation Date:   2023-03-29
# Last Update:     2023-04-20
#
#################################################################################

from utils import *

class BodyPartAngle:
    def __init__(self, landmarks):
        self.landmarks = landmarks
        self.body_parts = detection_body_parts(self.landmarks)
        self.l_shoulder = self.body_parts['LEFT_SHOULDER'] # 11
        self.l_elbow = self.body_parts['LEFT_ELBOW'] # 13
        self.l_wrist = self.body_parts['LEFT_WRIST'] # 15
        self.r_shoulder = self.body_parts['RIGHT_SHOULDER'] # 12
        self.r_elbow = self.body_parts['RIGHT_ELBOW'] # 14
        self.r_wrist = self.body_parts['RIGHT_WRIST'] # 16
        self.l_hip = self.body_parts['LEFT_HIP'] # 23
        self.r_hip = self.body_parts['RIGHT_HIP'] # 24
        self.l_knee = self.body_parts['LEFT_KNEE'] # 25
        self.r_knee = self.body_parts['RIGHT_KNEE'] # 26
        self.l_ankle = self.body_parts['LEFT_ANKLE'] # 27
        self.r_ankle = self.body_parts['RIGHT_ANKLE'] # 28
        
        
    def angle_of_elbow(self):
        return max(calculate_angle(self.l_shoulder, self.l_elbow, self.l_wrist), calculate_angle(self.r_shoulder, self.r_elbow, self.r_wrist))
    
    def angle_of_shoulder(self):
        return max(calculate_angle(self.l_elbow, self.l_shoulder, self.l_hip), calculate_angle(self.r_elbow, self.r_shoulder, self.r_hip))
    
    def angle_of_hip(self):
        return max(calculate_angle(self.l_shoulder, self.l_hip, self.l_knee), calculate_angle(self.r_shoulder, self.r_hip, self.r_knee))
    
    def angle_of_knee(self):
        return max(calculate_angle(self.l_hip, self.l_knee, self.l_ankle), calculate_angle(self.r_hip, self.r_knee, self.r_ankle))

