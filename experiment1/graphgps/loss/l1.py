import torch.nn as nn
from torch_geometric.graphgym.config import cfg
from torch_geometric.graphgym.register import register_loss


def l1_losses(pred, true):
    if cfg.model.loss_fun == 'l1':
        l1_loss = nn.L1Loss()
        loss = l1_loss(pred, true)
        return loss, pred
    if cfg.model.loss_fun == 'l2':
        l2_loss = nn.MSELoss()
        # import pdb; pdb.set_trace()
        loss = l2_loss(pred, true)
        return loss, pred
    elif cfg.model.loss_fun == 'smoothl1':
        l1_loss = nn.SmoothL1Loss()
        loss = l1_loss(pred, true)
        return loss, pred


register_loss('l1_losses', l1_losses)