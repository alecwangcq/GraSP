# Picking Winning Tickets Before Training by Preserving Gradient Flow
This repo contains the official implementations of [Picking Winning Tickets Before Training by Preserving Gradient Flow](https://openreview.net/forum?id=SkgsACVKPH).

1. The config file for the experiments are under the directory of `configs/`.

# Requirements
python3.6
```
pip install https://download.pytorch.org/whl/cu90/torch-0.4.1-cp36-cp36m-linux_x86_64.whl
pip install torchvision
pip install tqdm
pip install tensorflow
pip install tensorboardX
pip install easydict
```

# Dataset
1. Download tiny imagenet from "https://tiny-imagenet.herokuapp.com", and place it in ../data/tiny_imagenet.
   Please make sure there will be two folders, `train` and `val`,  under the directory of `../data/tiny_imagenet`.
   In either `train` or `val`, there will be 200 folders storing the images of each category.  <b>Or</b> You can also download the processed data from [here]( https://drive.google.com/file/d/1juoN5cRVa8I1TsfFMtsCec2Wy_0z646K/view?usp=sharing ).
   
2. For cifar datasets, it will be automatically downloaded.

# How to run?
```
# CIFAR-100, VGG19, Pruning ratio = 98%
$ python main_prune_non_imagenet.py --config configs/cifar100/vgg19/GraSP_98.json

# CIFAR-10, VGG19, Pruning ratio = 98%
$ python main_prune_non_imagenet.py --config configs/cifar10/vgg19/GraSP_98.json

# For all the experiments, please refer to the folder configs.
```

# Citation
To cite this work, please use
```
@inproceedings{
Wang2020Picking,
title={Picking Winning Tickets Before Training by Preserving Gradient Flow},
author={Chaoqi Wang and Guodong Zhang and Roger Grosse},
booktitle={International Conference on Learning Representations},
year={2020},
url={https://openreview.net/forum?id=SkgsACVKPH}
}
```

