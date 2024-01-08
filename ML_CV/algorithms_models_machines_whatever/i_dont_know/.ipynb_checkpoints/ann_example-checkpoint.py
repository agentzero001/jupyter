import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.facecolor'] = '0.2'
plt.rcParams['axes.facecolor'] = 'black'

weights = np.random.randn

obs = 15
np.random.seed(15)
data = np.random.randint(0,5, (obs,5))
data_unique = np.unique(data, axis=0)
xs = np.c_[np.ones(obs), data_unique] 

ys = np.random.choice(list(range(1,10)), (obs, 1))

ins = 5
outs = 1
lr = .0001

w0 = weights(ins+1, 10)
w1 = weights(10, 5) 
w2 = weights(5, outs)
err = []

#xs.shape, w0.shape, w1.shape, w2.shape, ys.shape

for i in range(50000):
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

plt.plot(err,color='red', linewidth=1)
plt.title('yhat - ys')
plt.show()
