'''
Created on Dec 9, 2011

@author: cma330
'''

import matplotlib.pyplot as plt
import sys, fileinput, datetime

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print "usage: %s <filename>+" % sys.argv[0]
        sys.exit(-1)
    
    print sys.argv[1:]
    
    times = []
    points = []
    for filename in sys.argv[1:]:
        p = 0
        pts  = []
        time = []
        print "Processing %s" % filename
        for line in open(filename, "r"):
            (ts, data) = line.split()
            p = p + 1
            t = float(ts)
            time.append(t)
            pts.append(p)
        times.append(time)
        points.append(pts)
    
    fig = plt.figure()
    axes = fig.add_subplot(111)
    
    for i in range(0, len(times)):
        axes.plot(times[i], points[i])
    
    axes.autoscale_view(True, True, True)
    
    plt.show()
    