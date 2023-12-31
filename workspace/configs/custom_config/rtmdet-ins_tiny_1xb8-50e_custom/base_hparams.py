# -*- coding: utf-8 -*-
# @Author: Luis Condados
# @Date:   2023-07-02 22:51:00
# @Last Modified by:   Luis Condados
# @Last Modified time: 2023-07-03 02:04:50

# dataloader hparams

_base_ = '../../dataset/shoes_dataset_metainfo.py'

data_root = '/workspace/datasets/shoes_cv'
train_images_dir = 'train/'
train_annotation_file = 'train/_annotations.coco.json'

val_images_dir = 'valid/'
val_annotation_file = 'valid/_annotations.coco.json'

test_images_dir = 'test/'
test_annotation_file = 'test/_annotations.coco.json'

val_evaluator_annotation_file = f'{data_root}/{val_annotation_file}'
test_evaluator_annotation_file = val_evaluator_annotation_file


imsize = (640, 640)
batch_size = 34
num_workers= 10

# train and testing hparams
max_epochs = 100
base_lr = 0.004

stage2_num_epochs = 20

eval_interval = 1

# model hparams
checkpoint = '/workspace/mmdetection_lightly_ssl/configs/base_config/rtmdet-ins_tiny_8xb32-300e_coco_20221130_151727-ec670f7e.pth'
load_from = checkpoint

# optimization hparams
param_scheduler_begin = max_epochs//2

# hooks hparams
log_interval = 50
save_checkpoint_interval = 1
switch_epoch = max_epochs//2  # when to swtich to a different data pipeline