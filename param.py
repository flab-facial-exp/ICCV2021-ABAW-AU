# About this code
#   This is a code for ICCV2021 ABAW2 AU detection Challenge.
#   Copyright 2021 FUJITSU LIMITED.

import json

au_name = "AU06"
target_dataset_name = "ICCV_v2"
int_occ_mode = "occ"

only_intensity_net_process = False
data_load_path = None


epoch_num = 10
dataset_num_lst = { "Train":10000, "Valid":500, "Test":500 }
intensity_conv_dataset_num_lst = { "Train":10000, "Valid":5000, "Test":5000, "ValidFull":-1, "TestFull":-1 }
intensity_tune_sampling_max = 100000000
trial_num = 5


pairwise_net_optimizer = "Adam"
intensity_net_optimizer = "Adam"

intensity_net_feature_lst = [ "percentile", "conf", "percentile_conf", "pseudo_window", "conf_window" ]

intensity_net_percentile_th_lst = [0.0,0.1,0.2]
intensity_net_conf_th_lst = [ 0.0, 0.25, 0.5, 0.75, 1.0 ]
intensity_net_percentile_window_size_lst = [300,300*2]
intensity_net_pseudo_window_size = 300

pair_net_loss_m = 1
pair_net_loss_m_conf = 1
epsilon = 1.0e-10

pair_net_divide_task = True
pair_net_dataset_only_same_subject = True
pair_net_conf_mode = "separated"

intensity_net_dataset_train_balance = True

corpus_top_dirname = "../../corpus"
dataset_lst_dirname = "./BinaryData"


map_location = 'cuda:0'

batch_size_bin = 32
batch_size_int = 32


if int_occ_mode == "int":
    intensity_level = 6
    measurement_name = "ICC"
else:    
    intensity_level = 2
    measurement_name = "F1"



        
if int_occ_mode == "occ":

    if target_dataset_name.find("ICCV") == 0:
        
        corpus_name = "ICCV"
        phase_full_lst = ["ValidFull","TestFull"]
        pose_lst = [1]
        enable_pair_dataset_equal_test = True
        
        imgs_top_dirname_lst = {}
        imgs_top_dirname_lst["ICCV"] = corpus_top_dirname + "/ICCV/imgs"
        

        dataset_path_lst = {}
        dataset_path_lst["Train"] = {}
        dataset_path_lst["Train"]["posesall"] = {}
        dataset_path_lst["Train"]["posesall"][corpus_name] =  [ (corpus_top_dirname + "/ICCV/labels/labels_for_pytorch_procrustes_occ_pose%d/Train"% pose) for pose in pose_lst ]
        dataset_path_lst["Valid"] = { "pose%d" % pose : {corpus_name:[(corpus_top_dirname + "/ICCV/labels/labels_for_pytorch_procrustes_occ_pose%d/Valid"% pose) ]}  for pose in pose_lst }
        dataset_path_lst["Test"] = { "pose%d" % pose : {corpus_name:[(corpus_top_dirname + "/ICCV/labels/labels_for_pytorch_procrustes_occ_pose%d/Test"% pose)]}  for pose in pose_lst }

        
        intensity_tune_dataset_path_lst = {}
        intensity_tune_dataset_path_lst["Train"] = {}
        intensity_tune_dataset_path_lst["Train"]["posesall"] = {}
        intensity_tune_dataset_path_lst["Train"]["posesall"][corpus_name] = [ (corpus_top_dirname + "/ICCV/labels/labels_for_pytorch_procrustes_occ_pose%d/Train"% pose) for pose in pose_lst ]    
        intensity_tune_dataset_path_lst["Valid"] =  { "pose%d" % pose : { corpus_name: [(corpus_top_dirname + "/ICCV/labels/labels_for_pytorch_procrustes_occ_pose%d/Valid"% pose)]}  for pose in pose_lst }
        intensity_tune_dataset_path_lst["Test"] = { "pose%d" % pose : {corpus_name: [(corpus_top_dirname + "/ICCV/labels/labels_for_pytorch_procrustes_occ_pose%d/Test"% pose)]}  for pose in pose_lst }
        intensity_tune_dataset_path_lst["ValidFull"] =  { "pose%d" % pose : { corpus_name: [(corpus_top_dirname + "/ICCV/labels/labels_for_pytorch_procrustes_occ_pose%d/Valid"% pose)]}  for pose in pose_lst }
        intensity_tune_dataset_path_lst["TestFull"] = { "pose%d" % pose : {corpus_name: [(corpus_top_dirname + "/ICCV/labels/labels_for_pytorch_procrustes_occ_pose%d/Test"% pose)]}  for pose in pose_lst }
        
        partition_filename_lst = { corpus_name: corpus_top_dirname+"/ICCV/partition/partition_%s.json" %  target_dataset_name[len("ICCV_"):] }
        
#         dataset_path_lst["Train"]["posesall"]["BP4Df"] =  [ (corpus_top_dirname + "/BP4Df/labels/labels_for_pytorch_procrustes_int_pose%d/Train"% pose) for pose in range(1,15+1) ]
#         imgs_top_dirname_lst["BP4Df"] = corpus_top_dirname + "/BP4Df/imgs"
#         partition_filename_lst["BP4Df"] = corpus_top_dirname+"/BP4Df/partition/partition_v1.json"    

#         dataset_path_lst["Train"]["posesall"]["BP4Dpf"] =  [ (corpus_top_dirname + "/BP4Dpf/labels/labels_for_pytorch_procrustes_int_pose%d/Train"% pose) for pose in range(1,15+1) ]
#         imgs_top_dirname_lst["BP4Dpf"] = corpus_top_dirname + "/BP4Dpf/imgs"
#         partition_filename_lst["BP4Dpf"] = corpus_top_dirname+"/BP4Dpf/partition/partition_v1.json"

#         dataset_path_lst["Train"]["posesall"]["DISFA"] =  [ (corpus_top_dirname + "/DISFA/tmp/frames_for_pytorch_procrustes_int_pose%d/Train"% pose) for pose in [2] ]
#         partition_filename_lst["DISFA"] = corpus_top_dirname+"/DISFA/partition/partition_all_train_v1.json"

    else:
        raise

else:
    raise


enable_subject_lst = {}

for phase in ["Train","Valid","Test"]:
    enable_subject_lst[phase] = {}
    for pose in dataset_path_lst[phase].keys():
        enable_subject_lst[phase][pose] = {}
        for corpus_name in dataset_path_lst[phase][pose].keys():
            
            fp = open(partition_filename_lst[corpus_name])
            partition_db = json.load(fp)
            fp.close()            
            
            enable_subject_lst[phase][pose][corpus_name] = partition_db[phase]
            
use_valid = False
for pose, db in enable_subject_lst["Valid"].items():
    for db_name, subject_lst in db.items():
        if len(subject_lst) > 0:
            use_valid = True
if use_valid:
    phase_lst = ["Train","Valid","Test"]
else:
    phase_lst = ["Train","Test"]    



    
    
