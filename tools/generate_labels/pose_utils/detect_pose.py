# Pose detector.
# Author: Anodev (https://github.com/OPHoperHPO)

# Imports
import os
import cv2
import sys

def init():
    # Try to import OpenPose
    try:
        # Get path from system environment
        OPENPOSE_ROOT = os.environ["OPENPOSE_ROOT"]
        sys.path.append(OPENPOSE_ROOT + '/'+'build/python/');
        from openpose import pyopenpose as op

    except ImportError as e:
        print('Error: OpenPose library could not be found. '
              'Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
        raise e
    # Init OpenPose
    global Data, PoseDetector
    # Set OpenPose parameters
    params = dict()
    params["model_folder"] = OPENPOSE_ROOT + os.sep + "models" + os.sep
    params["face"] = False
    params["hand"] = False
    params["disable_blending"] = True
    # Start OpenPose wrapper
    op_wrapper = op.WrapperPython()
    op_wrapper.configure(params)
    op_wrapper.start()
    # Init Datum object
    Data = op.Datum()
    # Rename op_wrapper
    PoseDetector = op_wrapper


def process(image):
    # Open image file
    img = cv2.imread(image)
    # Send data to OpenPose
    Data.cvInputData = img
    PoseDetector.emplaceAndPop([Data])
    output_image = Data.cvOutputData
    return output_image


def detect(filename):
    # Run process
    img = process(filename)
    return img


# Run initialization
init()
