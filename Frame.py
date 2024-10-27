import cv2
import numpy as np
from TauLidarCommon.frame import FrameType, Frame

from TauCamera import m_camera

def show_frame_cv2():
    distanceframe = m_camera.readFrame(FrameType.DISTANCE)
    grayscaleframe = m_camera.readFrame(FrameType.DISTANCE_GRAYSCALE)
    amplitudeframe = m_camera.readFrame(FrameType.DISTANCE_AMPLITUDE)

    processed_frame = distanceframe

    mat_depth_rgb = np.frombuffer(processed_frame.data_depth_rgb, dtype=np.uint16, count=-1, offset=0).reshape(processed_frame.height,
                                                                                                     processed_frame.width, 3)
    mat_depth_rgb = mat_depth_rgb.astype(np.uint8)

    cv2.imshow('Depth Map', mat_depth_rgb)
