import numpy as np
import matplotlib.pyplot as plt
import torch
from torch.nn import functional as F
plt.rcParams['figure.facecolor'] = '0.2'
plt.rcParams['axes.facecolor'] = 'black'

#hyperparameters
obs = 15
ins = 5
outs = 1
lr = .003

weights = lambda ins, outs: torch.randn(ins,outs).requires_grad_(True)

    
#create non-linear problem
data = np.random.choice(torch.linspace(-10,10,1000), (obs, 1))
data_unique = np.unique(data, axis=0)
ys = data_unique**2
ys = torch.tensor(ys).float()
xs = np.c_[torch.ones(obs), data_unique]
xs = torch.tensor(xs).float()


#define nn structure
w0 = weights(xs.shape[1], 100)
w1 = weights(100, 100) 
w2 = weights(100, ys.shape[1])

optimizer = torch.optim.Adam([w0, w1, w2], lr)


#train the model
err = []
for i in range(5000):
    x0 = xs
    
    #Forward Propagation
    z0 = x0 @ w0; x1 = torch.sin(z0)
    z1 = x1 @ w1; x2 = torch.sin(z1)
    yh = (x2 @ w2)    
    
    #Backward Propagation
    loss = F.mse_loss(yh, ys)
    optimizer.zero_grad()
    
    loss.backward()
    optimizer.step()
    
    
    e  = loss.item()
    
    if i % 500 == 0:
        print('loss', e)   
    err.append(e)

#show the optimization curve
plt.figure(1)
plt.plot(err,color='red', linewidth=1)
plt.title('yhat - ys')

plt.figure(2)
plt.plot(ys,linewidth=10)
plt.plot(yh.detach().numpy())
