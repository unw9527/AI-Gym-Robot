from utils import *

class BodyPartAngle:
    def __init__(self, landmarks):
        self.landmarks = landmarks

    def angle_of_elbow(self):
        left_shoulder = detection_body_part(self.landmarks, "LEFT_SHOULDER") # 11
        left_elbow = detection_body_part(self.landmarks, "LEFT_ELBOW") # 13
        left_wrist = detection_body_part(self.landmarks, "LEFT_WRIST") # 15
        return calculate_angle(left_shoulder, left_elbow, left_wrist)
    
    def angle_of_shoulder(self):
        left_shoulder = detection_body_part(self.landmarks, "LEFT_SHOULDER") # 11
        left_elbow = detection_body_part(self.landmarks, "LEFT_ELBOW") # 13
        left_hip = detection_body_part(self.landmarks, "LEFT_HIP") # 23
        return calculate_angle(left_elbow, left_shoulder, left_hip)
    
    def angle_of_hip(self):
        left_shoulder = detection_body_part(self.landmarks, "LEFT_SHOULDER") # 11
        left_hip = detection_body_part(self.landmarks, "LEFT_HIP") # 23
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE") # 25
        return calculate_angle(left_shoulder, left_hip, left_knee)
    
    def angle_of_knee(self):
        left_hip = detection_body_part(self.landmarks, "LEFT_HIP") # 23
        left_knee = detection_body_part(self.landmarks, "LEFT_KNEE") # 25
        left_ankle = detection_body_part(self.landmarks, "LEFT_ANKLE") # 27
        return calculate_angle(left_hip, left_knee, left_ankle)

    def angle_of_the_abdomen(self):
        # Calculate angle of the avg shoulder
        r_shoulder = detection_body_part(self.landmarks, "RIGHT_SHOULDER")
        l_shoulder = detection_body_part(self.landmarks, "LEFT_SHOULDER")
        shoulder_avg = [(r_shoulder[0] + l_shoulder[0]) / 2,
                        (r_shoulder[1] + l_shoulder[1]) / 2]

        # Calculate angle of the avg hip
        r_hip = detection_body_part(self.landmarks, "RIGHT_HIP")
        l_hip = detection_body_part(self.landmarks, "LEFT_HIP")
        hip_avg = [(r_hip[0] + l_hip[0]) / 2, (r_hip[1] + l_hip[1]) / 2]

        # Calculate angle of the avg knee
        r_knee = detection_body_part(self.landmarks, "RIGHT_KNEE")
        l_knee = detection_body_part(self.landmarks, "LEFT_KNEE")
        knee_avg = [(r_knee[0] + l_knee[0]) / 2, (r_knee[1] + l_knee[1]) / 2]

        return calculate_angle(shoulder_avg, hip_avg, knee_avg)
    
