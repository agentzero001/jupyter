import matplotlib.pyplot as plt
import numpy as np
import statistics
import scipy.stats

def boxplot(data):
    '''Input data has to be a list of positive numbers'''
    
    print(scipy.stats.describe(data))
    
    mean = statistics.fmean(data)
    hmean = statistics.harmonic_mean(data)
    gmean = statistics.geometric_mean(data)
    median = statistics.median(data)
    
    plt.figure(facecolor='0.6',figsize=(10,1.1),dpi=300)
    plt.axes().set_facecolor('0.4')
    plt.axis([min(data)-2,max(data)+2,-0.5,0.5])

    plt.scatter(data,np.zeros(len(data)),color = 'black',zorder=2)
    plt.axvline(x = gmean,color='red', linestyle='--',label='gmean')
    plt.axvline(x = hmean,color='blue', linestyle='--',zorder=1,label='hmean')
    plt.axvline(x = mean,color='purple', linestyle='--',label='armean')
    plt.axvline(x = median,color='yellow', linestyle='--',label='median')
    
    plt.yticks(np.arange(0))
    plt.legend(loc='lower right',prop={'size': 3})
    plt.legend().get_frame().set_alpha(0.1)
    plt.grid()
    plt.show()

def boxplot2(data,prop,p=0):

    plt.figure(facecolor='0.6',figsize=(10,1.1),dpi=300)
    plt.axes().set_facecolor('0.4')
    plt.axis([min(data)-2,max(data)+2,-0.5,0.5])
    plt.scatter(data,np.zeros(len(data)),color = 'black',zorder=2)   
    
    
    if prop == 'gmean':
        gmean = statistics.geometric_mean(data)
        plt.axvline(x = gmean,color='red', linestyle='--',label='gmean')
    elif prop == 'hmean':
        hmean = statistics.harmonic_mean(data)
        plt.axvline(x = hmean,color='blue', linestyle='--',zorder=1,label='hmean')
    elif prop == 'median':
        median = statistics.median(data)
        plt.axvline(x = median,color='yellow', linestyle='--',label='median')
    elif prop == 'mean':
        mean = statistics.fmean(data)
        plt.axvline(x = mean,color='purple', linestyle='--',label='armean')
    elif prop == 'quantil':
        L = statistics.quantiles(data,n=p)
        plt.axhline(y=20,label='quantiles',color='red', linestyle='--')
        for i in range(p-1):
            plt.axvline(x = L[i],color='red', linestyle='--')

    
    plt.yticks(np.arange(0))
    plt.legend(loc='lower right',prop={'size': 3})
    plt.legend().get_frame().set_alpha(0.1)
    plt.grid()
    plt.show()