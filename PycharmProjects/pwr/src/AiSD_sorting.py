from matplotlib import animation
from pylab import *

theFile = open("MY_PATH", "r")
theInts = []
for val in theFile.read().split("/"):
    theInts.append(int(val))
theFile.close()

title("sorting alghoritms")
plot(theInts, 'r', label="shell sort")
nums = [1,2,4,8,16,32]
rands = [1,5,12,25,16,3,24,11,14]
plot( nums,'b', label="library sort")
plot(rands, 'g', label="quick sort")
legend(loc='upper right')

savefig('graph1.png')

"""
'r' = red
 'g' = green
 'b' = blue
 'c' = cyan
 'm' = magenta
 'y' = yellow
 'k' = black
 'w' = white

  '-' = solid
 '--' = dashed
 ':' = dotted
 '-.' = dot-dashed
 '.' = points
 'o' = filled circles
 '^' = filled triangles
"""

"""
with open('MY_PATH') as f:

array = [[int(x) for x in line.split("/")] for line in f]
title("sorting alghoritms")
plot(1, 2, 3, 4, 'r', label="shell sort")
legend(loc='upper right')
savefig('graph1.png')

"""
"""
values = []
for line in file:
    fields = line.strip().split("/")

    #for nums in range(len(fields)):
  #      values = fields[nums]
    title("sorting alghoritms")
    plot(1,2,3,4,'r', label = "shell sort")
    legend(loc='upper right')
    savefig('graph1.png')
"""

"""
    text_file = open("filename.dat", "r")
    print
    lines
    print
    len(lines)
    text_file.close()
"""

"""
    filename = "MY_PATH"
    values = []
    with open(filename) as f:
        for line in f:
            values.append([int(n) for n in line.sptrip().split("/")])
            for num in values:
            plot([values[num]])
"""
