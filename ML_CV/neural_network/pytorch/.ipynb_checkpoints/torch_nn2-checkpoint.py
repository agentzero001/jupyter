import torch
import torch.nn.functional as F
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch import nn, optim, Tensor as t
from torch.utils.data import DataLoader 
import matplotlib.pyplot as plt
import numpy as np


class NN(nn.Module):
    def __init__(self, input_size, num_classes):
        super(NN, self).__init__()
        self.fc1 = nn.Linear(input_size, 50)
        self.fc2 = nn.Linear(50, num_classes)
        
    def Forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
    
model = NN(784, 10)
x = torch.randn(64, 784)

model.Forward(x)

        

# mnist_path = './data'
# train_dataset = datasets.MNIST(root=mnist_path, train=True, download=True)
# test_dataset = datasets.MNIST(root=mnist_path, train=False, download=True)
# img, label = train_dataset[0]
# to_tensor = transforms.ToTensor()
# tensor_img = to_tensor(img)
