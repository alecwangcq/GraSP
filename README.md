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

# How to run?
```
# CIFAR-100, VGG19, Pruning ratio = 98%
$ python main_prune_non_imagenet.py --config configs/cifar100/vgg19/GraSP_98.json

# CIFAR-10, VGG19, Pruning ratio = 98%
$ python main_prune_non_imagenet.py --config configs/cifar10/vgg19/GraSP_98.json

# For all the experiments, please refer to the folder configs.
``

