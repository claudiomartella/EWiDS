'''
Created on Dec 9, 2011

@author: cma330
'''

from binascii import unhexlify
from struct import unpack
from collections import defaultdict

import fileinput, sys, datetime

header = '<?xml version="1.0" encoding="UTF-8"?>\n<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\nxmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\nxsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\nhttp://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n'
graphd = '  <graph id="G" edgedefault="undirected">\n'
footer = '  </graph>\n</graphml>\n'
edged  = '  <key id="ts" for="edge" attr.name="ts" attr.type="float"/>\n'
vertd  = '  <key id="id" for="node" attr.name="id" attr.type="int"/>\n'

def dict_to_graphml(nodes_dict, filename):
    output = open(filename, "w")
    # print header
    output.write(header)
    output.write(edged)
    output.write(vertd)
    output.write(graphd)
    
    for nodeid, edges in nodes_dict.items():
        output.write('    <node id="%d">\n' % nodeid)
        output.write('      <data key="id">%d</data>\n')
        output.write('    </node>\n')
        for edge in edges:
            (other, ts) = edge
            output.write('    <edge source="%d" target="%d">\n' % (nodeid, other))
            output.write('      <data key="ts">%f</data>\n' % float(ts))
            output.write('    </edge>\n')
    # print footer
    output.write(footer)
    output.close()

if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        print "usage: %s <filename>" % sys.argv[0]
        sys.exit(-1)
    
    nodes = defaultdict(lambda: [])
    
    for line in fileinput.input(sys.argv[1]):
        (ts, HEXdata) = line.strip().split()
        
        # parse the HEX data
        data   = unhexlify(HEXdata)
        packet = unpack("<I IIH H HHHHH HHHHH", data)
        
        # extract neighborhood data
        nodeid  = packet[5]
        neighb1 = packet[7]
        neighb2 = packet[8]
        neighb3 = packet[9]

        date = datetime.datetime.fromtimestamp(float(ts))

        edges = nodes[nodeid]
        
        if neighb1 != 0:
            edges.append((neighb1, ts))
        if neighb2 != 0:
            edges.append((neighb2, ts))
        if neighb3 != 0:
            edges.append((neighb3, ts))

    dict_to_graphml(nodes, sys.argv[1]+".graphml")

#EOF