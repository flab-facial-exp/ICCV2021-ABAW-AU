# Action Unit Recognition by Improved Pairwise Deep Architecture
This is a code for ICCV2021 ABAW2 AU detection Challenge.

Paper link is [here](https://)

# Tested environment
- software
  - python 3.7.8
  - pytorch 1.3.1
  - scipy 1.6.2
  - numpy 1.20.2
  - jupyterlab 3.0.16
- hardware
  - AWS g3s.xlarge (GPU is needed)

# How to run
- (1) prepare datasets
  - Aff-Wild2
  - BP4D, BP4D+
    - 15 face orientations ( 9 face orientations like FERA2017 and 6 mirrored orientations ) from 3D data
  - DISFA
- (2) preprocess images
  - face detection
    - MTCNN
  - image normalization
    - perform procrustes analysis
      - ref: https://www.mathworks.com/help/stats/procrustes.html
      - ref: K. Niinuma, L. A. Jeni, I. O. Ertugrul, and J. F. Cohn, “Unmasking the devil in the details: What works for deep facial action coding?,” in BMVC: proceedings of the British Machine Vision Conference. British Machine Vision Conference, 2019.
  - resizing
    - resize all images to 224x224 (VGG16 input size)
- (3) locate datasets
  - locate datasets as followings
    - Aff-Wild2
      - ~/corpus/ICCV/imgs/ICCV_TR_(VIDEO_ID)_(TASK_ID)_(POSE_ID)_frame(FRAME_ID).jpg
        - POSE_ID: 1
        - VIDEO_ID: 1-30-1280x720, ...
        - TASK_ID: T1
        - FRAME_ID: 000000, ...
      - ~/corpus/ICCV/labels/labels_for_pytorch_procrustes_occ_pose1/(MODE_ID)/(AU_ID)/ICCV_TR_(VIDEO_ID)_(TASK_ID)_(POSE_ID)_(AU_ID)_Occ.csv
        - MODE_ID: Train, Valid, Test
        - AU_ID: AU01,...
        - POSE_ID: 1
        - VIDEO_ID: 1-30-1280x720, ...
        - TASK_ID: T1
        - FRAME_ID: 000000, ...
        - [csv format]: frame id and occurrence (0 or 1)
           - frame000000,0
           - frame000001,0
           - ...
      - ~/corpus/ICCV/partition/partition_v2.json
         - set VIDEO_ID for each MODE_ID as followings
         - { "Train":\["1-30-1280x720",...\], "Valid":\[...\], "Test":\[...\] }
    - For other datasets, make as Aff-Wild2 dataset
- (4) locate and run the program (au_abaw2.ipynb, param.py)
  - locate the program to ~/au/abaw2/
  - set parameters at param.py
  - run au_abaw2.ipynb by jupyterlab
- (5) confirm result
  - result csv file path
    - validation set
      - ~/au/abaw2/pred_result/pred_result__(au_name)_procrustes-intensity-pose1_ValidFull.csv
      - ~/au/abaw2/pred_result/pred_result__(au_name)_procrustes-intensity-pose1_ValidFull_raw.csv  # before quantization
    - test set
      - ~/au/abaw2/pred_result/pred_result__(au_name)_procrustes-intensity-pose1_TestFull.csv
      - ~/au/abaw2/pred_result/pred_result__(au_name)_procrustes-intensity-pose1_TestFull_raw.csv  # before quantization
  - format
    - column 0: path ( image file path )
    - column 1: label ( for test set, dummy data )
    - column 2: pred ( this is prediction result )

# Copyright
Copyright 2021 FUJITSU LIMITED.
