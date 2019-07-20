# Pose2Pose video label generator from videofile.
# Module version: 2.0.7 [Public][New]
# Author: Anodev (https://github.com/OPHoperHPO)

# Imports
import os
import cv2
import argparse
from tqdm import tqdm
from pose_utils.detect_pose import detect


# Define functions
def main(args):
    """Marks a body pose and writes a landmark to an image file."""
    # Open file
    video = cv2.VideoCapture(args.filename)
    # Get total frames
    video_length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print('Total frames: ', video_length)
    # Run processing
    for i in tqdm(range(1, video_length+1), ascii=True, desc='Frame Marking', unit='frame'):
        try:
            # Get frame from video file
            ret, frame = video.read()
            # Resize frame for fast frame processing
            frame_resized = cv2.resize(frame, (1024, 512), interpolation=cv2.INTER_CUBIC)
        except Exception as e:
            break
        # Write frame to the temp folder
        cv2.imwrite('temp/' + args.temp_filename, frame_resized)
        if os.path.exists('temp/' + args.temp_filename) and os.path.getsize('temp/' + args.temp_filename) != 0:
            # Get label image
            label = detect('temp/' + args.temp_filename)
            # Save images
            cv2.imwrite("pose2pose/test_A/{}.png".format(i), label)
            cv2.imwrite("pose2pose/original/{}.png".format(i), frame_resized)
            # Remove temp file
            os.remove('temp/' + args.temp_filename)
        else:
            break
    # Remove temp folder
    clean(args)


def clean(args):
    """Cleans the trash."""
    try:
        os.rmdir('temp/')
    except Exception as e:
        try:
            os.remove('temp/', args.temp_filename)
            os.rmdir('temp/')
        except Exception as e:
            print('Clean was failed! Error: ', e)


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', dest='filename', type=str, help='Name of the video file.')
    parser.add_argument('--temp_file', dest='temp_filename', default='temp.jpg',
                        type=str, help='Name of the image temp file.')
    args = parser.parse_args()
    if args.filename is None:
        print('Please specify a video file with the argument "--file"')
        exit(1)
    # Create dirs if dirs don't exists
    if not os.path.exists(os.path.join('./pose2pose', 'test_label')):
        os.makedirs(os.path.join('./pose2pose', 'test_label'))

    if not os.path.exists(os.path.join('./pose2pose', 'original')):
        os.makedirs(os.path.join('./pose2pose', 'original'))

    if not os.path.exists(os.path.join('./', 'temp')):
        os.makedirs(os.path.join('./', 'temp'))

    # Run frame marking
    main(args)
