'''
Created on Dec 9, 2011

@author: cma330
'''

import matplotlib.pyplot as plt
import sys

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print "usage: %s <filename>+" % sys.argv[0]
        sys.exit(-1)
    
    print sys.argv[1:]
    
    times  = []
    points = []
    for filename in sys.argv[1:]:
        time = []
        print "Processing %s" % filename
        for line in open(filename, "r"):
            (ts, data) = line.split()
            t = float(ts)
            time.append(t)
        times.append(time)
    
    fig  = plt.figure()
    axes = fig.add_subplot(111)
    
    for i in range(0, len(times)):
        axes.plot(times[i], range(1, len(times[i])+1), '+')
    
    axes.autoscale_view(True, True, True)

    plt.title("Distribution of messages in time")
    plt.xlabel("Time")
    plt.ylabel("#Messages")
    plt.show()
    