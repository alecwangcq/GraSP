from models.base import (VGG,
                         resnet)


def get_network(network, depth, dataset, use_bn=True):
    if network == 'vgg':
        print('Use batch norm is: %s' % use_bn)
        return VGG(depth=depth, dataset=dataset, batchnorm=use_bn)
    elif network == 'resnet':
        return resnet(depth=depth, dataset=dataset)
    else:
        raise NotImplementedError('Network unsupported ' + network)


def stablize_bn(net, trainloader, device='cuda'):
    """Iterate over the dataset for stabilizing the
    BatchNorm statistics.
    """
    net = net.train()
    for batch, (inputs, _) in enumerate(trainloader):
        inputs = inputs.to(device)
        net(inputs)