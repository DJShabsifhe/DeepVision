from TauLidarCommon.frame import FrameType, Frame
from TauLidarCamera.camera import Camera
from TauLidarCamera.constants import VALUE_20MHZ
from TauLidarCommon.color import ColorMode

from Frame import detect_rectangles  # Import the function

import cv2

try:
    print("Attempting to open Tau LiDAR Camera...")
    m_camera = Camera.open()
    print("Camera opened successfully.")

    def open_camera(camera, modulation_channel, integration_time_3d, minimal_amplitude, range_low, range_high, integration_time_grayscale):
        # Fetch info
        m_info = Camera.info(camera)

        model = m_info.model
        firmware = m_info.firmware
        uid = m_info.uid
        resolution = m_info.resolution
        port = m_info.port

        print("\nTauLidarCamera started successfully:")
        print("    model:      %s" % model)
        print("    firmware:   %s" % firmware)
        print("    uid:        %s" % uid)
        print("    resolution: %s" % resolution)
        print("    port:       %s" % port)

        m_camera.setModulationChannel(modulation_channel)
        m_camera.setIntegrationTime3d(0, integration_time_3d)
        m_camera.setMinimalAmplitude(0, minimal_amplitude)
        m_camera.setRange(range_low, range_high)
        m_camera.setIntegrationTimeGrayscale(integration_time_grayscale)

    def __init__():
        open_camera(m_camera, 800, 0, 60, 0, 4500, 15000)
        while True:
            detect_rectangles(m_camera)  # Pass the camera object
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()

except Exception as e:
    print(f"An error occurred: {e}")
