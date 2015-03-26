
import matplotlib.pyplot as plt

print "plotbuf is imported"

def isFloat(fstr):
    try:
        y = float(fstr)
    except:
        return False
    return True


#print list(vim.current.buffer)
def Plotbuffer(b, n0):
    """
    b : buffer contains numbers need to plot
    n0: current cursor posioin 
    """
    n = n0

    while True:
        n = n-1
        if n < 0:
            break
        s = b[n]
        s = [x for x in s.replace(","," ").split(" ") if len(x)>0]
        if len(s) ==0:
            break
        if isFloat(s[0]) == False:
            break

    nstart = n+1

    n = n0
    while True:
        n = n+1
        if n >= len(b):
            break
        s = b[n]
        s = [x for x in s.replace(","," ").split(" ") if len(x)>0]
        if len(s) ==0:
            break
        if isFloat(s[0]) == False:
            break

    nend = n-1
    print nstart, nend

    bfloat = b[nstart:nend+1]

    x = y = []

    for bxy in bfloat:
        try:
            [x0, y0] = [float(z) for z in bxy.replace(",", " ").split(" ") if len(z) > 0]
            x = x + [x0]
            y = y + [y0]
        except ValueError:
            print "cannot convert %s" % (bxy)
            x = []
            y = []
            break
    return x, y

if __name__ == "__main__":

    b = [' ','real ', '1 2','3 4','5 6','end']
    n0 = 3
    x, y = Plotbuffer(b, n0)

    plt.plot(x,y,'r*--')
    plt.show()

