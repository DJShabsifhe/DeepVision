import cv2
import numpy as np
from TauLidarCommon.frame import FrameType

def detect_rectangles(camera):
    # Capture both distance and grayscale frames
    distance_frame = camera.readFrame(FrameType.DISTANCE)
    grayscale_frame = camera.readFrame(FrameType.DISTANCE_GRAYSCALE)
    
    # Convert the distance data to a grayscale image
    mat_distance = np.frombuffer(distance_frame.data_depth, dtype=np.uint16).reshape(distance_frame.height, distance_frame.width)
    mat_distance = cv2.normalize(mat_distance, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    # Convert the grayscale data to a grayscale image
    mat_grayscale = np.frombuffer(grayscale_frame.data, dtype=np.uint8).reshape(grayscale_frame.height, grayscale_frame.width)

    # Combine the distance and grayscale images
    combined = cv2.addWeighted(mat_distance, 0.5, mat_grayscale, 0.5, 0)

    # Apply a threshold to get a binary image
    _, thresh = cv2.threshold(combined, 50, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over the contours to find rectangles
    for contour in contours:
        # Approximate the contour to a polygon
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Check if the approximated contour has four points (rectangle)
        if len(approx) == 4:
            # Draw the rectangle on the combined image
            cv2.drawContours(combined, [approx], 0, (255, 0, 0), 2)

    # Display the result
    cv2.imshow('Rectangles', combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
