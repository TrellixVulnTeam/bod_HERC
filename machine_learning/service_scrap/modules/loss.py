import torch

def EuclideanLoss(tenserA, tenserB,distent):
    value = 0 
    for i,x in zip(tenserA[0], tenserB[0]):
        value = (i-x)**2 + value
    value = torch.sqrt(value)
    return torch.abs(value) - distent

def MuitEuclideanLoss(tensersA, tensersB,distents):
    loss = None
    for tenserA,tenserB,distent in zip(tensersA, tensersB,distents):
        if loss is None:
            loss = EuclideanLoss(tenserA, tenserB,distent)
        else:
            loss = EuclideanLoss(tenserA, tenserB,distent) + loss
    return torch.max(*loss)
