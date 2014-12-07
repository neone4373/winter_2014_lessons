# Whats Next

So now you have your Python stack up and running, and even your iPython window taunting you to do some cool stuff.  Here are a couple sample visualizations to get you going and give you a taste of just how powerful this setup is.

## Import statement

I like to add these to individual cell at the top on the off chance I add more libraries later.

```python
import numpy as np
import pandas as pd
import matplotlib.dates as dates
import matplotlib.mlab as mlab
from mpl_toolkits.mplot3d import Axes3D
from sklearn import mixture
```

## Bar Charts

This example generates some random data male and female data and then displays it in bar chart format.

```python
N = 5
menMeans   = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd     = (2, 3, 4, 1, 2)
womenStd   = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans,   width, color='r', yerr=womenStd)
p2 = plt.bar(ind, womenMeans, width, color='y',
             bottom=menMeans, yerr=menStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind+width/2., ('G1', 'G2', 'G3', 'G4', 'G5') )
plt.yticks(np.arange(0,81,10))
plt.legend( (p1[0], p2[0]), ('Men', 'Women') )
```

## Time Series

Here we display some simple time series data that is again randomly generated.  

```python
idx = pd.date_range('2011-05-01', '2011-07-01')
s = pd.Series(np.random.randn(len(idx)), index=idx)

fig, ax = plt.subplots()
ax.plot_date(idx, s, 'v-')
ax.xaxis.set_minor_locator(dates.WeekdayLocator(byweekday=(1),
                                                interval=1))
ax.xaxis.set_minor_formatter(dates.DateFormatter('%d\n%a'))
ax.xaxis.grid(True, which="minor")
ax.yaxis.grid()
ax.xaxis.set_major_locator(dates.MonthLocator())
ax.xaxis.set_major_formatter(dates.DateFormatter('\n\n\n%b\n%Y'))
# idx
plt.tight_layout()
```

## Advanced Fun

This example creates random sample of data which is actually a comprised of two different normally distributed distribution.  The statistical term for this is would be a Gaussian Mixture Model.  Examples this advanced should serve as inspiration for the kinds of problems machine learning can solve.

```python
def q(x, y):
    g1 = mlab.bivariate_normal(x, y, 1.0, 1.0, -1, -1, -0.8)
    g2 = mlab.bivariate_normal(x, y, 1.5, 0.8, 1, 2, 0.6)
    return 0.6*g1+28.4*g2/(0.6+28.4)
 
def plot_q():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.arange(-5, 5, 0.1)
    Y = np.arange(-5, 5, 0.1)
    X, Y = np.meshgrid(X, Y)
    Z = q(X, Y)
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('coolwarm'),
            linewidth=0, antialiased=True)
    fig.colorbar(surf, shrink=0.5, aspect=5)
 
#     plt.savefig('3dgauss.png')
    plt.show()
    plt.clf()
 
def sample():
    '''Metropolis Hastings'''
    N = 10000
    s = 10
    r = np.zeros(2)
    p = q(r[0], r[1])
    print p
    samples = []
    for i in xrange(N):
        rn = r + np.random.normal(size=2)
        pn = q(rn[0], rn[1])
        if pn >= p:
            p = pn
            r = rn
        else:
            u = np.random.rand()
            if u < pn/p:
                p = pn
                r = rn
        if i % s == 0:
            samples.append(r)
 
    samples = np.array(samples)
    plt.scatter(samples[:, 0], samples[:, 1], alpha=0.5, s=1)
 
    '''Plot target'''
    dx = 0.01
    x = np.arange(np.min(samples), np.max(samples), dx)
    y = np.arange(np.min(samples), np.max(samples), dx)
    X, Y = np.meshgrid(x, y)
    Z = q(X, Y)
    CS = plt.contour(X, Y, Z, 10, alpha=0.5)
    plt.clabel(CS, inline=1, fontsize=10)
#     plt.savefig("samples.png")
#     plt.show()
    return samples

def fit_samples(samples):
    gmix = mixture.GMM(n_components=2, covariance_type='full')
    gmix.fit(samples)
    print gmix.means_
    colors = ['r' if i==0 else 'g' for i in gmix.predict(samples)]
    ax = plt.gca()
    ax.scatter(samples[:,0], samples[:,1], c=colors, alpha=0.5)
#     plt.show()
    
plot_q()
s = sample()
fit_samples(s)
```