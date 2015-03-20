"""
"
"
python import sys
python import vim
python import matplotlib.pyplot as plt
python from pylab import *
python import numpy as np
python sys.path.append(vim.eval('expand("<sfile>:h")'))

python PlotbufFlag  = 0
python clr=['b*--','r*--','g^--', 'ro--']

"""========================================================
function! BufferPlot()
	
python << endOfPython


from plotbuf import Plotbuffer

if PlotbufFlag == 0:
    xyArray =[]
    PlotbufFlag = 1
    clrIx = 0
    
b = list(vim.current.buffer)
r = vim.current.range

x,y = Plotbuffer(b, r.start)

xyArray = xyArray +[x,y,clr[clrIx]]

clrIx = clrIx + 1
if clrIx == len(clr):
    clrIx = 0

plt.plot(*xyArray)

theTitle = vim.current.buffer.name.split('/')[-2:]
theTitle = "/".join(theTitle)

plt.title(theTitle) 


plt.xlabel('x')
plt.ylabel('y')
plt.show()

endOfPython
endfunction


"""========================================================
function! BufferPlot_cur()
python << endOfPython

xyArray =[]
clrIx = 0
endOfPython
call BufferPlot()
endfunction


"""
command! Plot call BufferPlot()
command! PlotC call BufferPlot_cur()
