import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
from matplotlib.testing.decorators import image_comparison
import matplotlib.ticker as ticker

def test_sine_wave_plot():
    fig=plt.figure(figsize=(12,3))
    ax=fig.add_subplot(111)
    t=np.linspace(0.0, 2.0 ,200)
    v=np.sin(2.5*np.pi*t)
    ax.set(title='Sine Wave',xlabel='Time (seconds)', ylabel='Voltage (mV)',xlim=(0,2), ylim=(-1,1))
    xmajor=[0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8,2.0]
    ymajor=[-1,0,1]
    plt.xticks(xmajor)
    plt.yticks(ymajor)
    ax.plot(t,v, color='red', label='sin(t)')
    plt.grid(linestyle='--')
    plt.legend()
    plt.savefig('sinewave.png')
    
test_sine_wave_plot()



#Task2

def test_multi_curve_plot():
    fig = plt.figure(figsize=(12,3))
    ax = fig.add_subplot(111)
    x = np.linspace(0.0,5.0,20)
    y1 = x
    y2 = x**2
    y3 = x**3
    ax.set(title='Linear, Quadratic, & Cubic Equations',xlabel='X', ylabel='f(x)')
    ax.plot(x, y1, label='y = x',marker = 'o',color = 'red')
    ax.plot(x, y2, label='y = x**2',marker = "s",color = 'green')
    ax.plot(x, y3, label='y == x**3',marker = "v",color = 'blue')
    plt.legend()
    plt.savefig('multicurve.png')
    
test_multi_curve_plot()    

#Task3
    
def test_scatter_plot():
    fig = plt.figure(figsize=(12,3))
    ax = fig.add_subplot(111)
    s = [50, 60, 55, 50, 70, 65, 75, 65, 80, 90, 93, 95]
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    ax.set(title="Cars Sold by Company 'X' in 2017",xlabel='Months',ylabel='No. of Cars Sold',xlim=(0, 13), ylim=(20,100))
    ax.scatter(months, s,marker = 'o',color = 'red')
    plt.xticks([1, 3, 5, 7, 9,11])
    ax.set_xticklabels(['Jan', 'Mar', 'May', 'Jul', 'Sep','Nov'])
    plt.savefig('scatter.png')
    
    
test_scatter_plot()
