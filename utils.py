import numpy as np
import random
from scipy.ndimage.interpolation import rotate
from scipy.misc import imresize

def oneHot(df , col):
    res = dict()
    values = set(df[col])
    for v in values:
        res[col+'='+str(v)] = [ int(vv == v) for vv in df[col] ]
    for k, s in res.items():
        df[k] = s
    df = df.drop(col, 1)
    return df


class batch:
    def __init__(self, X, y, size):
        self.X = X
        self.y = y
        self.size = size
        self.length = X.shape[0]
        self.index = range(self.length) 
        random.shuffle( self.index )
        self.i = 0
        self.wasLast = False
    def getNextBatch(self):
        self.wasLast = False
        resX = self.X[self.index[ self.i : self.i + self.size  ] , :]
        resY = self.y[self.index[ self.i : self.i + self.size  ], : ]
        self.i += self.size
        if (self.i + self.size > self.length):
            self.i = 0
            self.wasLast = True
        return resX,resY
    
    
def rotate_img(s , r):
    s = s.reshape(28,28)
    s = rotate(s ,r )
    s = imresize(s, (28,28))
    s = s.reshape( 1, 28*28 )
    return s
        