from TauLidarCommon.frame import FrameType, Frame
from TauLidarCamera.camera import Camera
from TauLidarCamera.constants import VALUE_20MHZ
from TauLidarCommon.color import ColorMode

from Frame import show_frame_cv2

m_camera = Camera.open()

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
    show_frame_cv2()
