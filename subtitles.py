#! /usr/bin/python3
import sys

def sync(fich, dec):
    """
    Function that corrects the .srt file.
    It takes the file name and the correction value (in seconds) as input
    """
    with open(fich,'r') as f:
        txt = f.readlines()
    fich2 = fich[:-4]+'_sync.srt'
    old = []
    for el in txt :
        if ' --> ' in el :
            old.append(el)
    new = []
    for el in old :
        t = el.split(' --> ')
        t[0]=calcul(t[0], dec)
        t[1]=calcul(t[1], dec)
        new.append(t[0] + ' --> ' + t[1] + '\n')
    count = 0
    for c, el in enumerate(txt) :
        if ' --> ' in el :
            txt[c] = new[count]
            count += 1
    with open(fich2,'w') as f:
        for el in txt :
            f.write(el)


def conv(t):
    """
    Converts .srt time format to seconds
    """
    f=t.split(',')[1]
    tout = t.split(',')[0].split(':')
    s= int(tout[0])*3600 + int(tout[1])*60 + int(tout[2]) + int(f)/1000
    return s
    
def convback(t):
    """
    Converts seconds back to .srt time format
    """
    h = int(t//3600)
    m = int(t//60%60)
    s = int(t%60)
    f = round(t%1*1000)
    ch = "{0:0=2d}".format(h) + ':' + "{0:0=2d}".format(m) + ':' + "{0:0=2d}".format(s) + ',' + "{0:0=3d}".format(f)
    return ch

def calcul(x, dec):
    """
    Corrects a single .srt format time. It takes the time (.srt format) and the correction value as input
    """
    old = conv(x)
    old += dec
    new = convback(old)
    return new

if __name__ == '__main__':
    if len(sys.argv) < 2:
        fich = input("Path to .srt file :\n")
        dec  = float(input("Correction (in seconds) :\n"))
    elif len(sys.argv) < 3:
        dec = float(input("Correction (in seconds) :\n"))
    else :
        fich = sys.argv[1]
        dec  = float(sys.argv[2])
    sync(fich, dec)
    print('done !')
