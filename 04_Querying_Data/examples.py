# classwork 1
baseball_x.index = baseball_x.index + baseball.team
baseball_x.head()

# classwork 2

slg = lambda x: (x['h']-x['X2b']-x['X3b']-x['hr'] + 2*x['X2b'] + 3*x['X3b'] + 4*x['hr'])/(x['ab']+1e-6)
p3d = lambda x: '%.3f' % x 

baseball['SLG'] = baseball.apply(slg, axis=1).apply(p3d)
baseball['SLG']

