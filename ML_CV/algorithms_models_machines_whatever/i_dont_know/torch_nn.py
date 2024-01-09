import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.facecolor'] = '0.2'
plt.rcParams['axes.facecolor'] = 'black'
weights = np.random.randn

#hyperparameters
obs = 15
ins = 5
outs = 1
lr = .000001

#create labeled data
# np.random.seed(16)
# data = np.random.randint(0,5, (obs,ins))
# data_unique = np.unique(data, axis=0)
# xs = np.c_[np.ones(obs), data_unique] 
# ys = np.random.choice(list(range(1,10)), (obs, 1))

#create a linear problem
# data = np.random.choice(np.linspace(-10,10,1000), (obs, 1))
# data_unique = np.unique(data, axis=0)
# ys = 3 * data_unique - 2
# xs = np.c_[np.ones(obs), data_unique]

#create non-linear problem
data = np.random.choice(np.linspace(-10,10,1000), (obs, 1))
data_unique = np.unique(data, axis=0)
ys = data_unique**2
xs = np.c_[np.ones(obs), data_unique]


#define nn structure
w0 = weights(xs.shape[1], 20)
w1 = weights(20, 20) 
w2 = weights(20, ys.shape[1])

#train the model
err = []
for i in range(350000):
    x0 = xs
    
    #Forward Propagation
    z0 = x0 @ w0; x1 = np.sin(z0)
    z1 = x1 @ w1; x2 = np.sin(z1)
    yh = (x2 @ w2)    
    
    #Backward Propagation
    e  = (yh - ys) * 1
    e2 = (e)
    e1 = (e2 @ w2.T) * np.cos(z1)
    e0 = (e1 @ w1.T) * np.cos(z0)
    
    #Update path
    w2 -= (x2.T @ e2) * lr
    w1 -= (x1.T @ e1) * lr
    w0 -= (x0.T @ e0) * lr 
    
    e  = np.sum(np.abs(e))
    
    if e < .01:
        break
    err.append(e)

#show the optimization curve
plt.figure(1)
plt.plot(err,color='red', linewidth=1)
plt.title('yhat - ys')

plt.figure(2)
plt.plot(ys,linewidth=10)
plt.plot(yh)
