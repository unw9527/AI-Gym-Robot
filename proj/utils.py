#################################################################################
#
# tab:4
#
# utils.py: utilities
# 
# Author:          Kunle Li
# Creation Date:   2023-03-29
# Last Update:     2023-04-20
#
#################################################################################

import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose

def calculate_angle(a: list, b: list, c: list) -> int:
    """Calculate the angle of the triangle formed by the three points.
    
    Args:
        a: [x, y, visibility]

    Returns:
        int: angle in degrees
    """
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End
    
    # Prevent low confidence guess
    for i in [a, b, c]:
        # print(i[2]) # Confidence
        if i[2] < 0.8:
            return 0

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) -\
              np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    # Calculate complementary angle
    if angle < 0:
        angle += 360
        if angle > 180:
            angle = 360 - angle
    elif angle > 180:
        angle = 360 - angle

    return angle


def detection_body_parts(landmarks) -> dict:
    """Detect all body parts from landmarks.

    Args:
        landmarks: landmarks from mediapipe

    Returns:
        dict: {body_part_name: [x, y, visibility]}
    """
    body_parts = {}

    for lndmrk in mp_pose.PoseLandmark:
        body_part_name = str(lndmrk).split(".")[1] # body_part_name is e.g. "NOSE"
        body_parts[body_part_name] = [
            landmarks[mp_pose.PoseLandmark[body_part_name].value].x,
            landmarks[mp_pose.PoseLandmark[body_part_name].value].y,
            landmarks[mp_pose.PoseLandmark[body_part_name].value].visibility
        ]

    return body_parts
