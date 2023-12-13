from pathlib import Path
import torch
import torch.utils.data
import os
import glob
import numpy as np
import cv2
from transforms import *
import json, argparse


class WildVSR(object):
    def __init__(self, data_dir,
        convert_gray=True,
        ):

        self._data_dir = data_dir
        self.fps = 25
        self._convert_gray = convert_gray

        self.vid_transform = self.get_video_transform()
        self._data_files = []

        search_str_original = os.path.join(self._data_dir , 'videos', '*.mp4')
        
        self._data_files.extend( glob.glob( search_str_original ) )
        
        labels_path = os.path.join(self._data_dir , 'labels.json')
        
        with open(labels_path, 'r') as file:
            self.labels = json.load(file)
 
        print(len(self._data_files))

        
    def get_video_transform(self):
        """get_video_transform.

        :param speed_rate: float, the speed rate between the frame rate of \
            the input video and the frame rate used for training.
        """

        crop_size = (88, 88)
        (mean, std) = (0.421, 0.165)
    
        return Compose([
            Normalize(0.0, 255.0),
            CenterCrop(crop_size),
            Normalize(mean, std),])
            
    
    def read_video_as_np_array(self, video_path):
        # Open the video file
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            raise IOError(f"Cannot open video file {video_path}")

        # Read the video frame by frame
        frames = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frames.append(frame)

        # Close the video file
        cap.release()

        # Convert the list of frames to a numpy array
        frames_array = np.array(frames)

        return frames_array
    

    def __getitem__(self, idx):    
        
        path_video = self._data_files[idx]
        video_ID = path_video.split('/')[-1]
        raw_data = self.read_video_as_np_array(path_video)
        preprocess_data = torch.FloatTensor(raw_data)
        preprocess_data = self.vid_transform(preprocess_data)

        label =  self.labels[video_ID]
        
        return preprocess_data, label                                                                                                                                                                                                                                               

    
    def __len__(self):
        return len(self._data_files)


def build(args):
    root = Path(args.wildvsr_path)
    assert root.exists(), f'provided WildVSR path {root} does not exist'

    dataset = WildVSR(data_dir=root)
    
    return dataset

def get_args_parser():
    parser = argparse.ArgumentParser('Loading the WildVSR', add_help=False)
    parser.add_argument('--dataset_file', default='wildvsr')
    parser.add_argument('--wildvsr_path', default='', type=str)

    return parser

def main(args):
    wildVSR_test_set = build(args=args)
    # Define  model
    # model.eval()
    for idx in range(len(wildVSR_test_set)):
        clip, label = wildVSR_test_set[idx]
        # Process the clip and label as needed
        #prediction = model(clip)
        #wer_score = wer(prediction, clip)
        print(f"Ground-truth: {label}") # For demonstration purposes

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Loading the WildVSR', parents=[get_args_parser()])
    args = parser.parse_args()
    main(args)