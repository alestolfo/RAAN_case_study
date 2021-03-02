"""
This script reads an .xlsx file describing a network architecture at the path
provided as input, and creates the .json file that is then read by the
javascript app and used to render the network graph
"""

import os
import sys
import pandas as pd

if len(sys.argv) < 2:
    print('No input file specified. Aborting.')
    exit(-1)

# load file
filename = sys.argv[1]
xlsx = pd.ExcelFile(filename)

# read the two sheets
edges = pd.read_excel(xlsx, 'edges')
nodes = pd.read_excel(xlsx, 'nodes')

# create output file
os.makedirs('data', exist_ok=True)
out = open('data/data.json', 'w')

# write information relative to the nodes
out.write('{\n"nodes" : [\n')

for i in range(len(nodes)):
    split = list(nodes.loc[i,:])
    id = str(split[0])
    color = split[1]
    label = split[2]

    s = '{"id" : ' + id + ', "color": "' + color + '", "label" : "' + label + '"},\n'

    if i == len(nodes)-1:
        s = s[:-2] + '\n'

    out.write(s)

# write information relative to the edges
out.write('],\n"links" : [\n')

for i in range(len(edges)):
    split = list(edges.loc[i,:])
    source = str(split[0])
    target = str(split[1])
    weight = str(split[2])

    s = '{"source" : ' + source + ', "target": ' + target + ', "weight" : ' + weight + '},\n'

    if i == len(edges)-1:
        s = s[:-2] + '\n'

    out.write(s)

out.write(']\n}')
out.close()

